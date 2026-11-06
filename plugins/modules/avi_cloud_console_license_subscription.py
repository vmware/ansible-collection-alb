#!/usr/bin/python
# module_check: supported

# Avi Version: 17.1.1
# Copyright (c) 2026 Broadcom Inc. and/or its subsidiaries. All Rights Reserved. Broadcom Confidential.
# SPDX-License-Identifier: Apache License 2.0

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_cloud_console_license_subscription
author: Yograj Shisode (@shisodeyograj) <yograj.shisode@broadcom.com>
short_description: Avi API Module for pulse cloud license subscription
description:
    - This module can be used for subscribing or unsubscribing the controller to cloud licensing.
options:
    state:
        description:
            - The state that should be applied on the entity.
            - C(present) subscribes the controller.
            - C(absent) unsubscribes the controller.
        default: present
        choices: ["absent", "present"]
        type: str
    pool_id:
        description:
            - pool id to be specified for subscription.
        required: false
        type: str
extends_documentation_fragment:
    - vmware.alb.avi
'''

EXAMPLES = """
- name: Pulse cloud license subscription
  hosts: localhost
  vars:
    avi_credentials:
      username: "{{ username }}"
      password: "{{ password }}"
      controller: "{{ controller }}"
      api_version: "{{ api_version }}"
  tasks:
    - name: Pulse cloud license subscription
      vmware.alb.avi_cloud_console_license_subscription:
        avi_credentials: "{{ avi_credentials }}"
        state: present
        pool_id: 'Default'
"""
RETURN = '''
obj:
    description: Avi REST resource
    returned: success, changed
    type: dict
'''

import time
from ansible.module_utils.basic import AnsibleModule
try:
    from ansible_collections.vmware.alb.plugins.module_utils.utils.ansible_utils import (
        avi_common_argument_spec)
    from ansible_collections.vmware.alb.plugins.module_utils.avi_api import (
        ApiSession, AviCredentials)
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False


def main():
    argument_specs = dict(
        state=dict(default='present', choices=['absent', 'present']),
        pool_id=dict(type='str', required=False),
        api_context=dict(type='dict',),
        username=dict(type='str', default=''),
        tenant_uuid=dict(type='str', default=''),
        tenant=dict(type='str', default='admin'),
        password=dict(type='str', default='', no_log=True),
        controller=dict(type='str', default=''),
        api_version=dict(type='str', default='30.2.1'),
        avi_credentials=dict(type='dict',),
        avi_deactivate_session_cache_as_fact=dict(type='bool', default=False),
    )
    if HAS_REQUESTS:
        argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_REQUESTS:
        return module.fail_json(msg=(
            'Python requests package is not installed. '
            'For installation instructions, visit https://pypi.org/project/requests.'))

    api_creds = AviCredentials()
    api_creds.update_from_ansible_module(module)
    api = ApiSession.get_session(
        api_creds.controller, api_creds.username, password=api_creds.password,
        api_version=api_creds.api_version, timeout=api_creds.timeout,
        tenant=api_creds.tenant, tenant_uuid=api_creds.tenant_uuid,
        token=api_creds.token, port=api_creds.port)

    check_mode = module.check_mode
    state = module.params.get('state', None)
    pool_id = module.params.get('pool_id', None)

    path = "licensing/v1/cloud/subscribe/"

    # Check current status
    status_rsp = api.get("licensing/status")
    current_pool = None
    if status_rsp.status_code >= 300:
        return module.fail_json(msg='Failed to get licensing status: %s' % status_rsp.text)
    current_status = status_rsp.json()
    saas_status = current_status.get("saas_status", {})
    is_subscribed = saas_status.get("enabled", False)
    if is_subscribed and saas_status.get("pool"):
        current_pool = saas_status.get("pool").get("pool_id")

    if state == 'present':
        if not pool_id:
            return module.fail_json(msg='pool_id is required when state is present')

        if is_subscribed and current_pool == pool_id:
            return module.exit_json(changed=False, msg='Already subscribed', obj=current_status)

        if not check_mode:
            data = {"pool_id": pool_id}
            rsp = api.post(path, data=data)
            if rsp.status_code > 300:
                return module.fail_json(msg='Failed to subscribe: %s' % rsp.text)
            changed = True
            time.sleep(5)

            resp_data = {}
            try:
                resp_data = rsp.json()
            except Exception:
                pass

            return module.exit_json(changed=changed, msg='Subscribed successfully', obj=resp_data)
        else:
            return module.exit_json(changed=True, msg='Check mode: would have subscribed')
    else:
        if not is_subscribed:
            return module.exit_json(changed=False, msg='Already unsubscribed', obj=current_status)

        if not check_mode:
            rsp = api.delete(path)
            if rsp.status_code > 300:
                return module.fail_json(msg='Failed to unsubscribe: %s' % rsp.text)
            changed = True

            resp_data = {}
            try:
                resp_data = rsp.json()
            except Exception:
                pass

            return module.exit_json(changed=changed, msg='Unsubscribed successfully', obj=resp_data)
        else:
            return module.exit_json(changed=True, msg='Check mode: would have unsubscribed')


if __name__ == '__main__':
    main()
