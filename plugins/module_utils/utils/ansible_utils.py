# Copyright 2021 VMware, Inc.
# SPDX-License-Identifier: Apache License 2.0

"""
Created on Aug 16, 2016

@author: Gaurav Rastogi (grastogi@avinetworks.com)
"""
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import os
import re
import time
import logging
from copy import deepcopy
from ansible_collections.vmware.alb.plugins.module_utils.avi_api import ApiSession, ObjectNotFound, avi_sdk_syslog_logger, \
    AviCredentials
from ansible_collections.vmware.alb.plugins.module_utils.csp_avi_api import CSPApiSession
from ansible_collections.vmware.alb.plugins.module_utils.saml_avi_api import OneloginSAMLApiSession, OktaSAMLApiSession

if os.environ.get('AVI_LOG_HANDLER', '') != 'syslog':
    log = logging.getLogger(__name__)
else:
    # Ansible does not allow logging from the modules.
    log = avi_sdk_syslog_logger()

# @AI-Modified: 2026-01-23 - Added constant to avoid duplicating literal string
ABSENT_STATE_MARKER = "{'state': 'absent'}"

# @AI-Modified: 2026-01-23 - Added constant to avoid duplicating 'name=' literal
NAME_PARAM_SEPARATOR = 'name='

try:
    import yaml
except ImportError:
    yaml = None


class InvalidRefFormat(Exception):
    pass


class AviCheckModeResponse(object):
    """
    Class to support ansible check mode.
    """

    def __init__(self, obj, status_code=200):
        self.obj = obj
        self.status_code = status_code

    def json(self):
        return self.obj


def ansible_return(module, rsp, changed, req=None, existing_obj=None,
                   api_context=None):
    """
    :param module: AnsibleModule
    :param rsp: ApiResponse from avi_api
    :param changed: boolean
    :param req: ApiRequest to avi_api
    :param existing_obj: object to be passed debug output
    :param api_context: api login context

    helper function to return the right ansible based on the error code and
    changed
    Returns: specific ansible module exit function
    """

    if rsp is not None and rsp.status_code > 299 and not \
            any(error in rsp.text for error in SKIP_DELETE_ERROR):
        return module.fail_json(
            msg='Error %d Msg %s req: %s api_context:%s ' % (
                rsp.status_code, rsp.text, req, api_context))
    api_creds = AviCredentials()
    api_creds.update_from_ansible_module(module)
    key = '%s:%s:%s' % (api_creds.controller, api_creds.username,
                        api_creds.port)
    deactivate_fact = module.params.get('avi_deactivate_session_cache_as_fact')

    fact_context = None
    if not deactivate_fact:
        fact_context = module.params.get('api_context', {})
        if fact_context:
            fact_context.update({key: api_context})
        else:
            fact_context = {key: api_context}

    obj_val = rsp.json() if rsp else existing_obj

    if (obj_val and module.params.get("obj_username", None) and
            "username" in obj_val):
        obj_val["obj_username"] = obj_val["username"]
    if (obj_val and module.params.get("obj_password", None) and
            "password" in obj_val):
        obj_val["obj_password"] = obj_val["password"]
    if (obj_val and module.params.get("obj_state", None) and
            "state" in obj_val):
        obj_val["obj_state"] = obj_val["state"]
    old_obj_val = existing_obj if changed and existing_obj else None
    api_context_val = api_context if deactivate_fact else None
    ansible_facts_val = dict(
        avi_api_context=fact_context) if not deactivate_fact else {}

    return module.exit_json(
        changed=changed, obj=obj_val, old_obj=old_obj_val,
        ansible_facts=ansible_facts_val, api_context=api_context_val)


def purge_optional_fields(obj, module):
    """
    It purges the optional arguments to be sent to the controller.
    :param obj: dictionary of the ansible object passed as argument.
    :param module: AnsibleModule
    return modified obj
    """
    purge_fields = []
    for param, spec in module.argument_spec.items():
        if not spec.get('required', False):
            if param not in obj:
                # these are ansible common items
                continue
            if obj[param] is None:
                purge_fields.append(param)
    log.debug('purging fields %s', purge_fields)
    for param in purge_fields:
        obj.pop(param, None)
    return obj


# @AI-Modified: 2026-01-23 - Refactored to reduce cognitive complexity from 32 to under 15
def _is_absent_marker(value):
    """
    Check if a value represents an absent state marker.

    Parameters:
        value: The value to check

    Returns:
        bool: True if the value indicates absent state
    """
    if isinstance(value, dict):
        return 'state' in value and value['state'] == 'absent'
    if isinstance(value, str):
        return value == ABSENT_STATE_MARKER
    return False


