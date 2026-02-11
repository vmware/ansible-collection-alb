# Copyright 2021 VMware, Inc.
# SPDX-License-Identifier: Apache License 2.0

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import os
import sys
import copy
import json
import logging
import time
import ipaddress

if sys.version_info < (3, 5):
    from urlparse import urlparse
else:
    from urllib.parse import urlparse

from datetime import datetime, timedelta, timezone
from ssl import SSLError


logger = logging.getLogger(__name__)

global sessionDict  # pylint: disable=global-at-module-level
sessionDict = {}

try:
    from requests import ConnectionError
    from requests import Response
    from requests.exceptions import ChunkedEncodingError
    from requests.sessions import Session
except ImportError:
    ConnectionError = None
    Response = None
    ChunkedEncodingError = None
    Session = None


def avi_timedelta(td):
    """
    This is a wrapper class to workaround python 2.6 builtin datetime.timedelta
    does not have total_seconds method
    :param td timedelta object
    """
    if not isinstance(td, timedelta):
        raise TypeError()
    if sys.version_info >= (2, 7):
        ts = td.total_seconds()
    else:
        ts = td.seconds + (24 * 3600 * td.days)
    return ts


# @AI-Modified: 2026-01-23 - Added helper to replace deprecated datetime.utcnow()
def get_utc_now():
    """
    Get current UTC time in a timezone-aware manner.

    This replaces the deprecated datetime.utcnow() which is deprecated
    in Python 3.12+ and will be removed in future versions.

    Returns:
        datetime: Current UTC time (timezone-aware)
    """
    return datetime.now(timezone.utc)


def avi_sdk_syslog_logger(logger_name='ansible_collections.vmware.alb.plugins.module_utils'):
    # The following sets up syslog module to log underlying avi SDK messages
    # based on the environment variables:
    #   AVI_LOG_HANDLER: names the logging handler to use. Only syslog is
    #     supported.
    #   AVI_LOG_LEVEL: Logging level used for the avi SDK. Default is DEBUG
    #   AVI_SYSLOG_ADDRESS: Destination address for the syslog handler.
    #   Default is /dev/log
    from logging.handlers import SysLogHandler
    lf = '[%(asctime)s] %(levelname)s [' \
         '%(module)s.%(funcName)s:%(lineno)d] %(message)s'
    log = logging.getLogger(logger_name)
    log_level = os.environ.get('AVI_LOG_LEVEL', 'DEBUG')
    if log_level:
        log.setLevel(getattr(logging, log_level))
    formatter = logging.Formatter(lf)
    sh = SysLogHandler(address=os.environ.get('AVI_SYSLOG_ADDRESS',
                                              '/dev/log'))
    sh.setFormatter(formatter)
    log.addHandler(sh)
    return log


class ObjectNotFound(Exception):
    pass


class APIError(Exception):
    def __init__(self, arg, rsp=None):
        self.args = [arg, rsp]
        self.rsp = rsp


class AviServerError(APIError):
    def __init__(self, arg, rsp=None):
        super(AviServerError, self).__init__(arg, rsp)


class AviMultipartUploadError(Exception):
    def __init__(self, arg, rsp=None):
        self.args = [arg]
        self.rsp = rsp


class APINotImplemented(Exception):
    pass


if Response:
    class ApiResponse(Response):
        """
        Returns copy of the requests.Response object provides additional helper
        routines
            1. obj: returns dictionary of Avi Object
        """
        def __init__(self, rsp):
            super(ApiResponse, self).__init__()
            for k, v in list(rsp.__dict__.items()):
                setattr(self, k, v)

        def json(self):
            """
            Extends the session default json interface to handle special errors
            and raise Exceptions
            returns the Avi object as a dictionary from rsp.text
            """
            if self.status_code > 199 and self.status_code < 300:
                if not self.text:
                    # In cases like status_code == 201 the response text could be
                    # empty string.
                    return None
                return super(ApiResponse, self).json()
            elif self.status_code == 404:
                raise ObjectNotFound('HTTP Error: %d Error Msg %s' % (
                    self.status_code, self.text), self)
            elif self.status_code >= 500:
                raise AviServerError('HTTP Error: %d Error Msg %s' % (
                    self.status_code, self.text), self)
            else:
                raise APIError('HTTP Error: %d Error Msg %s' % (
                    self.status_code, self.text), self)

        def count(self):
            """
            return the number of objects in the collection response. If it is not
            a collection response then it would simply return 1.
            """
            obj = self.json()
            if 'count' in obj:
                # this was a resposne to collection
                return obj['count']
            return 1

        @staticmethod
        def to_avi_response(resp):
            if isinstance(resp, Response):
                return ApiResponse(resp)
            return resp
else:
    class ApiResponse:
        def __init__(self, rsp):
            self.rsp = rsp


class AviCredentials(object):
    controller = ''
    username = ''
    password = ''
    api_version = '20.1.1'
    tenant = None
    tenant_uuid = None
    token = None
    port = None
    timeout = 300
    session_id = None
    csrftoken = None
    ssl_cert = None
    ssl_key = None
    idp_class = None
    csp_host = None
    csp_token = None

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def update_from_ansible_module(self, m):
        """
        :param m: ansible module
        :return:
        """
        if m.params.get('avi_credentials'):
            for k, v in m.params['avi_credentials'].items():
                if hasattr(self, k):
                    setattr(self, k, v)
        if m.params['controller']:
            self.controller = m.params['controller']
        if m.params['username']:
            self.username = m.params['username']
        if m.params['password']:
            self.password = m.params['password']
        if (m.params['api_version'] and
                (m.params['api_version'] != '20.1.1')):
            self.api_version = m.params['api_version']
        if m.params['tenant']:
            self.tenant = m.params['tenant']
        if m.params['tenant_uuid']:
            self.tenant_uuid = m.params['tenant_uuid']
        if m.params.get('session_id'):
            self.session_id = m.params['session_id']
        if m.params.get('csrftoken'):
            self.csrftoken = m.params['csrftoken']
        if m.params.get('ssl_cert'):
            self.ssl_cert = m.params['ssl_cert']
        if m.params.get('ssl_key'):
            self.ssl_key = m.params['ssl_key']

    def __str__(self):
        return 'controller %s user %s api %s tenant %s' % (
            self.controller, self.username, self.api_version, self.tenant)


