#!/usr/bin/python
# module_check: not supported

# Copyright 2021 VMware, Inc. All rights reserved. VMware Confidential
# SPDX-License-Identifier: Apache License 2.0
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)


from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}


DOCUMENTATION = '''
---
module: avi_saml_api_session
author: Shrikant Chaudhari (@gitshrikant) <shrikant.chaudhari@avinetworks.com>
short_description: Avi API Module
description:
    - This module is useful to get SAML session after successful SAML authentication from a given IDP.
    - This module return api_context and token after successful authentication from IDP.
options:
    idp_class:
        description:
            - IDP class which will be used to authenticate session with that corresponding IDP such as Okta,
            - Onelogin and Pingfederate. Currently, we support two idp classes OktaSAMLApiSession, OneloginSAMLApiSession.
        required: true
        type: str
        # Fields from avi_common_argument_spec()
    controller:
        description:
            - Avi controller hostname or IP address.
        type: str
        required: false
    username:
        description:
            - Avi username for authentication.
        type: str
        required: false
    password:
        description:
            - Avi password for authentication.
        type: str
        required: false
    tenant:
        description:
            - Tenant name.
        type: str
        required: false
    tenant_uuid:
        description:
            - Tenant UUID.
        type: str
        required: false
    api_version:
        description:
            - Avi API version to use.
        type: str
        required: false
    avi_credentials:
        description:
            - Dictionary of Avi credentials (alternative to controller/username/password/token).
        type: dict
        required: false
        suboptions:
            controller:
                description: Avi controller hostname or IP address.
                type: str
                default: ""
            username:
                description: Avi username.
                type: str
            password:
                description: Avi password.
                type: str
                default: ""
            api_version:
                description: Avi API version.
                type: str
                default: "20.1.1"
            tenant:
                description: Tenant name.
                type: str
                default: "admin"
            tenant_uuid:
                description: Tenant UUID.
                type: str
                default: ""
            port:
                description: Port of the Avi controller.
                type: int
            token:
                description: Avi API token.
                type: str
                default: ""
            timeout:
                description: Timeout for API requests (in seconds).
                type: int
                default: 300
            session_id:
                description: Session ID for authentication.
                type: str
                default: ""
            csrftoken:
                description: CSRF token for authentication.
                type: str
                default: ""
            ssl_cert:
                description: SSL certificate path for HTTPS requests.
                type: str
                default: ""
            ssl_key:
                description: SSL private key path for HTTPS requests.
                type: str
                default: ""
            idp_class:
                description: Identity provider class.
                type: str
                required: false
                default: ''
            csp_token:
                description: Identity provider class.
                type: str
                required: false
                default: ''
            csp_host:
                description: Identity provider class.
                type: str
                required: false
                default: ''
    api_context:
        description:
            - Optional dictionary for API context.
        type: dict
        required: false
    avi_deactivate_session_cache_as_fact:
        description:
            - Boolean to deactivate session cache and expose it as an Ansible fact.
        type: bool
        required: false

'''

EXAMPLES = '''
- name: Get SAML Session
  hosts: all
  vars:
    avi_credentials:
      username: "{{ username }}"
      password: "{{ password }}"
      controller: "{{ controller }}"
      api_version: "{{ api_version }}"
    idp_class: "{{ idp_class }}"
  tasks:
    - name: Get SAML Session
      vmware.alb.avi_saml_api_session:
        idp_class: "{{ idp_class }}"
        avi_credentials: "{{ avi_credentials }}"
      register: saml_api_session

    - name: Set SAML API Context
      ansible.builtin.set_fact:
        saml_api_context: "{{ saml_api_session.ansible_facts.avi_api_context }}"

    - name: Create Pool
      vmware.alb.avi_pool:
        api_context: "{{ saml_api_context | default(omit) }}"
        avi_credentials: "{{ avi_credentials }}"
        state: "{{ state | default(present) }}"
        name: vs-simple-pool
        lb_algorithm: LB_ALGORITHM_ROUND_ROBIN
        servers:
          - ip:
              addr: 10.90.64.12
              type: 'V4'
          - ip:
              addr: 10.90.64.11
              type: 'V4'
          - ip:
              addr: 10.90.64.13
              type: 'V4'

    - name: Create Virtual Service
      vmware.alb.avi_virtualservice:
        api_context: "{{ saml_api_context | default(omit) }}"
        avi_credentials: "{{ avi_credentials }}"
        state: "{{ state | default(present) }}"
        name: vs-simple
        services:
          - port: 80
        pool_ref: '/api/pool?name=vs-simple-pool'
        vip:
          - ip_address:
              addr: 10.90.64.244
              type: 'V4'
            vip_id: '1'
'''


RETURN = '''
obj:
    description: Avi REST resource
    returned: success, changed
    type: dict
'''

from ansible.module_utils.basic import AnsibleModule
try:
    from ansible_collections.vmware.alb.plugins.module_utils.utils.ansible_utils import (
        avi_common_argument_spec, ansible_return)
    from ansible_collections.vmware.alb.plugins.module_utils.avi_api import (
        ApiSession, AviCredentials)
    from requests import ConnectionError
    from ssl import SSLError
    from requests.exceptions import ChunkedEncodingError
    from ansible_collections.vmware.alb.plugins.module_utils.saml_avi_api import OktaSAMLApiSession, OneloginSAMLApiSession
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False


def get_idp_class(idp):
    """
    This return corresponding idp class.
    :param idp: idp type such as okta, onelogin, pingfed
    :return: IDP class or ApiSession class
    """

    if str(idp).lower() == "oktasamlapisession":
        idp_class = OktaSAMLApiSession
    elif str(idp).lower() == 'oneloginsamlapisession':
        idp_class = OneloginSAMLApiSession
    else:
        idp_class = None
    return idp_class


def main():
    argument_specs = dict(
        idp_class=dict(type="str", required=True, ),
    )

    STATIC_COMMON_ARGS = dict(
        controller=dict(type='str', required=False),
        username=dict(type='str', required=False),
        password=dict(type='str', required=False, no_log=True),
        tenant=dict(type='str', required=False),
        tenant_uuid=dict(type='str', required=False),
        api_version=dict(type='str', required=False),
        avi_credentials=dict(type='dict', required=False),
        api_context=dict(type='dict', required=False),
        avi_deactivate_session_cache_as_fact=dict(type='bool', required=False),
    )
    argument_specs.update(STATIC_COMMON_ARGS)
    if HAS_REQUESTS:
        argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(argument_spec=argument_specs)

    if not HAS_REQUESTS:
        return module.fail_json(msg=(
            'Python requests package is not installed. '
            'For installation instructions, visit https://pypi.org/project/requests.'))
    idp_class = module.params.get("idp_class", None)
    idp = get_idp_class(idp_class)
    if not idp:
        msg = "IDP {1} not supported yet.".format(idp_class)
        return module.fail_json(msg=msg)
    avi_credentials = AviCredentials()
    avi_credentials.update_from_ansible_module(module)
    try:
        api = ApiSession.get_session(
            avi_credentials.controller, avi_credentials.username, password=avi_credentials.password,
            timeout=avi_credentials.timeout, tenant=avi_credentials.tenant,
            tenant_uuid=avi_credentials.tenant_uuid, port=avi_credentials.port, idp_class=idp)
        changed = True
    except (ConnectionError, SSLError, ChunkedEncodingError) as e:
        msg = "Error during get session {1}".format(e.message)
        return module.fail_json(msg=msg)
    return ansible_return(module, None, changed, None, api_context=api.get_context())


if __name__ == '__main__':
    main()