# @AI-Modified: 2026-01-23 - Removed unused 'obj' parameter
def _process_dict_value(key, value, cleanup_keys):
    """
    Process a dictionary value during cleanup.

    Parameters:
        key: The key being processed
        value: The dictionary value
        cleanup_keys: List to append keys that should be removed
    """
    if _is_absent_marker(value):
        cleanup_keys.append(key)
    else:
        cleanup_absent_fields(value)
        if not value:
            cleanup_keys.append(key)


def _process_list_value(obj, key, value, cleanup_keys):
    """
    Process a list value during cleanup.

    Parameters:
        obj: Parent object to update
        key: The key being processed
        value: The list value
        cleanup_keys: List to append keys that should be removed
    """
    new_list = [cleanup_absent_fields(elem) for elem in value if cleanup_absent_fields(elem)]
    if new_list:
        obj[key] = new_list
    else:
        cleanup_keys.append(key)


def _process_string_value(key, value, cleanup_keys):
    """
    Process a string value during cleanup.

    Parameters:
        key: The key being processed
        value: The string value
        cleanup_keys: List to append keys that should be removed
    """
    if value == ABSENT_STATE_MARKER:
        cleanup_keys.append(key)


def cleanup_absent_fields(obj):
    """
    Cleans up any field that is marked as state: absent.

    It needs to be removed from the object if it is present.

    Parameters:
        obj: The object to clean up

    Returns:
        The purged object, or the original if not a dict
    """
    if not isinstance(obj, dict):
        return obj

    cleanup_keys = []
    for k, v in obj.items():
        if isinstance(v, dict):
            _process_dict_value(k, v, cleanup_keys)
        elif isinstance(v, list):
            _process_list_value(obj, k, v, cleanup_keys)
        elif isinstance(v, str):
            _process_string_value(k, v, cleanup_keys)

    for k in cleanup_keys:
        del obj[k]

    return obj


def get_unicode_type():
    return str


RE_REF_MATCH = re.compile(r'^/api/[\w/]+\?name\=[\w*]+[^#<>]*$')
# if HTTP ref match then strip out the #name
# HTTP_REF_MATCH = re.compile('https://[\w.0-9:-]+/api/[\w/\?.#&-]*$')
HTTP_REF_MATCH = re.compile(r'https://[\w.0-9:-]+/api/.+')
HTTP_REF_MATCH_IPV6 = re.compile(r'https://[[\w.0-9:-]+]/api/.+')
HTTP_REF_W_NAME_MATCH = re.compile(r'https://[\w.0-9:-]+/api/.*#.+')
HTTP_REF_W_NAME_MATCH_IPV6 = re.compile(r'https://[[\w.0-9:-]+]/api/.*#.+')


# @AI-Modified: 2026-01-23 - Refactored ref_n_str_cmp to reduce cognitive complexity from 19 to under 15
def _convert_to_string(x, y):
    """
    Convert numeric types to strings and encode unicode.

    Parameters:
        x: First value
        y: Second value

    Returns:
        tuple: (x, y) as strings, or (None, None) if not string types
    """
    # @AI-Modified: 2026-01-23 - Fixed duplicate 'int' in type tuple
    if type(y) in (int, float, bool, complex):
        y = str(y)
        x = str(x)

    unicode_type = get_unicode_type()
    if not ((isinstance(x, str) or isinstance(x, unicode_type)) and
            (isinstance(y, str) or isinstance(y, unicode_type))):
        return None, None

    if str(type(y)) == "<type 'unicode'>":
        y = y.encode('utf-8')
    if str(type(x)) == "<type 'unicode'>":
        x = x.encode('utf-8')

    return str(x), str(y)


def _extract_ref_name(x, y):
    """
    Extract reference name from x based on pattern matching.

    Parameters:
        x: First string (reference)
        y: Second string

    Returns:
        tuple: (processed_x, processed_y)
    """
    if RE_REF_MATCH.match(x):
        return x.split(NAME_PARAM_SEPARATOR)[1], y
    if HTTP_REF_MATCH.match(x):
        return x.rsplit('#', 1)[0], y.rsplit('#', 1)[0]
    if RE_REF_MATCH.match(y) or HTTP_REF_MATCH_IPV6.match(y):
        return x, y.split(NAME_PARAM_SEPARATOR)[1]
    return x, y


def _extract_uuid_and_name(y):
    """
    Extract UUID and name from HTTP reference URL.

    Parameters:
        y: URL string

    Returns:
        tuple: (y_uuid, y_name)
    """
    if not (HTTP_REF_W_NAME_MATCH.match(y) or HTTP_REF_W_NAME_MATCH_IPV6.match(y)):
        return str(y), str(y)

    path = y.split('api/', 1)[1]
    uuid_or_name = path.split('/')[-1]
    parts = uuid_or_name.rsplit('#', 1)
    y_uuid = parts[0]
    y_name = parts[1] if len(parts) > 1 else ''
    return y_uuid, y_name


