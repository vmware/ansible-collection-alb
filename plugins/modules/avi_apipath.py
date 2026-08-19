#!/usr/bin/python
# module_check: supported

# Copyright (c) 2026 Broadcom Inc. and/or its subsidiaries. All Rights Reserved. Broadcom Confidential.
# SPDX-License-Identifier: Apache License 2.0

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_apipath
author: Parikshit Manur (@pm020058) <parikshit.manur@broadcom.com>
short_description: Module for setup of ApiPath Avi RESTful Object
description:
    - This module is used to configure ApiPath object.
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
    configpb_attributes:
        description:
            - Protobuf versioning for config pbs.
            - Field introduced in 32.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    description:
        description:
            - Description of this api path.
            - Field introduced in 32.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    endpoints:
        description:
            - List of api endpoints for this path.
            - Field introduced in 32.2.1.
            - Maximum of 10 items allowed.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: dict
    name:
        description:
            - Name of this object, unique per tenant.
            - Field introduced in 32.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        required: true
        type: str
    path_template:
        description:
            - The uri path template for the object.
            - Parameters can be defined in curly braces, for example /pet/{pet_id}.
            - Field introduced in 32.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        required: true
        type: str
    source:
        description:
            - Indicates whether this path was user-defined or imported from an openapi specification file.
            - Enum options - SOURCE_USER_DEFINED, SOURCE_API_SPEC, SOURCE_DISCOVERED.
            - Field introduced in 32.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as SOURCE_USER_DEFINED.
        type: str
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
            - Field introduced in 32.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    unknown_http_method_action:
        description:
            - Action to take when a request matches this path but uses an http method not defined for this path.
            - Overrides the policy-level unknown_http_method_action when not inherit.
            - Enum options - API_ACTION_INHERIT_FROM_API_POLICY, API_ACTION_PASS, API_ACTION_FLAG, API_ACTION_REJECT.
            - Field introduced in 32.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as API_ACTION_INHERIT_FROM_API_POLICY.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - The object uuid.
            - Field introduced in 32.2.1.
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
    - name: Example to create ApiPath object
      vmware.alb.avi_apipath:
        avi_credentials: "{{ avi_credentials }}"
        state: present
        name: sample_apipath
"""

RETURN = '''
obj:
    description: ApiPath (api/apipath) object
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
        configpb_attributes=dict(type='dict',),
        description=dict(type='str',),
        endpoints=dict(type='list', elements='dict',),
        name=dict(type='str', required=True),
        path_template=dict(type='str', required=True),
        source=dict(type='str',),
        tenant_ref=dict(type='str',),
        unknown_http_method_action=dict(type='str',),
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
    return avi_ansible_api(module, 'apipath',
                           set())


if __name__ == '__main__':
    main()
