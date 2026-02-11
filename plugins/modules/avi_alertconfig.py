#!/usr/bin/python
# module_check: supported

# Copyright 2021 VMware, Inc.  All rights reserved. VMware Confidential
# SPDX-License-Identifier: Apache License 2.0
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_alertconfig
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of AlertConfig Avi RESTful Object
description:
    - This module is used to configure AlertConfig object.
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
    action_group_ref:
        description:
            - The alert config will trigger the selected alert action, which can send notifications and execute a controlscript.
            - It is a reference to an object of type actiongroupconfig.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    alert_rule:
        description:
            - List of filters matching on events or client logs used for triggering alerts.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        required: true
        type: dict
    autoscale_alert:
        description:
            - This alert config applies to auto scale alerts.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: bool
    category:
        description:
            - Determines whether an alert is raised immediately when event occurs (realtime) or after specified number of events occurs within rolling time
            - window.
            - Enum options - REALTIME, ROLLINGWINDOW, WATERMARK.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as REALTIME.
        type: str
    configpb_attributes:
        description:
            - Protobuf versioning for config pbs.
            - Field introduced in 21.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    description:
        description:
            - A custom description field.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    enabled:
        description:
            - Enable or disable this alert config from generating new alerts.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    expiry_time:
        description:
            - An alert is expired and deleted after the expiry time has elapsed.
            - The original event triggering the alert remains in the events log.
            - Allowed values are 1-31536000.
            - Unit is sec.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 86400.
        type: int
    name:
        description:
            - Name of the alert configuration.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        required: true
        type: str
    obj_uuid:
        description:
            - Instance of the resource for which alert was raised.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    object_type:
        description:
            - The object type to which the alert config is associated with.
            - Valid object types are - virtual service, pool, service engine.
            - Enum options - VIRTUALSERVICE, POOL, HEALTHMONITOR, NETWORKPROFILE, APPLICATIONPROFILE, HTTPPOLICYSET, DNSPOLICY, SECURITYPOLICY, IPADDRGROUP,
            - STRINGGROUP, SSLPROFILE, SSLKEYANDCERTIFICATE, NETWORKSECURITYPOLICY, APPLICATIONPERSISTENCEPROFILE, ANALYTICSPROFILE, VSDATASCRIPTSET, TENANT,
            - PKIPROFILE, AUTHPROFILE, CLOUD...
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    recommendation:
        description:
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    rolling_window:
        description:
            - Only if the number of events is reached or exceeded within the time window will an alert be generated.
            - Allowed values are 1-31536000.
            - Unit is sec.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 300.
        type: int
    source:
        description:
            - Signifies system events or the type of client logsused in this alert configuration.
            - Enum options - CONN_LOGS, APP_LOGS, EVENT_LOGS, METRICS.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        required: true
        type: str
    summary:
        description:
            - Summary of reason why alert is generated.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    threshold:
        description:
            - An alert is created only when the number of events meets or exceeds this number within the chosen time frame.
            - Allowed values are 1-65536.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1.
        type: int
    throttle:
        description:
            - Alerts are suppressed (throttled) for this duration of time since the last alert was raised for this alert config.
            - Allowed values are 0-31536000.
            - Unit is sec.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 600.
        type: int
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    # Fields from avi_common_argument_spec()
    controller:
        description:
            - Avi controller hostname or IP address.
        type: str
        required: false
        default: ""
    username:
        description:
            - Avi username for authentication.
        type: str
        required: false
        default: ""
    password:
        description:
            - Avi password for authentication.
        type: str
        required: false
        default: ""
    tenant:
        description:
            - Tenant name.
        type: str
        required: false
        default: admin
    tenant_uuid:
        description:
            - Tenant UUID.
        type: str
        required: false
        default: ""
    api_version:
        description:
            - Avi API version to use.
        type: str
        required: false
        default: "20.1.1"
    avi_credentials:
        description:
            - Dictionary of Avi credentials (alternative to controller/username/password/token).
        type: dict
        required: false
        suboptions:
            controller:
                description: Avi controller hostname or IP address.
                type: str
                default: ""
            username:
                description: Avi username.
                type: str
                default: ""
            password:
                description: Avi password.
                type: str
                default: ""
            api_version:
                description: Avi API version.
                type: str
                default: "20.1.1"
            tenant:
                description: Tenant name.
                type: str
                default: "admin"
            tenant_uuid:
                description: Tenant UUID.
                type: str
                default: ""
            port:
                description: Port of the Avi controller.
                type: int
            token:
                description: Avi API token.
                type: str
                default: ""
            timeout:
                description: Timeout for API requests (in seconds).
                type: int
                default: 300
            session_id:
                description: Session ID for authentication.
                type: str
                default: ""
            csrftoken:
                description: CSRF token for authentication.
                type: str
                default: ""
            ssl_cert:
                description: SSL certificate path for HTTPS requests.
                type: str
                default: ""
            ssl_key:
                description: SSL private key path for HTTPS requests.
                type: str
                default: ""
            idp_class:
                description: Identity provider class.
                type: str
                required: false
                default: ''
            csp_token:
                description: Identity provider class.
                type: str
                required: false
                default: ''
            csp_host:
                description: Identity provider class.
                type: str
                required: false
                default: ''
    api_context:
        description:
            - Optional dictionary for API context.
        type: dict
        required: false
    avi_deactivate_session_cache_as_fact:
        description:
            - Boolean to deactivate session cache and expose it as an Ansible fact.
        type: bool
        required: false
        default: false

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
    - name: Example to create AlertConfig object
      vmware.alb.avi_alertconfig:
        avi_credentials: "{{ avi_credentials }}"
        state: present
        name: sample_alertconfig
"""

RETURN = '''
obj:
    description: AlertConfig (api/alertconfig) object
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
        action_group_ref=dict(type='str',),
        alert_rule=dict(type='dict', required=True),
        autoscale_alert=dict(type='bool',),
        category=dict(type='str',),
        configpb_attributes=dict(type='dict',),
        description=dict(type='str',),
        enabled=dict(type='bool',),
        expiry_time=dict(type='int',),
        name=dict(type='str', required=True),
        obj_uuid=dict(type='str',),
        object_type=dict(type='str',),
        recommendation=dict(type='str',),
        rolling_window=dict(type='int',),
        source=dict(type='str', required=True),
        summary=dict(type='str',),
        tenant_ref=dict(type='str',),
        threshold=dict(type='int',),
        throttle=dict(type='int',),
        url=dict(type='str',),
        uuid=dict(type='str',),
    )
    STATIC_COMMON_ARGS = dict(
        controller=dict(type='str', required=False),
        username=dict(type='str', required=False),
        password=dict(type='str', required=False, no_log=True),
        tenant=dict(type='str', required=False),
        tenant_uuid=dict(type='str', required=False),
        api_version=dict(type='str', required=False),
        avi_credentials=dict(type='dict', required=False),
        api_context=dict(type='dict', required=False),
        avi_deactivate_session_cache_as_fact=dict(type='bool', required=False),
    )
    argument_specs.update(STATIC_COMMON_ARGS)
    if HAS_REQUESTS:
        argument_specs.update(avi_common_argument_spec())

    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_REQUESTS:
        return module.fail_json(msg=(
            'Python requests package is not installed. '
            'For installation instructions, visit https://pypi.org/project/requests.'))
    return avi_ansible_api(module, 'alertconfig',
                           set())


if __name__ == '__main__':
    main()