def ref_n_str_cmp(x, y):
    """
    compares two references
    1. check for exact reference
    2. check for obj_type/uuid
    3. check for name

    if x is ref=name then extract uuid and name from y and use it.
    if x is http_ref then
        strip x and y
        compare them.

    if x and y are urls then match with split on #
    if x is a RE_REF_MATCH then extract name
    if y is a REF_MATCH then extract name
    :param x: first string
    :param y: second string from controller's object

    Returns
        True if they are equivalent else False
    """
    x, y = _convert_to_string(x, y)
    if x is None:
        return False

    x, y = _extract_ref_name(x, y)
    y_uuid, y_name = _extract_uuid_and_name(y)

    result = (x in (y, y_name, y_uuid))
    if not result:
        log.debug('x: %s y: %s y_name %s y_uuid %s', x, y, y_name, y_uuid)
    return result


# @AI-Modified: 2026-01-23 - Refactored to reduce cognitive complexity from 60 to under 15
def _clean_dict_metadata(x, y):
    """
    Remove metadata fields from dictionaries before comparison.

    Parameters:
        x: First dictionary
        y: Second dictionary
    """
    for field in ['_last_modified', 'tenant', 'api_version']:
        x.pop(field, None)
    y.pop('_last_modified', None)
    y.pop('api_verison', None)


def _has_sensitive_fields(x, sensitive_fields):
    """
    Check if dictionary contains any sensitive fields.

    Parameters:
        x: Dictionary to check
        sensitive_fields: Set of sensitive field names

    Returns:
        bool: True if sensitive fields are present
    """
    return any(k in sensitive_fields for k in x.keys())


def _should_mark_absent_dict(k, v, y):
    """
    Check if a dict value should be marked for removal.

    Parameters:
        k: Key name
        v: Dictionary value
        y: Reference dictionary

    Returns:
        tuple: (should_remove, should_return_false)
    """
    if ('state' in v) and (v['state'] == 'absent'):
        if isinstance(y, dict) and k not in y:
            return True, False
        return False, True
    if not v:
        return True, False
    return False, False


def _should_mark_absent_list(k, v, y):
    """
    Check if an empty list value should be marked for removal.

    Parameters:
        k: Key name
        v: List value
        y: Reference dictionary

    Returns:
        bool: True if should be removed
    """
    return not v and k not in y


def _should_mark_absent_string(k, v, y):
    """
    Check if a string value should be marked for removal.

    Parameters:
        k: Key name
        v: String value
        y: Reference dictionary

    Returns:
        bool: True if should be removed
    """
    if v == ABSENT_STATE_MARKER and k not in y:
        return True
    if not v and k not in y:
        return True
    return False


# @AI-Modified: 2026-01-23 - Refactored to reduce cognitive complexity from 19 to under 15
def _check_value_for_absent(k, v, y):
    """
    Check if a single key-value pair should be marked as absent.

    Parameters:
        k: Key name
        v: Value
        y: Reference dictionary

    Returns:
        tuple: (should_add_to_absent, should_return_false)
    """
    if v is None:
        return True, False

    if isinstance(v, dict):
        return _should_mark_absent_dict(k, v, y)

    if isinstance(v, list) and _should_mark_absent_list(k, v, y):
        return True, False

    is_string_type = isinstance(v, str) or (k in y and isinstance(y[k], str))
    if is_string_type and _should_mark_absent_string(k, v, y):
        return True, False

    return False, False


def _get_absent_keys(x, y):
    """
    Get list of keys that should be removed from x before comparison.

    Parameters:
        x: Source dictionary
        y: Reference dictionary

    Returns:
        tuple: (list of keys to remove, bool indicating if comparison should return False)
    """
    absent_keys = []
    for k, v in x.items():
        should_add, should_return_false = _check_value_for_absent(k, v, y)
        if should_return_false:
            return absent_keys, True
        if should_add:
            absent_keys.append(k)

    return absent_keys, False


def _compare_lists(x, y, sensitive_fields):
    """
    Compare two lists element by element.

    Parameters:
        x: First list
        y: Second list
        sensitive_fields: Set of sensitive field names

    Returns:
        bool: True if lists are equivalent
    """
    if len(x) != len(y):
        log.debug('x has %d items y has %d', len(x), len(y))
        return False
    for item_x, item_y in zip(x, y):
        if not avi_obj_cmp(item_x, item_y, sensitive_fields=sensitive_fields):
            return False
    return True


