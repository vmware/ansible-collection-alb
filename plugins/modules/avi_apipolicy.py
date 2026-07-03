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
module: avi_apipolicy
author: Parikshit Manur (@pm020058) <parikshit.manur@broadcom.com>
short_description: Module for setup of ApiPolicy Avi RESTful Object
description:
    - This module is used to configure ApiPolicy object.
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
    active_api_labels:
        description:
            - List of labels applied to active api endpoints.
            - An active api is an endpoint whose type is api_active.
            - Endpoints defined in the policy are active by default.
            - Field introduced in 32.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    api_spec_info:
        description:
            - Api specification metadata extracted from the associated openapi specification.
            - Automatically populated when a fileobject is associated with this policy.
            - Field introduced in 32.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    configpb_attributes:
        description:
            - Protobuf versioning for config pbs.
            - Field introduced in 32.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    description:
        description:
            - Description of this api policy.
            - Field introduced in 32.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    file_object_refs:
        description:
            - Reference to the uploaded openapi specification file associated with this policy.
            - Only one file is supported at a time.
            - It is a reference to an object of type fileobject.
            - Field introduced in 32.2.1.
            - Maximum of 1 items allowed.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: str
    label_mappings:
        description:
            - Mapping of labels to api policy actions.
            - Field introduced in 32.2.1.
            - Maximum of 256 items allowed.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: dict
    name:
        description:
            - Name of this object, unique per tenant.
            - Field introduced in 32.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        required: true
        type: str
    non_api_url_labels:
        description:
            - List of labels applied to non-api url requests.
            - Non-api urls are methods and urls that are outside the scope of the policy.
            - These are usually used to retrieve static information that are not tied to back-end business logic.
            - Field introduced in 32.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    orphan_api_classification_settings:
        description:
            - Orphan api classification settings for this api policy.
            - Field introduced in 32.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    orphan_api_labels:
        description:
            - List of labels applied to orphan api endpoints.
            - An orphan api is an endpoint that is specified in the api-spec but has not been seen in the datapath for a predefined duration.
            - Field introduced in 32.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    path_refs:
        description:
            - List of path specifications.
            - When an oas fileobject is associated to this apipolicy, the paths defined in the oas fileobject will be automatically added to this list.
            - If oas fileobject has a path that is already defined in the list, the existing path in the list will be updated as per the oas fileobject.
            - It is a reference to an object of type apipath.
            - Field introduced in 32.2.1.
            - Maximum of 5000 items allowed.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: str
    routing_info:
        description:
            - Optional header-based routing configuration for evh child vs selection.
            - When set, the rules inside are used in addition to server fqdns (host match) and server_info.path_prefix (path match) to determine which child vs
            - handles a request.
            - Field introduced in 32.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    server_info:
        description:
            - Server list defining the scope of this api policy.
            - Requests not matching any server url are treated as non-api traffic.
            - Field introduced in 32.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    shadow_api_labels:
        description:
            - List of labels applied to shadow api endpoints.
            - A shadow api is an endpoint that is not specified in the api-spec but is inside the scope of this policy (matching the server url and path
            - prefix) and is seen in the datapath.
            - Field introduced in 32.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
            - Field introduced in 32.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
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
    validation_settings:
        description:
            - Validation settings for this api policy.
            - Field introduced in 32.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    zombie_api_classification_settings:
        description:
            - Zombie api classification settings for this api policy.
            - Field introduced in 32.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    zombie_api_labels:
        description:
            - List of labels applied to zombie api endpoints.
            - A zombie api is an endpoint that is specified in the api-spec but is seen in the datapath only as drip-traffic over a predefined duration.
            - Field introduced in 32.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
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
    - name: Example to create ApiPolicy object
      vmware.alb.avi_apipolicy:
        avi_credentials: "{{ avi_credentials }}"
        state: present
        name: sample_apipolicy
"""

RETURN = '''
obj:
    description: ApiPolicy (api/apipolicy) object
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
        active_api_labels=dict(type='dict',),
        api_spec_info=dict(type='dict',),
        configpb_attributes=dict(type='dict',),
        description=dict(type='str',),
        file_object_refs=dict(type='list', elements='str',),
        label_mappings=dict(type='list', elements='dict',),
        name=dict(type='str', required=True),
        non_api_url_labels=dict(type='dict',),
        orphan_api_classification_settings=dict(type='dict',),
        orphan_api_labels=dict(type='dict',),
        path_refs=dict(type='list', elements='str',),
        routing_info=dict(type='dict',),
        server_info=dict(type='dict',),
        shadow_api_labels=dict(type='dict',),
        tenant_ref=dict(type='str',),
        url=dict(type='str',),
        uuid=dict(type='str',),
        validation_settings=dict(type='dict',),
        zombie_api_classification_settings=dict(type='dict',),
        zombie_api_labels=dict(type='dict',),
    )
    if HAS_REQUESTS:
        argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_REQUESTS:
        return module.fail_json(msg=(
            'Python requests package is not installed. '
            'For installation instructions, visit https://pypi.org/project/requests.'))
    return avi_ansible_api(module, 'apipolicy',
                           set())


if __name__ == '__main__':
    main()
