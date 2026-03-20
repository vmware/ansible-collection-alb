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
module: avi_ratelimitconfiguration
author: Parikshit Manur (@pm020058) <parikshit.manur@broadcom.com>
short_description: Module for setup of RateLimitConfiguration Avi RESTful Object
description:
    - This module is used to configure RateLimitConfiguration object.
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
    burst:
        description:
            - The maximum request per second(rps) user intends to support for this category.this is not guaranteed as this will be the minimum of the rps
            - supported by the resources in the category and this value.if user doesnt provide then it will be minimum value of the resources in this category.
            - Allowed values are 1-1000.
            - Field introduced in 31.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1.
        type: int
    configpb_attributes:
        description:
            - Protobuf versioning for config pbs.
            - Field introduced in 31.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    description:
        description:
            - Description for the rate limit configuration.
            - Field introduced in 31.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    http_methods:
        description:
            - List of http method(s) of the resources that need to be rate limited.
            - Enum options - HTTP_METHOD_GET, HTTP_METHOD_HEAD, HTTP_METHOD_PUT, HTTP_METHOD_DELETE, HTTP_METHOD_POST, HTTP_METHOD_OPTIONS, HTTP_METHOD_TRACE,
            - HTTP_METHOD_CONNECT, HTTP_METHOD_PATCH, HTTP_METHOD_PROPFIND, HTTP_METHOD_PROPPATCH, HTTP_METHOD_MKCOL, HTTP_METHOD_COPY, HTTP_METHOD_MOVE,
            - HTTP_METHOD_LOCK, HTTP_METHOD_UNLOCK.
            - Field introduced in 31.2.1.
            - Minimum of 1 items required.
            - Maximum of 5 items allowed.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        required: true
        type: list
        elements: str
    name:
        description:
            - Name of the rate limit configuration(unique).
            - Field introduced in 31.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        required: true
        type: str
    resource:
        description:
            - Ratelimitresource which needs to be rate limited.
            - Enum options - RATE_LIMIT_VIRTUALSERVICE, RATE_LIMIT_POOL, RATE_LIMIT_LOGIN, RATE_LIMIT_AUTHTOKEN, RATE_LIMIT_HEALTHMONITOR.
            - Field introduced in 31.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        required: true
        type: str
    tenant_ref:
        description:
            - Tenant ref for the auth rate limit configuration.
            - It is a reference to an object of type tenant.
            - Field introduced in 31.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    token_refill_rate:
        description:
            - Token refill rate.
            - Field introduced in 31.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        required: true
        type: dict
    type:
        description:
            - Type of the rate limiter, for now we only support api categorization based.
            - Enum options - RATE_LIMITER_API_CATEGORY.
            - Field introduced in 31.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as RATE_LIMITER_API_CATEGORY.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Uuid of the rate limit configuration.
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
    - name: Example to create RateLimitConfiguration object
      vmware.alb.avi_ratelimitconfiguration:
        avi_credentials: "{{ avi_credentials }}"
        state: present
        name: sample_ratelimitconfiguration
"""

RETURN = '''
obj:
    description: RateLimitConfiguration (api/ratelimitconfiguration) object
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
        burst=dict(type='int',),
        configpb_attributes=dict(type='dict',),
        description=dict(type='str',),
        http_methods=dict(type='list', elements='str', required=True),
        name=dict(type='str', required=True),
        resource=dict(type='str', required=True),
        tenant_ref=dict(type='str',),
        token_refill_rate=dict(type='dict', required=True),
        type=dict(type='str',),
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
    return avi_ansible_api(module, 'ratelimitconfiguration',
                           set())


if __name__ == '__main__':
    main()