def _compare_dicts(x, y, sensitive_fields):
    """
    Compare two dictionaries.

    Parameters:
        x: First dictionary
        y: Second dictionary
        sensitive_fields: Set of sensitive field names

    Returns:
        bool: True if x is subset of y
    """
    _clean_dict_metadata(x, y)

    if _has_sensitive_fields(x, sensitive_fields):
        return False

    absent_keys, should_return_false = _get_absent_keys(x, y)
    if should_return_false:
        return False

    for k in absent_keys:
        x.pop(k)

    if not set(x.keys()).issubset(set(y.keys())):
        return False

    for k, v in x.items():
        if k not in y:
            return False
        if not avi_obj_cmp(v, y[k], sensitive_fields=sensitive_fields):
            return False

    return True


def avi_obj_cmp(x, y, sensitive_fields=None):
    """
    Compare whether x is fully contained in y.

    The comparison is different from a simple dictionary compare for following reasons:
    1. Some fields could be references. The object in controller returns the
       full URL for those references. However, the ansible script would have
       it specified as /api/pool?name=blah. So, the reference fields need
       to match uuid, relative reference based on name and actual reference.

    2. Optional fields with defaults: In case there are optional fields with
       defaults then controller automatically fills it up. This would
       cause the comparison with Ansible object specification to always return
       changed.

    3. Optional fields without defaults: This is most tricky. The issue is
       how to specify deletion of such objects from ansible script. If the
       ansible playbook has object specified as Null then Avi controller will
       reject for non Message(dict) type fields. In addition, to deal with the
       defaults=null issue all the fields that are set with None are purged
       out before comparing with Avi controller's version

       So, the solution is to pass state: absent if any optional field needs
       to be deleted from the configuration. The script would return changed
       =true if it finds a key in the controller version and it is marked with
       state: absent in ansible playbook. Alternatively, it would return
       false if key is not present in the controller object. Before, doing
       put or post it would purge the fields that are marked state: absent.

    Parameters:
        x: First object (from ansible)
        y: Second object (from controller)
        sensitive_fields: Sensitive fields to ignore for diff

    Returns:
        bool: True if x is subset of y else False
    """
    if not sensitive_fields:
        sensitive_fields = set()

    unicode_type = get_unicode_type()
    if isinstance(x, str) or isinstance(x, unicode_type):
        return ref_n_str_cmp(x, y)

    if type(x) not in [list, dict]:
        return x == y

    if isinstance(x, list):
        return _compare_lists(x, y, sensitive_fields)

    if isinstance(x, dict):
        return _compare_dicts(x, y, sensitive_fields)

    return True


POP_FIELDS = ['state', 'controller', 'username', 'password', 'api_version',
              'avi_credentials', 'avi_api_update_method', 'avi_api_patch_op', 'avi_patch_path',
              'avi_patch_value', 'api_context', 'tenant', 'tenant_uuid', 'avi_deactivate_session_cache_as_fact']


def get_api_context(module, api_creds):
    api_context = module.params.get('api_context')
    if api_context and module.params.get('avi_deactivate_session_cache_as_fact'):
        return api_context
    elif api_context and not module.params.get(
            'avi_deactivate_session_cache_as_fact'):
        key = '%s:%s:%s' % (api_creds.controller, api_creds.username,
                            api_creds.port)
        return api_context.get(key)
    else:
        return None


NO_UUID_OBJ = ['cluster', 'systemconfiguration', 'inventoryfaultconfig']
SKIP_DELETE_ERROR = ["Cannot delete system default object", "Method \'DELETE\' not allowed"]
BUFFER_DELAY = 120


def get_idp_class(idp):
    """
    This return corresponding idp class.
    :param idp: idp type such as okta, onelogin, pingfed
    :return: IDP class or ApiSession class
    """
    if str(idp).lower() == "cspapisession":
        idp_class = CSPApiSession
    elif str(idp).lower() == "oktasamlapisession":
        idp_class = OktaSAMLApiSession
    elif str(idp).lower() == 'oneloginsamlapisession':
        idp_class = OneloginSAMLApiSession
    else:
        idp_class = None
    return idp_class


