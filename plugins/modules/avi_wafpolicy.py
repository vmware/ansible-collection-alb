#!/usr/bin/python3
# module_check: supported

# Copyright 2021 VMware, Inc. All rights reserved. VMware Confidential
# SPDX-License-Identifier: Apache License 2.0


from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_wafpolicy
author: Chaitanya Deshpande (@chaitanyaavi) <chaitanya.deshpande@avinetworks.com>
short_description: Avi WAF Policy Module
description:
    - This module can be used for creation, updation and deletion of a user.
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
    name:
        description:
            - Name of Waf policy.
        required: true
        type: str
    base_waf_policy:
        description:
            - Name of the base waf policy on which patch is applied
        required: true
        type: str
    patch_file:
        description:
            - File path of json patch file
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
    allow_mode_delegation:
        description:
            - Allow Rules to overwrite the policy mode.
            - This must be set if the policy mode is set to enforcement.
        type: bool
    created_by:
        description:
            - Creator name.
        type: str
    crs_groups:
        description:
            - WAF Rules are categorized in to groups based on their characterization.
            - These groups are system created with CRS groups.
        type: list
    description:
        description:
            - Free-text comment about this exclusion.
        type: str
    enable_app_learning:
        description:
            - Enable Application Learning for this WAF policy.
        type: bool
    failure_mode:
        description:
            - WAF Policy failure mode. This can be 'Open' or 'Closed'.
        type: str
    learning:
        description:
            - Configure parameters for WAF learning.
        type: dict
    mode:
        description:
            - WAF Rule mode. This can be detection or enforcement.
            - If this is not set, the Policy mode is used.
            - This only takes effect if the policy allows delegation.
        type: str
    paranoia_level:
        description:
            - WAF Ruleset paranoia mode. This is used to select Rules based on the paranoia-level.
        type: str
    positive_security_model:
        description:
            - The Positive Security Model.
            - This is used to describe how the request or parts of the request should look like.
            - It is executed in the Request Body Phase of Avi WAF.",
        type: dict
    post_crs_groups:
        description:
            - WAF Rules are categorized in to groups based on their characterization.
            - These groups are created by the user and will be enforced after the CRS groups.
        type: list
    pre_crs_groups:
        description:
            - WAF Rules are categorized in to groups based on their characterization.
            - These groups are created by the user and will be enforced before the CRS groups.
        type: list
    waf_crs_ref:
        description:
            - It is a reference to an object of type waf crs.
        type: str
    waf_profile_ref:
        description:
            - It is a reference to an object of type waf profile.
        type: str
    whitelist:
        description:
            - Rules to bypass WAF.
        type: dict
    avi_patch_path:
        description:
            - Patch path to use when using avi_api_update_method as patch.
        type: str
    avi_patch_value:
        description:
            - Patch value to use when using avi_api_update_method as patch.
        type: str
extends_documentation_fragment:
    - vmware.alb.avi
'''

EXAMPLES = '''
  - name: Create WAF Policy Example using System-Waf-Policy as base policy
    vmware.alb.avi_wafpolicy:
      avi_credentials: ''
      patch_file: ./vs-1-waf-policy-patches.json
      base_waf_policy: System-WAF-Policy
      name: vs1-waf-policy
      state: present
'''

RETURN = '''
obj:
    description: Avi REST resource
    returned: success, changed
    type: dict
