#!/usr/bin/python3
# module_check: supported

# Avi Version: 17.1.1
# Copyright 2021 VMware, Inc.  All rights reserved. VMware Confidential
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_tenant
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>

short_description: Module for setup of Tenant Avi RESTful Object
description:
    - This module is used to configure Tenant object
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
        choices: ["add", "replace", "delete"]
        type: str
    config_settings:
        description:
            - Tenantconfiguration settings for tenant.
        type: dict
    created_by:
        description:
            - Creator of this tenant.
        type: str
    description:
        description:
            - User defined description for the object.
        type: str
    local:
        description:
            - Boolean flag to set local.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    name:
        description:
            - Name of the object.
        required: true
        type: str
    suggested_object_labels:
        description:
            - Suggestive pool of key value pairs for recommending assignment of labels to objects in the user interface.
            - Every entry is unique in both key and value.
            - Field introduced in 20.1.2.
            - Maximum of 256 items allowed.
        type: list
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Unique object identifier of the object.
        type: str
extends_documentation_fragment:
    - vmware.alb.avi
'''

EXAMPLES = """
  - name: Create Tenant using Service Engines in provider mode
    vmware.alb.avi_tenant:
      controller: '{{ controller }}'
      password: '{{ password }}'
      username: '{{ username }}'
      config_settings:
        se_in_provider_context: false
        tenant_access_to_provider_se: true
        tenant_vrf: false
      description: VCenter, Open Stack, AWS Virtual services
      local: true
      name: Demo
"""

RETURN = '''
obj:
    description: Tenant (api/tenant) object
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
        avi_api_patch_op=dict(choices=['add', 'replace', 'delete']),
        config_settings=dict(type='dict',),
        created_by=dict(type='str',),
        description=dict(type='str',),
        local=dict(type='bool',),
        name=dict(type='str', required=True),
        suggested_object_labels=dict(type='list',),
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
    return avi_ansible_api(module, 'tenant',
                           set())


if __name__ == '__main__':
    main()