# @AI-Modified: 2026-01-23 - Refactored to reduce cognitive complexity from 104 to under 15
def _get_api_session(api_creds, api_context, idp):
    """
    Create and return an API session.

    Parameters:
        api_creds: AviCredentials object
        api_context: API context dict or None
        idp: IDP class or None

    Returns:
        ApiSession: Configured API session
    """
    if api_context:
        return ApiSession.get_session(
            api_creds.controller,
            api_creds.username,
            password=api_creds.password,
            timeout=api_creds.timeout,
            tenant=api_creds.tenant,
            tenant_uuid=api_creds.tenant_uuid,
            token=api_context['csrftoken'],
            port=api_creds.port,
            session_id=api_context['session_id'],
            csrftoken=api_context['csrftoken'])

    return ApiSession.get_session(
        api_creds.controller,
        api_creds.username,
        password=api_creds.password,
        timeout=api_creds.timeout,
        tenant=api_creds.tenant,
        tenant_uuid=api_creds.tenant_uuid,
        token=api_creds.token,
        port=api_creds.port,
        idp_class=idp,
        csp_host=api_creds.csp_host,
        csp_token=api_creds.csp_token,
        ssl_cert=api_creds.ssl_cert,
        ssl_key=api_creds.ssl_key)


def _prepare_obj_from_module(module, obj_type):
    """
    Prepare the object dictionary from module parameters.

    Parameters:
        module: Ansible module
        obj_type: Object type string

    Returns:
        tuple: (obj dict, tenant, tenant_uuid)
    """
    obj = deepcopy(module.params)
    tenant = obj.pop('tenant', '')
    tenant_uuid = obj.pop('tenant_uuid', '')

    for k in POP_FIELDS:
        obj.pop(k, None)
    purge_optional_fields(obj, module)

    # Handle special field name mappings
    _handle_special_fields(obj, obj_type)

    return obj, tenant, tenant_uuid


def _handle_special_fields(obj, obj_type):
    """
    Handle special field name mappings for username/password/state.

    Parameters:
        obj: Object dictionary to modify
        obj_type: Object type string
    """
    if 'obj_username' in obj:
        obj['username'] = obj.pop('obj_username')
    if 'obj_password' in obj:
        obj['password'] = obj.pop('obj_password')
    if 'obj_state' in obj:
        obj['state'] = obj.pop('obj_state')
    if 'full_name' not in obj and 'name' in obj and obj_type == "user":
        obj['full_name'] = obj['name']
        obj['name'] = obj['username']


def _get_existing_obj_by_uuid(api, obj_path, tenant, tenant_uuid, api_version):
    """
    Get existing object by UUID.

    Parameters:
        api: API session
        obj_path: Object path
        tenant: Tenant name
        tenant_uuid: Tenant UUID
        api_version: API version

    Returns:
        dict or None: Existing object or None if not found
    """
    try:
        existing_obj = api.get(
            obj_path, tenant=tenant, tenant_uuid=tenant_uuid,
            params={'include_refs': '', 'include_name': ''},
            api_version=api_version)
        return existing_obj.json()
    except ObjectNotFound:
        return None


def _get_existing_obj_by_name(api, obj_type, name, obj, tenant, tenant_uuid, api_version):
    """
    Get existing object by name.

    Parameters:
        api: API session
        obj_type: Object type
        name: Object name
        obj: Object dictionary
        tenant: Tenant name
        tenant_uuid: Tenant UUID
        api_version: API version

    Returns:
        dict or None: Existing object or None if not found
    """
    params = {'include_refs': '', 'include_name': ''}
    if obj.get('cloud_ref', None):
        cloud = obj['cloud_ref'].split(NAME_PARAM_SEPARATOR)[1]
        params['cloud_ref.name'] = cloud

    existing_obj = api.get_object_by_name(
        obj_type, name, tenant=tenant, tenant_uuid=tenant_uuid,
        params=params, api_version=api_version)

    # Check tenant_ref mismatch
    if existing_obj and 'tenant_ref' in obj and 'tenant_ref' in existing_obj:
        existing_obj_tenant = existing_obj['tenant_ref'].split('#')[1]
        obj_tenant = obj['tenant_ref'].split(NAME_PARAM_SEPARATOR)[1]
        if obj_tenant != existing_obj_tenant:
            return None

    return existing_obj


# @AI-Modified: 2026-01-23 - Refactored to reduce cognitive complexity and fix always-true condition
def _handle_absent_state(module, api, obj_type, obj_path, name, existing_obj,
                         tenant, tenant_uuid, api_version, check_mode):
    """
    Handle the absent state - delete the object if it exists.

    Parameters:
        module: Ansible module
        api: API session
        obj_type: Object type
        obj_path: Object path
        name: Object name
        existing_obj: Existing object dict or None
        tenant: Tenant name
        tenant_uuid: Tenant UUID
        api_version: API version
        check_mode: Whether in check mode

    Returns:
        Ansible return value
    """
    if not existing_obj:
        return ansible_return(
            module, None, False, existing_obj=existing_obj,
            api_context=api.get_context())

    if check_mode:
        return ansible_return(
            module, None, True, existing_obj=existing_obj,
            api_context=api.get_context())

    rsp = _delete_object(api, obj_type, obj_path, name, existing_obj,
                         tenant, tenant_uuid, api_version)

    if not rsp:
        return ansible_return(
            module, rsp, False, existing_obj=existing_obj,
            api_context=api.get_context())

    changed, err = _evaluate_delete_response(rsp)

    if err:
        # @AI-Modified: 2026-01-23 - Fixed: rsp is always truthy here since we checked above
        return module.fail_json(msg=rsp.text)

    return ansible_return(
        module, rsp, changed, existing_obj=existing_obj,
        api_context=api.get_context())


