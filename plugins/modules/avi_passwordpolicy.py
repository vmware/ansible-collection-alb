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
module: avi_passwordpolicy
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of PasswordPolicy Avi RESTful Object
description:
    - This module is used to configure PasswordPolicy object
    - more examples at U(https://github.com/avinetworks/devops)
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
            - Field introduced in 31.3.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    lockout_evaluation_period:
        description:
            - Time window for evaluating failed attempts in seconds.
            - Defaults to 900 seconds.
            - Allowed values are 300-1800.
            - Field introduced in 31.3.1.
            - Unit is sec.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 900.
        type: int
    lockout_max_auth_failures:
        description:
            - Number of failed attempts before account lockout.
            - Defaults to 3.
            - Allowed values are 0-5.
            - Special values are 0- unlimited login attempts allowed.
            - Field introduced in 31.3.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 3.
        type: int
    lockout_period:
        description:
            - Account lockout duration in seconds.
            - Defaults to 900 seconds.
            - Allowed values are 600-1800.
            - Field introduced in 31.3.1.
            - Unit is sec.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 900.
        type: int
    min_length:
        description:
            - Minimum password length.
            - Defaults to 15 characters.
            - Allowed values are 8-64.
            - Field introduced in 31.3.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 15.
        type: int
    min_lowercase:
        description:
            - Minimum number of lowercase characters required.
            - Allowed values are 0-10.
            - Field introduced in 31.3.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1.
        type: int
    min_numeric:
        description:
            - Minimum number of numeric characters required.
            - Allowed values are 0-10.
            - Field introduced in 31.3.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1.
        type: int
    min_special:
        description:
            - Minimum number of special characters required.
            - Allowed values are 0-10.
            - Field introduced in 31.3.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1.
        type: int
    min_uppercase:
        description:
            - Minimum number of uppercase characters required.
            - Allowed values are 0-10.
            - Field introduced in 31.3.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1.
        type: int
    name:
        description:
            - Name of the password policy configuration.
            - Field introduced in 31.3.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        required: true
        type: str
    password_expiration_days:
        description:
            - Password expiry period in days.
            - Defaults to 365 days.
            - Allowed values are 30-730.
            - Field introduced in 31.3.1.
            - Unit is days.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 365.
        type: int
    password_history:
        description:
            - Number of previous passwords to remember.
            - Defaults to 5.
            - Allowed values are 1-10.
            - Field introduced in 31.3.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 5.
        type: int
    tenant_ref:
        description:
            - Tenant ref for the passwordpolicy.
            - It is a reference to an object of type tenant.
            - Field introduced in 31.3.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Unique object identifier of the passwordpolicy.
            - Field introduced in 31.3.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
extends_documentation_fragment:
    - vmware.alb.avi
'''

EXAMPLES = """
- hosts: all
  vars:
    avi_credentials:
      username: "admin"
      password: "something"
      controller: "192.168.15.18"
      api_version: "21.1.1"

- name: Example to create PasswordPolicy object
  vmware.alb.avi_passwordpolicy:
    avi_credentials: "{{ avi_credentials }}"
    state: present
    name: sample_passwordpolicy
"""

RETURN = '''
obj:
    description: PasswordPolicy (api/passwordpolicy) object
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
        configpb_attributes=dict(type='dict',),
        lockout_evaluation_period=dict(type='int',),
        lockout_max_auth_failures=dict(type='int',),
        lockout_period=dict(type='int',),
        min_length=dict(type='int',),
        min_lowercase=dict(type='int',),
        min_numeric=dict(type='int',),
        min_special=dict(type='int',),
        min_uppercase=dict(type='int',),
        name=dict(type='str', required=True),
        password_expiration_days=dict(type='int',),
        password_history=dict(type='int',),
        tenant_ref=dict(type='str',),
        url=dict(type='str',),
        uuid=dict(type='str',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_REQUESTS:
        return module.fail_json(msg=(
            'Python requests package is not installed. '
            'For installation instructions, visit https://pypi.org/project/requests.'))
    return avi_ansible_api(module, 'passwordpolicy',
                           set())


if __name__ == '__main__':
    main()
