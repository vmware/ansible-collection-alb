#!/usr/bin/python3
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
module: avi_image
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>

short_description: Module for setup of Image Avi RESTful Object
description:
    - This module is used to configure Image object
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
    cloud_info_values:
        description:
            - This field describes the cloud info specific to the base image.
            - Field introduced in 20.1.1.
        type: list
    controller_info:
        description:
            - Controller package details.
            - Field introduced in 18.2.6.
        type: dict
    controller_patch_name:
        description:
            - Mandatory controller patch name that is applied along with this base image.
            - Field introduced in 18.2.10, 20.1.1.
        type: str
    controller_patch_uuid:
        description:
            - It references the controller-patch associated with the uber image.
            - Field introduced in 18.2.8, 20.1.1.
        type: str
    migrations:
        description:
            - This field describes the api migration related information.
            - Field introduced in 18.2.6.
        type: dict
    name:
        description:
            - Name of the image.
            - Field introduced in 18.2.6.
        required: true
        type: str
    se_info:
        description:
            - Se package details.
            - Field introduced in 18.2.6.
        type: dict
    se_patch_name:
        description:
            - Mandatory serviceengine patch name that is applied along with this base image.
            - Field introduced in 18.2.10, 20.1.1.
        type: str
    se_patch_uuid:
        description:
            - It references the service engine patch associated with the uber image.
            - Field introduced in 18.2.8, 20.1.1.
        type: str
    status:
        description:
            - Status to check if the image is present.
            - Enum options - SYSERR_SUCCESS, SYSERR_FAILURE, SYSERR_OUT_OF_MEMORY, SYSERR_NO_ENT, SYSERR_INVAL, SYSERR_ACCESS, SYSERR_FAULT, SYSERR_IO,
            - SYSERR_TIMEOUT, SYSERR_NOT_SUPPORTED, SYSERR_NOT_READY, SYSERR_UPGRADE_IN_PROGRESS, SYSERR_WARM_START_IN_PROGRESS, SYSERR_TRY_AGAIN,
            - SYSERR_NOT_UPGRADING, SYSERR_PENDING, SYSERR_EVENT_GEN_FAILURE, SYSERR_CONFIG_PARAM_MISSING, SYSERR_RANGE, SYSERR_BAD_REQUEST...
            - Field introduced in 18.2.6.
        type: str
    tenant_ref:
        description:
            - Tenant that this object belongs to.
            - It is a reference to an object of type tenant.
            - Field introduced in 18.2.6.
        type: str
    type:
        description:
            - Type of the image patch/system.
            - Enum options - IMAGE_TYPE_PATCH, IMAGE_TYPE_SYSTEM, IMAGE_TYPE_MUST_CHECK.
            - Field introduced in 18.2.6.
        type: str
    uber_bundle:
        description:
            - Status to check if the image is an uber bundle.
            - Field introduced in 18.2.8, 20.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Uuid of the image.
            - Field introduced in 18.2.6.
        type: str
extends_documentation_fragment:
    - vmware.alb.avi
'''

EXAMPLES = """
- name: Example to create Image object
  vmware.alb.avi_image:
    controller: 192.168.15.18
    username: admin
    password: something
    state: present
    name: sample_image
"""

RETURN = '''
obj:
    description: Image (api/image) object
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
        cloud_info_values=dict(type='list',),
        controller_info=dict(type='dict',),
        controller_patch_name=dict(type='str',),
        controller_patch_uuid=dict(type='str',),
        migrations=dict(type='dict',),
        name=dict(type='str', required=True),
        se_info=dict(type='dict',),
        se_patch_name=dict(type='str',),
        se_patch_uuid=dict(type='str',),
        status=dict(type='str',),
        tenant_ref=dict(type='str',),
        type=dict(type='str',),
        uber_bundle=dict(type='bool',),
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
    return avi_ansible_api(module, 'image',
                           set())


if __name__ == '__main__':
    main()