if Session:
    class ApiSession(Session):
        """
        Extends the Request library's session object to provide helper
        utilities to work with Avi Controller like authentication, api massaging
        etc.
        """

        # This keeps track of the process which created the cache.
        # At anytime the pid of the process changes then it would create
        # a new cache for that process.
        AVI_SLUG = 'Slug'
        SESSION_CACHE_EXPIRY = 20 * 60
        SHARED_USER_HDRS = ['X-CSRFToken', 'Session-Id', 'Referer', 'Content-Type']
        MAX_API_RETRIES = 3
        CSP_HOST = 'console.cloud.vmware.com'
        IPV6 = 6
        # @AI-Modified: 2026-01-23 - Added constant to avoid duplicating error message literal
        API_ERROR_MSG_FORMAT = 'Failed: %s Status Code %s msg %s'

        # @AI-Modified: 2026-01-23 - Refactored __init__ to reduce cognitive complexity
        # @AI-Modified: 2026-01-23 - Extracted nested conditional into independent statement
        def _build_prefix_for_http(self, port):
            """
            Build URL prefix when controller starts with http.

            Parameters:
                port: Port number

            Returns:
                tuple: (prefix, k_port)
            """
            # Determine port: use 80 if no port configured, otherwise use provided port or default to 443
            if not self.avi_credentials.port:
                k_port = 80
            else:
                k_port = port if port else 443

            prefix = self.avi_credentials.controller
            if port and int(port) not in (80, 443):
                prefix = '{x}:{y}'.format(
                    x=self.avi_credentials.controller,
                    y=self.avi_credentials.port)
            return prefix, k_port

        def _build_prefix_for_https(self, port):
            """
            Build URL prefix for https connections.

            Parameters:
                port: Port number

            Returns:
                str: URL prefix
            """
            protocol = 'https'
            is_ipv6 = self.is_ipv6_address(self.avi_credentials.controller)
            port = int(port) if port and int(port) not in (80, 443) else None

            if is_ipv6:
                prefix = '{}://[{}]'.format(protocol, self.avi_credentials.controller)
            else:
                prefix = '{}://{}'.format(protocol, self.avi_credentials.controller)

            if port:
                prefix += ':{}'.format(port)

            return prefix

        def _handle_csp_authentication(self):
            """Handle CSP token-based authentication."""
            if not self.avi_credentials.csp_host:
                raise APIError("CSP host is not provided for csp login.")

            if self.avi_credentials.csp_host.startswith('https'):
                self.avi_credentials.csp_host = self.avi_credentials.csp_host.replace('https://', '')

            self.csp_prefix = 'https://{x}/csp/gateway'.format(x=self.avi_credentials.csp_host)
            self.generate_access_token()

        def _setup_session_authentication(self, lazy_authentication):
            """
            Set up session authentication based on credentials.

            Parameters:
                lazy_authentication: Whether to defer authentication
            """
            if self.user_hdrs and 'Authorization' in self.user_hdrs:
                return

            # @AI-Modified: 2026-01-23 - Replaced datetime.utcnow() with get_utc_now()
            if self.avi_credentials.csrftoken:
                sessionDict[self.key] = {
                    'api': self,
                    "csrftoken": self.avi_credentials.csrftoken,
                    "session_id": self.avi_credentials.session_id,
                    "last_used": get_utc_now()
                }
            elif lazy_authentication:
                sessionDict.get(self.key, {}).update(
                    {'api': self, "last_used": get_utc_now()})
            elif self.avi_credentials.csp_token:
                self._handle_csp_authentication()
            else:
                self.authenticate_session()

        def __init__(self, controller_ip=None, username=None, password=None,
                     token=None, tenant=None, tenant_uuid=None, verify=False,
                     port=None, timeout=60, api_version=None,
                     retry_conxn_errors=True, data_log=False,
                     avi_credentials=None, session_id=None, csrftoken=None,
                     lazy_authentication=False, max_api_retries=None, csp_host=CSP_HOST, csp_token=None, user_hdrs=None, ssl_cert=None, ssl_key=None):
            """
             ApiSession takes ownership of avi_credentials and may update the
             information inside it.

            Initialize new session object with authenticated token from login api.
            It also keeps a cache of user sessions that are cleaned up if inactive
            for more than 20 mins.

            Notes:
            01. If mode is https and port is none or 443, we don't embed the
                port in the prefix. The prefix would be 'https://ip'. If port
                is a non-default value then we concatenate https://ip:port
                in the prefix.
            02. If mode is http and the port is none or 80, we don't embed the
                port in the prefix. The prefix would be 'http://ip'. If port is
                a non-default value, then we concatenate http://ip:port in
                the prefix.
            """

            super(ApiSession, self).__init__()
            logger.debug("Creating session with following values:\n "
                         "controller_ip: %s, username: %s, tenant: %s, "
                         "tenant_uuid: %s, verify: %s, port: %s, timeout: %s, "
                         "api_version: %s, retry_conxn_errors: %s, data_log: %s, "
                         "avi_credentials: %s, session_id: %s, csrftoken: %s, "
                         "lazy_authentication: %s, max_api_retries: %s",
                         controller_ip, username, tenant,
                         tenant_uuid, verify, port,
                         timeout, api_version, retry_conxn_errors,
                         data_log, avi_credentials, session_id,
                         csrftoken, lazy_authentication, max_api_retries)

            if not avi_credentials:
                tenant = tenant if tenant else "admin"
                self.avi_credentials = AviCredentials(
                    controller=controller_ip, username=username,
                    password=password, api_version=api_version,
                    tenant=tenant, tenant_uuid=tenant_uuid,
                    token=token, port=port, timeout=timeout,
                    session_id=session_id, csp_host=csp_host, csp_token=csp_token, csrftoken=csrftoken, ssl_cert=ssl_cert, ssl_key=ssl_key)
            else:
                self.avi_credentials = avi_credentials

            self.headers = {}
            self.verify = verify
            self.retry_conxn_errors = retry_conxn_errors
            self.remote_api_version = {}
            self.user_hdrs = user_hdrs if user_hdrs else {}
            self.data_log = data_log
            self.num_session_retries = 0
            self.num_api_retries = 0
            self.retry_wait_time = 0
            self.max_session_retries = (
                self.MAX_API_RETRIES if max_api_retries is None
                else int(max_api_retries))

            # Build URL prefix based on controller format
            k_port = port if port else 443
            if self.avi_credentials.controller.startswith('http'):
                self.prefix, k_port = self._build_prefix_for_http(port)
            else:
                self.prefix = self._build_prefix_for_https(port)

            self.timeout = timeout
            self.key = '%s:%s:%s' % (self.avi_credentials.controller,
                                     self.avi_credentials.username, k_port)

            self._setup_session_authentication(lazy_authentication)

            self.num_session_retries = 0
            self.pid = os.getpid()
            ApiSession._clean_inactive_sessions()

        @property
        def controller_ip(self):
            return self.avi_credentials.controller

        @controller_ip.setter
        def controller_ip(self, controller_ip):
            self.avi_credentials.controller = controller_ip

        @property
        def username(self):
            return self.avi_credentials.username

        @property
        def connected(self):
            return sessionDict.get(self.key, {}).get('connected', False)

        @username.setter
        def username(self, username):
            self.avi_credentials.username = username

        @property
        def password(self):
            return self.avi_credentials.password

        @password.setter
        def password(self, password):
            self.avi_credentials.password = password

        @property
        def keystone_token(self):
            return sessionDict.get(self.key, {}).get('csrftoken', None)

        @keystone_token.setter
        def keystone_token(self, token):
            sessionDict[self.key]['csrftoken'] = token

        @property
        def tenant_uuid(self):
            self.avi_credentials.tenant_uuid

        @tenant_uuid.setter
        def tenant_uuid(self, tenant_uuid):
            self.avi_credentials.tenant_uuid = tenant_uuid

        @property
        def tenant(self):
            return self.avi_credentials.tenant

        @tenant.setter
        def tenant(self, tenant):
            if tenant:
                self.avi_credentials.tenant = tenant
            else:
                self.avi_credentials.tenant = 'admin'

        @property
        def port(self):
            self.avi_credentials.port

        @port.setter
        def port(self, port):
            self.avi_credentials.port = port

        @property
        def api_version(self):
            return self.avi_credentials.api_version

        @api_version.setter
        def api_version(self, api_version):
            self.avi_credentials.api_version = api_version

        @property
        def session_id(self):
            return sessionDict[self.key]['session_id']

        def get_context(self):
            return {
                'session_id': sessionDict.get(self.key, {}).get('session_id'),
                'csrftoken': sessionDict.get(self.key, {}).get('csrftoken')
            }

        @staticmethod
        def clear_cached_sessions():
            global sessionDict
            sessionDict = {}

        # @AI-Modified: 2026-01-23 - Refactored get_session to reduce cognitive complexity from 17 to under 15
        @staticmethod
        def _validate_idp_class(idp_class):
            """
            Validate and return the IDP class to use.

            Parameters:
                idp_class: IDP class or None

            Returns:
                class: Validated IDP class

            Raises:
                APIError: If idp_class is invalid
            """
            if not idp_class:
                return ApiSession
            if "ApiSession" not in str(idp_class.__base__):
                raise APIError("idp_class {} not valid class. Please provide "
                               "correct idp class. Base class of idp class is "
                               "{}".format(idp_class, str(idp_class.__base__)))
            return idp_class

        @staticmethod
        def _compute_session_key(avi_credentials):
            """
            Compute the session cache key from credentials.

            Parameters:
                avi_credentials: AviCredentials object

            Returns:
                str: Session cache key
            """
            k_port = avi_credentials.port if avi_credentials.port else 443
            if avi_credentials.controller.startswith('http'):
                k_port = 80 if not avi_credentials.port else k_port
            return '%s:%s:%s' % (avi_credentials.controller,
                                 avi_credentials.username, k_port)

        @staticmethod
        def get_session(
                controller_ip=None, username=None, password=None, token=None,
                tenant=None, tenant_uuid=None, verify=False, port=None, timeout=60,
                retry_conxn_errors=True, api_version=None, data_log=False,
                avi_credentials=None, session_id=None, csrftoken=None,
                lazy_authentication=False, max_api_retries=None, csp_host=None, csp_token=None, idp_class=None, user_hdrs=None, ssl_cert=None, ssl_key=None):
            """
            returns the session object for same user and tenant
            calls init if session dose not exist and adds it to session cache
            :param controller_ip: controller IP address
            :param username:
            :param password:
            :param token: Token to use; example, a valid keystone token
            :param tenant: Name of the tenant on Avi Controller
            :param tenant_uuid: Don't specify tenant when using tenant_id
            :param port: Rest-API may use a different port other than 443
            :param timeout: timeout for API calls; Default value is 60 seconds
            :param retry_conxn_errors: retry on connection errors
            :param api_version: Controller API version
            :param idp_class: IDP class. Currently supports OKtaSAMLApiSession,
            OneloginApiSession
            """
            max_api_retries = 1 if max_api_retries == 0 else max_api_retries
            idp_class = ApiSession._validate_idp_class(idp_class)

            if not avi_credentials:
                tenant = tenant if tenant else "admin"
                avi_credentials = AviCredentials(
                    controller=controller_ip, username=username,
                    password=password, api_version=api_version,
                    tenant=tenant, tenant_uuid=tenant_uuid,
                    token=token, port=port, timeout=timeout,
                    session_id=session_id, csrftoken=csrftoken, csp_host=csp_host, csp_token=csp_token, ssl_cert=ssl_cert, ssl_key=ssl_key)

            key = ApiSession._compute_session_key(avi_credentials)
            cached_session = sessionDict.get(key)

            if cached_session:
                user_session = cached_session['api']
                needs_auth = not (user_session.avi_credentials.csrftoken or lazy_authentication)
                if needs_auth:
                    user_session.authenticate_session()
                return user_session

            return idp_class(
                controller_ip, username, password, token=token,
                tenant=tenant, tenant_uuid=tenant_uuid,
                verify=verify, port=port, timeout=timeout,
                retry_conxn_errors=retry_conxn_errors,
                api_version=api_version, data_log=data_log,
                avi_credentials=avi_credentials,
                lazy_authentication=lazy_authentication,
                max_api_retries=max_api_retries, csp_host=csp_host, csp_token=csp_token, user_hdrs=user_hdrs)

        def reset_session(self):
            """
            resets and re-authenticates the current session.
            """
            sessionDict[self.key]['connected'] = False
            logger.info('resetting session for %s', self.key)
            self.user_hdrs = {}
            for k, v in self.headers.items():
                if k not in self.SHARED_USER_HDRS:
                    self.user_hdrs[k] = v
            self.headers = self.user_hdrs
            if self.avi_credentials.csp_token:
                self.generate_access_token()
            else:
                self.authenticate_session()

        # @AI-Modified: 2026-01-23 - Refactored authenticate_session to reduce cognitive complexity
        def _build_auth_body(self):
            """
            Build authentication request body with credentials.

            Returns:
                dict: Authentication body with username and password/token

            Raises:
                APIError: If neither password nor token is provided
            """
            body = {"username": self.avi_credentials.username}
            if self.avi_credentials.password:
                body["password"] = self.avi_credentials.password
            elif self.avi_credentials.token:
                body["token"] = self.avi_credentials.token
            else:
                raise APIError("Neither user password or token provided for "
                               "controller %s" % self.controller_ip)
            return body

        def _handle_successful_auth(self, rsp):
            """
            Handle successful authentication response.

            Parameters:
                rsp: Response object from login request
            """
            self.num_session_retries = 0
            self.remote_api_version = rsp.json().get('version', {})
            session_cookie_name = rsp.json().get('session_cookie_name', 'sessionid')

            if self.user_hdrs:
                self.headers.update(self.user_hdrs)

            # @AI-Modified: 2026-01-23 - Replaced datetime.utcnow() with get_utc_now()
            if rsp.cookies and 'csrftoken' in rsp.cookies:
                csrftoken = rsp.cookies['csrftoken']
                sessionDict[self.key] = {
                    'csrftoken': csrftoken,
                    'session_id': rsp.cookies[session_cookie_name],
                    'last_used': get_utc_now(),
                    'api': self,
                    'connected': True
                }
                self.avi_credentials.csrftoken = csrftoken
                self.avi_credentials.session_id = rsp.cookies[session_cookie_name]

            logger.debug("authentication success for user %s",
                         self.avi_credentials.username)

        def _handle_auth_error(self, rsp):
            """
            Handle authentication error response.

            Parameters:
                rsp: Response object from failed login request

            Raises:
                APIError: Always raises with error details
            """
            logger.error('Status Code %s msg %s', rsp.status_code, rsp.text)
            err = APIError(self.API_ERROR_MSG_FORMAT % (rsp.url, rsp.status_code, rsp.text), rsp)
            raise err

        def _handle_auth_retry(self, err):
            """
            Handle retry logic for authentication failures.

            Parameters:
                err: The error that triggered the retry

            Raises:
                Exception: Re-raises err if max retries exceeded
            """
            if self.retry_wait_time:
                time.sleep(self.retry_wait_time)

            self.num_session_retries += 1
            if self.num_session_retries > self.max_session_retries:
                self.num_session_retries = 0
                logger.error("giving up after %d retries connection failure %s",
                             self.max_session_retries, True)
                raise err

            self.authenticate_session()

        def authenticate_session(self):
            """
            Performs session authentication with Avi controller and stores
            session cookies and sets header options like tenant.
            """
            body = self._build_auth_body()
            logger.debug('authenticating user %s prefix %s',
                         self.avi_credentials.username, self.prefix)
            self.cookies.clear()
            err = None
            certificate = self.avi_credentials.ssl_cert
            key = self.avi_credentials.ssl_key

            try:
                rsp = super(ApiSession, self).post(
                    self.prefix + "/login", body, timeout=self.timeout,
                    verify=self.verify, cert=(certificate, key))

                if rsp.status_code == 200:
                    self._handle_successful_auth(rsp)
                    return

                self._handle_auth_error(rsp)

            except (ConnectionError, SSLError, ChunkedEncodingError) as e:
                if not self.retry_conxn_errors:
                    raise
                logger.warning('Connection error retrying %s', e)
                err = e

            self._handle_auth_retry(err)

        def _resolve_tenant_info(self, tenant, tenant_uuid):
            """
            Resolve tenant and tenant_uuid based on provided values.

            Returns:
                tuple: (tenant, tenant_uuid) - one will be None
            """
            if tenant:
                return tenant, None
            if tenant_uuid:
                return None, tenant_uuid
            return self.avi_credentials.tenant, self.avi_credentials.tenant_uuid

        def _set_tenant_headers(self, api_hdrs, tenant, tenant_uuid):
            """Set tenant-related headers in api_hdrs."""
            if tenant_uuid:
                api_hdrs["X-Avi-Tenant-UUID"] = str(tenant_uuid)
                api_hdrs.pop("X-Avi-Tenant", None)
            elif tenant:
                api_hdrs["X-Avi-Tenant"] = str(tenant)
                api_hdrs.pop("X-Avi-Tenant-UUID", None)

        def _ensure_csrf_token(self, api_hdrs):
            """Ensure CSRF token is set in headers, authenticating if needed."""
            if 'Authorization' in api_hdrs:
                return

            session_data = sessionDict.get(self.key, {})
            if 'csrftoken' not in session_data:
                self.authenticate_session()
                session_data = sessionDict.get(self.key, {})

            api_hdrs['X-CSRFToken'] = session_data['csrftoken']

        def _get_api_version_header(self, api_version):
            """Get the API version to use in headers."""
            if api_version:
                return api_version
            if self.avi_credentials.api_version:
                return str(self.avi_credentials.api_version)
            return None

        def _get_api_headers(self, tenant, tenant_uuid, timeout, headers, api_version):
            """
            Returns the headers that are passed to the requests.Session api calls.

            Parameters:
                tenant: Tenant name override
                tenant_uuid: Tenant UUID override
                timeout: Request timeout value
                headers: Additional headers to merge
                api_version: API version override

            Returns:
                dict: Headers dictionary for API request
            """
            api_hdrs = copy.deepcopy(self.headers)
            api_hdrs.update({
                "Referer": self.prefix,
                "Content-Type": "application/json"
            })

            if self.user_hdrs:
                api_hdrs.update(self.user_hdrs)

            api_hdrs['timeout'] = str(timeout)

            # Set API version header
            version = self._get_api_version_header(api_version)
            if version:
                api_hdrs['X-Avi-Version'] = version

            # Resolve and set tenant headers
            tenant, tenant_uuid = self._resolve_tenant_info(tenant, tenant_uuid)
            self._set_tenant_headers(api_hdrs, tenant, tenant_uuid)

            # Ensure CSRF token is present
            self._ensure_csrf_token(api_hdrs)

            # Apply user-provided header overrides
            if headers:
                api_hdrs.update(headers)

            return api_hdrs

        # @AI-Modified: 2026-01-23 - Added helper methods to reduce cognitive complexity of _api method
        def _handle_pid_change(self):
            """
            Handle process ID change by closing and resetting session.

            This detects if the current process ID differs from when the session
            was created (e.g., after a fork) and resets the session accordingly.
            """
            if self.pid != os.getpid():
                logger.info('pid %d change detected new %d. Closing session',
                            self.pid, os.getpid())
                self.close()
                self.pid = os.getpid()

        def _prepare_cookies(self, api_hdrs, timeout):
            """
            Prepare cookies dictionary for API request.

            Parameters:
                api_hdrs: API headers dictionary
                timeout: Request timeout value (may be modified)

            Returns:
                tuple: (cookies dict, timeout value)
            """
            cookies = {}
            if 'X-CSRFToken' in api_hdrs:
                cookies['csrftoken'] = api_hdrs['X-CSRFToken']

            if 'Authorization' not in api_hdrs:
                self._handle_pid_change()
                if timeout is None:
                    timeout = self.timeout
                session_data = sessionDict.get(self.key, {})
                session_id = session_data.get('session_id')
                if session_id:
                    cookies['sessionid'] = session_id
                    cookies['avi-sessionid'] = session_id

            return cookies, timeout

        def _execute_request(self, fn, fullpath, data, api_hdrs, timeout, cookies, **kwargs):
            """
            Execute the HTTP request.

            Parameters:
                fn: The HTTP method function to call
                fullpath: Full API path
                data: Request body data
                api_hdrs: API headers
                timeout: Request timeout
                cookies: Request cookies

            Returns:
                tuple: (response, connection_error flag, error object)
            """
            try:
                if data is not None and isinstance(data, dict):
                    resp = fn(fullpath, data=json.dumps(data), headers=api_hdrs,
                              timeout=timeout, cookies=cookies, **kwargs)
                else:
                    resp = fn(fullpath, data=data, headers=api_hdrs,
                              timeout=timeout, cookies=cookies, **kwargs)
                return resp, False, None
            except (ConnectionError, SSLError, ChunkedEncodingError) as e:
                logger.warning('Connection error retrying %s', e)
                if not self.retry_conxn_errors:
                    raise
                return None, True, e
            except Exception as e:
                logger.error('Error in Requests library %s', e)
                raise

        def _handle_multipart_error(self, connection_error, resp):
            """
            Handle errors for multipart uploads.

            Parameters:
                connection_error: Whether a connection error occurred
                resp: Response object (may be None if connection_error)

            Raises:
                AviMultipartUploadError: Always raises for multipart requests with errors
            """
            if connection_error:
                raise AviMultipartUploadError("Connection failed or aborted")
            raise AviMultipartUploadError(
                'Received error,: %d Error Msg %s' % (resp.status_code, resp.text), resp)

        def _handle_connection_error(self):
            """Handle connection error by closing session and waiting if configured."""
            try:
                self.close()
            except Exception:
                pass  # Ignore exception in cleanup path
            logger.warning('Connection failed, retrying.')
            if self.retry_wait_time:
                time.sleep(self.retry_wait_time)

        def _log_request(self, fullpath, api_name, api_hdrs, kwargs, data, resp):
            """
            Log API request details for debugging.

            Parameters:
                fullpath: Full API path
                api_name: HTTP method name
                api_hdrs: API headers
                kwargs: Additional request arguments
                data: Request body data
                resp: Response object
            """
            logger.debug('path: %s http_method: %s hdrs: %s params: %s data: %s rsp: %s',
                         fullpath, api_name.upper(), api_hdrs, kwargs, data,
                         (resp.text if self.data_log else 'None'))

        def _update_csrf_token(self, resp):
            """
            Update CSRF token from response cookies if present.

            Parameters:
                resp: Response object containing cookies
            """
            if resp.cookies and 'csrftoken' in resp.cookies:
                csrftoken = resp.cookies['csrftoken']
                self.headers.update({"X-CSRFToken": csrftoken})

        def _handle_retry(self, api_name, path, tenant, tenant_uuid, data, headers,
                          api_version, timeout, api_hdrs, connection_error, resp, err, **kwargs):
            """
            Handle retry logic for failed requests.

            Parameters:
                api_name: HTTP method name
                path: API path
                tenant: Tenant override
                tenant_uuid: Tenant UUID override
                data: Request body data
                headers: Additional headers
                api_version: API version override
                timeout: Request timeout
                api_hdrs: Current API headers
                connection_error: Whether a connection error occurred
                resp: Response object (may be None if connection_error)
                err: Error object from connection failure

            Returns:
                Response object from retry attempt

            Raises:
                AviMultipartUploadError: For multipart upload failures
                APIError: When max retries exceeded
            """
            # Check for multipart upload
            if 'multipart/form-data' in api_hdrs.get('Content-Type', ''):
                self._handle_multipart_error(connection_error, resp)

            # Handle connection vs auth error
            if connection_error:
                self._handle_connection_error()
            else:
                logger.info('received error %d %s so resetting connection',
                            resp.status_code, resp.text)

            # Reset session if not using basic auth
            if 'Authorization' in api_hdrs:
                logger.info("Retying using the basic authentication.")
            else:
                ApiSession.reset_session(self)

            self.num_api_retries += 1

            # Check retry limit
            if self.num_api_retries > self.max_session_retries:
                self.num_api_retries = 0
                if not connection_error:
                    err = APIError(self.API_ERROR_MSG_FORMAT % (
                        resp.url, resp.status_code, resp.text), resp)
                logger.error("giving up after %d retries conn failure %s err %s",
                             self.max_session_retries, connection_error, err)
                raise err

            # Recursive retry
            resp = self._api(api_name, path, tenant, tenant_uuid, data,
                             headers=headers, api_version=api_version,
                             timeout=timeout, **kwargs)
            self.num_api_retries = 0
            return resp

        def _api(self, api_name, path, tenant, tenant_uuid, data=None,
                 headers=None, timeout=None, api_version=None, **kwargs):
            """
            Call requests.Session APIs with session expiry handling.

            This method handles authentication, session management, and automatic
            retry logic for API calls.

            Parameters:
                api_name: HTTP method name (get, post, put, delete, patch)
                path: Relative path to the AVI API
                tenant: Overrides tenant used during session creation
                tenant_uuid: Overrides tenant_uuid during session creation
                data: Request body data (dict or string)
                headers: Additional headers to override session headers
                timeout: Request timeout in seconds (default from session)
                api_version: API version override

            Returns:
                ApiResponse: Response object with helper methods
            """
            fullpath = self._get_api_path(path)
            fn = getattr(super(ApiSession, self), api_name)

            api_hdrs = self._get_api_headers(tenant, tenant_uuid, timeout, headers,
                                             api_version)
            cookies, timeout = self._prepare_cookies(api_hdrs, timeout)

            resp, connection_error, err = self._execute_request(
                fn, fullpath, data, api_hdrs, timeout, cookies, **kwargs)

            if not connection_error:
                self._log_request(fullpath, api_name, api_hdrs, kwargs, data, resp)

            # Check if retry is needed
            if connection_error or resp.status_code in (401, 419):
                resp = self._handle_retry(
                    api_name, path, tenant, tenant_uuid, data, headers,
                    api_version, timeout, api_hdrs, connection_error, resp, err, **kwargs)

            self._update_csrf_token(resp)
            self._update_session_last_used()
            return ApiResponse.to_avi_response(resp)

        def get_controller_details(self):
            result = {
                "controller_ip": self.controller_ip,
                "controller_api_version": self.remote_api_version
            }
            return result

        def get(self, path, tenant='', tenant_uuid='', timeout=None, params=None,
                api_version=None, **kwargs):
            """
            It extends the Session Library interface to add AVI API prefixes,
            handle session exceptions related to authentication and update
            the global user session cache.
            :param path: takes relative path to the AVI api.
            :param tenant: overrides the tenant used during session creation
            :param tenant_uuid: overrides the tenant or tenant_uuid during session
                creation
            :param timeout: timeout for API calls; Default value is 60 seconds
            :param params: dictionary of key value pairs to be sent as query
                parameters
            :param api_version: overrides x-avi-header in request header during
                session creation
            get method takes relative path to service and kwargs as per Session
                class get method
            returns session's response object
            """
            return self._api('get', path, tenant, tenant_uuid, timeout=timeout,
                             params=params, api_version=api_version, **kwargs)

        # @AI-Modified: 2026-01-23 - Refactored get_object_by_name to reduce cognitive complexity
        def _handle_auth_retry_for_get(self, path, name, tenant, tenant_uuid,
                                       timeout, params, api_version, **kwargs):
            """
            Handle authentication retry for get_object_by_name.

            Parameters:
                path: Relative path to service
                name: Name of the object
                tenant: Tenant override
                tenant_uuid: Tenant UUID override
                timeout: Request timeout
                params: Query parameters
                api_version: API version override

            Returns:
                Response object from retry attempt
            """
            if 'Authorization' in self.headers:
                logger.info("Retying using the basic authentication.")
            else:
                ApiSession.reset_session(self)
            return self.get_object_by_name(
                path, name, tenant, tenant_uuid, timeout=timeout,
                params=params, api_version=api_version, **kwargs)

        def _extract_object_from_response(self, resp, path, name):
            """
            Extract object from API response.

            Parameters:
                resp: Response object
                path: API path (for logging)
                name: Object name (for logging)

            Returns:
                dict or None: Extracted object or None if not found
            """
            try:
                json_resp = resp.json()
                if 'results' in json_resp:
                    return json_resp['results'][0]
                return json_resp
            except IndexError:
                logger.warning('Warning: Object Not found for %s named %s', path, name)
                return None

        def get_object_by_name(self, path, name, tenant='', tenant_uuid='',
                               timeout=None, params=None, api_version=None,
                               **kwargs):
            """
            Helper function to access Avi REST Objects using object
            type and name. It behaves like python dictionary interface where it
            returns None when the object is not present in the AviController.
            Internally, it transforms the request to api/path?name=<name>...
            :param path: relative path to service
            :param name: name of the object
            :param tenant: overrides the tenant used during session creation
            :param tenant_uuid: overrides the tenant or tenant_uuid during session
                creation
            :param timeout: timeout for API calls; Default value is 60 seconds
            :param params: dictionary of key value pairs to be sent as query
                parameters
            :param api_version: overrides x-avi-header in request header during
                session creation
            returns dictionary object if successful else None
            """
            if not params:
                params = {}
            params['name'] = name

            resp = self.get(path, tenant=tenant, tenant_uuid=tenant_uuid,
                            timeout=timeout,
                            params=params, api_version=api_version, **kwargs)

            # Handle auth errors with retry
            if resp.status_code in (401, 419):
                return self._handle_auth_retry_for_get(
                    path, name, tenant, tenant_uuid, timeout, params,
                    api_version, **kwargs)

            # Handle server errors
            if resp.status_code > 499 or 'Invalid version' in resp.text:
                logger.error('Error in get object by name for %s named %s. '
                             'Error: %s', path, name, resp.text)
                raise AviServerError(resp.text, rsp=resp)

            # Handle client errors
            if resp.status_code > 299:
                return None

            self._update_session_last_used()
            return self._extract_object_from_response(resp, path, name)

        def post(self, path, data=None, tenant='', tenant_uuid='', timeout=None,
                 force_uuid=None, params=None, api_version=None, **kwargs):
            """
            It extends the Session Library interface to add AVI API prefixes,
            handle session exceptions related to authentication and update
            the global user session cache.
            :param path: takes relative path to the AVI api.It is modified by
            the library to conform to AVI Controller's REST API interface
            :param data: dictionary of the data. Support for json string
                is deprecated
            :param tenant: overrides the tenant used during session creation
            :param tenant_uuid: overrides the tenant or tenant_uuid during session
                creation
            :param timeout: timeout for API calls; Default value is 60 seconds
            :param params: dictionary of key value pairs to be sent as query
                parameters
            :param api_version: overrides x-avi-header in request header during
                session creation
            returns session's response object
            """
            if force_uuid is not None:
                headers = kwargs.get('headers', {})
                headers[self.AVI_SLUG] = force_uuid
                kwargs['headers'] = headers
            return self._api('post', path, tenant, tenant_uuid, data=data,
                             timeout=timeout, params=params,
                             api_version=api_version, **kwargs)

        def put(self, path, data=None, tenant='', tenant_uuid='',
                timeout=None, params=None, api_version=None, **kwargs):
            """
            It extends the Session Library interface to add AVI API prefixes,
            handle session exceptions related to authentication and update
            the global user session cache.
            :param path: takes relative path to the AVI api.It is modified by
                the library to conform to AVI Controller's REST API interface
            :param data: dictionary of the data. Support for json string
                is deprecated
            :param tenant: overrides the tenant used during session creation
            :param tenant_uuid: overrides the tenant or tenant_uuid during session
                creation
            :param timeout: timeout for API calls; Default value is 60 seconds
            :param params: dictionary of key value pairs to be sent as query
                parameters
            :param api_version: overrides x-avi-header in request header during
                session creation
            returns session's response object
            """
            return self._api('put', path, tenant, tenant_uuid, data=data,
                             timeout=timeout, params=params,
                             api_version=api_version, **kwargs)

        def patch(self, path, data=None, tenant='', tenant_uuid='',
                  timeout=None, params=None, api_version=None, **kwargs):
            """
            It extends the Session Library interface to add AVI API prefixes,
            handle session exceptions related to authentication and update
            the global user session cache.
            :param path: takes relative path to the AVI api.It is modified by
                the library to conform to AVI Controller's REST API interface
            :param data: dictionary of the data. Support for json string
                is deprecated
            :param tenant: overrides the tenant used during session creation
            :param tenant_uuid: overrides the tenant or tenant_uuid during session
                creation
            :param timeout: timeout for API calls; Default value is 60 seconds
            :param params: dictionary of key value pairs to be sent as query
                parameters
            :param api_version: overrides x-avi-header in request header during
                session creation
            returns session's response object
            """
            return self._api('patch', path, tenant, tenant_uuid, data=data,
                             timeout=timeout, params=params,
                             api_version=api_version, **kwargs)

        def put_by_name(self, path, name, data=None, tenant='',
                        tenant_uuid='', timeout=None, params=None,
                        api_version=None, **kwargs):
            """
            Helper function to perform HTTP PUT on Avi REST Objects using object
            type and name.
            Internally, it transforms the request to api/path?name=<name>...
            :param path: relative path to service
            :param name: name of the object
            :param data: dictionary of the data. Support for json string
                is deprecated
            :param tenant: overrides the tenant used during session creation
            :param tenant_uuid: overrides the tenant or tenant_uuid during session
                creation
            :param timeout: timeout for API calls; Default value is 60 seconds
            :param params: dictionary of key value pairs to be sent as query
                parameters
            :param api_version: overrides x-avi-header in request header during
                session creation
            returns session's response object
            """
            uuid = self._get_uuid_by_name(
                path, name, tenant, tenant_uuid, api_version=api_version)
            path = '%s/%s' % (path, uuid)
            return self.put(path, data, tenant, tenant_uuid, timeout=timeout,
                            params=params, api_version=api_version, **kwargs)

        def delete(self, path, tenant='', tenant_uuid='',
                   timeout=None, params=None, data=None,
                   api_version=None, **kwargs):
            """
            It extends the Session Library interface to add AVI API prefixes,
            handle session exceptions related to authentication and update
            the global user session cache.
            :param path: takes relative path to the AVI api.It is modified by
            the library to conform to AVI Controller's REST API interface
            :param tenant: overrides the tenant used during session creation
            :param tenant_uuid: overrides the tenant or tenant_uuid during session
                creation
            :param timeout: timeout for API calls; Default value is 60 seconds
            :param params: dictionary of key value pairs to be sent as query
                parameters
            :param data: dictionary of the data. Support for json string
                is deprecated
            :param api_version: overrides x-avi-header in request header during
                session creation
            returns session's response object
            """
            return self._api('delete', path, tenant, tenant_uuid, data=data,
                             timeout=timeout, params=params,
                             api_version=api_version, **kwargs)

        def delete_by_name(self, path, name, tenant='', tenant_uuid='',
                           timeout=None, params=None, api_version=None, **kwargs):
            """
            Helper function to perform HTTP DELETE on Avi REST Objects using object
            type and name.Internally, it transforms the request to
            api/path?name=<name>...
            :param path: relative path to service
            :param name: name of the object
            :param tenant: overrides the tenant used during session creation
            :param tenant_uuid: overrides the tenant or tenant_uuid during session
                creation
            :param timeout: timeout for API calls; Default value is 60 seconds
            :param params: dictionary of key value pairs to be sent as query
                parameters
            :param api_version: overrides x-avi-header in request header during
                session creation
            returns session's response object
            """
            uuid = self._get_uuid_by_name(path, name, tenant, tenant_uuid,
                                          api_version=api_version)
            if not uuid:
                raise ObjectNotFound("%s/?name=%s" % (path, name))
            path = '%s/%s' % (path, uuid)
            return self.delete(path, tenant, tenant_uuid, timeout=timeout,
                               params=params, api_version=api_version, **kwargs)

        def get_obj_ref(self, obj):
            """returns reference url from dict object"""
            if not obj:
                return None
            if isinstance(obj, Response):
                obj = json.loads(obj.text)
            if obj.get(0, None):
                return obj[0]['url']
            elif obj.get('url', None):
                return obj['url']
            elif obj.get('results', None):
                return obj['results'][0]['url']
            else:
                return None

        def get_obj_uuid(self, obj):
            """returns uuid from dict object"""
            if not obj:
                raise ObjectNotFound('Object %s Not found' % (obj))
            if isinstance(obj, Response):
                obj = json.loads(obj.text)
            if obj.get('uuid', None):
                return obj['uuid'].split('#')[0]
            elif obj.get('results', None):
                return obj['results'][0]['uuid'].split('#')[0]
            else:
                return None

        def _paginator(self, *args, **kwargs):
            """
            This is a private method to simulate an iterator
            on top of the pagination functionality provided by Avi Controller.

            :param *args: Accepts all args accepted by get method of class
                ApiSession.
            :params **kwargs: Accepts all kwargs accepted by get method of class
                ApiSession.

            Yields batch of objects in the range of 0 to page_size passed in kwargs.
            """
            resp = self.get(*args, **kwargs).json()
            if 'results' in resp:
                yield resp['results']
            else:
                # For apis returning single object eg. api/cluster
                yield [resp]

            page = 2  # Initialized to 2 for new page requests
            while resp.get('next', None) is not None:
                kwargs['params']['page'] = page
                resp = self.get(*args, **kwargs).json()
                page += 1
                yield resp['results']

        def get_objects_iter(self, obj_type, tenant='', tenant_uuid='',
                             timeout=None, params=None, api_version=None, **kwargs):
            """
            Iterator to fetch objects of any type from Avi Controller.
            By default, 100 objects are fetched in every batch. However, user can
            override this behaviour by passing page_size as params.

            Irrespective of page_size the method will yield only one object for
            each iteration.

            :param obj_type: Type of object that needs to be fetched from Avi Controller. Ex: pool, virtualservice
            :param tenant: overrides the tenant used during session creation.
            :param tenant_uuid: overrides the tenant or tenant_uuid during session
                creation.
            :param timeout: timeout for API calls; Default value is 60 seconds.
            :param params: dictionary of key value pairs to be sent as query
                parameters.
            :param api_version: overrides x-avi-header in request header during
                session creation.
            :param **kwargs: Accepts any other params accepted by Session class get method.

            Yields objects of type obj_type one by one. Example

            >>> # Looping over get_objects_iter
            >>> all_pools_iter = get_objects_iter('pool', params={'fields':'name'})
            >>> for pool in all_pools_iter:
            ...  #Do something with pool
            ...  print(pool)
            {u'name': u'pool-avi',
            u'server_count': 0,
            u'url': u'https://192.10.20.30/api/pool/<uuid>',
            u'uuid': u'<uuid>'}
            """
            if params is None:
                params = {}

            if params.get('page_size', None) is None:
                params['page_size'] = 100

            page_size = params.get('page_size')
            if int(page_size) > 200:
                raise ValueError('page_size cannot be more than 200')
            pages_iter = self._paginator(obj_type, tenant=tenant, params=params,
                                         tenant_uuid=tenant_uuid, timeout=timeout,
                                         api_version=api_version, **kwargs)
            for page in pages_iter:
                yield from page

        def get_slug_from_uri(self, uri):
            """return uuid/slug from URI"""
            if not uri or '/' not in uri:
                return uri
            parsed = urlparse(uri)
            path = parsed.path
            uuid = os.path.basename(path)
            if '#' in uuid:
                uuid = uuid.split('#')[0]
            return uuid

        def _get_api_path(self, path, uuid=None):
            """
            This function returns the full url from relative path and uuid.
            """
            if path == 'logout':
                return self.prefix + '/' + path
            elif uuid:
                return self.prefix + '/api/' + path + '/' + uuid
            else:
                return self.prefix + '/api/' + path

        def _get_uuid_by_name(self, path, name, tenant='admin',
                              tenant_uuid='', api_version=None):
            """gets object by name and service path and returns uuid"""
            resp = self.get_object_by_name(
                path, name, tenant, tenant_uuid, api_version=api_version)
            if not resp:
                raise ObjectNotFound("%s/%s" % (path, name))
            return self.get_obj_uuid(resp)

        # @AI-Modified: 2026-01-23 - Replaced datetime.utcnow() with get_utc_now()
        def _update_session_last_used(self):
            if self.key in sessionDict:
                sessionDict[self.key]["last_used"] = get_utc_now()

        # @AI-Modified: 2026-01-23 - Replaced datetime.utcnow() with get_utc_now() and refactored to reduce complexity
        @staticmethod
        def _clean_inactive_sessions():
            """Removes sessions which are inactive more than 20 min"""
            session_cache = sessionDict
            logger.debug("cleaning inactive sessions in pid %d num elem %d",
                         os.getpid(), len(session_cache))
            for key, session in list(session_cache.items()):
                tdiff = avi_timedelta(get_utc_now() - session["last_used"])
                if tdiff < ApiSession.SESSION_CACHE_EXPIRY:
                    continue
                ApiSession._logout_and_remove_session(session_cache, key, session)

        @staticmethod
        def _logout_and_remove_session(session_cache, key, session):
            """
            Logout and remove a session from the cache.

            Parameters:
                session_cache: The session cache dictionary
                key: The session key
                session: The session data
            """
            try:
                session["api"].post("logout")
            except Exception as e:
                logger.warning("Session not found on controller "
                               "for session ID: %s %s",
                               session, e)
            if session_cache.get(key):
                del session_cache[key]
            logger.debug("Cleaned inactive session : %s", key)

        def delete_session(self):
            """ Removes the session for cleanup"""
            logger.debug("Removed session for : %s", self.key)
            sessionDict.pop(self.key, None)
            return

        def is_ipv6_address(self, controller_ip):
            try:
                logger.info('Verifing Controller IP %s', controller_ip)
                ip = ipaddress.ip_address(controller_ip)
                return ip.version == self.IPV6
            except ValueError as ve:
                logger.warning('Invalid Controller IP6 Address: %s - %s', controller_ip, ve)
                return False
    # End of file
else:
    ApiSession = None