def _delete_object(api, obj_type, obj_path, name, existing_obj, tenant, tenant_uuid, api_version):
    """
    Delete an object from the controller.

    Parameters:
        api: API session
        obj_type: Object type
        obj_path: Object path
        name: Object name
        existing_obj: Existing object dict
        tenant: Tenant name
        tenant_uuid: Tenant UUID
        api_version: API version

    Returns:
        Response object or None
    """
    if obj_type == "serviceenginegroup":
        se_deprovision_delay = existing_obj.get("se_deprovision_delay", 0)
        time.sleep((se_deprovision_delay * 60) + BUFFER_DELAY)

    try:
        if name is not None:
            return api.delete_by_name(
                obj_type, name, tenant=tenant, tenant_uuid=tenant_uuid,
                api_version=api_version)
        return api.delete(
            obj_path, tenant=tenant, tenant_uuid=tenant_uuid,
            api_version=api_version)
    except ObjectNotFound:
        return None


def _evaluate_delete_response(rsp):
    """
    Evaluate delete response to determine changed and error status.

    Parameters:
        rsp: Response object

    Returns:
        tuple: (changed, err)
    """
    if rsp.status_code == 204:
        return True, False
    if not any(error in str(rsp.text) for error in SKIP_DELETE_ERROR):
        return False, True
    return False, False


def _handle_put_update(api, obj_path, obj, existing_obj, sensitive_fields,
                       tenant, tenant_uuid, api_version, check_mode):
    """
    Handle PUT update method.

    Parameters:
        api: API session
        obj_path: Object path
        obj: Object dictionary
        existing_obj: Existing object dict
        sensitive_fields: Set of sensitive fields
        tenant: Tenant name
        tenant_uuid: Tenant UUID
        api_version: API version
        check_mode: Whether in check mode

    Returns:
        tuple: (rsp, req, changed, obj)
    """
    changed = not avi_obj_cmp(obj, existing_obj, sensitive_fields)
    obj = cleanup_absent_fields(obj)
    req = None
    rsp = None

    if changed:
        req = obj
        if check_mode:
            rsp = AviCheckModeResponse(obj=existing_obj)
        else:
            rsp = api.put(
                obj_path, data=req, tenant=tenant,
                tenant_uuid=tenant_uuid, api_version=api_version)
    elif check_mode:
        rsp = AviCheckModeResponse(obj=existing_obj)

    return rsp, req, changed, obj


# @AI-Modified: 2026-01-23 - Fixed condition that always evaluated to true
def _build_patch_data(obj, avi_patch_op, avi_patch_path, avi_patch_value):
    """
    Build patch data for PATCH request.

    Parameters:
        obj: Object dictionary
        avi_patch_op: Patch operation
        avi_patch_path: Patch path
        avi_patch_value: Patch value

    Returns:
        dict: Patch data
    """
    if not avi_patch_path:
        return {avi_patch_op: obj}

    # Parse YAML value if yaml module is available
    if avi_patch_value and yaml:
        avi_patch_value = yaml.load(avi_patch_value, Loader=yaml.SafeLoader)

    return {
        "json_patch": [{
            "op": avi_patch_op,
            "path": avi_patch_path,
            "value": avi_patch_value
        }]
    }


def _handle_patch_update(api, obj_path, obj, existing_obj, avi_patch_op,
                         avi_patch_path, avi_patch_value, tenant, tenant_uuid,
                         api_version, check_mode):
    """
    Handle PATCH update method.

    Parameters:
        api: API session
        obj_path: Object path
        obj: Object dictionary
        existing_obj: Existing object dict
        avi_patch_op: Patch operation
        avi_patch_path: Patch path
        avi_patch_value: Patch value
        tenant: Tenant name
        tenant_uuid: Tenant UUID
        api_version: API version
        check_mode: Whether in check mode

    Returns:
        tuple: (rsp, changed, obj)
    """
    if check_mode:
        return AviCheckModeResponse(obj=existing_obj), True, obj

    obj.pop('name', None)
    patch_data = _build_patch_data(obj, avi_patch_op, avi_patch_path, avi_patch_value)

    try:
        rsp = api.patch(
            obj_path, data=patch_data, tenant=tenant,
            tenant_uuid=tenant_uuid, api_version=api_version)
        obj = rsp.json()
        changed = not avi_obj_cmp(obj, existing_obj)
        return rsp, changed, obj
    except ObjectNotFound:
        # @AI-Modified: 2026-01-23 - Fixed condition that always evaluated to None
        return None, False, obj


