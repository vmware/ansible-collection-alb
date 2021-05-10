#!/usr/bin/python3
# module_check: supported

# Avi Version: 17.1.1
# Copyright 2021 VMware, Inc.  All rights reserved. VMware Confidential
# SPDX-License-Identifier: Apache License 2.0

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_httppolicyset
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>

short_description: Module for setup of HTTPPolicySet Avi RESTful Object
description:
    - This module is used to configure HTTPPolicySet object
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
    cloud_config_cksum:
        description:
            - Checksum of cloud configuration for pool.
            - Internally set by cloud connector.
        type: str
    configpb_attributes:
        description:
            - Protobuf versioning for config pbs.
            - Field introduced in 21.1.1.
        type: dict
    created_by:
        description:
            - Creator name.
        type: str
    description:
        description:
            - User defined description for the object.
        type: str
    geo_db_ref:
        description:
            - Geo database.
            - It is a reference to an object of type geodb.
            - Field introduced in 21.1.1.
        type: str
    http_request_policy:
        description:
            - Http request policy for the virtual service.
        type: dict
    http_response_policy:
        description:
            - Http response policy for the virtual service.
        type: dict
    http_security_policy:
        description:
            - Http security policy for the virtual service.
        type: dict
    ip_reputation_db_ref:
        description:
            - Ip reputation database.
            - It is a reference to an object of type ipreputationdb.
            - Field introduced in 20.1.3.
        type: str
    is_internal_policy:
        description:
            - Boolean flag to set is_internal_policy.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    labels:
        description:
            - Key value pairs for granular object access control.
            - Also allows for classification and tagging of similar objects.
            - Field deprecated in 20.1.5.
            - Field introduced in 20.1.2.
            - Maximum of 4 items allowed.
        type: list
    markers:
        description:
            - List of labels to be used for granular rbac.
            - Field introduced in 20.1.5.
        type: list
    name:
        description:
            - Name of the http policy set.
        required: true
        type: str
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Uuid of the http policy set.
        type: str
extends_documentation_fragment:
    - vmware.alb.avi
'''

EXAMPLES = """
- name: Create a HTTP Policy set two switch between testpool1 and testpool2
  vmware.alb.avi_httppolicyset:
    controller: 192.168.138.18
    username: admin
    password: password
    name: test-HTTP-Policy-Set
    tenant_ref: /api/tenant?name=admin
    http_request_policy:
    rules:
      - index: 1
        enable: true
        name: test-test1
        match:
          path:
            match_case: INSENSITIVE
            match_str:
              - /test1
            match_criteria: EQUALS
        switching_action:
          action: HTTP_SWITCHING_SELECT_POOL
          status_code: HTTP_LOCAL_RESPONSE_STATUS_CODE_200
          pool_ref: "/api/pool?name=testpool1"
      - index: 2
        enable: true
        name: test-test2
        match:
          path:
            match_case: INSENSITIVE
            match_str:
              - /test2
            match_criteria: CONTAINS
        switching_action:
          action: HTTP_SWITCHING_SELECT_POOL
          status_code: HTTP_LOCAL_RESPONSE_STATUS_CODE_200
          pool_ref: "/api/pool?name=testpool2"
    is_internal_policy: false
"""

RETURN = '''
obj:
    description: HTTPPolicySet (api/httppolicyset) object
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
        cloud_config_cksum=dict(type='str',),
        configpb_attributes=dict(type='dict',),
        created_by=dict(type='str',),
        description=dict(type='str',),
        geo_db_ref=dict(type='str',),
        http_request_policy=dict(type='dict',),
        http_response_policy=dict(type='dict',),
        http_security_policy=dict(type='dict',),
        ip_reputation_db_ref=dict(type='str',),
        is_internal_policy=dict(type='bool',),
        labels=dict(type='list',),
        markers=dict(type='list',),
        name=dict(type='str', required=True),
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
    return avi_ansible_api(module, 'httppolicyset',
                           set())


if __name__ == '__main__':
    main()
