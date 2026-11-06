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
module: avi_cloud_console_registration
author: Yograj Shisode (@shisodeyograj) <yograj.shisode@broadcom.com>

short_description: Avi API Module for cloud registration
description:
    - This module can be used for registering or deregistering the controller with pulse.
options:
    state:
        description:
            - The state that should be applied on the entity.
            - C(present) registers the controller.
            - C(absent) deregisters the controller.
        default: present
        choices: ["absent", "present"]
        type: str
    jwt_token:
        description:
            - Token which is used to login to pulse from controller for the specific user.
            - For generation of the jwt_token paste the link https://portal.pulse.broadcom.com/portal/auth/broadcomtoken
              in Incognito window to prevent IdP from considering any existing valid login session
            - jwt_token is valid for 180 days.
            - Required when I(state=present).
        required: false
        type: str
    name:
        description:
            - Controller name to be specified for registration.
            - Required when I(state=present).
        required: false
        type: str
    description:
        description:
            - description to be specified for registration.
            - Required when I(state=present).
        required: false
        type: str
    email:
        description:
            - email to be specified for registration.
            - Required when I(state=present).
        required: false
        type: str
    site_id:
        description:
            - site id to be specified for registration.
            - Required when I(state=present).
        required: false
        type: str
extends_documentation_fragment:
    - vmware.alb.avi
'''

EXAMPLES = """
- name: Register for Avi Pulse
  hosts: localhost
  vars:
    avi_credentials:
      username: "{{ username }}"
      password: "{{ password }}"
      controller: "{{ controller }}"
      api_version: "{{ api_version }}"
  tasks:
    - name: Cloud registration or deregistration
      vmware.alb.avi_cloud_console_registration:
        avi_credentials: "{{ avi_credentials }}"
        state: present
        jwt_token: "{{ jwt_token }}"
        name: 'AviPulse'
        description: 'Registration and deregistration'
        email: 'user@gmail.com'
        site_id: '123456789'
    - name: Sleep for 7 seconds and continue with play
      ansible.builtin.wait_for:
        timeout: 7
      delegate_to: localhost
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
        avi_common_argument_spec, AviCheckModeResponse)
    from ansible_collections.vmware.alb.plugins.module_utils.avi_api import (
        ApiSession, AviCredentials)
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False


def main():
    argument_specs = dict(
        state=dict(default='present', choices=['absent', 'present']),
        jwt_token=dict(type='str', required=False, no_log=True),
        name=dict(required=False, type='str'),
        description=dict(type='str', required=False),
        email=dict(type='str', required=False),
        site_id=dict(type='str', required=False),
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
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True,
        required_if=[('state', 'present', ['jwt_token', 'name', 'description', 'email', 'site_id'])])
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
    api_version = api_creds.api_version
    tenant_uuid = api_creds.tenant_uuid
    tenant = api_creds.tenant
    check_mode = module.check_mode
    path = module.params.get('path', '')
    state = module.params.get('state', None)
    jwt_token = module.params.get('jwt_token', None)
    name = module.params.get('name', None)
    description = module.params.get('description', None)
    email = module.params.get('email', None)
    site_id = module.params.get('site_id', None)
    changed = False

    path = "albservices/status"
    resp = api.get(path, tenant=tenant, tenant_uuid=tenant_uuid, api_version=api_version)
    if resp.status_code > 300:
        return module.fail_json(msg='Failed to get albservices status: %s' % resp.text)
    existing_obj = resp

    if state == 'present':
        # registration
        connectivity_status = resp.json().get("connectivity_status")
        registration_status = resp.json().get("registration_status")
        needs_refresh = connectivity_status in ("ALBSERVICES_DISCONNECTED", "ALBSERVICES_CONNECTIVITY_UNKNOWN")
        needs_register = registration_status in ("ALBSERVICES_DEREGISTERED", "ALBSERVICES_REGISTRATION_UNKNOWN")

        if not (check_mode) and needs_refresh:
            data = {"jwt_token": jwt_token}
            path = "portal/refresh-access-token"
            rsp = api.post(path, api_version=api_version, data=data)
            if rsp.status_code > 300:
                return module.fail_json(msg='Failed to refresh access token: %s' % rsp.text)
            else:
                changed = True
                time.sleep(10)

        if not (check_mode) and needs_register:
            path = "albservices/register"
            data = {"name": name, "description": description, "email": email,
                    "site_id": site_id}
            rsp = api.post(path, data=data)

            if rsp.status_code > 300:
                return module.fail_json(msg='Failed to register controller with pulse: %s' % rsp.text)
            else:
                changed = True
                time.sleep(5)

        if check_mode:
            rsp = AviCheckModeResponse(obj=existing_obj)
            changed = needs_refresh or needs_register
            time.sleep(5)

        return module.exit_json(changed=changed, msg='Registered successfully')
    else:
        # deregistration
        if not (check_mode) and resp.json().get("registration_status") == "ALBSERVICES_REGISTERED":
            path = "albservices/register"
            data = {"status": "Obsolete"}
            rsp = api.put(path, data=data)
            if rsp.status_code > 300:
                return module.fail_json(msg='Failed to deregister controller from pulse: %s' % rsp.text)
            else:
                changed = True
                time.sleep(5)

        if check_mode:
            rsp = AviCheckModeResponse(obj=existing_obj)
            changed = True
            time.sleep(5)

        if resp.json().get("registration_status") == "ALBSERVICES_DEREGISTERED":
            changed = False

        return module.exit_json(
            changed=changed, msg="Deregistered successfully")


if __name__ == '__main__':
    main()
