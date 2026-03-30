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
module: avi_sspinstance
author: Parikshit Manur (@pm020058) <parikshit.manur@broadcom.com>
short_description: Module for setup of SspInstance Avi RESTful Object
description:
    - This module is used to configure SspInstance object.
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
    avi_client_cert:
        description:
            - Client certificate that avi uses to authenticate with the ssp instance.
            - Field introduced in 32.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    client_cert:
        description:
            - Client certificate that the ssp instance uses to authenticate with avi.
            - Field introduced in 32.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    configpb_attributes:
        description:
            - Protobuf versioning for config pbs.
            - Field introduced in 32.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    description:
        description:
            - Description of the onboarded ssp feature instance.
            - Field introduced in 32.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    feature:
        description:
            - Type of the ssp feature instance.
            - Enum options - SSP_INTELLIGENT_ASSIST, SSP_CENTRAL_LICENSING_SERVICE.
            - Field introduced in 32.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        required: true
        type: str
    hostname:
        description:
            - Hostname of the ssp feature instance.
            - Field introduced in 32.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        required: true
        type: str
    ingress_cert:
        description:
            - Ingress (server) certificate chain that the ssp endpoint uses.
            - Field introduced in 32.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    name:
        description:
            - Name of the onboarded ssp feature instance.
            - Field introduced in 32.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        required: true
        type: str
    resources:
        description:
            - Resources associated with the ssp feature instance.
            - Field introduced in 32.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    status:
        description:
            - Status of the ssp feature instance.
            - Enum options - SSP_STATUS_IN_PROGRESS, SSP_STATUS_ACTIVE, SSP_STATUS_CERT_UPDATE_FAILED.
            - Field introduced in 32.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        required: true
        type: str
    tenant_ref:
        description:
            - Tenant reference for the ssp object.
            - It is a reference to an object of type tenant.
            - Field introduced in 32.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Uuid for the onboarded ssp feature instance.
            - Field introduced in 32.1.1.
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
    - name: Example to create SspInstance object
      vmware.alb.avi_sspinstance:
        avi_credentials: "{{ avi_credentials }}"
        state: present
        name: sample_sspinstance
"""

RETURN = '''
obj:
    description: SspInstance (api/sspinstance) object
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
        api_version=dict(type='str', default='18.2.6'),
        avi_credentials=dict(type='dict',),
        avi_deactivate_session_cache_as_fact=dict(type='bool', default=False),
        avi_client_cert=dict(type='str',),
        client_cert=dict(type='str',),
        configpb_attributes=dict(type='dict',),
        description=dict(type='str',),
        feature=dict(type='str', required=True),
        hostname=dict(type='str', required=True),
        ingress_cert=dict(type='str',),
        name=dict(type='str', required=True),
        resources=dict(type='dict',),
        status=dict(type='str', required=True),
        tenant_ref=dict(type='str',),
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
    return avi_ansible_api(module, 'sspinstance',
                           set())


if __name__ == '__main__':
    main()
