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
module: avi_healthmonitor
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>

short_description: Module for setup of HealthMonitor Avi RESTful Object
description:
    - This module is used to configure HealthMonitor object
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
    allow_duplicate_monitors:
        description:
            - By default, multiple instances of the same healthmonitor to the same server are suppressed intelligently.
            - In rare cases, the monitor may have specific constructs that go beyond the server keys (ip, port, etc.) during which such suppression is not
            - desired.
            - Use this knob to allow duplicates.
            - Field introduced in 18.2.8.
            - Allowed in basic(allowed values- true) edition, essentials(allowed values- true) edition, enterprise edition.
        type: bool
    authentication:
        description:
            - Authentication information for username/password.
            - Field introduced in 20.1.1.
            - Allowed in basic edition, essentials edition, enterprise edition.
        type: dict
    configpb_attributes:
        description:
            - Protobuf versioning for config pbs.
            - Field introduced in 21.1.1.
        type: dict
    description:
        description:
            - User defined description for the object.
        type: str
    disable_quickstart:
        description:
            - During addition of a server or healthmonitors or during bootup, avi performs sequential health checks rather than waiting for send-interval to
            - kick in, to mark the server up as soon as possible.
            - This knob may be used to turn this feature off.
            - Field introduced in 18.2.7.
            - Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.
        type: bool
    dns_monitor:
        description:
            - Healthmonitordns settings for healthmonitor.
        type: dict
    external_monitor:
        description:
            - Healthmonitorexternal settings for healthmonitor.
        type: dict
    failed_checks:
        description:
            - Number of continuous failed health checks before the server is marked down.
            - Allowed values are 1-50.
            - Default value when not specified in API or module is interpreted by Avi Controller as 2.
        type: int
    http_monitor:
        description:
            - Healthmonitorhttp settings for healthmonitor.
        type: dict
    https_monitor:
        description:
            - Healthmonitorhttp settings for healthmonitor.
        type: dict
    imap_monitor:
        description:
            - Health monitor for imap.
            - Field introduced in 21.1.1.
        type: dict
    imaps_monitor:
        description:
            - Health monitor for imaps.
            - Field introduced in 21.1.1.
        type: dict
    is_federated:
        description:
            - This field describes the object's replication scope.
            - If the field is set to false, then the object is visible within the controller-cluster and its associated service-engines.
            - If the field is set to true, then the object is replicated across the federation.
            - Field introduced in 17.1.3.
            - Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    markers:
        description:
            - List of labels to be used for granular rbac.
            - Field introduced in 20.1.5.
        type: list
    monitor_port:
        description:
            - Use this port instead of the port defined for the server in the pool.
            - If the monitor succeeds to this port, the load balanced traffic will still be sent to the port of the server defined within the pool.
            - Allowed values are 1-65535.
            - Special values are 0 - 'use server port'.
        type: int
    name:
        description:
            - A user friendly name for this health monitor.
        required: true
        type: str
    pop3_monitor:
        description:
            - Health monitor for pop3.
            - Field introduced in 21.1.1.
        type: dict
    pop3s_monitor:
        description:
            - Health monitor for pop3s.
            - Field introduced in 21.1.1.
        type: dict
    radius_monitor:
        description:
            - Health monitor for radius.
            - Field introduced in 18.2.3.
            - Allowed in basic edition, essentials edition, enterprise edition.
        type: dict
    receive_timeout:
        description:
            - A valid response from the server is expected within the receive timeout window.
            - This timeout must be less than the send interval.
            - If server status is regularly flapping up and down, consider increasing this value.
            - Allowed values are 1-2400.
            - Unit is sec.
            - Default value when not specified in API or module is interpreted by Avi Controller as 4.
        type: int
    send_interval:
        description:
            - Frequency, in seconds, that monitors are sent to a server.
            - Allowed values are 1-3600.
            - Unit is sec.
            - Default value when not specified in API or module is interpreted by Avi Controller as 10.
        type: int
    sip_monitor:
        description:
            - Health monitor for sip.
            - Field introduced in 17.2.8, 18.1.3, 18.2.1.
            - Allowed in basic edition, essentials edition, enterprise edition.
        type: dict
    smtp_monitor:
        description:
            - Health monitor for smtp.
            - Field introduced in 21.1.1.
        type: dict
    smtps_monitor:
        description:
            - Health monitor for smtps.
            - Field introduced in 21.1.1.
        type: dict
    successful_checks:
        description:
            - Number of continuous successful health checks before server is marked up.
            - Allowed values are 1-50.
            - Default value when not specified in API or module is interpreted by Avi Controller as 2.
        type: int
    tcp_monitor:
        description:
            - Healthmonitortcp settings for healthmonitor.
        type: dict
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
        type: str
    type:
        description:
            - Type of the health monitor.
            - Enum options - HEALTH_MONITOR_PING, HEALTH_MONITOR_TCP, HEALTH_MONITOR_HTTP, HEALTH_MONITOR_HTTPS, HEALTH_MONITOR_EXTERNAL, HEALTH_MONITOR_UDP,
            - HEALTH_MONITOR_DNS, HEALTH_MONITOR_GSLB, HEALTH_MONITOR_SIP, HEALTH_MONITOR_RADIUS, HEALTH_MONITOR_SMTP, HEALTH_MONITOR_SMTPS,
            - HEALTH_MONITOR_POP3, HEALTH_MONITOR_POP3S, HEALTH_MONITOR_IMAP, HEALTH_MONITOR_IMAPS.
            - Allowed in basic(allowed values- health_monitor_ping,health_monitor_tcp,health_monitor_udp,health_monitor_http,health_monitor_https) edition,
            - essentials(allowed values- health_monitor_ping,health_monitor_tcp,health_monitor_udp) edition, enterprise edition.
        required: true
        type: str
    udp_monitor:
        description:
            - Healthmonitorudp settings for healthmonitor.
        type: dict
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Uuid of the health monitor.
        type: str
