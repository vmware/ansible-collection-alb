#!/usr/bin/python
# module_check: supported

# Copyright 2021 VMware, Inc.  All rights reserved. VMware Confidential
# SPDX-License-Identifier: Apache License 2.0

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_systemreport
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of SystemReport Avi RESTful Object
description:
    - This module is used to configure SystemReport object.
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
    archive_ref:
        description:
            - Relative path to the report archive file on filesystem.the archive includes exported system configuration and current object as json.
            - Field introduced in 22.1.6, 30.2.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: str
    controller_patch_image_ref:
        description:
            - Controller patch image associated with the report.
            - It is a reference to an object of type image.
            - Field introduced in 22.1.6, 30.2.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: str
    downloadable:
        description:
            - Indicates whether this report is downloadable as an archive.
            - Field introduced in 22.1.6, 30.2.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    events:
        description:
            - List of events associated with the report.
            - Field introduced in 22.1.6, 30.2.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: list
        elements: dict
    image_ref:
        description:
            - System image associated with the report.
            - It is a reference to an object of type image.
            - Field introduced in 22.1.6, 30.2.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: str
    name:
        description:
            - Name of the report derived from operation in a readable format.
            - Ex  upgrade_system_1a5c.
            - Field introduced in 22.1.6, 30.2.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: str
    obj_state:
        description:
            - Report state combines all applicable states.
            - Ex  readiness_reports.system_readiness.state.
            - Field introduced in 22.1.6, 30.2.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: dict
    readiness_reports:
        description:
            - Readiness state of the system.
            - Ex  upgrade pre-check results.
            - Field introduced in 22.1.6, 30.2.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: list
        elements: dict
    se_patch_image_ref:
        description:
            - Se patch image associated with the report.
            - It is a reference to an object of type image.
            - Field introduced in 22.1.6, 30.2.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: str
    summary:
        description:
            - Summary of the report.
            - Field introduced in 22.1.6, 30.2.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: dict
    tasks:
        description:
            - List of tasks associated with the report.
            - Field introduced in 30.2.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: list
        elements: dict
    tenant_ref:
        description:
            - Tenant uuid associated with the object.
            - It is a reference to an object of type tenant.
            - Field introduced in 22.1.6, 30.2.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Uuid identifier for the report.
            - Field introduced in 22.1.6, 30.2.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: str
    # Fields from avi_common_argument_spec()
    controller:
        description:
            - Avi controller hostname or IP address.
        type: str
        required: false
        default: ""
    username:
        description:
            - Avi username for authentication.
        type: str
        required: false
        default: ""
    password:
        description:
            - Avi password for authentication.
        type: str
        required: false
        default: ""
    tenant:
        description:
            - Tenant name.
        type: str
        required: false
        default: admin
    tenant_uuid:
        description:
            - Tenant UUID.
        type: str
        required: false
        default: ""
    api_version:
        description:
            - Avi API version to use.
        type: str
        required: false
        default: "18.2.6"
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
                default: ""
            password:
                description: Avi password.
                type: str
                default: ""
            api_version:
                description: Avi API version.
                type: str
                default: "18.2.6"
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
        default: false

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
    - name: Example to create SystemReport object
      vmware.alb.avi_systemreport:
        avi_credentials: "{{ avi_credentials }}"
        state: present
        name: sample_systemreport
"""

RETURN = '''
obj:
    description: SystemReport (api/systemreport) object
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
        archive_ref=dict(type='str',),
        controller_patch_image_ref=dict(type='str',),
        downloadable=dict(type='bool',),
        events=dict(type='list', elements='dict',),
        image_ref=dict(type='str',),
        name=dict(type='str',),
        obj_state=dict(type='dict',),
        readiness_reports=dict(type='list', elements='dict',),
        se_patch_image_ref=dict(type='str',),
        summary=dict(type='dict',),
        tasks=dict(type='list', elements='dict',),
        tenant_ref=dict(type='str',),
        url=dict(type='str',),
        uuid=dict(type='str',),
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

    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_REQUESTS:
        return module.fail_json(msg=(
            'Python requests package is not installed. '
            'For installation instructions, visit https://pypi.org/project/requests.'))
    return avi_ansible_api(module, 'systemreport',
                           set())


if __name__ == '__main__':
    main()
