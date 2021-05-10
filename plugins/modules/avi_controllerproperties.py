#!/usr/bin/python3
# module_check: supported

# Avi Version: 17.1.2
# Copyright 2021 VMware, Inc.  All rights reserved. VMware Confidential
# SPDX-License-Identifier: Apache License 2.0

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_controllerproperties
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>

short_description: Module for setup of ControllerProperties Avi RESTful Object
description:
    - This module is used to configure ControllerProperties object
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
    allow_admin_network_updates:
        description:
            - Allow non-admin tenants to update admin vrfcontext and network objects.
            - Field introduced in 18.2.7, 20.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    allow_ip_forwarding:
        description:
            - Field introduced in 17.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    allow_unauthenticated_apis:
        description:
            - Allow unauthenticated access for special apis.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    allow_unauthenticated_nodes:
        description:
            - Boolean flag to set allow_unauthenticated_nodes.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    api_idle_timeout:
        description:
            - Allowed values are 0-1440.
            - Unit is min.
            - Default value when not specified in API or module is interpreted by Avi Controller as 15.
        type: int
    api_perf_logging_threshold:
        description:
            - Threshold to log request timing in portal_performance.log and server-timing response header.
            - Any stage taking longer than 1% of the threshold will be included in the server-timing header.
            - Field introduced in 18.1.4, 18.2.1.
            - Unit is milliseconds.
            - Default value when not specified in API or module is interpreted by Avi Controller as 10000.
        type: int
    appviewx_compat_mode:
        description:
            - Export configuration in appviewx compatibility mode.
            - Field introduced in 17.1.1.
            - Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    async_patch_merge_period:
        description:
            - Period for which asynchronous patch requests are queued.
            - Allowed values are 30-120.
            - Special values are 0 - 'deactivated'.
            - Field introduced in 18.2.11, 20.1.3.
            - Unit is sec.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    async_patch_request_cleanup_duration:
        description:
            - Duration for which asynchronous patch requests should be kept, after being marked as success or fail.
            - Allowed values are 5-120.
            - Field introduced in 18.2.11, 20.1.3.
            - Unit is min.
            - Default value when not specified in API or module is interpreted by Avi Controller as 60.
        type: int
    attach_ip_retry_interval:
        description:
            - Unit is sec.
            - Default value when not specified in API or module is interpreted by Avi Controller as 360.
        type: int
    attach_ip_retry_limit:
        description:
            - Number of attach_ip_retry_limit.
            - Default value when not specified in API or module is interpreted by Avi Controller as 4.
        type: int
    bm_use_ansible:
        description:
            - Use ansible for se creation in baremetal.
            - Field introduced in 17.2.2.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    cleanup_expired_authtoken_timeout_period:
        description:
            - Period for auth token cleanup job.
            - Field introduced in 18.1.1.
            - Unit is min.
            - Default value when not specified in API or module is interpreted by Avi Controller as 60.
        type: int
    cleanup_sessions_timeout_period:
        description:
            - Period for sessions cleanup job.
            - Field introduced in 18.1.1.
            - Unit is min.
            - Default value when not specified in API or module is interpreted by Avi Controller as 60.
        type: int
    cloud_reconcile:
        description:
            - Enable/disable periodic reconcile for all the clouds.
            - Field introduced in 17.2.14,18.1.5,18.2.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    cluster_ip_gratuitous_arp_period:
        description:
            - Period for cluster ip gratuitous arp job.
            - Unit is min.
            - Default value when not specified in API or module is interpreted by Avi Controller as 60.
        type: int
    configpb_attributes:
        description:
            - Protobuf versioning for config pbs.
            - Field introduced in 21.1.1.
        type: dict
    consistency_check_timeout_period:
        description:
            - Period for consistency check job.
            - Field introduced in 18.1.1.
            - Unit is min.
            - Default value when not specified in API or module is interpreted by Avi Controller as 60.
        type: int
    controller_resource_info_collection_period:
        description:
            - Periodically collect stats.
            - Field introduced in 20.1.3.
            - Unit is min.
            - Default value when not specified in API or module is interpreted by Avi Controller as 30.
        type: int
    crashed_se_reboot:
        description:
            - Unit is sec.
            - Default value when not specified in API or module is interpreted by Avi Controller as 900.
        type: int
    dead_se_detection_timer:
        description:
            - Unit is sec.
            - Default value when not specified in API or module is interpreted by Avi Controller as 360.
        type: int
    default_minimum_api_timeout:
        description:
            - Minimum api timeout value.if this value is not 60, it will be the default timeout for all apis that do not have a specific timeout.if an api has
            - a specific timeout but is less than this value, this value will become the new timeout.
            - Allowed values are 60-3600.
            - Field introduced in 18.2.6.
            - Unit is sec.
            - Default value when not specified in API or module is interpreted by Avi Controller as 60.
        type: int
    del_offline_se_after_reboot_delay:
        description:
            - The amount of time the controller will wait before deleting an offline se after it has been rebooted.
            - For unresponsive ses, the total time will be  unresponsive_se_reboot + del_offline_se_after_reboot_delay.
            - For crashed ses, the total time will be crashed_se_reboot + del_offline_se_after_reboot_delay.
            - Field introduced in 20.1.5.
            - Unit is sec.
            - Default value when not specified in API or module is interpreted by Avi Controller as 300.
        type: int
    dns_refresh_period:
        description:
            - Period for refresh pool and gslb dns job.
            - Unit is min.
            - Allowed in basic(allowed values- 60) edition, essentials(allowed values- 60) edition, enterprise edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 60.
        type: int
    dummy:
        description:
            - Number of dummy.
        type: int
    edit_system_limits:
        description:
            - Allow editing of system limits.
            - Keep in mind that these system limits have been carefully selected based on rigorous testing in our testig environments.
            - Modifying these limits could destabilize your cluster.
            - Do this at your own risk!.
            - Field introduced in 20.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    enable_api_sharding:
        description:
            - This setting enables the controller leader to shard api requests to the followers (if any).
            - Field introduced in 18.1.5, 18.2.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    enable_memory_balancer:
        description:
            - Enable/disable memory balancer.
            - Field introduced in 17.2.8.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    enable_resmgr_log_cache_print:
        description:
            - Enable printing of cached logs inside resource manager.
            - Used for debugging purposes only.
            - Field introduced in 21.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    fatal_error_lease_time:
        description:
            - Unit is sec.
            - Default value when not specified in API or module is interpreted by Avi Controller as 120.
        type: int
    federated_datastore_cleanup_duration:
        description:
            - Federated datastore will not cleanup diffs unless they are at least this duration in the past.
            - Field introduced in 20.1.1.
            - Unit is hours.
            - Default value when not specified in API or module is interpreted by Avi Controller as 120.
        type: int
    file_object_cleanup_period:
        description:
            - Period for file object cleanup job.
            - Field introduced in 20.1.1.
            - Unit is min.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1440.
        type: int
    max_dead_se_in_grp:
        description:
            - Number of max_dead_se_in_grp.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1.
        type: int
    max_pcap_per_tenant:
        description:
            - Maximum number of pcap files stored per tenant.
            - Default value when not specified in API or module is interpreted by Avi Controller as 4.
        type: int
    max_se_spawn_interval_delay:
        description:
            - Maximum delay possible to add to se_spawn_retry_interval after successive se spawn failure.
            - Field introduced in 20.1.1.
            - Unit is sec.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1800.
        type: int
    max_seq_attach_ip_failures:
        description:
            - Maximum number of consecutive attach ip failures that halts vs placement.
            - Field introduced in 17.2.2.
            - Default value when not specified in API or module is interpreted by Avi Controller as 3.
        type: int
    max_seq_vnic_failures:
        description:
            - Number of max_seq_vnic_failures.
            - Default value when not specified in API or module is interpreted by Avi Controller as 3.
        type: int
    max_threads_cc_vip_bg_worker:
        description:
            - Maximum number of threads in threadpool used by cloud connector ccvipbgworker.
            - Allowed values are 1-100.
            - Field introduced in 20.1.3.
            - Default value when not specified in API or module is interpreted by Avi Controller as 20.
        type: int
    permission_scoped_shared_admin_networks:
        description:
            - Network and vrfcontext objects from the admin tenant will not be shared to non-admin tenants unless admin permissions are granted.
            - Field introduced in 18.2.7, 20.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    persistence_key_rotate_period:
        description:
            - Period for rotate app persistence keys job.
            - Allowed values are 1-1051200.
            - Special values are 0 - 'disabled'.
            - Unit is min.
            - Allowed in basic(allowed values- 0) edition, essentials(allowed values- 0) edition, enterprise edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    portal_request_burst_limit:
        description:
            - Burst limit on number of incoming requests.
            - 0 to disable.
            - Field introduced in 20.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    portal_request_rate_limit:
        description:
            - Maximum average number of requests allowed per second.
            - 0 to disable.
            - Field introduced in 20.1.1.
            - Unit is per_second.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    portal_token:
        description:
            - Token used for uploading tech-support to portal.
            - Field introduced in 16.4.6,17.1.2.
        type: str
    process_locked_useraccounts_timeout_period:
        description:
            - Period for process locked user accounts job.
            - Field introduced in 18.1.1.
            - Unit is min.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1.
        type: int
    process_pki_profile_timeout_period:
        description:
            - Period for process pki profile job.
            - Field introduced in 18.1.1.
            - Unit is min.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1440.
        type: int
    query_host_fail:
        description:
            - Unit is sec.
            - Default value when not specified in API or module is interpreted by Avi Controller as 180.
        type: int
    resmgr_log_caching_period:
        description:
            - Period for each cycle of log caching in resource manager.
            - At the end of each cycle, the in memory cached log history will be cleared.
            - Field introduced in 20.1.5.
            - Unit is sec.
            - Default value when not specified in API or module is interpreted by Avi Controller as 21600.
        type: int
    safenet_hsm_version:
        description:
            - Version of the safenet package installed on the controller.
            - Field introduced in 16.5.2,17.2.3.
        type: str
    se_create_timeout:
        description:
            - Unit is sec.
            - Default value when not specified in API or module is interpreted by Avi Controller as 900.
        type: int
    se_failover_attempt_interval:
        description:
            - Interval between attempting failovers to an se.
            - Unit is sec.
            - Default value when not specified in API or module is interpreted by Avi Controller as 300.
        type: int
    se_from_marketplace:
        description:
            - This setting decides whether se is to be deployed from the cloud marketplace or to be created by the controller.
            - The setting is applicable only when byol license is selected.
            - Enum options - MARKETPLACE, IMAGE.
            - Field introduced in 18.1.4, 18.2.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as IMAGE.
        type: str
    se_offline_del:
        description:
            - Unit is sec.
            - Default value when not specified in API or module is interpreted by Avi Controller as 172000.
        type: int
    se_spawn_retry_interval:
        description:
            - Default retry period before attempting another service engine spawn in se group.
            - Field introduced in 20.1.1.
            - Unit is sec.
            - Default value when not specified in API or module is interpreted by Avi Controller as 300.
        type: int
    se_vnic_cooldown:
        description:
            - Unit is sec.
            - Default value when not specified in API or module is interpreted by Avi Controller as 120.
        type: int
    se_vnic_gc_wait_time:
        description:
            - Duration to wait after last vnic addition before proceeding with vnic garbage collection.
            - Used for testing purposes.
            - Field introduced in 20.1.4.
            - Unit is sec.
            - Default value when not specified in API or module is interpreted by Avi Controller as 300.
        type: int
    secure_channel_cleanup_timeout:
        description:
            - Period for secure channel cleanup job.
            - Unit is min.
            - Default value when not specified in API or module is interpreted by Avi Controller as 60.
        type: int
    secure_channel_controller_token_timeout:
        description:
            - Unit is min.
            - Default value when not specified in API or module is interpreted by Avi Controller as 60.
        type: int
    secure_channel_se_token_timeout:
        description:
            - Unit is min.
            - Default value when not specified in API or module is interpreted by Avi Controller as 60.
        type: int
    seupgrade_copy_pool_size:
        description:
            - This parameter defines the number of simultaneous se image downloads in a segroup.
            - It is used to pace the se downloads so that controller network/cpu bandwidth is a bounded operation.
            - A value of 0 will disable the pacing scheme and all the se(s) in the segroup will attempt to download the image.
            - Field introduced in 18.2.6.
            - Default value when not specified in API or module is interpreted by Avi Controller as 5.
        type: int
    seupgrade_fabric_pool_size:
        description:
            - Pool size used for all fabric commands during se upgrade.
            - Default value when not specified in API or module is interpreted by Avi Controller as 20.
        type: int
    seupgrade_segroup_min_dead_timeout:
        description:
            - Time to wait before marking segroup upgrade as stuck.
            - Unit is sec.
            - Default value when not specified in API or module is interpreted by Avi Controller as 360.
        type: int
    shared_ssl_certificates:
        description:
            - Ssl certificates in the admin tenant can be used in non-admin tenants.
            - Field introduced in 18.2.5.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    ssl_certificate_expiry_warning_days:
        description:
            - Number of days for ssl certificate expiry warning.
            - Unit is days.
        type: list
    unresponsive_se_reboot:
        description:
            - Unit is sec.
            - Default value when not specified in API or module is interpreted by Avi Controller as 300.
        type: int
    upgrade_dns_ttl:
        description:
            - Time to account for dns ttl during upgrade.
            - This is in addition to vs_scalein_timeout_for_upgrade in se_group.
            - Field introduced in 17.1.1.
            - Unit is sec.
            - Allowed in basic(allowed values- 5) edition, essentials(allowed values- 5) edition, enterprise edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 5.
        type: int
    upgrade_fat_se_lease_time:
        description:
            - Amount of time controller waits for a large-sized se (>=128gb memory) to reconnect after it is rebooted during upgrade.
            - Field introduced in 18.2.10, 20.1.1.
            - Unit is sec.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1200.
        type: int
    upgrade_lease_time:
        description:
            - Amount of time controller waits for a regular-sized se (<128gb memory) to reconnect after it is rebooted during upgrade.
            - Starting 18.2.10/20.1.1, the default time has increased from 360 seconds to 600 seconds.
            - Unit is sec.
            - Default value when not specified in API or module is interpreted by Avi Controller as 600.
        type: int
    upgrade_se_per_vs_scale_ops_txn_time:
        description:
            - This parameter defines the upper-bound value of the vs scale-in or vs scale-out operation executed in the sescalein and sescale context.
            - User can tweak this parameter to a higher value if the segroup gets suspended due to sescalein or sescaleout timeout failure typically associated
            - with high number of vs(es) scaled out.
            - Field introduced in 18.2.10, 20.1.1.
            - Unit is sec.
            - Default value when not specified in API or module is interpreted by Avi Controller as 3.
        type: int
    url:
        description:
            - Avi controller URL of the object.
        type: str
    user_agent_cache_config:
        description:
            - Configuration for user-agent cache used in bot management.
            - Field introduced in 21.1.1.
        type: dict
    uuid:
        description:
            - Unique object identifier of the object.
        type: str
    vnic_op_fail_time:
        description:
            - Unit is sec.
            - Default value when not specified in API or module is interpreted by Avi Controller as 180.
        type: int
    vs_apic_scaleout_timeout:
        description:
            - Time to wait for the scaled out se to become ready before marking the scaleout done, applies to apic configuration only.
            - Unit is sec.
            - Default value when not specified in API or module is interpreted by Avi Controller as 360.
        type: int
    vs_awaiting_se_timeout:
        description:
            - Unit is sec.
            - Default value when not specified in API or module is interpreted by Avi Controller as 60.
        type: int
    vs_key_rotate_period:
        description:
            - Period for rotate vs keys job.
            - Allowed values are 1-1051200.
            - Special values are 0 - 'disabled'.
            - Unit is min.
            - Default value when not specified in API or module is interpreted by Avi Controller as 360.
        type: int
    vs_scaleout_ready_check_interval:
        description:
            - Interval for checking scaleout_ready status while controller is waiting for scaleoutready rpc from the service engine.
            - Field introduced in 18.2.2.
            - Unit is sec.
            - Default value when not specified in API or module is interpreted by Avi Controller as 60.
        type: int
    vs_se_attach_ip_fail:
        description:
            - Time to wait before marking attach ip operation on an se as failed.
            - Field introduced in 17.2.2.
            - Unit is sec.
            - Default value when not specified in API or module is interpreted by Avi Controller as 600.
        type: int
    vs_se_bootup_fail:
        description:
            - Unit is sec.
            - Default value when not specified in API or module is interpreted by Avi Controller as 480.
        type: int
    vs_se_create_fail:
        description:
            - Unit is sec.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1500.
        type: int
    vs_se_ping_fail:
        description:
            - Unit is sec.
            - Default value when not specified in API or module is interpreted by Avi Controller as 60.
        type: int
    vs_se_vnic_fail:
        description:
            - Unit is sec.
            - Default value when not specified in API or module is interpreted by Avi Controller as 300.
        type: int
    vs_se_vnic_ip_fail:
        description:
            - Unit is sec.
            - Default value when not specified in API or module is interpreted by Avi Controller as 120.
        type: int
    warmstart_se_reconnect_wait_time:
        description:
            - Unit is sec.
            - Default value when not specified in API or module is interpreted by Avi Controller as 480.
        type: int
    warmstart_vs_resync_wait_time:
        description:
            - Timeout for warmstart vs resync.
            - Field introduced in 18.1.4, 18.2.1.
            - Unit is sec.
            - Default value when not specified in API or module is interpreted by Avi Controller as 300.
        type: int
