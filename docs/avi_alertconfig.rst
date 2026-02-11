
.. vmware.alb.avi_alertconfig:


**********************************************
vmware.alb.avi_alertconfig
**********************************************

**Module for setup of AlertConfig Avi RESTful Object**


.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module is used to configure AlertConfig object.
- More examples at (https://github.com/avinetworks/devops).


Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="7">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
        <tr>
            <td colspan="7">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>state</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                <ul style="margin: 0; padding: 0">
                    <li>absent</li>
                    <li><div style="color: blue"><b>present</b>&nbsp;&larr;</div></li>
                </ul>
            </td>
            <td>
                <div style="font-size: small">
                    - The state that should be applied on the entity.
                </div>
            </td>
        </tr>
        <tr>
            <td colspan="7">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>avi_api_update_method</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                <ul style="margin: 0; padding: 0">
                    <li><div style="color: blue"><b>put</b>&nbsp;&larr;</div></li>
                    <li>patch</li>
                </ul>
            </td>
            <td>
                <div style="font-size: small">
                    - Default method for object update is HTTP PUT.
                </div>
                <div style="font-size: small">
                    - Setting to patch will override that behavior to use HTTP PATCH.
                </div>
            </td>
        </tr>
        <tr>
            <td colspan="7">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>avi_api_patch_op</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                <ul style="margin: 0; padding: 0">
                    <li><div style="color: blue"><b>add</b>&nbsp;&larr;</div></li>
                    <li>replace</li>
                    <li>delete</li>
                    <li>remove</li>
                </ul>
            </td>
            <td>
                <div style="font-size: small">
                    - Patch operation to use when using avi_api_update_method as patch.
                </div>
            </td>
        </tr>
        <tr>
            <td colspan="7">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>avi_patch_path</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td></td>
            <td>
                <div style="font-size: small">
                    - Patch path to use when using avi_api_update_method as patch.
                </div>
            </td>
        </tr>
        <tr>
            <td colspan="7">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>avi_patch_value</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td></td>
            <td>
                <div style="font-size: small">
                    - Patch value to use when using avi_api_update_method as patch.
                </div>
            </td>
        </tr>
            <tr>
                                            <td colspan="7">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>action_group_ref</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - The alert config will trigger the selected alert action, which can send notifications and execute a controlscript.
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type actiongroupconfig.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                                            <td colspan="7">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>alert_rule</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                            <span style="color: purple">dict / elements=dictionary </span>
                                                            </div>
            </td>
            <td>
                                <div style="font-size: small">
                <b>required: true</b>
                </div>
                            </td>
            <td>
                                                <div style="font-size: small">
                  - List of filters matching on events or client logs used for triggering alerts.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                <tr>
                                    <td class="elbow-placeholder"></td>
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>conn_app_log_rule</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                            <span style="color: purple">dict / elements=dictionary </span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                <tr>
                                    <td class="elbow-placeholder"></td>
                            <td class="elbow-placeholder"></td>
                                    <td colspan="5">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>filter_action</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                            <td class="elbow-placeholder"></td>
                                    <td colspan="5">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>filter_string</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
        
                                        <td class="elbow-placeholder"></td>
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>event_match_filter</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>metrics_rule</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">list / elements=dictionary </span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                <tr>
                                    <td class="elbow-placeholder"></td>
                            <td class="elbow-placeholder"></td>
                                    <td colspan="5">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>duration</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">int</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Evaluation window for the metrics.
                </div>
                                <div style="font-size: small">
                  - Unit is sec.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                            <td class="elbow-placeholder"></td>
                                    <td colspan="5">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>metric_id</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Metric id for the alert.
                </div>
                                <div style="font-size: small">
                  - Eg.
                </div>
                                <div style="font-size: small">
                  - L4_client.avg_complete_conns.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                            <td class="elbow-placeholder"></td>
                                    <td colspan="5">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>metric_threshold</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                            <span style="color: purple">dict / elements=dictionary </span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                <tr>
                                    <td class="elbow-placeholder"></td>
                            <td class="elbow-placeholder"></td>
                            <td class="elbow-placeholder"></td>
                                    <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>comparator</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Enum options - ALERT_OP_LT, ALERT_OP_LE, ALERT_OP_EQ, ALERT_OP_NE, ALERT_OP_GE, ALERT_OP_GT.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as ALERT_OP_GT.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                            <td class="elbow-placeholder"></td>
                            <td class="elbow-placeholder"></td>
                                    <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>threshold</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">int</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Metric threshold for comparison.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
        
            
                                        <td class="elbow-placeholder"></td>
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>operator</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Enum options - OPERATOR_AND, OPERATOR_OR.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as OPERATOR_AND.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>sys_event_rule</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">list / elements=dictionary </span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                <tr>
                                    <td class="elbow-placeholder"></td>
                            <td class="elbow-placeholder"></td>
                                    <td colspan="5">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>event_details</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">list / elements=dictionary </span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                <tr>
                                    <td class="elbow-placeholder"></td>
                            <td class="elbow-placeholder"></td>
                            <td class="elbow-placeholder"></td>
                                    <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>comparator</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Enum options - ALERT_OP_LT, ALERT_OP_LE, ALERT_OP_EQ, ALERT_OP_NE, ALERT_OP_GE, ALERT_OP_GT.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as ALERT_OP_EQ.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                            <td class="elbow-placeholder"></td>
                            <td class="elbow-placeholder"></td>
                                    <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>event_details_key</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                            <td class="elbow-placeholder"></td>
                            <td class="elbow-placeholder"></td>
                                    <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>event_details_value</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
        
                                        <td class="elbow-placeholder"></td>
                            <td class="elbow-placeholder"></td>
                                    <td colspan="5">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>event_id</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - When the selected event occurs, trigger this alert.
                </div>
                                <div style="font-size: small">
                  - Enum options - VINFRA_DISC_DC, VINFRA_DISC_HOST, VINFRA_DISC_CLUSTER, VINFRA_DISC_VM, VINFRA_DISC_NW, MGMT_NW_NAME_CHANGED,
                </div>
                                <div style="font-size: small">
                  - DISCOVERY_DATACENTER_DEL, VM_ADDED, VM_REMOVED, VINFRA_DISC_COMPLETE, VCENTER_ADDRESS_ERROR, SE_GROUP_CLUSTER_DEL, SE_GROUP_MGMT_NW_DEL,
                </div>
                                <div style="font-size: small">
                  - MGMT_NW_DEL, VCENTER_BAD_CREDENTIALS, ESX_HOST_UNREACHABLE, SERVER_DELETED, SE_GROUP_HOST_DEL, VINFRA_DISC_FAILURE, ESX_HOST_POWERED_DOWN,
                </div>
                                <div style="font-size: small">
                  - VCENTER_VERSION_NOT_SUPPORTED, VCENTER_CONNECTIVITY_FAIL, VCENTER_CONNECTIVITY_SUCCESS, VCENTER_ACCESS_SLOW, VCENTER_USER_ROLE_CHANGE,
                </div>
                                <div style="font-size: small">
                  - VCENTER_NETWQRK_OBJECT_LIMIT_REACHED, VCENTER_SE_TAGGING_FAIL, VCENTER_CLOUD_DELETE, VCENTER_QAT_CLUSTER_DRS_NOT_ENABLED, SE_FATAL_ERROR,
                </div>
                                <div style="font-size: small">
                  - SE_HEARTBEAT_FAILURE, SE_MARKED_DOWN, SE_VM_DELETED, SE_VM_PURGED, SE_UP, SE_POWERED_DOWN, SE_REBOOTED, SE_HEALTH_CHECK_FAIL,
                </div>
                                <div style="font-size: small">
                  - SE_EXTERNAL_HM_RESTART, SE_DOWN, SE_VERSION_CHECK_FAILED, SE_UPGRADING, SE_ENABLE_STATE_CHANGED, SE_MIGRATE, SE_MGMT_IP_CHANGE,
                </div>
                                <div style="font-size: small">
                  - VSPHERE_HA_HOST_FAILURE, SE_ENABLE, CREATING_SE, CREATED_SE, CREATE_SE_FAIL, CREATE_SE_TIMEOUT, DELETING_SE, DELETED_SE, DELETE_SE_FAIL,
                </div>
                                <div style="font-size: small">
                  - ADD_NW_SE, DEL_NW_SE, VS_ADD_SE_INT, VS_REMOVED_SE_INT, VS_ADD_SE, VS_REMOVED_SE, ADD_NW_FAIL, RM_DEL_NETWORK_FAIL, REBOOT_SE, MODIFY_NW,
                </div>
                                <div style="font-size: small">
                  - MODIFY_NW_FAIL, VS_SE_BOOTUP_FAIL, VS_SE_IP_FAIL, NO_HOST_AVAIL, VS_SWITCHOVER, VS_SWITCHOVER_FAIL, ADD_VIP_VNIC, DEL_VIP_VNIC,
                </div>
                                <div style="font-size: small">
                  - CC_ATTACH_IP_SKIPPED, CC_ATTACH_IP_SUCCESS, CC_ATTACH_IP_TIMEDOUT, CC_ATTACH_IP_FAILURE, CC_DETACH_IP_SKIPPED, CC_DETACH_IP_SUCCESS,
                </div>
                                <div style="font-size: small">
                  - CC_DETACH_IP_TIMEDOUT, CC_DETACH_IP_FAILURE, SHARED_VIP_ASYMMETRIC, SHARED_VIP_SYMMETRIC, VS_FSM_INACTIVE, VS_FSM_AWAITING_SE_ASSIGNMENT,
                </div>
                                <div style="font-size: small">
                  - VS_FSM_ACTIVE, VS_FSM_ACTIVE_AWAITING_SE_TRANSITION, VS_FSM_DISABLED, NEW_PROBABLE_SRVR, VS_SCALEOUT_DONE, VS_SCALEOUT_DONE_AWAITING_MORE_SE,
                </div>
                                <div style="font-size: small">
                  - VS_SCALEOUT_ERR, VS_SCALEIN_DONE, VS_SCALEIN_DONE_AWAITING_MORE_SE, VS_SCALEIN_ERR, VS_MIGRATE_SCALEOUT_DONE, VS_MIGRATE_SCALEOUT_ERROR,
                </div>
                                <div style="font-size: small">
                  - VS_MIGRATE_SCALEIN_DONE, VS_MIGRATE_SCALEIN_ERROR, VS_MIGRATE_DONE, VS_FSM_UNEXPECTED_EVENT, VS_RPC_TO_RESMGR_FAILED_EVENT,
                </div>
                                <div style="font-size: small">
                  - VS_RPC_TO_SE_FAILED_EVENT, VS_RPC_FAILED_EVENT, VS_SCALEOUT_COMPLETE, VS_SCALEIN_COMPLETE, VS_MIGRATE_STARTED, VS_MIGRATE_COMPLETE,
                </div>
                                <div style="font-size: small">
                  - VS_SCALEOUT_FAILED, VS_SCALEIN_FAILED, VS_MIGRATE_FAILED, VS_AWAITING_SE, VS_INITIAL_PLACEMENT_FAILED, VS_FSM_ACTIVE_AWAITING_SCALEOUT_READY,
                </div>
                                <div style="font-size: small">
                  - SE_READY_ON_CREATE_TIMEDOUT, SE_SCALEOUT_READY, SE_SCALEOUT_READY_TIMEDOUT, SE_SCALEIN_READY, SE_SCALEIN_READY_TIMEDOUT,
                </div>
                                <div style="font-size: small">
                  - SE_PRIMARY_SWITCHOVER_READY, SE_PRIMARY_SWITCHOVER_READY_TIMEDOUT, UPGRADE_ALL_SE_START, UPGRADE_ALL_SE_DONE, UPGRADE_ALL_SE_NOT_NEEDED,
                </div>
                                <div style="font-size: small">
                  - UPGRADE_SE_START, UPGRADE_SE_DONE, UPGRADE_SE_NOT_NEEDED, UPGRADE_SE_SUSPENDED, UPGRADE_SE_VS_SCALEOUT, UPGRADE_SE_VS_SCALEIN,
                </div>
                                <div style="font-size: small">
                  - UPGRADE_SE_VS_MIGRATE, UPGRADE_SE_VS_DISRUPTED, REBALANCE_VS_SCALEOUT, REBALANCE_VS_SCALEIN, REBALANCE_VS_MIGRATE, DISABLE_SE_VS_MIGRATE,
                </div>
                                <div style="font-size: small">
                  - ROLLBACK_ALL_SE_START, ROLLBACK_ALL_SE_DONE, MIGRATE_SE_STARTED, MIGRATE_SE_RESTARTED, MIGRATE_SE_FINISHED, MIGRATE_SE_FAILED,
                </div>
                                <div style="font-size: small">
                  - MIGRATE_SE_VS_MIGRATE_STARTED, MIGRATE_SE_VS_MIGRATE_FINISHED, MIGRATE_SE_VS_MIGRATE_FAILED, VIP_SCALEOUT, VIP_SCALEOUT_FAILED, VIP_SCALEIN,
                </div>
                                <div style="font-size: small">
                  - VIP_SCALEIN_FAILED, SE_HM_EVENT_SHM_DOWN, SE_HM_EVENT_SHM_UP, SERVER_DOWN, SERVER_UP, POOL_DOWN, POOL_UP, VS_DOWN, VS_UP, SE_SERVER_DELETED,
                </div>
                                <div style="font-size: small">
                  - SE_SERVER_DISABLED, SE_POOL_DELETED, SE_SERVER_APP_CHANGED, VS_CONN_LIMIT, VS_THROUGHPUT_LIMIT, CONN_DROP_MAX_SYN_TBL, CONN_DROP_MAX_FLOW_TBL,
                </div>
                                <div style="font-size: small">
                  - CONN_DROP_MAX_PERSIST_TBL, CONN_DROP_POOL_LB_FAILURE, CONN_DROP_NO_CONN_MEM, CONN_DROP_NO_PKT_BUFF, PKT_DROP_NO_PKT_BUFF, PKT_BUFF_ALLOC_FAIL,
                </div>
                                <div style="font-size: small">
                  - CACHE_OBJ_ALLOC_FAIL, SYN_ATTACK, CONN_THROTTLED_MEMFAIL_FLOW_TBL, SE_CPU_HIGH, SE_MEM_HIGH, SE_PKT_BUFF_HIGH, SE_PERSIST_TBL_HIGH,
                </div>
                                <div style="font-size: small">
                  - SE_CONN_MEM_HIGH, SE_DISK_HIGH, SE_FLOW_TBL_HIGH, SE_SYN_TBL_HIGH, SE_DP_HB_FAILED, SE_VNIC_DHCP_IP_ALLOC_FAILURE, SE_VNIC_DUPLICATE_IP,
                </div>
                                <div style="font-size: small">
                  - SE_SYN_CACHE_USAGE_HIGH, VM_CPU_HIGH, VM_MEM_HIGH, VS_SE_HA_ACTIVE, VS_SE_HA_COMPROMISED, POOL_SE_HA_ACTIVE, POOL_SE_HA_COMPROMISED,
                </div>
                                <div style="font-size: small">
                  - SERVER_DOWN_HA_COMPROMISED, SERVER_UP_HA_ACTIVE, SE_VNIC_IP_ADDED, SE_VNIC_IP_REMOVED, GS_MEMBER_DOWN, GS_MEMBER_UP, GS_GROUP_DOWN, GS_GROUP_UP,
                </div>
                                <div style="font-size: small">
                  - GS_DOWN, GS_UP, VIP_DOWN, VIP_UP, SE_GEO_DB_FAILURE, VS_GEO_DB_FAILURE, SE_GEO_DB_SUCCESS, VS_GEO_DB_SUCCESS,
                </div>
                                <div style="font-size: small">
                  - VS_CONFIG_SE_DATASTORE_DOWNLOAD_FAILED, SE_CONFIG_SE_DATASTORE_DOWNLOAD_FAILED, SE_EV_SERVER_DOWN, SE_EV_SERVER_UP, SE_EV_POOL_DOWN,
                </div>
                                <div style="font-size: small">
                  - SE_EV_POOL_UP, SE_EV_VS_DOWN, SE_EV_VS_UP, SE_HM_EVENT_GHM_DOWN, SE_HM_EVENT_GHM_UP, SE_EV_GS_GROUP_DELETED, SE_EV_GS_MEMBER_DOWN,
                </div>
                                <div style="font-size: small">
                  - SE_EV_GS_MEMBER_UP, SE_EV_GS_GROUP_DOWN, SE_EV_GS_GROUP_UP, SE_EV_GS_DOWN, SE_EV_GS_UP, SE_IP6_DAD_FAILED, SE_EV_VS_RL_CONFIG_FAILED,
                </div>
                                <div style="font-size: small">
                  - SE_DP_HB_RECOVERED, SE_VS_PKT_BUFF_HIGH, SE_DISCONTINUOUS_TIME_CHANGE, SE_HIGH_INGRESS_PROC_LATENCY, SE_VS_DEL_FLOWS_DISRUPTED,
                </div>
                                <div style="font-size: small">
                  - SE_NTP_SYNCHRONIZATION_FAILED, SE_HIGH_EGRESS_PROC_LATENCY, SE_ARP_RATE_LIMIT_DROP, SE_ND_RATE_LIMIT_DROP, DEBUG_MODE_ON, DEBUG_MODE_OFF,
                </div>
                                <div style="font-size: small">
                  - CONFIG_CREATE, CONFIG_UPDATE, CONFIG_DELETE, USER_LOGIN, USER_LOGOUT, CONFIG_ACTION, CONFIG_INTERNAL_CREATE, CONFIG_INTERNAL_UPDATE,
                </div>
                                <div style="font-size: small">
                  - USER_PASSWORD_CHANGE_REQUEST, USER_AUTHORIZED_BY_RULE, USER_NOT_AUTHORIZED_BY_ANY_RULE, CONFIG_SE_GRP_FLAVOR_UPDATE, API_VERSION_DEPRECATED,
                </div>
                                <div style="font-size: small">
                  - DNS_QUERY_ERROR, ASYNC_PATCH_STATUS, MERGED_ASYNC_PATCH_STATUS, CONFIG_EXPORT, TECHSUPPORT_COLLECTION_STARTED, TECHSUPPORT_COLLECTION_ONGOING,
                </div>
                                <div style="font-size: small">
                  - TECHSUPPORT_COLLECTION_SUCCESS, TECHSUPPORT_COLLECTION_SUCCESS_WITH_ERROR, WARNING_EVENT, SSL_CERT_EXPIRE, SSL_KEY_EXPORTED, SSL_CERT_RENEW,
                </div>
                                <div style="font-size: small">
                  - SSL_CERT_RENEW_FAILED, SSL_CERT_IGNORED, SSL_CERT_REVOKED, CONTROLLER_NODE_JOINED, CONTROLLER_NODE_LEFT, CONTROLLER_SERVICE_FAILURE,
                </div>
                                <div style="font-size: small">
                  - CONTROLLER_LEADER_FAILOVER, CONTROLLER_WARM_REBOOT, CONTROLLER_SERVICE_RESTORED, CONTROLLER_SERVICE_CRITICAL_FAILURE, CONTROLLER_NODE_SHUTDOWN,
                </div>
                                <div style="font-size: small">
                  - CONTROLLER_NODE_STARTED, CLUSTER_CONFIG_FAILED, SE_SECURE_KEY_EXCHANGE, CTLR_SECURE_KEY_EXCHANGE, MALFORMED_SECURE_KEY_EXCHANGE,
                </div>
                                <div style="font-size: small">
                  - CLUSTIFY_CHECK_EVENT, SYSTEM_UPGRADE_STARTED, SYSTEM_UPGRADE_COMPLETE, SYSTEM_UPGRADE_ABORTED, SYSTEM_ROLLBACK_STARTED, SYSTEM_ROLLBACK_COMPLETE,
                </div>
                                <div style="font-size: small">
                  - SYSTEM_ROLLBACK_ABORTED, CONTROLLER_NODE_DB_REPLICATION_FAILED, CONTROLLER_PROCESS_STOPPED, CONTROLLER_MEMORY_BALANCER_DISABLED,
                </div>
                                <div style="font-size: small">
                  - CONTROLLER_MEMORY_BALANCER_DEACTIVATED, CONTROLLER_DISCONTINUOUS_TIME_CHANGE, CONTROLLER_PROCESS_MODE_TRANSITION,
                </div>
                                <div style="font-size: small">
                  - CONTROLLER_PROCESS_TREND_TRANSITION, CONTROLLER_PROCESS_STOPPED_MEMORY_VIOLATION, LOG_MANAGER_TASKQUEUE_ABNORMAL_GROWTH,
                </div>
                                <div style="font-size: small">
                  - USAGE_METERING_REGISTRATION, USAGE_METERING_DE_REGISTRATION, METRIC_THRESHOLD_UP_VIOLATION, LICENSE_EXPIRY, ANOMALY, LICENSE_ADDITION_NOTIF,
                </div>
                                <div style="font-size: small">
                  - LICENSE_REMOVAL_NOTIF, METRICS_DB_DISK_FULL, METRICS_DB_QUEUE_FULL, METRICS_DB_QUEUE_HEALTHY, METRICS_DBSYNC_FAILURE, METRICS_GRPC_AUTH_FAILURE,
                </div>
                                <div style="font-size: small">
                  - OPENSTACK_ACCESS_FAILURE, OPENSTACK_ACCESS_SUCCESS, OPENSTACK_IMAGE_UPLOAD_FAILURE, OPENSTACK_IMAGE_UPLOAD_SUCCESS, OPENSTACK_SE_VM_CREATED,
                </div>
                                <div style="font-size: small">
                  - OPENSTACK_SE_VM_DELETED, OPENSTACK_SE_VM_DELETION_DETECTED, OPENSTACK_VNIC_ADDED, OPENSTACK_VNIC_REMOVED, OPENSTACK_IP_DETACHED,
                </div>
                                <div style="font-size: small">
                  - OPENSTACK_IP_ATTACHED, OPENSTACK_SE_CREATION_FAILURE, OPENSTACK_SE_DELETION_FAILURE, OPENSTACK_VNIC_ADDITION_FAILURE,
                </div>
                                <div style="font-size: small">
                  - OPENSTACK_VNIC_DELETION_FAILURE, OPENSTACK_IP_DETACH_FAILURE, OPENSTACK_IP_ATTACH_FAILURE, OPENSTACK_LBPROV_AUDIT_FAILURE,
                </div>
                                <div style="font-size: small">
                  - OPENSTACK_LBPROV_AUDIT_SUCCESS, OPENSTACK_LBPLUGIN_OP_FAILURE, OPENSTACK_LBPLUGIN_OP_SUCCESS, OPENSTACK_SYNC_SERVICES_SUCCESS,
                </div>
                                <div style="font-size: small">
                  - OPENSTACK_SYNC_SERVICES_FAILURE, OPENSTACK_TENANTS_DELETED, OPENSTACK_API_VERSION_CHECK_FAILED, AWS_ACCESS_FAILURE, AWS_ACCESS_SUCCESS,
                </div>
                                <div style="font-size: small">
                  - AWS_IMAGE_UPLOAD_FAILURE, AWS_IMAGE_UPLOAD_SUCCESS, AWS_SNS_ACCESS_FAILURE, AWS_SNS_ACCESS_SUCCESS, AWS_SQS_ACCESS_FAILURE,
                </div>
                                <div style="font-size: small">
                  - AWS_SQS_ACCESS_SUCCESS, AWS_ASG_PUT_NOTIFICATION_CONFIGURATION_FAILURE, AWS_ASG_PUT_NOTIFICATION_CONFIGURATION_SUCCESS,
                </div>
                                <div style="font-size: small">
                  - AWS_ASG_DELETE_NOTIFICATION_CONFIGURATION_FAILURE, AWS_ASG_DELETE_NOTIFICATION_CONFIGURATION_SUCCESS, AWS_ASG_NOTIFICATION_PROCESSING_FAILURE,
                </div>
                                <div style="font-size: small">
                  - AWS_ASG_NOTIFICATION_PROCESSING_SUCCESS, AWS_ASG_NOTIFICATION_INSTANCE_ADDED, AWS_ASG_NOTIFICATION_INSTANCE_REMOVED, AWS_ASG_ACCESS_FAILURE,
                </div>
                                <div style="font-size: small">
                  - AWS_ASG_ACCESS_SUCCESS, AWS_ASG_NOTIFICATION_INSTANCE_LAUNCH_ERROR, AWS_ASG_NOTIFICATION_INSTANCE_TERMINATE_ERROR,
                </div>
                                <div style="font-size: small">
                  - AWS_ASG_NOTIFICATION_AUTOSCALE_GROUP_DELETED, CLOUD_AUTOSCALING_CONFIG_FAILURE, CLOUD_AUTOSCALING_DECONFIG_FAILURE,
                </div>
                                <div style="font-size: small">
                  - CLOUD_AUTOSCALING_ASG_ADD_FAILURE, CLOUD_AUTOSCALING_ASG_REMOVE_FAILURE, CLOUD_AUTOSCALING_NOTIFICATION_PROCESSING_FAILURE,
                </div>
                                <div style="font-size: small">
                  - CLOUD_ROUTE_CREATION_FAILURE, CLOUD_ROUTE_CREATION_SUCCESS, CLOUD_ROUTE_REMOVE_FAILURE, CLOUD_ROUTE_REMOVE_SUCCESS, CLOUDSTACK_ACCESS_FAILURE,
                </div>
                                <div style="font-size: small">
                  - CLOUDSTACK_ACCESS_SUCCESS, CLOUDSTACK_IMAGE_UPLOAD_FAILURE, CLOUDSTACK_IMAGE_UPLOAD_SUCCESS, DOCKER_UCP_ACCESS_SUCCESS, DOCKER_UCP_ACCESS_FAILURE,
                </div>
                                <div style="font-size: small">
                  - DOCKER_UCP_IMAGE_UPLOAD_FAILURE, DOCKER_UCP_IMAGE_UPLOAD_SUCCESS, DOCKER_UCP_IMAGE_UPLOAD_IN_PROGRESS, VCA_ACCESS_FAILURE, VCA_ACCESS_SUCCESS,
                </div>
                                <div style="font-size: small">
                  - VCA_IMAGE_UPLOAD_FAILURE, VCA_IMAGE_UPLOAD_SUCCESS, LS_ACCESS_FAILURE, LS_ACCESS_SUCCESS, LS_IMAGE_UPLOAD_FAILURE, LS_IMAGE_UPLOAD_SUCCESS,
                </div>
                                <div style="font-size: small">
                  - MESOS_ACCESS_SUCCESS, MESOS_ACCESS_FAILURE, MESOS_IMAGE_UPLOAD_FAILURE, MESOS_IMAGE_UPLOAD_SUCCESS, MESOS_IMAGE_UPLOAD_IN_PROGRESS,
                </div>
                                <div style="font-size: small">
                  - MESOS_CREATED_SE, MESOS_CREATE_SE_FAIL, MESOS_DELETED_SE, MESOS_DELETE_SE_FAIL, MESOS_STOPPED_SE, MESOS_STOP_SE_FAIL, MESOS_STARTED_SE,
                </div>
                                <div style="font-size: small">
                  - MESOS_START_SE_FAIL, MESOS_UPDATED_HOSTS, CC_SE_CREATED, CC_SE_CREATION_FAILURE, CC_SE_DELETED, CC_SE_DELETION_FAILURE, CC_SE_DELETION_DETECTED,
                </div>
                                <div style="font-size: small">
                  - CC_VNIC_ADDED, CC_VNIC_ADDITION_FAILURE, CC_VNIC_DELETED, CC_VNIC_DELETION_FAILURE, CC_IP_ATTACHED, CC_IP_ATTACH_FAILURE, CC_IP_DETACHED,
                </div>
                                <div style="font-size: small">
                  - CC_IP_DETACH_FAILURE, CC_SYNC_SERVICES_SUCCESS, CC_SYNC_SERVICES_FAILURE, CC_UPDATE_VIP_FAILURE, CC_DELETE_VIP_FAILURE, CC_CONFIG_FAILURE,
                </div>
                                <div style="font-size: small">
                  - CC_DECONFIG_FAILURE, CC_GENERIC_FAILURE, CC_CLUSTER_VIP_CONFIG_SUCCESS, CC_CLUSTER_VIP_CONFIG_FAILURE, CC_CLUSTER_VIP_DECONFIG_SUCCESS,
                </div>
                                <div style="font-size: small">
                  - CC_CLUSTER_VIP_DECONFIG_FAILURE, CC_MARATHON_SERVICE_PORT_OUTSIDE_VALID_RANGE, CC_MARATHON_SERVICE_PORT_ALREADY_IN_USE,
                </div>
                                <div style="font-size: small">
                  - CC_VIP_DNS_REGISTER_FAILURE, CC_TENANT_INIT_FAILURE, CC_HEALTH_FAILURE, CC_HEALTH_OK, CC_SE_STARTED, CC_SE_START_FAILURE, CC_SE_STOPPED,
                </div>
                                <div style="font-size: small">
                  - CC_SE_STOP_FAILURE, CC_VIP_PARK_INTF_SUCCESS, CC_VIP_PARK_INTF_FAILURE, CC_VIP_DNS_DEREGISTER_FAILURE, CC_VIP_DNS_VALIDATION_FAILURE,
                </div>
                                <div style="font-size: small">
                  - CC_VIP_DNS_REGISTER_SUCCESS, CC_VIP_DNS_DEREGISTER_SUCCESS, AWS_ROUTE53_ACCESS_FAILURE, AWS_ROUTE53_ACCESS_SUCCESS, CC_SCALE_SET_POLLING_FAILURE,
                </div>
                                <div style="font-size: small">
                  - CC_SCALE_SET_POLLING_SUCCESS, VS_HEALTH_CHANGE, SE_HEALTH_CHANGE, POOL_HEALTH_CHANGE, SERVER_HEALTH_CHANGE, VS_HEALTH_DEGRADED,
                </div>
                                <div style="font-size: small">
                  - SE_HEALTH_DEGRADED, POOL_HEALTH_DEGRADED, SERVER_HEALTH_DEGRADED, DUPLICATE_SUBNETS, SUMMARIZED_SUBNETS, IP_POOL_ALMOST_EXHAUSTED,
                </div>
                                <div style="font-size: small">
                  - IP_POOL_EXHAUSTED, IP_POOL_ALMOST_EXHAUSTED_VIP, IP_POOL_EXHAUSTED_VIP, IP_POOL_ALMOST_EXHAUSTED_SE, IP_POOL_EXHAUSTED_SE, LICENSE_LIMIT_SERVERS,
                </div>
                                <div style="font-size: small">
                  - LICENSE_LIMIT_SE_VCPUS, LICENSE_LIMIT_THROUGHPUT, LICENSE_LIMIT_VS, LICENSE_LIMIT_HOSTS, LICENSE_LIMIT_SE_SOCKETS, LICENSE_EXPIRED,
                </div>
                                <div style="font-size: small">
                  - BURST_RESOURCE_CONSUMED, BURST_RESOURCE_EXPIRY_ALERT, LICENSE_LIMIT_SE_SERVICE_CORES, APIC_BAD_CREDENTIALS, APIC_CREATE_LIFS, APIC_DELETE_LIFS,
                </div>
                                <div style="font-size: small">
                  - APIC_CREATE_LIF_CONTEXTS, APIC_DELETE_LIF_CONTEXTS, APIC_CREATE_CDEV, APIC_DELETE_CDEV, APIC_ATTACH_CIF_TO_LIF, APIC_DETACH_CIF_FROM_LIF,
                </div>
                                <div style="font-size: small">
                  - APIC_VS_PLACEMENT, APIC_BIND_VNIC_TO_NETWORK, APIC_CREATE_TENANT, APIC_DELETE_TENANT, APIC_CREATE_NETWORK, APIC_DELETE_NETWORK,
                </div>
                                <div style="font-size: small">
                  - APIC_NETWORK_VRF_CHANGED, APIC_VS_NETWORK_RESOLVE_ERROR, CONTAINER_CLOUD_ACCESS_SUCCESS, CONTAINER_CLOUD_ACCESS_FAILURE,
                </div>
                                <div style="font-size: small">
                  - CONTAINER_CLOUD_IMAGE_UPLOAD_FAILURE, CONTAINER_CLOUD_IMAGE_UPLOAD_SUCCESS, CONTAINER_CLOUD_IMAGE_UPLOAD_IN_PROGRESS, CONTAINER_CLOUD_CREATED_SE,
                </div>
                                <div style="font-size: small">
                  - CONTAINER_CLOUD_CREATE_SE_FAIL, CONTAINER_CLOUD_DELETED_SE, CONTAINER_CLOUD_DELETE_SE_FAIL, CONTAINER_CLOUD_STOPPED_SE,
                </div>
                                <div style="font-size: small">
                  - CONTAINER_CLOUD_STOP_SE_FAIL, CONTAINER_CLOUD_STARTED_SE, CONTAINER_CLOUD_START_SE_FAIL, CONTAINER_CLOUD_UPDATED_HOSTS,
                </div>
                                <div style="font-size: small">
                  - CONTAINER_CLOUD_SERVICE_SUCCESS, CONTAINER_CLOUD_SERVICE_FAILURE, CONTAINER_CLOUD_SERVICE_INCOMPLETE, CONTAINER_CLOUD_HEALTHCHECK_SE,
                </div>
                                <div style="font-size: small">
                  - CONTAINER_CLOUD_HEALTHCHECK_SE_FAIL, AVG_UPTIME_CHANGE, DOS_ATTACK, SE_DOS_ATTACK, SERVER_AUTOSCALE_OUT, SERVER_AUTOSCALE_IN,
                </div>
                                <div style="font-size: small">
                  - SERVER_AUTOSCALE_OUT_COMPLETE, SERVER_AUTOSCALE_IN_COMPLETE, SERVER_AUTOSCALE_FAILED, SERVER_AUTOSCALE_IN_FAILED, SERVER_AUTOSCALE_OUT_FAILED,
                </div>
                                <div style="font-size: small">
                  - SE_GATEWAY_HEARTBEAT_FAILED, SE_GATEWAY_HEARTBEAT_SUCCESS, SE_VNIC_DOWN_EVENT, SE_VNIC_TX_QUEUE_STALL, SE_BGP_PEER_STATE_CHANGE,
                </div>
                                <div style="font-size: small">
                  - SE_LICENSED_BANDWIDTH_EXCEEDED, SERVER_AUTOSCALE_OUT_TRIGGERED, SERVER_AUTOSCALE_IN_TRIGGERED, SE_BGP_PEER_DOWN, SE_OBJSYNC_PEER_DOWN,
                </div>
                                <div style="font-size: small">
                  - SE_REDIS_CONNECTION_DOWN, POOL_AUTO_DEPLOYMENT_FAILED, POOL_AUTO_DEPLOYMENT_SUCCESS, SE_VNIC_UP_EVENT, POOL_AUTO_DEPLOYMENT_UPDATE,
                </div>
                                <div style="font-size: small">
                  - GSLB_SITE_OPER_STATUS, GSLB_DNS_STATUS, GSLB_SITE_EXCEPTION_STATUS, GSLB_GS_STATUS, GSLB_SITE_SYNC_STATUS, VSGS_STATUS, GSLB_SM_STATUS,
                </div>
                                <div style="font-size: small">
                  - GSLB_CRM_STATUS, SCHEDULER_ACTION_SUCCESS, SCHEDULER_ACTION_FAILURE, SCHEDULER_ACTION_FAILED_WITH_ERROR,
                </div>
                                <div style="font-size: small">
                  - CONTROLLER_SCHEDULER_UNENCRYPTED_CONFIG_EXPORT, REMOTE_BACKUP_FAILURE, GCP_ACCESS_SUCCESS, GCP_ACCESS_FAIL, GCP_SE_DETECTED, GCP_API_FAIL,
                </div>
                                <div style="font-size: small">
                  - GCP_SUBNET_NOT_FOUND, GCP_SUBNET_ATTACH_FAIL, GCP_ROUTE_ADD_SUCCESS, GCP_ROUTE_DELETE_SUCCESS, GCP_ROUTE_ADD_FAIL, GCP_ROUTE_DELETE_FAIL,
                </div>
                                <div style="font-size: small">
                  - GCP_CLOUD_ROUTER_UPDATE_SUCCESS, GCP_CLOUD_ROUTER_UPDATE_FAIL, VIP_DNS_REGISTER_SUCCESS, VIP_DNS_REGISTER_FAILURE, VIP_DNS_DEREGISTER_SUCCESS,
                </div>
                                <div style="font-size: small">
                  - VIP_DNS_DEREGISTER_FAILURE, SYNC_DNS_RECORDS_SUCCESS, SYNC_DNS_RECORDS_FAILURE, FLUSH_DNS_RECORDS_SUCCESS, FLUSH_DNS_RECORDS_FAILURE,
                </div>
                                <div style="font-size: small">
                  - CC_HOST_SSH_FAILURE, CC_HOST_SSH_SUCCESS, AZURE_ACCESS_SUCCESS, AZURE_ACCESS_FAILURE, AZURE_ALB_UPDATE_FAILURE, AZURE_NIC_UPDATE_FAILURE,
                </div>
                                <div style="font-size: small">
                  - AZURE_ALB_UPDATE_SUCCESS, AZURE_NIC_UPDATE_SUCCESS, AZURE_NIC_DELETE_SUCCESS, AZURE_NIC_DELETE_FAILURE, AZURE_IMAGE_UPLOAD_FAILURE,
                </div>
                                <div style="font-size: small">
                  - AZURE_IMAGE_UPLOAD_SUCCESS, AZURE_MARKETPLACE_LICENSE_TERMS_SUCCESS, AZURE_MARKETPLACE_LICENSE_TERMS_FAILURE, VS_FAULT, SE_SHM_MEM_HIGH,
                </div>
                                <div style="font-size: small">
                  - SE_CONFIG_MEM_USAGE_ABOVE_LIMIT, OCI_ACCESS_SUCCESS, OCI_ACCESS_FAILURE, TENCENT_ACCESS_SUCCESS, TENCENT_ACCESS_FAILURE, CONTROLLER_CPU_HIGH,
                </div>
                                <div style="font-size: small">
                  - CONTROLLER_MEM_HIGH, CONTROLLER_DISK_HIGH, ALBSERVICES_CONNECTION_FAILURE, ALBSERVICES_CONTROLLER_DEREGISTERED, CRS_UPDATE,
                </div>
                                <div style="font-size: small">
                  - CRS_DEPLOYMENT_SUCCESS, CRS_DEPLOYMENT_FAILURE, IP_REPUTATION_DB_SYNC_SUCCESS, IP_REPUTATION_DB_SYNC_FAILURE, APPSIGNATURE_SYNC_SUCCESS,
                </div>
                                <div style="font-size: small">
                  - APPSIGNATURE_SYNC_FAILURE, IPV6_REPUTATION_DB_SYNC_SUCCESS, IPV6_REPUTATION_DB_SYNC_FAILURE, PSM_PROGRAM_FAILURE, PSM_MAX_PARAM_EVENT,
                </div>
                                <div style="font-size: small">
                  - PSM_MAX_URI_EVENT, SEC_MGR_DATA_ERROR_EVENT, UACACHE_PULSE_CONN_FAILED_EVENT, APP_INSIGHTS_MAX_URI_EVENT, APP_INSIGHTS_MAX_PARAM_EVENT,
                </div>
                                <div style="font-size: small">
                  - ALBSERVICES_CONTROLLER_REGISTERED, ALBSERVICES_SUPPORT_CASE_CREATED, ALBSERVICES_SUPPORT_CASE_UPDATED,
                </div>
                                <div style="font-size: small">
                  - ALBSERVICES_SUPPORT_CASE_FILE_ATTACHMENT_TRIGGERED, ALBSERVICES_SUPPORT_CASE_FILE_ATTACHMENT_SUCCESS,
                </div>
                                <div style="font-size: small">
                  - ALBSERVICES_SUPPORT_CASE_FILE_ATTACHMENT_FAILURE, ALBSERVICES_FILE_DOWNLOAD_TRIGGERED, ALBSERVICES_FILE_DOWNLOAD_SUCCESS,
                </div>
                                <div style="font-size: small">
                  - ALBSERVICES_FILE_DOWNLOAD_FAILURE, NSXT_ACCESS_SUCCESS, VCENTER_ACCESS_SUCCESS, NSXT_ACCESS_FAIL, VCENTER_ACCESS_FAIL, NSXT_IMAGE_UPLOAD_FAILURE,
                </div>
                                <div style="font-size: small">
                  - NSXT_IMAGE_UPLOAD_SUCCESS, NSXT_IMAGE_DELETE_FAILURE, NSXT_IMAGE_DELETE_SUCCESS, VCENTER_VSPHERE_HA_NOT_CONFIGURED,
                </div>
                                <div style="font-size: small">
                  - NSXT_SI_SERVICE_CREATE_UPDATE_SUCCESS, NSXT_SI_SERVICE_CREATE_UPDATE_FAILURE, NSXT_SI_SERVICE_DELETE_SUCCESS, NSXT_SI_SERVICE_DELETE_FAILURE,
                </div>
                                <div style="font-size: small">
                  - NSXT_SI_VIRTUALENDPOINT_CREATE_UPDATE_SUCCESS, NSXT_SI_VIRTUALENDPOINT_CREATE_UPDATE_FAILURE, NSXT_SI_VIRTUALENDPOINT_DELETE_SUCCESS,
                </div>
                                <div style="font-size: small">
                  - NSXT_SI_VIRTUALENDPOINT_DELETE_FAILURE, NSXT_SI_REDIRECTPOLICY_CREATE_UPDATE_SUCCESS, NSXT_SI_REDIRECTPOLICY_CREATE_UPDATE_FAILURE,
                </div>
                                <div style="font-size: small">
                  - NSXT_SI_REDIRECTPOLICY_DELETE_SUCCESS, NSXT_SI_REDIRECTPOLICY_DELETE_FAILURE, NSXT_SI_REDIRECTRULE_CREATE_UPDATE_SUCCESS,
                </div>
                                <div style="font-size: small">
                  - NSXT_SI_REDIRECTRULE_CREATE_UPDATE_FAILURE, NSXT_SI_REDIRECTRULE_DELETE_SUCCESS, NSXT_SI_REDIRECTRULE_DELETE_FAILURE,
                </div>
                                <div style="font-size: small">
                  - VCENTER_IMAGE_UPLOAD_FAILURE, VCENTER_IMAGE_UPLOAD_SUCCESS, VCENTER_IMAGE_DELETE_FAILURE, VCENTER_IMAGE_DELETE_SUCCESS, NSXT_INVALID_T1_SEG,
                </div>
                                <div style="font-size: small">
                  - NSXT_STREAMAGENT_CONNECT, NSXT_STREAMAGENT_DISCONNECT, NSXT_DFW_GROUP_UPDATE_SUCCESS, NSXT_DFW_GROUP_UPDATE_FAILURE,
                </div>
                                <div style="font-size: small">
                  - NSXT_DFW_GROUP_DELETE_FAILURE, NSXT_DFW_GROUP_DELETE_SUCCESS, NSXT_DFW_SERVICE_UPDATE_SUCCESS, NSXT_DFW_SERVICE_UPDATE_FAILED,
                </div>
                                <div style="font-size: small">
                  - NSXT_DFW_SERVICE_DELETE_SUCCESS, NSXT_DFW_SERVICE_DELETE_FAILED, NSXT_DFW_TAG_SEGMENT_PORT_SUCCESS, NSXT_DFW_TAG_SEGMENT_PORT_FAILED,
                </div>
                                <div style="font-size: small">
                  - NSXT_DFW_TAG_VM_SUCCESS, NSXT_DFW_TAG_VM_FAILED, UPGRADE_CONTROLLER_STARTED, UPGRADE_SE_GROUP_STARTED, RESUME_SE_GROUP_STARTED,
                </div>
                                <div style="font-size: small">
                  - PATCH_CONTROLLER_STARTED, PATCH_SE_GROUP_STARTED, ROLLBACK_CONTROLLER_STARTED, ROLLBACK_SE_GROUP_STARTED, ROLLBACKPATCH_CONTROLLER_STARTED,
                </div>
                                <div style="font-size: small">
                  - ROLLBACKPATCH_SE_GROUP_STARTED, UPGRADE_CONTROLLER_COMPLETE, UPGRADE_SE_GROUP_COMPLETE, PATCH_CONTROLLER_COMPLETE, PATCH_SE_GROUP_COMPLETE,
                </div>
                                <div style="font-size: small">
                  - ROLLBACK_CONTROLLER_COMPLETE, ROLLBACK_SE_GROUP_COMPLETE, ROLLBACKPATCH_CONTROLLER_COMPLETE, ROLLBACKPATCH_SE_GROUP_COMPLETE,
                </div>
                                <div style="font-size: small">
                  - UPGRADE_CONTROLLER_ABORTED, PATCH_CONTROLLER_ABORTED, UPGRADE_SE_GROUP_SUSPENDED, PATCH_SE_GROUP_SUSPENDED, ROLLBACK_SE_GROUP_SUSPENDED,
                </div>
                                <div style="font-size: small">
                  - ROLLBACKPATCH_SE_GROUP_SUSPENDED, UPGRADE_REQUEST, LICENSE_TRANSACTION, LICENSE_SE_RECONCILE, LICENSE_CONTROLLER_LICENSE_RECONCILE,
                </div>
                                <div style="font-size: small">
                  - LICENSE_TIER_SWITCH, CENTRAL_LICENSE_SUBSCRIPTION, CENTRAL_LICENSE_UNSUBSCRIPTION, CENTRAL_LICENSE_REFRESH_SUCCESS,
                </div>
                                <div style="font-size: small">
                  - CENTRAL_LICENSE_REFRESH_FAILURE, ROLLBACK_CONTROLLER_ABORTED, ROLLBACKPATCH_CONTROLLER_ABORTED, UPGRADE_DRYRUN_STARTED, UPGRADE_DRYRUN_COMPLETED,
                </div>
                                <div style="font-size: small">
                  - UPGRADE_DRYRUN_ABORTED, AUDIT_COMPLIANCE_EVENT, LOGAGENT_STREAMING_CONN_EVENT, CONTROLLER_DB_ERROR, AVI_FALSE_POSITIVE_DETECTION,
                </div>
                                <div style="font-size: small">
                  - CONNECT_TO_METRICSMGR_ERROR, DNS_VS_STATUS, CONFIG_VERSION_ACK_STATUS, PRE_CHECK_STARTED, PRE_CHECK_COMPLETED, POSTGRES_REPLICATION_FAILED,
                </div>
                                <div style="font-size: small">
                  - SAML_METADATA_UPDATE_FAILED, RESTORE_CONTROLLER_STARTED, RESTORE_CONTROLLER_ABORTED, RESTORE_CONTROLLER_COMPLETED, LOG_FREQUENT_DISK_CLEANUP,
                </div>
                                <div style="font-size: small">
                  - REQUEST_QUEUE_FULL, REQUEST_QUEUE_RECOVERING, POSTGRES_MAX_CONN_LIMIT_BREACHED, POSTGRES_CONN_RECOVERY, REQUEST_RATELIMIT,
                </div>
                                <div style="font-size: small">
                  - SYSTEM_REPORT_GENERATION_STARTED, SYSTEM_REPORT_GENERATION_COMPLETED, SYSTEM_REPORT_GENERATION_FAILED, SYSTEM_REPORT_DELETED,
                </div>
                                <div style="font-size: small">
                  - CRL_ENDPOINT_EXPIRED, CRL_ENDPOINT_EXPIRING_SOON, CRL_INVALID_ETAG, UBER_EVENT_TEMPLATE, UBER_EVENT_ERR_TEMPLATE, UPGRADE_FILECOPY_COMPLETED,
                </div>
                                <div style="font-size: small">
                  - UPGRADE_FILECOPY_FAILED, SE_PROCESS_CRASHED, CONTROLSCRIPT_EXECUTION_FAILURE, SYSTEM_LIMIT_BEYOND_SUPPORTED_CONFIG,
                </div>
                                <div style="font-size: small">
                  - SYSTEM_LIMIT_WITHIN_SUPPORTED_CONFIG, SYSTEM_CONFIG_SYNC_FAILURE, SE_AUTOSCALER_ACTIONS_GENERATED.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                            <td class="elbow-placeholder"></td>
                                    <td colspan="5">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>not_cond</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">bool</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as False.
                </div>
                                            </td>
    </tr>
        
            
                                                <td colspan="7">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>autoscale_alert</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">bool</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - This alert config applies to auto scale alerts.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                                            <td colspan="7">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>category</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Determines whether an alert is raised immediately when event occurs (realtime) or after specified number of events occurs within rolling time
                </div>
                                <div style="font-size: small">
                  - window.
                </div>
                                <div style="font-size: small">
                  - Enum options - REALTIME, ROLLINGWINDOW, WATERMARK.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as REALTIME.
                </div>
                                            </td>
    </tr>
                                            <td colspan="7">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>configpb_attributes</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                            <span style="color: purple">dict / elements=dictionary </span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Protobuf versioning for config pbs.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 21.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                <tr>
                                    <td class="elbow-placeholder"></td>
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>version</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">int</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Version sequence number that monotonically advances with each configuration update event.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 21.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as 1.
                </div>
                                            </td>
    </tr>
        
                                                <td colspan="7">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>description</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - A custom description field.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                                            <td colspan="7">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>enabled</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">bool</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Enable or disable this alert config from generating new alerts.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as True.
                </div>
                                            </td>
    </tr>
                                            <td colspan="7">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>expiry_time</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">int</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - An alert is expired and deleted after the expiry time has elapsed.
                </div>
                                <div style="font-size: small">
                  - The original event triggering the alert remains in the events log.
                </div>
                                <div style="font-size: small">
                  - Allowed values are 1-31536000.
                </div>
                                <div style="font-size: small">
                  - Unit is sec.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as 86400.
                </div>
                                            </td>
    </tr>
                                            <td colspan="7">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                <div style="font-size: small">
                <b>required: true</b>
                </div>
                            </td>
            <td>
                                                <div style="font-size: small">
                  - Name of the alert configuration.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                                            <td colspan="7">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>obj_uuid</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Instance of the resource for which alert was raised.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                                            <td colspan="7">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>object_type</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - The object type to which the alert config is associated with.
                </div>
                                <div style="font-size: small">
                  - Valid object types are - virtual service, pool, service engine.
                </div>
                                <div style="font-size: small">
                  - Enum options - VIRTUALSERVICE, POOL, HEALTHMONITOR, NETWORKPROFILE, APPLICATIONPROFILE, HTTPPOLICYSET, DNSPOLICY, SECURITYPOLICY, IPADDRGROUP,
                </div>
                                <div style="font-size: small">
                  - STRINGGROUP, SSLPROFILE, SSLKEYANDCERTIFICATE, NETWORKSECURITYPOLICY, APPLICATIONPERSISTENCEPROFILE, ANALYTICSPROFILE, VSDATASCRIPTSET, TENANT,
                </div>
                                <div style="font-size: small">
                  - PKIPROFILE, AUTHPROFILE, CLOUD...
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                                            <td colspan="7">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>recommendation</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                                            <td colspan="7">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>rolling_window</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">int</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Only if the number of events is reached or exceeded within the time window will an alert be generated.
                </div>
                                <div style="font-size: small">
                  - Allowed values are 1-31536000.
                </div>
                                <div style="font-size: small">
                  - Unit is sec.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as 300.
                </div>
                                            </td>
    </tr>
                                            <td colspan="7">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>source</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                <div style="font-size: small">
                <b>required: true</b>
                </div>
                            </td>
            <td>
                                                <div style="font-size: small">
                  - Signifies system events or the type of client logsused in this alert configuration.
                </div>
                                <div style="font-size: small">
                  - Enum options - CONN_LOGS, APP_LOGS, EVENT_LOGS, METRICS.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                                            <td colspan="7">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>summary</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Summary of reason why alert is generated.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                                            <td colspan="7">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>tenant_ref</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - It is a reference to an object of type tenant.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                                            <td colspan="7">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>threshold</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">int</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - An alert is created only when the number of events meets or exceeds this number within the chosen time frame.
                </div>
                                <div style="font-size: small">
                  - Allowed values are 1-65536.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as 1.
                </div>
                                            </td>
    </tr>
                                            <td colspan="7">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>throttle</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">int</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Alerts are suppressed (throttled) for this duration of time since the last alert was raised for this alert config.
                </div>
                                <div style="font-size: small">
                  - Allowed values are 0-31536000.
                </div>
                                <div style="font-size: small">
                  - Unit is sec.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as 600.
                </div>
                                            </td>
    </tr>
                                            <td colspan="7">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>url</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Avi controller URL of the object.
                </div>
                                            </td>
    </tr>
                                            <td colspan="7">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>uuid</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
        
    </table>
    <br/>

Examples
--------

.. code-block:: yaml

    - name: Deploy Controller
      hosts: localhost
      connection: 
      collections:
        - vmware.alb
      vars:
        avi_credentials:
          username: "avi_user"
          password: "avi_password"
          controller: "192.168.138.18"
          api_version: "21.1.1"
          tenant: "admin"
      tasks:
        - name: Example to create AlertConfig object
          avi_alertconfig:
            avi_credentials: "{{ avi_credentials }}"
            state: present
            name: sample_alertconfig


Authors
~~~~~~~
- Anurag Palsule (anurag.palsule@broadcom.com)
- Parikshit Manur (parikshit.manur@broadcom.com)
- Rohan Suryavanshi (rohan.suryavanshi@broadcom.com)
