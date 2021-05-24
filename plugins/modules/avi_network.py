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
module: avi_network
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>

short_description: Module for setup of Network Avi RESTful Object
description:
    - This module is used to configure Network object
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
    attrs:
        description:
            - Key/value network attributes.
            - Field introduced in 20.1.1.
        type: list
    cloud_ref:
        description:
            - It is a reference to an object of type cloud.
        type: str
    configpb_attributes:
        description:
            - Protobuf versioning for config pbs.
            - Field introduced in 21.1.1.
        type: dict
    configured_subnets:
        description:
            - List of subnet.
        type: list
    dhcp_enabled:
        description:
            - Select the ip address management scheme for this network.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    exclude_discovered_subnets:
        description:
            - When selected, excludes all discovered subnets in this network from consideration for virtual service placement.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    ip6_autocfg_enabled:
        description:
            - Enable ipv6 auto configuration.
            - Field introduced in 18.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    labels:
        description:
            - Key/value labels which can be used for object access policy permission scoping.
            - Field deprecated in 20.1.5.
            - Field introduced in 18.2.7, 20.1.1.
        type: list
    markers:
        description:
            - List of labels to be used for granular rbac.
            - Field introduced in 20.1.5.
        type: list
    name:
        description:
            - Name of the object.
        required: true
        type: str
    synced_from_se:
        description:
            - Boolean flag to set synced_from_se.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
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
            - Unique object identifier of the object.
        type: str
    vcenter_dvs:
        description:
            - Boolean flag to set vcenter_dvs.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    vimgrnw_ref:
        description:
            - It is a reference to an object of type vimgrnwruntime.
        type: str
    vrf_context_ref:
        description:
            - It is a reference to an object of type vrfcontext.
        type: str
extends_documentation_fragment:
    - vmware.alb.avi
'''

EXAMPLES = """
- name: Example to create Network object
  vmware.alb.avi_network:
    controller: 192.168.15.18
    username: admin
    password: something
    state: present
    name: sample_network
"""

RETURN = '''
obj:
    description: Network (api/network) object
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
        attrs=dict(type='list',),
        cloud_ref=dict(type='str',),
        configpb_attributes=dict(type='dict',),
        configured_subnets=dict(type='list',),
        dhcp_enabled=dict(type='bool',),
        exclude_discovered_subnets=dict(type='bool',),
        ip6_autocfg_enabled=dict(type='bool',),
        labels=dict(type='list',),
        markers=dict(type='list',),
        name=dict(type='str', required=True),
        synced_from_se=dict(type='bool',),
        tenant_ref=dict(type='str',),
        url=dict(type='str',),
        uuid=dict(type='str',),
        vcenter_dvs=dict(type='bool',),
        vimgrnw_ref=dict(type='str',),
        vrf_context_ref=dict(type='str',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_REQUESTS:
        return module.fail_json(msg=(
            'Python requests package is not installed. '
            'For installation instructions, visit https://pypi.org/project/requests.'))
    return avi_ansible_api(module, 'network',
                           set())


if __name__ == '__main__':
    main()