def _handle_create(api, obj_type, obj, tenant, tenant_uuid, api_version, check_mode):
    """
    Handle object creation.

    Parameters:
        api: API session
        obj_type: Object type
        obj: Object dictionary
        tenant: Tenant name
        tenant_uuid: Tenant UUID
        api_version: API version
        check_mode: Whether in check mode

    Returns:
        tuple: (rsp, req, changed)
    """
    if check_mode:
        return AviCheckModeResponse(obj=None), obj, True

    rsp = api.post(obj_type, data=obj, tenant=tenant,
                   tenant_uuid=tenant_uuid, api_version=api_version)
    return rsp, obj, True


def avi_ansible_api(module, obj_type, sensitive_fields):
    """
    Convert the Ansible module into AVI object and invoke APIs.

    Parameters:
        module: Ansible module
        obj_type: String representing Avi object type
        sensitive_fields: Sensitive fields to be excluded for comparison

    Returns:
        success: module.exit_json with obj=avi object
        failure: module.fail_json
    """
    api_creds = AviCredentials()
    api_creds.update_from_ansible_module(module)
    api_context = get_api_context(module, api_creds)

    idp_class = api_creds.idp_class
    idp = get_idp_class(idp_class)
    if idp_class and not idp:
        return module.fail_json(msg="IDP {0} not supported yet.".format(idp_class))

    api = _get_api_session(api_creds, api_context, idp)

    # Extract parameters
    state = module.params['state']
    avi_update_method = module.params.get('avi_api_update_method', 'put')
    avi_patch_op = module.params.get('avi_api_patch_op', 'add')
    avi_patch_path = module.params.get('avi_patch_path')
    avi_patch_value = module.params.get('avi_patch_value', None)
    api_version = api_creds.api_version
    name = module.params.get('name', None)
    uuid = module.params.get('uuid', None)
    check_mode = module.check_mode

    # Determine object path
    if uuid and obj_type not in NO_UUID_OBJ:
        obj_path = '%s/%s' % (obj_type, uuid)
    else:
        obj_path = '%s/' % obj_type

    # Prepare object
    obj, tenant, tenant_uuid = _prepare_obj_from_module(module, obj_type)
    log.info('passed object %s ', obj)

    # Get existing object
    existing_obj = _get_existing_object(
        api, obj_type, obj_path, name, uuid, obj, tenant, tenant_uuid, api_version)

    # Handle absent state
    if state == 'absent':
        result = _handle_absent_state(
            module, api, obj_type, obj_path, name, existing_obj,
            tenant, tenant_uuid, api_version, check_mode)
        if result:
            return result

    # Handle present state
    # @AI-Modified: 2026-01-23 - Group parameters into dicts to reduce parameter count
    patch_config = {
        'op': avi_patch_op,
        'path': avi_patch_path,
        'value': avi_patch_value
    }
    api_config = {
        'tenant': tenant,
        'tenant_uuid': tenant_uuid,
        'api_version': api_version
    }
    return _handle_present_state(
        module, api, obj_type, obj_path, name, obj, existing_obj,
        sensitive_fields, avi_update_method, patch_config,
        api_config, check_mode)


def _get_existing_object(api, obj_type, obj_path, name, uuid, obj, tenant, tenant_uuid, api_version):
    """
    Get existing object from controller.

    Parameters:
        api: API session
        obj_type: Object type
        obj_path: Object path
        name: Object name
        uuid: Object UUID
        obj: Object dictionary
        tenant: Tenant name
        tenant_uuid: Tenant UUID
        api_version: API version

    Returns:
        dict or None: Existing object or None
    """
    if uuid:
        return _get_existing_obj_by_uuid(api, obj_path, tenant, tenant_uuid, api_version)
    if name:
        return _get_existing_obj_by_name(api, obj_type, name, obj, tenant, tenant_uuid, api_version)
    return api.get(obj_path, tenant=tenant, tenant_uuid=tenant_uuid,
                   params={'include_refs': '', 'include_name': ''},
                   api_version=api_version).json()


