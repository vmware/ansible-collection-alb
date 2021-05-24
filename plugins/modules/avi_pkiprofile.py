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
module: avi_pkiprofile
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>

short_description: Module for setup of PKIProfile Avi RESTful Object
description:
    - This module is used to configure PKIProfile object
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
    ca_certs:
        description:
            - List of certificate authorities (root and intermediate) trusted that is used for certificate validation.
        type: list
    configpb_attributes:
        description:
            - Protobuf versioning for config pbs.
            - Field introduced in 21.1.1.
        type: dict
    created_by:
        description:
            - Creator name.
        type: str
    crl_check:
        description:
            - When enabled, avi will verify via crl checks that certificates in the trust chain have not been revoked.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    crls:
        description:
            - Certificate revocation lists.
        type: list
    ignore_peer_chain:
        description:
            - When enabled, avi will not trust intermediate and root certs presented by a client.
            - Instead, only the chain certs configured in the certificate authority section will be used to verify trust of the client's cert.
            - Allowed in basic(allowed values- true) edition, essentials(allowed values- true) edition, enterprise edition.
            - Special default for basic edition is true, essentials edition is true, enterprise is false.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    is_federated:
        description:
            - This field describes the object's replication scope.
            - If the field is set to false, then the object is visible within the controller-cluster and its associated service-engines.
            - If the field is set to true, then the object is replicated across the federation.
            - Field introduced in 17.1.3.
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
            - Name of the pki profile.
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
            - Unique object identifier of the object.
        type: str
    validate_only_leaf_crl:
        description:
            - When enabled, avi will only validate the revocation status of the leaf certificate using crl.
            - To enable validation for the entire chain, disable this option and provide all the relevant crls.
            - Allowed in basic(allowed values- true) edition, essentials(allowed values- true) edition, enterprise edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
extends_documentation_fragment:
    - vmware.alb.avi
'''

EXAMPLES = """
- name: Example to create PKIProfile object
  vmware.alb.avi_pkiprofile:
    controller: 192.168.15.18
    username: admin
    password: something
    state: present
    name: sample_pkiprofile
"""

RETURN = '''
obj:
    description: PKIProfile (api/pkiprofile) object
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
        ca_certs=dict(type='list',),
        configpb_attributes=dict(type='dict',),
        created_by=dict(type='str',),
        crl_check=dict(type='bool',),
        crls=dict(type='list',),
        ignore_peer_chain=dict(type='bool',),
        is_federated=dict(type='bool',),
        labels=dict(type='list',),
        markers=dict(type='list',),
        name=dict(type='str', required=True),
        tenant_ref=dict(type='str',),
        url=dict(type='str',),
        uuid=dict(type='str',),
        validate_only_leaf_crl=dict(type='bool',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_REQUESTS:
        return module.fail_json(msg=(
            'Python requests package is not installed. '
            'For installation instructions, visit https://pypi.org/project/requests.'))
    return avi_ansible_api(module, 'pkiprofile',
                           set())


if __name__ == '__main__':
    main()
