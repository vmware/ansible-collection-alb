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
module: avi_poolgroup
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>

short_description: Module for setup of PoolGroup Avi RESTful Object
description:
    - This module is used to configure PoolGroup object
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
            - Checksum of cloud configuration for poolgroup.
            - Internally set by cloud connector.
        type: str
    cloud_ref:
        description:
            - It is a reference to an object of type cloud.
        type: str
    configpb_attributes:
        description:
            - Protobuf versioning for config pbs.
            - Field introduced in 21.1.1.
        type: dict
    created_by:
        description:
            - Name of the user who created the object.
        type: str
    deployment_policy_ref:
        description:
            - When setup autoscale manager will automatically promote new pools into production when deployment goals are met.
            - It is a reference to an object of type poolgroupdeploymentpolicy.
        type: str
    description:
        description:
            - Description of pool group.
        type: str
    enable_http2:
        description:
            - Enable http/2 for traffic from virtualservice to all the backend servers in all the pools configured under this poolgroup.
            - Field introduced in 20.1.1.
            - Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    fail_action:
        description:
            - Enable an action - close connection, http redirect, or local http response - when a pool group failure happens.
            - By default, a connection will be closed, in case the pool group experiences a failure.
        type: dict
    implicit_priority_labels:
        description:
            - Whether an implicit set of priority labels is generated.
            - Field introduced in 17.1.9,17.2.3.
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
    members:
        description:
            - List of pool group members object of type poolgroupmember.
        type: list
    min_servers:
        description:
            - The minimum number of servers to distribute traffic to.
            - Allowed values are 1-65535.
            - Special values are 0 - 'disable'.
            - Allowed in basic(allowed values- 0) edition, essentials(allowed values- 0) edition, enterprise edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    name:
        description:
            - The name of the pool group.
        required: true
        type: str
    priority_labels_ref:
        description:
            - Uuid of the priority labels.
            - If not provided, pool group member priority label will be interpreted as a number with a larger number considered higher priority.
            - It is a reference to an object of type prioritylabels.
        type: str
    service_metadata:
        description:
            - Metadata pertaining to the service provided by this poolgroup.
            - In openshift/kubernetes environments, app metadata info is stored.
            - Any user input to this field will be overwritten by avi vantage.
            - Field introduced in 17.2.14,18.1.5,18.2.1.
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
            - Uuid of the pool group.
        type: str
extends_documentation_fragment:
    - vmware.alb.avi
'''

EXAMPLES = """
- name: Example to create PoolGroup object
  vmware.alb.avi_poolgroup:
    controller: 192.168.15.18
    username: admin
    password: something
    state: present
    name: sample_poolgroup
"""

RETURN = '''
obj:
    description: PoolGroup (api/poolgroup) object
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
        cloud_ref=dict(type='str',),
        configpb_attributes=dict(type='dict',),
        created_by=dict(type='str',),
        deployment_policy_ref=dict(type='str',),
        description=dict(type='str',),
        enable_http2=dict(type='bool',),
        fail_action=dict(type='dict',),
        implicit_priority_labels=dict(type='bool',),
        labels=dict(type='list',),
        markers=dict(type='list',),
        members=dict(type='list',),
        min_servers=dict(type='int',),
        name=dict(type='str', required=True),
        priority_labels_ref=dict(type='str',),
        service_metadata=dict(type='str',),
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
    return avi_ansible_api(module, 'poolgroup',
                           set())


if __name__ == '__main__':
    main()
