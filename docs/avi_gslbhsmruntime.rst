.. vmware.alb.avi_gslbhsmruntime:


**********************************************
vmware.alb.avi_gslbhsmruntime
**********************************************

**Module for setup of GslbHSMRuntime Avi RESTful Object**


.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module is used to configure GslbHSMRuntime object.
- More examples at (https://github.com/avinetworks/devops).


Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="4">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
        <tr>
            <td colspan="4">
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
            <td colspan="4">
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
            <td colspan="4">
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
            <td colspan="4">
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
            <td colspan="4">
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
            <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>cluster_uuid</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - The site controller cluster uuid.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 31.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, enterprise with cloud services edition.
                </div>
                                            </td>
        </tr>
                        <tr>
            <td colspan="4">
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
                  - Represents whether hsm is enabled/disabled.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 31.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, enterprise with cloud services edition.
                </div>
                                            </td>
        </tr>
                        <tr>
            <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>events</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Events captured wrt to config replication.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 31.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, enterprise with cloud services edition.
                </div>
                                            </td>
        </tr>
                <tr>
                    <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> msg </b>
                    <div style="font-size: small">
                                                    <span style="color: purple">list / elements=string </span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                            <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> name </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                            <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> timestamp </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Event creation time.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 31.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                <tr>
                    <td class="elbow-placeholder"></td>
            <td class="elbow-placeholder"></td>
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> secs </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>     
        </tr>
                    <td class="elbow-placeholder"></td>
            <td class="elbow-placeholder"></td>
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> usecs </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>     
        </tr>
                                    <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> uuid </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                                        <tr>
            <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>local_info</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Represents local info for the site.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 31.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, enterprise with cloud services edition.
                </div>
                                            </td>
        </tr>
                <tr>
                    <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> gs_status </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - This field encapsulates the gs-status edge-triggered framework.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 31.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                <tr>
                    <td class="elbow-placeholder"></td>
            <td class="elbow-placeholder"></td>
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> last_changed_time </b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Field introduced in 17.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>     
        </tr>
                    <td class="elbow-placeholder"></td>
            <td class="elbow-placeholder"></td>
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> num_partial_updates </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Counter to track the number of partial updates sent.
                </div>
                                <div style="font-size: small">
                  - Once it reaches the partial updates threshold, a full update is sent.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 17.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>     
        </tr>
                    <td class="elbow-placeholder"></td>
            <td class="elbow-placeholder"></td>
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> partial_update_threshold </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Threshold after which a full gs status is sent.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 17.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>     
        </tr>
                    <td class="elbow-placeholder"></td>
            <td class="elbow-placeholder"></td>
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> state </b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - State variable to trigger full or partial update.
                </div>
                                <div style="font-size: small">
                  - Enum options - GSLB_FULL_UPDATE_PENDING, GSLB_PARTIAL_UPDATE_PENDING.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 17.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>     
        </tr>
                    <td class="elbow-placeholder"></td>
            <td class="elbow-placeholder"></td>
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> type </b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Describes the type (partial/full) of the last gs status sent to dns-vs(es).
                </div>
                                <div style="font-size: small">
                  - Enum options - GSLB_NO_UPDATE, GSLB_FULL_UPDATE, GSLB_PARTIAL_UPDATE.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 17.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>     
        </tr>
                                    <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> gslb_info </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - This field keeps track of gslb object's information.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 31.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                <tr>
                    <td class="elbow-placeholder"></td>
            <td class="elbow-placeholder"></td>
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> repl_state </b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - The config replication info to se(es) and peer sites.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 31.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, enterprise with cloud services edition.
                </div>
                                            </td>     
        </tr>
                                                <tr>
            <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - The name of db entry.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 31.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, enterprise with cloud services edition.
                </div>
                                            </td>
        </tr>
                        <tr>
            <td colspan="4">
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
                  - Gslb hsm runtime object uuid.
                </div>
                                <div style="font-size: small">
                  - Points to the gslb to which this belongs.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 31.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, enterprise with cloud services edition.
                </div>
                                            </td>
        </tr>
                        <tr>
            <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>oper_status</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Gslb site operational status, represents whether site is up or down.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 31.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, enterprise with cloud services edition.
                </div>
                                            </td>
        </tr>
                <tr>
                    <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> last_changed_time </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                <tr>
                    <td class="elbow-placeholder"></td>
            <td class="elbow-placeholder"></td>
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> secs </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>     
        </tr>
                    <td class="elbow-placeholder"></td>
            <td class="elbow-placeholder"></td>
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> usecs </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>     
        </tr>
                                    <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> reason </b>
                    <div style="font-size: small">
                                                    <span style="color: purple">list / elements=string </span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                            <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> reason_code </b>
                    <div style="font-size: small">
                                                <span style="color: purple">integer</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                            <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> reason_code_string </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                            <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> state </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Enum options - OPER_UP, OPER_DOWN, OPER_CREATING, OPER_RESOURCES, OPER_INACTIVE, OPER_DISABLED, OPER_UNUSED, OPER_UNKNOWN, OPER_PROCESSING,
                </div>
                                <div style="font-size: small">
                  - OPER_INITIALIZING, OPER_ERROR_DISABLED, OPER_AWAIT_MANUAL_PLACEMENT, OPER_UPGRADING, OPER_SE_PROCESSING, OPER_PARTITIONED, OPER_DISABLING,
                </div>
                                <div style="font-size: small">
                  - OPER_FAILED, OPER_UNAVAIL, OPER_AGGREGATE_DOWN.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                                        <tr>
            <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>remote_info</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Remote info is basically updated by grw.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 31.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, enterprise with cloud services edition.
                </div>
                                            </td>
        </tr>
                <tr>
                    <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> gslb_info </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Gslb object related information in the site.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 31.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                <tr>
                    <td class="elbow-placeholder"></td>
            <td class="elbow-placeholder"></td>
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> repl_state </b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - The config replication info to se(es) and peer sites.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 31.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, enterprise with cloud services edition.
                </div>
                                            </td>     
        </tr>
                                    <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> ops_info </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Operational information of the site.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 31.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                <tr>
                    <td class="elbow-placeholder"></td>
            <td class="elbow-placeholder"></td>
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> rrtoken </b>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Current outstanding request-response token of the message to this site.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 31.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, enterprise with cloud services edition.
                </div>
                                            </td>     
        </tr>
                                    <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> sync_info </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Configuration sync-info of the site.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 31.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                <tr>
                    <td class="elbow-placeholder"></td>
            <td class="elbow-placeholder"></td>
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> errored_objects </b>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Objects that could not be synced to the site.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>     
        </tr>
                    <td class="elbow-placeholder"></td>
            <td class="elbow-placeholder"></td>
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> last_changed_time </b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>     
        </tr>
                    <td class="elbow-placeholder"></td>
            <td class="elbow-placeholder"></td>
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> last_fail_obj </b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Last object having replication issue.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 21.1.3.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, enterprise with cloud services edition.
                </div>
                                            </td>     
        </tr>
                    <td class="elbow-placeholder"></td>
            <td class="elbow-placeholder"></td>
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> prev_target_version </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Previous targer version for a site.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 31.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, enterprise with cloud services edition.
                </div>
                                            </td>     
        </tr>
                    <td class="elbow-placeholder"></td>
            <td class="elbow-placeholder"></td>
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> reason </b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Reason for the replication issues.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 21.1.3.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, enterprise with cloud services edition.
                </div>
                                            </td>     
        </tr>
                    <td class="elbow-placeholder"></td>
            <td class="elbow-placeholder"></td>
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> recommendation </b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Recommended way to resolve replication issue.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 21.1.3.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, enterprise with cloud services edition.
                </div>
                                            </td>     
        </tr>
                    <td class="elbow-placeholder"></td>
            <td class="elbow-placeholder"></td>
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> site_version </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Version of the site.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 31.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, enterprise with cloud services edition.
                </div>
                                            </td>     
        </tr>
                    <td class="elbow-placeholder"></td>
            <td class="elbow-placeholder"></td>
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> sync_state </b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Configuration sync-state of the site.
                </div>
                                <div style="font-size: small">
                  - Enum options - GSLB_SITE_CFG_IN_SYNC, GSLB_SITE_CFG_OUT_OF_SYNC, GSLB_SITE_CFG_SYNC_DISABLED, GSLB_SITE_CFG_SYNC_IN_PROGRESS,
                </div>
                                <div style="font-size: small">
                  - GSLB_SITE_CFG_SYNC_NOT_APPLICABLE, GSLB_SITE_CFG_SYNCED_TILL_CHECKPOINT, GSLB_SITE_CFG_SYNC_SUSPENDED, GSLB_SITE_CFG_SYNC_STALLED.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>     
        </tr>
                    <td class="elbow-placeholder"></td>
            <td class="elbow-placeholder"></td>
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> target_version </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Target version of the site.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 31.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, enterprise with cloud services edition.
                </div>
                                            </td>     
        </tr>
                                    <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> sync_stats </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Site replication specific statistic.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 31.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                <tr>
                    <td class="elbow-placeholder"></td>
            <td class="elbow-placeholder"></td>
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> acknowledged_version </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Last config version acknowledged.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 20.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>     
        </tr>
                    <td class="elbow-placeholder"></td>
            <td class="elbow-placeholder"></td>
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> pending_object_count </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Number of pending objects.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 20.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>     
        </tr>
                    <td class="elbow-placeholder"></td>
            <td class="elbow-placeholder"></td>
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> received_version </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Last config version received.
                </div>
                                <div style="font-size: small">
                  - On leader, this represents the version received from federated datastore.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 20.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>     
        </tr>
                                                <tr>
            <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>send_interval</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Frequency with which group members communicate.
                </div>
                                <div style="font-size: small">
                  - This field shadows glb_cfg.send_interval.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 31.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, enterprise with cloud services edition.
                </div>
                                            </td>
        </tr>
                        <tr>
            <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>site_name</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - The gslb site name.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 31.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, enterprise with cloud services edition.
                </div>
                                            </td>
        </tr>
                        <tr>
            <td colspan="4">
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
                  - Uuid of the tenant.
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type tenant.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 31.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, enterprise with cloud services edition.
                </div>
                                            </td>
        </tr>
                        <tr>
            <td colspan="4">
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
                        <tr>
            <td colspan="4">
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
                  - The uuid of db entry.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 31.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, enterprise with cloud services edition.
                </div>
                                            </td>
        </tr>
                    </table>
    <br/>


Examples
--------

.. code-block:: yaml

    - hosts: localhost
      connection: local
      collections:
        - vmware.alb
      vars:
        avi_credentials:
          username: "avi_user"
          password: "avi_password"
          controller: "192.168.138.18"
          api_version: "21.1.1"
      tasks:
        - name: Example to create GslbHSMRuntime object
          avi_gslbhsmruntime:
            avi_credentials: "{{ avi_credentials }}"
            state: present
            name: sample_gslbhsmruntime


Authors
~~~~~~~
- Gaurav Rastogi (grastogi@vmware.com)
- Sandeep Bandi (sbandi@vmware.com)
- Amol Shinde (samol@vmware.com)



