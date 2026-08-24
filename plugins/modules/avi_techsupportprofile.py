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
module: avi_techsupportprofile
author: Parikshit Manur (@pm020058) <parikshit.manur@broadcom.com>
short_description: Module for setup of TechSupportProfile Avi RESTful Object
description:
    - This module is used to configure TechSupportProfile object.
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
    archive_rules:
        description:
            - Define the policy for techsupport archive rules.
            - These rules allow you to specify files that should be collected in the techsupport bundle, even if they exceed the default file size threshold.
            - E.g.
            - To ensure a 450mb file, such as /var/sample.log, is collected with every invocation, configure and add its path to the techsupportprofile.
            - Field introduced in 31.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    event_params:
        description:
            - Specify this params to set threshold for event files.
            - User provided parameters will take precedence over the profile parameters.
            - Field introduced in 31.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    file_size_threshold:
        description:
            - Max file size threshold to archive in techsupport collection.
            - Files above this threshold will not be collected and an warning will be flagged.
            - Allowed values are 128-512.
            - Field introduced in 31.2.1.
            - Unit is mb.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 128.
        type: int
    max_disk_size_percent:
        description:
            - Max disk size in percent of total disk size reserved for the techsupport.
            - The value is in percentage to make it agnostic of controller flavors.
            - E.g.
            - Small [disk=5 gb, ts space available = 500mb] large [ disk= 100gb, ts space available= 10gb] xl [disk=1tb, ts space available=100gb].
            - Allowed values are 10-25.
            - Field introduced in 31.2.1.
            - Unit is percent.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 10.
        type: int
    min_free_disk_required:
        description:
            - Min free disk required for the techsupport invocation.
            - The value is in percentage to make it agnostic of controller flavors.
            - E.g.
            - Small [disk=5 gb, ts space available = 250mb] large [ disk= 100gb, ts space available= 5gb] xl [disk=1tb, ts space available=50gb].
            - Allowed values are 5-10.
            - Field introduced in 31.2.1.
            - Unit is percent.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 5.
        type: int
    no_of_techsupport_retentions:
        description:
            - Number of techsupport to retain from techsupport cleanup policy.
            - Allowed values are 1-5.
            - Field introduced in 31.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 4.
        type: int
    simultaneous_invocations:
        description:
            - Number of simultaneous techsupport invocation allowed.
            - Allowed values are 1-2.
            - Field introduced in 31.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1.
        type: int
    task_timeout:
        description:
            - Generic timeout for techsupport task collection.
            - This can be used for task, script executions etc.
            - Tweak the timeout value in cases of timeout observation in the logs.
            - Field introduced in 31.2.1.
            - Unit is sec.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 180.
        type: int
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Uuid identifier for the techsupport profile.
            - Field introduced in 31.2.1.
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
    - name: Example to create TechSupportProfile object
      vmware.alb.avi_techsupportprofile:
        avi_credentials: "{{ avi_credentials }}"
        state: present
        name: sample_techsupportprofile
"""

RETURN = '''
obj:
    description: TechSupportProfile (api/techsupportprofile) object
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
        archive_rules=dict(type='dict',),
        event_params=dict(type='dict',),
        file_size_threshold=dict(type='int',),
        max_disk_size_percent=dict(type='int',),
        min_free_disk_required=dict(type='int',),
        no_of_techsupport_retentions=dict(type='int',),
        simultaneous_invocations=dict(type='int',),
        task_timeout=dict(type='int',),
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
    return avi_ansible_api(module, 'techsupportprofile',
                           set())


if __name__ == '__main__':
    main()