'''

import json
from copy import deepcopy
from ansible.module_utils.basic import AnsibleModule


try:
    from ansible_collections.vmware.alb.plugins.module_utils.utils.ansible_utils import (
        avi_common_argument_spec, ansible_return, avi_obj_cmp,
        cleanup_absent_fields)
    from ansible_collections.vmware.alb.plugins.module_utils.avi_api import (
        ApiSession, AviCredentials)
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False


def update_patch(base_policy, patch):
    base_policy.pop('_last_modified', '')
    base_policy.pop('url', '')
    for k, v in base_policy.items():
        if k in patch and not k == 'crs_groups':
            base_policy[k] = patch[k]
    if 'crs_groups' in patch:
        base_group_dict = dict()
        # Converting list to dict for quick patch iterations
        for group in base_policy['crs_groups']:
            base_group_dict[group['name']] = group
            rules = group.pop('rules')
            group['rules'] = {}
            for rule in rules:
                rk = '%s$$%s' % (rule['rule_id'], rule['name'])
                base_group_dict[group['name']]['rules'][rk] = rule

        # Iterating over patch and updating base policy rules
        for p_group in patch['crs_groups']:
            base_group = base_group_dict.get(p_group['name'], None)
            if not base_group:
                base_group_dict[p_group['name']] = p_group
                continue
            for p_rule in p_group['rules']:
                p_rk = '%s$$%s' % (p_rule['rule_id'], p_rule['name'])
                base_rule = base_group['rules'].get(p_rk)
                state = base_rule.pop('state', 'present')
                if not state == 'present':
                    base_group['rules'].pop(p_rule['index'])
                    continue
                if base_rule:
                    base_rule.update(p_rule)
                else:
                    base_group['rules'][p_rule['index']] = p_rule

        # Converting dict back to object structure
        for bg_name in base_group_dict:
            base_group_dict[bg_name]['rules'] = sorted(
                base_group_dict[bg_name]['rules'].values(),
                key=lambda i: i['index'])
        base_policy['crs_groups'] = sorted(
            base_group_dict.values(), key=lambda i: i['index'])


def main():
    argument_specs = dict(
        state=dict(default='present',
                   choices=['absent', 'present']),
        avi_api_update_method=dict(default='put',
                                   choices=['put', 'patch']),
        avi_api_patch_op=dict(choices=['add', 'replace', 'delete', 'remove']),
        avi_patch_path=dict(type='str',),
        avi_patch_value=dict(type='str',),
        allow_mode_delegation=dict(type='bool',),
        created_by=dict(type='str',),
        crs_groups=dict(type='list',),
        description=dict(type='str',),
        enable_app_learning=dict(type='bool',),
        failure_mode=dict(type='str',),
        learning=dict(type='dict',),
        mode=dict(type='str'),
        name=dict(type='str', required=True),
        paranoia_level=dict(type='str',),
        positive_security_model=dict(type='dict',),
        post_crs_groups=dict(type='list',),
        pre_crs_groups=dict(type='list',),
        tenant_ref=dict(type='str',),
        url=dict(type='str',),
        uuid=dict(type='str',),
        waf_crs_ref=dict(type='str',),
        waf_profile_ref=dict(type='str'),
        whitelist=dict(type='dict',),
        base_waf_policy=dict(type='str', required=True),
        patch_file=dict(type='str', required=True),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(argument_spec=argument_specs,
                           supports_check_mode=True)
    if not HAS_REQUESTS:
        return module.fail_json(msg=(
                    'Python requests package is not installed. '
                    'For installation instructions, visit https://pypi.org/project/requests.'))
    api_creds = AviCredentials()
    api_creds.update_from_ansible_module(module)
    api = ApiSession.get_session(
        api_creds.controller, api_creds.username, password=api_creds.password,
        timeout=api_creds.timeout, tenant=api_creds.tenant,
        tenant_uuid=api_creds.tenant_uuid, token=api_creds.token,
        port=api_creds.port, api_version=api_creds.api_version)

    obj_uuid = None
    existing_obj = api.get_object_by_name(
        'wafpolicy', module.params.get('name'),
        params={"include_name": True})
    if existing_obj:
        obj_uuid = existing_obj.pop('uuid', None)

    changed = False

    # Delete call if state is absent
    if module.params.get('state') == 'absent':
        if obj_uuid:
            changed = True
        if changed and not module.check_mode:
            api.delete_by_name('wafpolicy', module.params.get('name'))
        ansible_return(
            module, None, changed, existing_obj=existing_obj,
            api_context=api.get_context())

    if not existing_obj:
        existing_obj = api.get_object_by_name(
            'wafpolicy', module.params.get('base_waf_policy'),
            params={"include_name": True})

    with open(module.params.get('patch_file'), "r+") as f:
        waf_patch = json.loads(f.read())
        waf_patch.update((k, v) for k, v in module.params.items()
                         if v and k not in waf_patch)
        new_obj = deepcopy(existing_obj)
        update_patch(new_obj, waf_patch)
        changed = not avi_obj_cmp(new_obj, existing_obj)
        if module.check_mode:
            ansible_return(
                module, None, changed, existing_obj=existing_obj,
                api_context=api.get_context())
        rsp = None
        if changed:
            if obj_uuid:
                new_obj['uuid'] = obj_uuid
                rsp = api.put('wafpolicy/%s' % obj_uuid, data=new_obj)
            else:
                rsp = api.post('wafpolicy', data=new_obj)

        ansible_return(module, rsp, changed, req=new_obj)


if __name__ == '__main__':
    main()
