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
module: avi_report
author: Parikshit Manur (@pm020058) <parikshit.manur@broadcom.com>
short_description: Module for setup of Report Avi RESTful Object
description:
    - This module is used to configure Report object.
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
    duration:
        description:
            - Time taken to complete report generation in seconds.
            - Field introduced in 31.2.1.
            - Unit is sec.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: int
    end_time:
        description:
            - End time of the report generation.
            - Field introduced in 31.2.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    filename:
        description:
            - Name of the report artifact on reports repository.
            - Field introduced in 31.2.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    name:
        description:
            - Name of the report.
            - Field introduced in 31.2.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    node:
        description:
            - Cluster member node on which the report is processed.
            - Field introduced in 31.2.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    obj_state:
        description:
            - State of the report generation.
            - Field introduced in 31.2.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: dict
    pre_check:
        description:
            - Pre-check details for the report generation.
            - Field introduced in 31.2.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: dict
    progress:
        description:
            - Percentage of tasks completed.
            - Allowed values are 0-100.
            - Field introduced in 31.2.1.
            - Unit is percent.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    request:
        description:
            - Request for the report generation.
            - Field introduced in 31.2.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: dict
    start_time:
        description:
            - Start time of the report generation.
            - Field introduced in 31.2.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    tasks:
        description:
            - List of tasks associated with the report generation.
            - Field introduced in 31.2.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: list
        elements: dict
    tasks_completed:
        description:
            - No.
            - Of tasks completed.
            - Field introduced in 31.2.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: int
    tenant_ref:
        description:
            - Tenant uuid of the report generation.
            - It is a reference to an object of type tenant.
            - Field introduced in 31.2.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    total_tasks:
        description:
            - Total no.
            - Of tasks.
            - Field introduced in 31.2.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: int
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Uuid identifier for the report generation.
            - Field introduced in 31.2.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
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
    - name: Example to create Report object
      vmware.alb.avi_report:
        avi_credentials: "{{ avi_credentials }}"
        state: present
        name: sample_report
"""

RETURN = '''
obj:
    description: Report (api/report) object
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
        api_version=dict(type='str', default='22.1.2'),
        avi_credentials=dict(type='dict',),
        avi_deactivate_session_cache_as_fact=dict(type='bool', default=False),
        duration=dict(type='int',),
        end_time=dict(type='str',),
        filename=dict(type='str',),
        name=dict(type='str',),
        node=dict(type='str',),
        obj_state=dict(type='dict',),
        pre_check=dict(type='dict',),
        progress=dict(type='int',),
        request=dict(type='dict',),
        start_time=dict(type='str',),
        tasks=dict(type='list', elements='dict',),
        tasks_completed=dict(type='int',),
        tenant_ref=dict(type='str',),
        total_tasks=dict(type='int',),
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
    return avi_ansible_api(module, 'report',
                           set())


if __name__ == '__main__':
    main()
