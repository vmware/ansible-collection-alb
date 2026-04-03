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
module: avi_techsupport
author: Parikshit Manur (@pm020058) <parikshit.manur@broadcom.com>
short_description: Module for setup of TechSupport Avi RESTful Object
description:
    - This module is used to configure TechSupport object.
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
    case_number:
        description:
            - Customer case number for which this techsupport is generated.
            - Useful for connected portal and other use-cases.
            - Field introduced in 31.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    description:
        description:
            - User provided description to capture additional details and context regarding the techsupport invocation.
            - Field introduced in 31.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    duration:
        description:
            - Total time taken for techsupport collection.
            - Field introduced in 31.2.1.
            - Unit is sec.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: int
    end_time:
        description:
            - End timestamp of techsupport collection.
            - Field introduced in 31.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    errors:
        description:
            - Error logged during techsupport collection.
            - Field introduced in 31.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: str
    level:
        description:
            - Name of the techsupport level.
            - Field introduced in 31.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    name:
        description:
            - Name of techsupport invocation.
            - Field introduced in 31.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    node:
        description:
            - Cluster member node on which the techsupport tarball bundle is saved.
            - Field introduced in 31.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    obj_name:
        description:
            - Object name if one exists.
            - Field introduced in 31.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    obj_state:
        description:
            - State of current/last techsupport invocation.
            - Field introduced in 31.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    obj_uuid:
        description:
            - Techsupport collection object uuid specified for different objects such as se/vs/pool etc.
            - Field introduced in 31.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    output:
        description:
            - Techsupport collection output file path.
            - Field introduced in 31.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    params:
        description:
            - Techsupport params associated with latest techsupport collection.
            - User passed params will have more preference.
            - Field introduced in 31.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    progress:
        description:
            - Techsupport collection progress which holds value between 0-100.
            - Allowed values are 0-100.
            - Field introduced in 31.2.1.
            - Unit is percent.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    size:
        description:
            - Size of collected techsupport tarball.
            - Field introduced in 31.2.1.
            - Unit is mb.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: float
    start_time:
        description:
            - Start timestamp of techsupport collection.
            - Field introduced in 31.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    tasks:
        description:
            - Events performed for techsupport collection.
            - Field introduced in 31.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: dict
    tasks_completed:
        description:
            - Completed set of tasks in the techsupport collection.
            - Field introduced in 31.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: int
    techsupport_readiness:
        description:
            - Techsupport readiness checks execution details.
            - Field introduced in 31.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    tenant_ref:
        description:
            - Tenant uuid associated with the techsupport.
            - It is a reference to an object of type tenant.
            - Field introduced in 31.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    total_tasks:
        description:
            - Total number of tasks in the techsupport collection.
            - Field introduced in 31.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: int
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Uuid identifier for the techsupport invocation.
            - Field introduced in 31.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    warnings:
        description:
            - Warning logged during techsupport collection.
            - Field introduced in 31.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: str
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
    - name: Example to create TechSupport object
      vmware.alb.avi_techsupport:
        avi_credentials: "{{ avi_credentials }}"
        state: present
        name: sample_techsupport
"""

RETURN = '''
obj:
    description: TechSupport (api/techsupport) object
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
        case_number=dict(type='str',),
        description=dict(type='str',),
        duration=dict(type='int',),
        end_time=dict(type='str',),
        errors=dict(type='list', elements='str',),
        level=dict(type='str',),
        name=dict(type='str',),
        node=dict(type='str',),
        obj_name=dict(type='str',),
        obj_state=dict(type='dict',),
        obj_uuid=dict(type='str',),
        output=dict(type='str',),
        params=dict(type='dict',),
        progress=dict(type='int',),
        size=dict(type='float',),
        start_time=dict(type='str',),
        tasks=dict(type='list', elements='dict',),
        tasks_completed=dict(type='int',),
        techsupport_readiness=dict(type='dict',),
        tenant_ref=dict(type='str',),
        total_tasks=dict(type='int',),
        url=dict(type='str',),
        uuid=dict(type='str',),
        warnings=dict(type='list', elements='str',),
    )
    if HAS_REQUESTS:
        argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_REQUESTS:
        return module.fail_json(msg=(
            'Python requests package is not installed. '
            'For installation instructions, visit https://pypi.org/project/requests.'))
    return avi_ansible_api(module, 'techsupport',
                           set())


if __name__ == '__main__':
    main()