extends_documentation_fragment:
    - vmware.alb.avi
'''

EXAMPLES = """
- name: Create a HTTPS health monitor
  vmware.alb.avi_healthmonitor:
    controller: 192.168.138.18
    username: admin
    password: password
    https_monitor:
      http_request: HEAD / HTTP/1.0
      http_response_code:
        - HTTP_2XX
        - HTTP_3XX
    receive_timeout: 4
    failed_checks: 3
    send_interval: 10
    successful_checks: 3
    type: HEALTH_MONITOR_HTTPS
    name: MyWebsite-HTTPS
"""

RETURN = '''
obj:
    description: HealthMonitor (api/healthmonitor) object
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
        allow_duplicate_monitors=dict(type='bool',),
        authentication=dict(type='dict',),
        configpb_attributes=dict(type='dict',),
        description=dict(type='str',),
        disable_quickstart=dict(type='bool',),
        dns_monitor=dict(type='dict',),
        external_monitor=dict(type='dict',),
        failed_checks=dict(type='int',),
        http_monitor=dict(type='dict',),
        https_monitor=dict(type='dict',),
        imap_monitor=dict(type='dict',),
        imaps_monitor=dict(type='dict',),
        is_federated=dict(type='bool',),
        markers=dict(type='list',),
        monitor_port=dict(type='int',),
        name=dict(type='str', required=True),
        pop3_monitor=dict(type='dict',),
        pop3s_monitor=dict(type='dict',),
        radius_monitor=dict(type='dict',),
        receive_timeout=dict(type='int',),
        send_interval=dict(type='int',),
        sip_monitor=dict(type='dict',),
        smtp_monitor=dict(type='dict',),
        smtps_monitor=dict(type='dict',),
        successful_checks=dict(type='int',),
        tcp_monitor=dict(type='dict',),
        tenant_ref=dict(type='str',),
        type=dict(type='str', required=True),
        udp_monitor=dict(type='dict',),
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
    return avi_ansible_api(module, 'healthmonitor',
                           set())


if __name__ == '__main__':
    main()