extends_documentation_fragment:
    - vmware.alb.avi
'''

EXAMPLES = """
- name: Example to create ControllerProperties object
  vmware.alb.avi_controllerproperties:
    controller: 192.168.15.18
    username: admin
    password: something
    state: present
    name: sample_controllerproperties
"""

RETURN = '''
obj:
    description: ControllerProperties (api/controllerproperties) object
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
        allow_admin_network_updates=dict(type='bool',),
        allow_ip_forwarding=dict(type='bool',),
        allow_unauthenticated_apis=dict(type='bool',),
        allow_unauthenticated_nodes=dict(type='bool',),
        api_idle_timeout=dict(type='int',),
        api_perf_logging_threshold=dict(type='int',),
        appviewx_compat_mode=dict(type='bool',),
        async_patch_merge_period=dict(type='int',),
        async_patch_request_cleanup_duration=dict(type='int',),
        attach_ip_retry_interval=dict(type='int',),
        attach_ip_retry_limit=dict(type='int',),
        bm_use_ansible=dict(type='bool',),
        cleanup_expired_authtoken_timeout_period=dict(type='int',),
        cleanup_sessions_timeout_period=dict(type='int',),
        cloud_reconcile=dict(type='bool',),
        cluster_ip_gratuitous_arp_period=dict(type='int',),
        configpb_attributes=dict(type='dict',),
        consistency_check_timeout_period=dict(type='int',),
        controller_resource_info_collection_period=dict(type='int',),
        crashed_se_reboot=dict(type='int',),
        dead_se_detection_timer=dict(type='int',),
        default_minimum_api_timeout=dict(type='int',),
        del_offline_se_after_reboot_delay=dict(type='int',),
        dns_refresh_period=dict(type='int',),
        dummy=dict(type='int',),
        edit_system_limits=dict(type='bool',),
        enable_api_sharding=dict(type='bool',),
        enable_memory_balancer=dict(type='bool',),
        enable_resmgr_log_cache_print=dict(type='bool',),
        fatal_error_lease_time=dict(type='int',),
        federated_datastore_cleanup_duration=dict(type='int',),
        file_object_cleanup_period=dict(type='int',),
        max_dead_se_in_grp=dict(type='int',),
        max_pcap_per_tenant=dict(type='int',),
        max_se_spawn_interval_delay=dict(type='int',),
        max_seq_attach_ip_failures=dict(type='int',),
        max_seq_vnic_failures=dict(type='int',),
        max_threads_cc_vip_bg_worker=dict(type='int',),
        permission_scoped_shared_admin_networks=dict(type='bool',),
        persistence_key_rotate_period=dict(type='int',),
        portal_request_burst_limit=dict(type='int',),
        portal_request_rate_limit=dict(type='int',),
        portal_token=dict(type='str', no_log=True,),
        process_locked_useraccounts_timeout_period=dict(type='int',),
        process_pki_profile_timeout_period=dict(type='int',),
        query_host_fail=dict(type='int',),
        resmgr_log_caching_period=dict(type='int',),
        safenet_hsm_version=dict(type='str',),
        se_create_timeout=dict(type='int',),
        se_failover_attempt_interval=dict(type='int',),
        se_from_marketplace=dict(type='str',),
        se_offline_del=dict(type='int',),
        se_spawn_retry_interval=dict(type='int',),
        se_vnic_cooldown=dict(type='int',),
        se_vnic_gc_wait_time=dict(type='int',),
        secure_channel_cleanup_timeout=dict(type='int',),
        secure_channel_controller_token_timeout=dict(type='int',),
        secure_channel_se_token_timeout=dict(type='int',),
        seupgrade_copy_pool_size=dict(type='int',),
        seupgrade_fabric_pool_size=dict(type='int',),
        seupgrade_segroup_min_dead_timeout=dict(type='int',),
        shared_ssl_certificates=dict(type='bool',),
        ssl_certificate_expiry_warning_days=dict(type='list',),
        unresponsive_se_reboot=dict(type='int',),
        upgrade_dns_ttl=dict(type='int',),
        upgrade_fat_se_lease_time=dict(type='int',),
        upgrade_lease_time=dict(type='int',),
        upgrade_se_per_vs_scale_ops_txn_time=dict(type='int',),
        url=dict(type='str',),
        user_agent_cache_config=dict(type='dict',),
        uuid=dict(type='str',),
        vnic_op_fail_time=dict(type='int',),
        vs_apic_scaleout_timeout=dict(type='int',),
        vs_awaiting_se_timeout=dict(type='int',),
        vs_key_rotate_period=dict(type='int',),
        vs_scaleout_ready_check_interval=dict(type='int',),
        vs_se_attach_ip_fail=dict(type='int',),
        vs_se_bootup_fail=dict(type='int',),
        vs_se_create_fail=dict(type='int',),
        vs_se_ping_fail=dict(type='int',),
        vs_se_vnic_fail=dict(type='int',),
        vs_se_vnic_ip_fail=dict(type='int',),
        warmstart_se_reconnect_wait_time=dict(type='int',),
        warmstart_vs_resync_wait_time=dict(type='int',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_REQUESTS:
        return module.fail_json(msg=(
            'Python requests package is not installed. '
            'For installation instructions, visit https://pypi.org/project/requests.'))
    return avi_ansible_api(module, 'controllerproperties',
                           {'portal_token'})


if __name__ == '__main__':
    main()
