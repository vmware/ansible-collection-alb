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
module: avi_wafpolicypsmgroup
author: Parikshit Manur (@pm020058) <parikshit.manur@broadcom.com>
short_description: Module for setup of WafPolicyPSMGroup Avi RESTful Object
description:
    - This module is used to configure WafPolicyPSMGroup object.
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
    completely_described_match_elements:
        description:
            - A list of all match element collections which are completely described in the psm group.
            - Every input value which matches one of the elements in this list but is not handled by a waf psm rule, will run the match_element miss_action.
            - Allowed values are waf_variable_args.
            - Enum options - WAF_VARIABLE_ARGS, WAF_VARIABLE_ARGS_GET, WAF_VARIABLE_ARGS_POST, WAF_VARIABLE_ARGS_NAMES, WAF_VARIABLE_REQUEST_COOKIES,
            - WAF_VARIABLE_QUERY_STRING, WAF_VARIABLE_REQUEST_BASENAME, WAF_VARIABLE_REQUEST_URI, WAF_VARIABLE_PATH_INFO, WAF_VARIABLE_REQUEST_HEADERS.
            - Field introduced in 31.2.1.
            - Maximum of 1 items allowed.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: list
        elements: str
    configpb_attributes:
        description:
            - Protobuf versioning for config pbs.
            - Field introduced in 21.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    description:
        description:
            - Free-text comment about this group.
            - Field introduced in 18.2.3.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    enable:
        description:
            - Enable or disable this waf rule group.
            - Field introduced in 18.2.3.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    hit_action:
        description:
            - If a rule in this group matches the match_value pattern, this action will be executed.
            - Allowed actions are waf_action_no_op and waf_action_allow_parameter.
            - Enum options - WAF_ACTION_NO_OP, WAF_ACTION_BLOCK, WAF_ACTION_ALLOW_PARAMETER.
            - Field introduced in 18.2.3.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as WAF_ACTION_ALLOW_PARAMETER.
        type: str
    is_learning_group:
        description:
            - This field indicates that this group is used for learning.
            - Field introduced in 18.2.3.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    location_match_miss_action:
        description:
            - If there is no location matching the request, this action will be executed.
            - Allowed actions are waf_action_no_op and waf_action_block.
            - Enum options - WAF_ACTION_NO_OP, WAF_ACTION_BLOCK, WAF_ACTION_ALLOW_PARAMETER.
            - Field introduced in 31.2.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as WAF_ACTION_NO_OP.
        type: str
    locations:
        description:
            - Positive security model locations.
            - These are used to partition the application name space.
            - Field introduced in 18.2.3.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: dict
    markers:
        description:
            - List of labels to be used for granular rbac.
            - Field introduced in 20.1.5.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: dict
    miss_action:
        description:
            - If a rule in this group does not match the match_value pattern, this action will be executed.
            - Allowed actions are waf_action_no_op and waf_action_block.
            - Enum options - WAF_ACTION_NO_OP, WAF_ACTION_BLOCK, WAF_ACTION_ALLOW_PARAMETER.
            - Field introduced in 18.2.3.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as WAF_ACTION_NO_OP.
        type: str
    name:
        description:
            - User defined name of the group.
            - Field introduced in 18.2.3.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        required: true
        type: str
    tenant_ref:
        description:
            - Tenant that this object belongs to.
            - It is a reference to an object of type tenant.
            - Field introduced in 18.2.3.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Uuid of this object.
            - Field introduced in 18.2.3.
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
    - name: Example to create WafPolicyPSMGroup object
      vmware.alb.avi_wafpolicypsmgroup:
        avi_credentials: "{{ avi_credentials }}"
        state: present
        name: sample_wafpolicypsmgroup
"""

RETURN = '''
obj:
    description: WafPolicyPSMGroup (api/wafpolicypsmgroup) object
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
        password=dict(type='str', default='', no_log=False),
        controller=dict(type='str', default=''),
        api_version=dict(type='str', default='18.2.6'),
        avi_credentials=dict(type='dict',),
        avi_deactivate_session_cache_as_fact=dict(type='bool', default=False),
        completely_described_match_elements=dict(type='list', elements='str',),
        configpb_attributes=dict(type='dict',),
        description=dict(type='str',),
        enable=dict(type='bool',),
        hit_action=dict(type='str',),
        is_learning_group=dict(type='bool',),
        location_match_miss_action=dict(type='str',),
        locations=dict(type='list', elements='dict',),
        markers=dict(type='list', elements='dict',),
        miss_action=dict(type='str',),
        name=dict(type='str', required=True),
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
    return avi_ansible_api(module, 'wafpolicypsmgroup',
                           set())


if __name__ == '__main__':
    main()
