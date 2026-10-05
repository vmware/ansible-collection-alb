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
module: avi_clfprofile
author: Parikshit Manur (@pm020058) <parikshit.manur@broadcom.com>
short_description: Module for setup of ClfProfile Avi RESTful Object
description:
    - This module is used to configure ClfProfile object.
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
    clf_pools:
        description:
            - List of pools associated with this profile.
            - Each pool must have a unique priority value.
            - The controller rejects profiles where two pools share the same priority (http 400).
            - Field introduced in 32.1.5.
            - Maximum of 8 items allowed.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: dict
    configpb_attributes:
        description:
            - Protobuf versioning and config-push attributes.
            - Field introduced in 32.1.5.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    description:
        description:
            - Human-readable description for this clf profile.
            - Field introduced in 32.1.5.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    enabled:
        description:
            - Enable or disable log delivery for this profile without disturbing pool state, health monitors, or virtualservice/datascriptset bindings.
            - When false, datascript log forwarding is a silent no-op for every vs attached via this profile; delivery resumes immediately when set back to
            - true.
            - Field introduced in 32.1.5.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    markers:
        description:
            - List of labels to be used for granular rbac.
            - Field introduced in 32.1.5.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: dict
    name:
        description:
            - The name of the clf profile.
            - Field introduced in 32.1.5.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        required: true
        type: str
    replicate:
        description:
            - When false (default), log records are routed to the highest-priority pool that has at least one up member (priority-based failover).
            - When true, log records are replicated to all pools regardless of priority.
            - Field introduced in 32.1.5.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    tenant_ref:
        description:
            - Reference to the tenant that owns this clf profile.
            - It is a reference to an object of type tenant.
            - Field introduced in 32.1.5.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Uuid of the clf profile.
            - Field introduced in 32.1.5.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    vrf_context_ref:
        description:
            - Virtual routing context for this profiles collector pools.
            - Only virtual services in the same virtual routing context can use this profile.
            - Cannot be changed once set.
            - It is a reference to an object of type vrfcontext.
            - Field introduced in 32.1.5.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        required: true
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
    - name: Example to create ClfProfile object
      vmware.alb.avi_clfprofile:
        avi_credentials: "{{ avi_credentials }}"
        state: present
        name: sample_clfprofile
"""

RETURN = '''
obj:
    description: ClfProfile (api/clfprofile) object
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
        api_version=dict(type='str', default='30.2.1'),
        avi_credentials=dict(type='dict',),
        avi_deactivate_session_cache_as_fact=dict(type='bool', default=False),
        clf_pools=dict(type='list', elements='dict',),
        configpb_attributes=dict(type='dict',),
        description=dict(type='str',),
        enabled=dict(type='bool',),
        markers=dict(type='list', elements='dict',),
        name=dict(type='str', required=True),
        replicate=dict(type='bool',),
        tenant_ref=dict(type='str',),
        url=dict(type='str',),
        uuid=dict(type='str',),
        vrf_context_ref=dict(type='str', required=True),
    )
    if HAS_REQUESTS:
        argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_REQUESTS:
        return module.fail_json(msg=(
            'Python requests package is not installed. '
            'For installation instructions, visit https://pypi.org/project/requests.'))
    return avi_ansible_api(module, 'clfprofile',
                           set())


if __name__ == '__main__':
    main()
