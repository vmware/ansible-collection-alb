#!/usr/bin/python
# module_check: supported

# Avi Version: 17.1.1
# Copyright (c) 2026 Broadcom Inc. and/or its subsidiaries. All Rights Reserved. Broadcom Confidential.
# SPDX-License-Identifier: Apache License 2.0

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_applicationpersistenceprofile
author: Parikshit Manur (@pm020058) <parikshit.manur@broadcom.com>
short_description: Module for setup of ApplicationPersistenceProfile Avi RESTful Object
description:
    - This module is used to configure ApplicationPersistenceProfile object.
    - More examples at U(https://github.com/avinetworks/devops)
options:
    state:
        description:
            - The state that should be applied on the entity.
        default: present
        choices: ["absent", "present"]
        type: str
    avi_api_update_method:
        description:
            - Default method for object update is HTTP PUT.
            - Setting to patch will override that behavior to use HTTP PATCH.
        default: put
        choices: ["put", "patch"]
        type: str
    avi_api_patch_op:
        description:
            - Patch operation to use when using avi_api_update_method as patch.
        choices: ["add", "replace", "delete", "remove"]
        type: str
    avi_patch_path:
        description:
            - Patch path to use when using avi_api_update_method as patch.
        type: str
    avi_patch_value:
        description:
            - Patch value to use when using avi_api_update_method as patch.
        type: str
    app_cookie_persistence_profile:
        description:
            - Specifies the application cookie persistence profile parameters.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    configpb_attributes:
        description:
            - Protobuf versioning for config pbs.
            - Field introduced in 21.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    description:
        description:
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    diameter_app_persistence_profile:
        description:
            - Specifies the diameter persistence profile parameters.
            - Field introduced in 31.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    hdr_persistence_profile:
        description:
            - Specifies the custom http header persistence profile parameters.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    http_cookie_persistence_profile:
        description:
            - Specifies the http cookie persistence profile parameters.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    ip_persistence_profile:
        description:
            - Specifies the client ip persistence profile parameters.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    is_federated:
        description:
            - This field describes the objects replication scope.
            - If the field is set to false, then the object is visible within the controller-cluster and its associated service-engines.
            - If the field is set to true, then the object is replicated across the federation.
            - Field introduced in 17.1.3.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    markers:
        description:
            - List of labels to be used for granular rbac.
            - Field introduced in 20.1.5.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: dict
    name:
        description:
            - A user-friendly name for the persistence profile.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        required: true
        type: str
    persistence_type:
        description:
            - Method used to persist clients to the same server for a duration of time or a session.
            - Enum options - PERSISTENCE_TYPE_CLIENT_IP_ADDRESS, PERSISTENCE_TYPE_HTTP_COOKIE, PERSISTENCE_TYPE_TLS, PERSISTENCE_TYPE_CLIENT_IPV6_ADDRESS,
            - PERSISTENCE_TYPE_CUSTOM_HTTP_HEADER, PERSISTENCE_TYPE_APP_COOKIE, PERSISTENCE_TYPE_GSLB_SITE, PERSISTENCE_TYPE_APP_DIAMETER.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as PERSISTENCE_TYPE_CLIENT_IP_ADDRESS.
        type: str
    persistence_update_interval:
        description:
            - Interval in minutes at which refreshed persistence entries are synced to peer ses.
            - If not set, it willsync at an interval of timeout/2.
            - Allowed values are 1-30.
            - Field introduced in 30.2.4.
            - Unit is min.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: int
    server_hm_down_recovery:
        description:
            - Specifies behavior when a persistent server has been marked down by a health monitor.
            - Enum options - HM_DOWN_PICK_NEW_SERVER, HM_DOWN_ABORT_CONNECTION, HM_DOWN_CONTINUE_PERSISTENT_SERVER.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as HM_DOWN_PICK_NEW_SERVER.
        type: str
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Uuid of the persistence profile.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
extends_documentation_fragment:
    - vmware.alb.avi
'''

EXAMPLES = """
- name: Deploy Avi Controller
  hosts: all
  vars:
    avi_credentials:
      username: "admin"
      password: "something"
      controller: "192.168.15.18"
      api_version: "21.1.1"
  tasks:
    - name: Create an Application Persistence setting using http cookie.
      vmware.alb.avi_applicationpersistenceprofile:
        avi_credentials: "{{ avi_credentials }}"
        http_cookie_persistence_profile:
          always_send_cookie: false
          cookie_name: My-HTTP
          key:
            - aes_key: ShYGZdMks8j6Bpvm2sCvaXWzvXms2Z9ob+TTjRy46lQ=
              name: c1276819-550c-4adf-912d-59efa5fd7269
            - aes_key: OGsyVk84VCtyMENFOW0rMnRXVnNrb0RzdG5mT29oamJRb0dlbHZVSjR1az0=
              name: a080de57-77c3-4580-a3ea-e7a6493c14fd
            - aes_key: UVN0cU9HWmFUM2xOUzBVcmVXaHFXbnBLVUUxMU1VSktSVU5HWjJOWmVFMTBUMUV4UmxsNk4xQmFZejA9
              name: 60478846-33c6-484d-868d-bbc324fce4a5
          timeout: 15
        name: My-HTTP-Cookie
        persistence_type: PERSISTENCE_TYPE_HTTP_COOKIE
        server_hm_down_recovery: HM_DOWN_PICK_NEW_SERVER
        tenant_ref: /api/tenant?name=Demo
"""

RETURN = '''
obj:
    description: ApplicationPersistenceProfile (api/applicationpersistenceprofile) object
    returned: success, changed
    type: dict
'''

from ansible.module_utils.basic import AnsibleModule
try:
    from ansible_collections.vmware.alb.plugins.module_utils.utils.ansible_utils import (
        avi_common_argument_spec, avi_ansible_api)
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False


def main():
    argument_specs = dict(
        state=dict(default='present',
                   choices=['absent', 'present']),
        avi_api_update_method=dict(default='put',
                                   choices=['put', 'patch']),
        avi_api_patch_op=dict(choices=['add', 'replace', 'delete', 'remove']),
        avi_patch_path=dict(type='str',),
        avi_patch_value=dict(type='str',),
        api_context=dict(type='dict',),
        username=dict(type='str', default=''),
        tenant_uuid=dict(type='str', default=''),
        tenant=dict(type='str', default='admin'),
        password=dict(type='str', default='', no_log=True),
        controller=dict(type='str', default=''),
        api_version=dict(type='str', default='20.1.7'),
        avi_credentials=dict(type='dict',),
        avi_deactivate_session_cache_as_fact=dict(type='bool', default=False),
        app_cookie_persistence_profile=dict(type='dict',),
        configpb_attributes=dict(type='dict',),
        description=dict(type='str',),
        diameter_app_persistence_profile=dict(type='dict',),
        hdr_persistence_profile=dict(type='dict',),
        http_cookie_persistence_profile=dict(type='dict',),
        ip_persistence_profile=dict(type='dict',),
        is_federated=dict(type='bool',),
        markers=dict(type='list', elements='dict',),
        name=dict(type='str', required=True),
        persistence_type=dict(type='str',),
        persistence_update_interval=dict(type='int',),
        server_hm_down_recovery=dict(type='str',),
        tenant_ref=dict(type='str',),
        url=dict(type='str',),
        uuid=dict(type='str',),
    )
    if HAS_REQUESTS:
        argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_REQUESTS:
        return module.fail_json(msg=(
            'Python requests package is not installed. '
            'For installation instructions, visit https://pypi.org/project/requests.'))
    return avi_ansible_api(module, 'applicationpersistenceprofile',
                           set())


if __name__ == '__main__':
    main()
