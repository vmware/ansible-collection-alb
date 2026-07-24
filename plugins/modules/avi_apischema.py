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
module: avi_apischema
author: Parikshit Manur (@pm020058) <parikshit.manur@broadcom.com>
short_description: Module for setup of ApiSchema Avi RESTful Object
description:
    - This module is used to configure ApiSchema object.
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
    additional_object_key_action:
        description:
            - Action to take on unspecified keys in an object.
            - Enum options - API_ACTION_INHERIT_FROM_API_POLICY, API_ACTION_PASS, API_ACTION_FLAG, API_ACTION_REJECT.
            - Field introduced in 32.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as API_ACTION_INHERIT_FROM_API_POLICY.
        type: str
    additional_properties_schema:
        description:
            - Type constraint for additional properties not defined in object_properties.
            - When set, unknown keys must conform to this schema.
            - Field introduced in 32.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    allow_additional_properties:
        description:
            - When true, object keys not defined in object_properties are permitted.
            - Corresponds to openapi additionalproperties  true.
            - Field introduced in 32.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: bool
    array_item_type:
        description:
            - If the type is array, this is the type of the array items.
            - Field introduced in 32.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    composite_types:
        description:
            - Sub-schemas for this composite type (oneof, anyof, or allof).
            - Each entry must be a schema_type_reference pointing to an apischema.
            - Field introduced in 32.2.1.
            - Maximum of 64 items allowed.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: dict
    configpb_attributes:
        description:
            - Protobuf versioning for config pbs.
            - Field introduced in 32.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    description:
        description:
            - Description of this api schema.
            - Field introduced in 32.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    discriminator:
        description:
            - Property used to distinguish between sub-schemas in oneof/anyof composite types.
            - Maps a discriminator property value to the matching schema.
            - Field introduced in 32.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    max_items:
        description:
            - Maximum number of items allowed in an array.
            - Field introduced in 32.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: int
    min_items:
        description:
            - Minimum number of items allowed in an array.
            - Field introduced in 32.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: int
    name:
        description:
            - Name of this object, unique per tenant.
            - Field introduced in 32.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        required: true
        type: str
    object_properties:
        description:
            - List of properties for this object schema.
            - Field introduced in 32.2.1.
            - Maximum of 512 items allowed.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: dict
    source:
        description:
            - Indicates whether this schema was user-defined or imported from an openapi specification file.
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
    type:
        description:
            - The data type of this schema.
            - Can be object, array, or a composite type (oneof, anyof, allof).
            - Enum options - SCHEMA_TYPE_UNDEFINED, SCHEMA_TYPE_STRING, SCHEMA_TYPE_INTEGER, SCHEMA_TYPE_NUMBER, SCHEMA_TYPE_BOOLEAN, SCHEMA_TYPE_NULL,
            - SCHEMA_TYPE_ARRAY, SCHEMA_TYPE_OBJECT, SCHEMA_TYPE_REFERENCE, SCHEMA_TYPE_ONE_OF, SCHEMA_TYPE_ALL_OF, SCHEMA_TYPE_ANY_OF.
            - Field introduced in 32.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        required: true
        type: str
    unique_items:
        description:
            - If true, all items in the array must be unique.
            - Field introduced in 32.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: bool
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
    - name: Example to create ApiSchema object
      vmware.alb.avi_apischema:
        avi_credentials: "{{ avi_credentials }}"
        state: present
        name: sample_apischema
"""

RETURN = '''
obj:
    description: ApiSchema (api/apischema) object
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
        additional_object_key_action=dict(type='str', no_log=True,),
        additional_properties_schema=dict(type='dict',),
        allow_additional_properties=dict(type='bool',),
        array_item_type=dict(type='dict',),
        composite_types=dict(type='list', elements='dict',),
        configpb_attributes=dict(type='dict',),
        description=dict(type='str',),
        discriminator=dict(type='dict',),
        max_items=dict(type='int',),
        min_items=dict(type='int',),
        name=dict(type='str', required=True),
        object_properties=dict(type='list', elements='dict',),
        source=dict(type='str',),
        tenant_ref=dict(type='str',),
        type=dict(type='str', required=True),
        unique_items=dict(type='bool',),
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
    return avi_ansible_api(module, 'apischema',
                           {'additional_object_key_action'})


if __name__ == '__main__':
    main()