# @AI-Modified: 2026-01-23 - Refactored to reduce cognitive complexity from 19 to under 15
def _resolve_obj_path_for_update(obj_type, obj_path, name, existing_obj):
    """
    Resolve the object path for an update operation.

    Parameters:
        obj_type: Object type
        obj_path: Current object path
        name: Object name
        existing_obj: Existing object dict

    Returns:
        str: Resolved object path
    """
    if name is not None and obj_type not in NO_UUID_OBJ:
        return '%s/%s' % (obj_type, existing_obj['uuid'])
    return obj_path


def _perform_update(api, obj_type, obj_path, name, obj, existing_obj,
                    sensitive_fields, avi_update_method, patch_config, api_config, check_mode):
    """
    Perform update operation on existing object.

    Parameters:
        api: API session
        obj_type: Object type
        obj_path: Object path
        name: Object name
        obj: Object dictionary
        existing_obj: Existing object dict
        sensitive_fields: Set of sensitive fields
        avi_update_method: Update method (put/patch)
        patch_config: Dict with patch operation config
        api_config: Dict with tenant, tenant_uuid, api_version
        check_mode: Whether in check mode

    Returns:
        tuple: (rsp, req, changed, obj)
    """
    tenant = api_config['tenant']
    tenant_uuid = api_config['tenant_uuid']
    api_version = api_config['api_version']

    obj_path = _resolve_obj_path_for_update(obj_type, obj_path, name, existing_obj)

    if avi_update_method == 'put':
        return _handle_put_update(
            api, obj_path, obj, existing_obj, sensitive_fields,
            tenant, tenant_uuid, api_version, check_mode)

    rsp, changed, obj = _handle_patch_update(
        api, obj_path, obj, existing_obj, patch_config['op'],
        patch_config['path'], patch_config['value'], tenant, tenant_uuid,
        api_version, check_mode)
    return rsp, None, changed, obj


def _handle_present_state(module, api, obj_type, obj_path, name, obj, existing_obj,
                          sensitive_fields, avi_update_method, patch_config,
                          api_config, check_mode):
    """
    Handle present state - create or update object.

    Parameters:
        module: Ansible module
        api: API session
        obj_type: Object type
        obj_path: Object path
        name: Object name
        obj: Object dictionary
        existing_obj: Existing object or None
        sensitive_fields: Set of sensitive fields
        avi_update_method: Update method (put/patch)
        patch_config: Dict with patch operation config (op, path, value)
        api_config: Dict with tenant, tenant_uuid, api_version
        check_mode: Whether in check mode

    Returns:
        Ansible return value
    """
    if existing_obj:
        rsp, req, changed, obj = _perform_update(
            api, obj_type, obj_path, name, obj, existing_obj,
            sensitive_fields, avi_update_method, patch_config, api_config, check_mode)
        if changed:
            log.debug('EXISTING OBJ %s', existing_obj)
            log.debug('NEW OBJ %s', obj)
    else:
        tenant = api_config['tenant']
        tenant_uuid = api_config['tenant_uuid']
        api_version = api_config['api_version']
        rsp, req, changed = _handle_create(
            api, obj_type, obj, tenant, tenant_uuid, api_version, check_mode)

    return ansible_return(module, rsp, changed, req, existing_obj=existing_obj,
                          api_context=api.get_context())


def avi_common_argument_spec():
    """
    Returns common arguments for all Avi modules
    :return: dict
    """
    credentials_spec = dict(
        controller=dict(default=os.environ.get('AVI_CONTROLLER', '')),
        username=dict(default=os.environ.get('AVI_USERNAME', '')),
        password=dict(default=os.environ.get('AVI_PASSWORD', ''), no_log=True),
        api_version=dict(default='20.1.1', type='str'),
        tenant=dict(default='admin'),
        tenant_uuid=dict(default='', type='str'),
        port=dict(type='int'),
        token=dict(default='', type='str', no_log=True),
        timeout=dict(default=300, type='int'),
        session_id=dict(default='', type='str', no_log=True),
        csrftoken=dict(default='', type='str', no_log=True),
        idp_class=dict(default='', type='str'),
        csp_host=dict(default='', type='str', no_log=True),
        csp_token=dict(default='', type='str', no_log=True),
        ssl_cert=dict(default='', type='str', no_log=True),
        ssl_key=dict(default='', type='str', no_log=True)
    )

    return dict(
        controller=dict(default=os.environ.get('AVI_CONTROLLER', '')),
        username=dict(default=os.environ.get('AVI_USERNAME', '')),
        password=dict(default=os.environ.get('AVI_PASSWORD', ''), no_log=True),
        tenant=dict(default='admin'),
        tenant_uuid=dict(default=''),
        api_version=dict(default='20.1.1', type='str'),
        avi_credentials=dict(default=None, type='dict',
                             options=credentials_spec),
        api_context=dict(type='dict'),
        avi_deactivate_session_cache_as_fact=dict(default=False, type='bool'))
