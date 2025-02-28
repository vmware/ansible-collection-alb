.. vmware.alb.avi_cloudproperties:


**********************************************
vmware.alb.avi_cloudproperties
**********************************************

**Module for setup of CloudProperties Avi RESTful Object**


.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module is used to configure CloudProperties object.
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
                <b>cc_props</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Cloudconnector properties.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
        </tr>
                <tr>
                    <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> rpc_poll_interval </b>
                    <div style="font-size: small">
                                                <span style="color: purple">integer</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Unit is sec.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                            <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> rpc_queue_size </b>
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
                                        <tr>
            <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>cc_vtypes</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Cloud types supported by cloudconnector.
                </div>
                                <div style="font-size: small">
                  - Enum options - CLOUD_NONE, CLOUD_VCENTER, CLOUD_OPENSTACK, CLOUD_AWS, CLOUD_VCA, CLOUD_APIC, CLOUD_MESOS, CLOUD_LINUXSERVER, CLOUD_DOCKER_UCP,
                </div>
                                <div style="font-size: small">
                  - CLOUD_RANCHER, CLOUD_OSHIFT_K8S, CLOUD_AZURE, CLOUD_GCP, CLOUD_NSXT.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
        </tr>
                        <tr>
            <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>configpb_attributes</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
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
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> version </b>
                    <div style="font-size: small">
                                                <span style="color: purple">integer</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
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
                                            </td>             
        </tr>
                                        <tr>
            <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>hyp_props</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Hypervisor properties.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
        </tr>
                <tr>
                    <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> htype </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Enum options - DEFAULT, VMWARE_ESX, KVM, VMWARE_VSAN, XEN.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                            <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> max_ips_per_nic </b>
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
                    <b> max_nics </b>
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
                                        <tr>
            <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>info</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Properties specific to a cloud type.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
        </tr>
                <tr>
                    <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> cca_props </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Cloudconnectoragent properties specific to this cloud type.
                </div>
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
                    <b> async_retries </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Maximum polls to check for async jobs to finish.
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
                    <b> async_retries_delay </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Delay between each async job status poll check.
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
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> poll_duration_target </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Discovery poll target duration; a scale factor of 1+ is computed with the actual discovery (actual/target) and used to tweak slow and fast poll
                </div>
                                <div style="font-size: small">
                  - intervals.
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
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> poll_fast_target </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Fast poll interval.
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
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> poll_slow_target </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Slow poll interval.
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
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> vcenter_host_ping_interval </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Vcenter host reachability check interval.
                </div>
                                <div style="font-size: small">
                  - Allowed values are 60-3600.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 22.1.3.
                </div>
                                <div style="font-size: small">
                  - Unit is sec.
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
                    <b> vcenter_inventory_max_object_updates </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Batch size of vcenter inventory updates.
                </div>
                                <div style="font-size: small">
                  - Allowed values are 1-500.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 22.1.3.
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
                    <b> vcenter_max_datastore_go_routines </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Max datastore processing go routines for vcenter datastore updates.
                </div>
                                <div style="font-size: small">
                  - Allowed values are 1-40.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 22.1.3.
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
                    <b> vcenter_reconcile_interval </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Reconcile interval for vcenter inventory.
                </div>
                                <div style="font-size: small">
                  - Allowed values are 60-3600.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 22.1.3.
                </div>
                                <div style="font-size: small">
                  - Unit is sec.
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
                    <b> vnic_retries </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Maximum polls to check for vnics to be attached to vm.
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
                    <b> vnic_retries_delay </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Delay between each vnic status poll check.
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
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> controller_props </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Controller properties specific to this cloud type.
                </div>
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
                    <b> alert_manager_use_evms </b>
                    <div style="font-size: small">
                        <span style="color: purple">bool</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Enable to use event manager as source of eventsdisable to use log manager as source of events.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 30.2.1.
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
                    <b> allow_admin_network_updates </b>
                    <div style="font-size: small">
                        <span style="color: purple">bool</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Allow non-admin tenants to update admin vrfcontext and network objects.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 18.2.7, 20.1.1.
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
                    <b> allow_ip_forwarding </b>
                    <div style="font-size: small">
                        <span style="color: purple">bool</span>
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
                    <b> allow_unauthenticated_apis </b>
                    <div style="font-size: small">
                        <span style="color: purple">bool</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Allow unauthenticated access for special apis.
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
                    <b> allow_unauthenticated_nodes </b>
                    <div style="font-size: small">
                        <span style="color: purple">bool</span>
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
                    <b> api_idle_timeout </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Allowed values are 0-1440.
                </div>
                                <div style="font-size: small">
                  - Unit is min.
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
                    <b> api_perf_logging_threshold </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Threshold to log request timing in portal_performance.log and server-timing response header.
                </div>
                                <div style="font-size: small">
                  - Any stage taking longer than 1% of the threshold will be included in the server-timing header.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 18.1.4, 18.2.1.
                </div>
                                <div style="font-size: small">
                  - Unit is milliseconds.
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
                    <b> appviewx_compat_mode </b>
                    <div style="font-size: small">
                        <span style="color: purple">bool</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Export configuration in appviewx compatibility mode.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 17.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Allowed in essentials (allowed values- false), basic (allowed values- false) edition.
                </div>
                                            </td>     
        </tr>
                    <td class="elbow-placeholder"></td>
            <td class="elbow-placeholder"></td>
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> archive_retention_framework_period </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Period for archive and retention framework job.
                </div>
                                <div style="font-size: small">
                  - Allowed values are 1-240.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 31.1.1.
                </div>
                                <div style="font-size: small">
                  - Unit is min.
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
                    <b> async_patch_merge_period </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Period for which asynchronous patch requests are queued.
                </div>
                                <div style="font-size: small">
                  - Allowed values are 30-120.
                </div>
                                <div style="font-size: small">
                  - Special values are 0 - deactivated.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 18.2.11, 20.1.3.
                </div>
                                <div style="font-size: small">
                  - Unit is sec.
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
                    <b> async_patch_request_cleanup_duration </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Duration for which asynchronous patch requests should be kept, after being marked as success or fail.
                </div>
                                <div style="font-size: small">
                  - Allowed values are 5-120.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 18.2.11, 20.1.3.
                </div>
                                <div style="font-size: small">
                  - Unit is min.
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
                    <b> attach_ip_retry_interval </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
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
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> attach_ip_retry_limit </b>
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
                    <b> bm_use_ansible </b>
                    <div style="font-size: small">
                        <span style="color: purple">bool</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Use ansible for se creation in baremetal.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 17.2.2.
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
                    <b> check_vsvip_fqdn_syntax </b>
                    <div style="font-size: small">
                        <span style="color: purple">bool</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Enforce vsvip fqdn syntax checks.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 20.1.6.
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
                    <b> cleanup_expired_authtoken_timeout_period </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Period for auth token cleanup job.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 18.1.1.
                </div>
                                <div style="font-size: small">
                  - Unit is min.
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
                    <b> cleanup_sessions_timeout_period </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Period for sessions cleanup job.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 18.1.1.
                </div>
                                <div style="font-size: small">
                  - Unit is min.
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
                    <b> cloud_discovery_interval </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Time in minutes to wait between consecutive cloud discovery cycles.
                </div>
                                <div style="font-size: small">
                  - Allowed values are 1-1440.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 22.1.5, 30.2.1.
                </div>
                                <div style="font-size: small">
                  - Unit is min.
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
                    <b> cloud_reconcile </b>
                    <div style="font-size: small">
                        <span style="color: purple">bool</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Enable/disable periodic reconcile for all the clouds.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 17.2.14,18.1.5,18.2.1.
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
                    <b> cloud_reconcile_interval </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Time in minutes to wait between consecutive cloud reconcile cycles.
                </div>
                                <div style="font-size: small">
                  - Allowed values are 1-1440.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 22.1.5, 30.2.1.
                </div>
                                <div style="font-size: small">
                  - Unit is min.
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
                    <b> cluster_ip_gratuitous_arp_period </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Period for cluster ip gratuitous arp job.
                </div>
                                <div style="font-size: small">
                  - Allowed values are 1-1440.
                </div>
                                <div style="font-size: small">
                  - Unit is min.
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
                    <b> configpb_attributes </b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
            </td>
            <td></td>
            <td></td>
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
                    <td class="elbow-placeholder"></td>
            <td class="elbow-placeholder"></td>
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> consistency_check_timeout_period </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Period for consistency check job.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 18.1.1.
                </div>
                                <div style="font-size: small">
                  - Unit is min.
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
                    <b> controller_resource_info_collection_period </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Periodically collect stats.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 20.1.3.
                </div>
                                <div style="font-size: small">
                  - Unit is min.
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
                    <b> crashed_se_reboot </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
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
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> dead_se_detection_timer </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
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
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> default_minimum_api_timeout </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Minimum api timeout value.if this value is not 60, it will be the default timeout for all apis that do not have a specific timeout.if an api has
                </div>
                                <div style="font-size: small">
                  - a specific timeout but is less than this value, this value will become the new timeout.
                </div>
                                <div style="font-size: small">
                  - Allowed values are 60-3600.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 18.2.6.
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
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> del_offline_se_after_reboot_delay </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - The amount of time the controller will wait before deleting an offline se after it has been rebooted.
                </div>
                                <div style="font-size: small">
                  - For unresponsive ses, the total time will be  unresponsive_se_reboot + del_offline_se_after_reboot_delay.
                </div>
                                <div style="font-size: small">
                  - For crashed ses, the total time will be crashed_se_reboot + del_offline_se_after_reboot_delay.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 20.1.5.
                </div>
                                <div style="font-size: small">
                  - Unit is sec.
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
                    <b> detach_ip_retry_interval </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Amount of time to wait after last detach ip failure before attempting next detach ip retry.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 21.1.3.
                </div>
                                <div style="font-size: small">
                  - Unit is sec.
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
                    <b> detach_ip_retry_limit </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Maximum number of detach ip retries.
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
                    <b> detach_ip_timeout </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Time to wait before marking detach ip as failed.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 21.1.3.
                </div>
                                <div style="font-size: small">
                  - Unit is sec.
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
                    <b> dns_refresh_period </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Period for refresh pool and gslb dns job.
                </div>
                                <div style="font-size: small">
                  - Unit is min.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Allowed in essentials (allowed values- 60), basic (allowed values- 60) edition.
                </div>
                                            </td>     
        </tr>
                    <td class="elbow-placeholder"></td>
            <td class="elbow-placeholder"></td>
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> dummy </b>
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
                    <b> edit_system_limits </b>
                    <div style="font-size: small">
                        <span style="color: purple">bool</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Allow editing of system limits.
                </div>
                                <div style="font-size: small">
                  - Keep in mind that these system limits have been carefully selected based on rigorous testing in our testig environments.
                </div>
                                <div style="font-size: small">
                  - Modifying these limits could destabilize your cluster.
                </div>
                                <div style="font-size: small">
                  - Do this at your own risk!.
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
                    <b> enable_api_sharding </b>
                    <div style="font-size: small">
                        <span style="color: purple">bool</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - This setting enables the controller leader to shard api requests to the followers (if any).
                </div>
                                <div style="font-size: small">
                  - Field introduced in 18.1.5, 18.2.1.
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
                    <b> enable_memory_balancer </b>
                    <div style="font-size: small">
                        <span style="color: purple">bool</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Enable/disable memory balancer.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 17.2.8.
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
                    <b> enable_nsx_streaming_agent </b>
                    <div style="font-size: small">
                        <span style="color: purple">bool</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - When set to true, avi controller will connect to dynamic config streaming agent on nsx manager to get live updates.
                </div>
                                <div style="font-size: small">
                  - If it cannot connect, it will fallback to using rest apis based periodic polling.
                </div>
                                <div style="font-size: small">
                  - Dynamic streaming is supported from nsx version 4.2.1 onwards.
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
                    <b> enable_per_process_stop </b>
                    <div style="font-size: small">
                        <span style="color: purple">bool</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Enable stopping of individual processes if process cross the given threshold limit, even when the total controller memory usage is belowits
                </div>
                                <div style="font-size: small">
                  - threshold limit.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 21.1.1.
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
                    <b> enable_resmgr_log_cache_print </b>
                    <div style="font-size: small">
                        <span style="color: purple">bool</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Enable printing of cached logs inside resource manager.
                </div>
                                <div style="font-size: small">
                  - Used for debugging purposes only.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 20.1.6.
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
                    <b> event_manager_max_goroutines </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Maximum number of goroutines for event manager process.
                </div>
                                <div style="font-size: small">
                  - Allowed values are 1-64.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 30.2.1.
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
                    <b> event_manager_max_subscribers </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Maximum number of subscribers for event manager process.
                </div>
                                <div style="font-size: small">
                  - Allowed values are 1-6.
                </div>
                                <div style="font-size: small">
                  - Special values are 0 - disabled.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 30.2.1.
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
                    <b> event_manager_processing_time_threshold </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Log instances for event manager processing delay; recorded whenever event processing delay exceeds configured interval specified in seconds.
                </div>
                                <div style="font-size: small">
                  - Allowed values are 1-5.
                </div>
                                <div style="font-size: small">
                  - Special values are 0 - disabled.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 30.2.1.
                </div>
                                <div style="font-size: small">
                  - Unit is sec.
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
                    <b> false_positive_learning_config </b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - False positive learning configuration.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 22.1.1.
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
                    <b> fatal_error_lease_time </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
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
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> federated_datastore_cleanup_duration </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Federated datastore will not cleanup diffs unless they are at least this duration in the past.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 20.1.1.
                </div>
                                <div style="font-size: small">
                  - Unit is hours.
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
                    <b> file_object_cleanup_period </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Period for file object cleanup job.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 20.1.1.
                </div>
                                <div style="font-size: small">
                  - Unit is min.
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
                    <b> file_reference_mappings </b>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - List of mapping for file reference and their absolute path.
                </div>
                                <div style="font-size: small">
                  - Field deprecated in 30.2.1.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 30.1.1.
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
                    <b> fileobject_max_file_versions </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - This is the max number of file versions that will be retained for a file referenced by the local fileobject.
                </div>
                                <div style="font-size: small">
                  - Subsequent uploads of file will result in the file rotation of the older version and the latest version retained.
                </div>
                                <div style="font-size: small">
                  - Example  when a file upload is done for the first time, there will be a v1 version.
                </div>
                                <div style="font-size: small">
                  - Subsequent uploads will get mapped to v1, v2 and v3 versions.
                </div>
                                <div style="font-size: small">
                  - On the fourth upload of the file, the v1 will be file rotated and v2, v3 and v4 will be retained.
                </div>
                                <div style="font-size: small">
                  - Allowed values are 1-5.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 30.2.1.
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
                    <b> gslb_fileobject_max_version_count </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Number of version copies for a givenfile object of gslb_geo_db type.
                </div>
                                <div style="font-size: small">
                  - Allowed values are 2-50000.
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
                    <b> gslb_purge_batch_size </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Batch size for the vs_mgr to perform datastrorecleanup during a gslb purge.
                </div>
                                <div style="font-size: small">
                  - Allowed values are 50-1200.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 22.1.3.
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
                    <b> gslb_purge_sleep_time_ms </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Sleep time in the vs_mgr during a federatedpurge rpc call.
                </div>
                                <div style="font-size: small">
                  - Allowed values are 50-100.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 22.1.3.
                </div>
                                <div style="font-size: small">
                  - Unit is milliseconds.
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
                    <b> ignore_vrf_in_networksubnetlist </b>
                    <div style="font-size: small">
                        <span style="color: purple">bool</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Ignore the vrf_context filter for /networksubnetlist api.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 22.1.4.
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
                    <b> max_dead_se_in_grp </b>
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
                    <b> max_pcap_per_tenant </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Maximum number of pcap files stored per tenant.
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
                    <b> max_se_spawn_interval_delay </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Maximum delay possible to add to se_spawn_retry_interval after successive se spawn failure.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 20.1.1.
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
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> max_seq_attach_ip_failures </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Maximum number of consecutive attach ip failures that halts vs placement.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 17.2.2.
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
                    <b> max_seq_vnic_failures </b>
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
                    <b> max_threads_cc_vip_bg_worker </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Maximum number of threads in threadpool used by cloud connector ccvipbgworker.
                </div>
                                <div style="font-size: small">
                  - Allowed values are 1-100.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 20.1.3.
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
                    <b> permission_scoped_shared_admin_networks </b>
                    <div style="font-size: small">
                        <span style="color: purple">bool</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Network and vrfcontext objects from the admin tenant will not be shared to non-admin tenants unless admin permissions are granted.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 18.2.7, 20.1.1.
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
                    <b> persistence_key_rotate_period </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Period for rotate app persistence keys job.
                </div>
                                <div style="font-size: small">
                  - Allowed values are 1-1051200.
                </div>
                                <div style="font-size: small">
                  - Special values are 0 - disabled.
                </div>
                                <div style="font-size: small">
                  - Unit is min.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Allowed in essentials (allowed values- 0), basic (allowed values- 0) edition.
                </div>
                                            </td>     
        </tr>
                    <td class="elbow-placeholder"></td>
            <td class="elbow-placeholder"></td>
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> portal_request_burst_limit </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Burst limit on number of incoming requests.
                </div>
                                <div style="font-size: small">
                  - 0 to disable.
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
                    <b> portal_request_rate_limit </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Maximum average number of requests allowed per second.
                </div>
                                <div style="font-size: small">
                  - 0 to disable.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 20.1.1.
                </div>
                                <div style="font-size: small">
                  - Unit is per_second.
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
                    <b> portal_token </b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Token used for uploading tech-support to portal.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 16.4.6,17.1.2.
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
                    <b> postgres_vacuum_period </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Period for which postgres vacuum are executed.
                </div>
                                <div style="font-size: small">
                  - Allowed values are 30-40320.
                </div>
                                <div style="font-size: small">
                  - Special values are 0 - deactivated.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 22.1.3.
                </div>
                                <div style="font-size: small">
                  - Unit is min.
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
                    <b> process_locked_useraccounts_timeout_period </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Period for process locked user accounts job.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 18.1.1.
                </div>
                                <div style="font-size: small">
                  - Unit is min.
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
                    <b> process_pki_profile_timeout_period </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Period for process pki profile job.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 18.1.1.
                </div>
                                <div style="font-size: small">
                  - Unit is min.
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
                    <b> query_host_fail </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
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
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> resmgr_log_caching_period </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Period for each cycle of log caching in resource manager.
                </div>
                                <div style="font-size: small">
                  - At the end of each cycle, the in memory cached log history will be cleared.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 20.1.5.
                </div>
                                <div style="font-size: small">
                  - Unit is sec.
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
                    <b> restrict_cloud_read_access </b>
                    <div style="font-size: small">
                        <span style="color: purple">bool</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Restrict read access to cloud.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 22.1.1.
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
                    <b> safenet_hsm_version </b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Version of the safenet package installed on the controller.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 16.5.2,17.2.3.
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
                    <b> se_create_timeout </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
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
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> se_failover_attempt_interval </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Interval between attempting failovers to an se.
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
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> se_from_marketplace </b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - This setting decides whether se is to be deployed from the cloud marketplace or to be created by the controller.
                </div>
                                <div style="font-size: small">
                  - The setting is applicable only when byol license is selected.
                </div>
                                <div style="font-size: small">
                  - Enum options - MARKETPLACE, IMAGE_SE.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 18.1.4, 18.2.1.
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
                    <b> se_offline_del </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
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
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> se_spawn_retry_interval </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Default retry period before attempting another service engine spawn in se group.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 20.1.1.
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
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> se_upgrade_flow_cleanup_timeout </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Timeout for flows cleanup by serviceengine during upgrade.internal knob  to be exercised under the surveillance of vmware avi support team.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 22.1.1.
                </div>
                                <div style="font-size: small">
                  - Unit is sec.
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
                    <b> se_vnic_cooldown </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
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
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> se_vnic_gc_wait_time </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Duration to wait after last vnic addition before proceeding with vnic garbage collection.
                </div>
                                <div style="font-size: small">
                  - Used for testing purposes.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 20.1.4.
                </div>
                                <div style="font-size: small">
                  - Unit is sec.
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
                    <b> secure_channel_cleanup_timeout </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Period for secure channel cleanup job.
                </div>
                                <div style="font-size: small">
                  - Unit is min.
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
                    <b> secure_channel_controller_token_timeout </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Unit is min.
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
                    <b> secure_channel_se_token_timeout </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Unit is min.
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
                    <b> seupgrade_copy_buffer_size </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - This parameter defines the buffer size during se image downloads in a segroup.
                </div>
                                <div style="font-size: small">
                  - It is used to pace the se downloads so that controller network/cpu bandwidth is a bounded operation.
                </div>
                                <div style="font-size: small">
                  - Please refer to upgradeprofile for equivalent fields.
                </div>
                                <div style="font-size: small">
                  - Field deprecated in 31.1.1.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 22.1.4.
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
                    <b> seupgrade_copy_pool_size </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - This parameter defines the number of simultaneous se image downloads in a segroup.
                </div>
                                <div style="font-size: small">
                  - It is used to pace the se downloads so that controller network/cpu bandwidth is a bounded operation.
                </div>
                                <div style="font-size: small">
                  - A value of 0 will disable the pacing scheme and all the se(s) in the segroup will attempt to download the image.
                </div>
                                <div style="font-size: small">
                  - Please refer to upgradeprofile for equivalent fields.
                </div>
                                <div style="font-size: small">
                  - Field deprecated in 31.1.1.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 18.2.6.
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
                    <b> seupgrade_fabric_pool_size </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - The pool size is used to control the number of concurrent segroup upgrades.
                </div>
                                <div style="font-size: small">
                  - This field value takes affect upon controller warm reboot.
                </div>
                                <div style="font-size: small">
                  - Please refer to upgradeprofile for equivalent fields.
                </div>
                                <div style="font-size: small">
                  - Allowed values are 2-20.
                </div>
                                <div style="font-size: small">
                  - Field deprecated in 31.1.1.
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
                    <b> seupgrade_segroup_min_dead_timeout </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Time to wait before marking segroup upgrade as stuck.
                </div>
                                <div style="font-size: small">
                  - Field deprecated in 31.1.1.
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
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> shared_ssl_certificates </b>
                    <div style="font-size: small">
                        <span style="color: purple">bool</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Ssl certificates in the admin tenant can be used in non-admin tenants.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 18.2.5.
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
                    <b> skip_beego_perf_collection </b>
                    <div style="font-size: small">
                        <span style="color: purple">bool</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Skip api performance collection for requests going through the apiserver.
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
                    <b> skopeo_retry_interval </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Time interval (in seconds) between retires for skopeo commands.
                </div>
                                <div style="font-size: small">
                  - Field deprecated in 31.1.1.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 30.1.1.
                </div>
                                <div style="font-size: small">
                  - Unit is sec.
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
                    <b> skopeo_retry_limit </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Number of times to try skopeo commands for remote image registries.
                </div>
                                <div style="font-size: small">
                  - Field deprecated in 31.1.1.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 30.1.1.
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
                    <b> soft_min_mem_per_se_limit </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Soft limit on the minimum se memory that an se needs to have on se register.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 30.1.1.
                </div>
                                <div style="font-size: small">
                  - Unit is mb.
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
                    <b> ssl_certificate_expiry_warning_days </b>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Number of days for ssl certificate expiry warning.
                </div>
                                <div style="font-size: small">
                  - Unit is days.
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
                    <b> statecache_properties </b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Configure statecache behavior for config, se, resmgr.
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
                    <b> system_report_cleanup_interval </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Time in minutes to wait between cleanup of systemreports.
                </div>
                                <div style="font-size: small">
                  - Allowed values are 15-300.
                </div>
                                <div style="font-size: small">
                  - Field deprecated in 31.1.1.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 22.1.6, 30.2.1.
                </div>
                                <div style="font-size: small">
                  - Unit is min.
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
                    <b> system_report_limit </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Number of systemreports retained in the system.
                </div>
                                <div style="font-size: small">
                  - Once the number of system reports exceed this threshold, the oldest systemreport will be removed and the latest one retained.
                </div>
                                <div style="font-size: small">
                  - I.e.
                </div>
                                <div style="font-size: small">
                  - The systemreport will be rotated and the reports don't exceed the threshold.
                </div>
                                <div style="font-size: small">
                  - Allowed values are 5-50.
                </div>
                                <div style="font-size: small">
                  - Field deprecated in 31.1.1.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 22.1.6, 30.2.1.
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
                    <b> unresponsive_se_reboot </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
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
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> update_dns_entry_retry_limit </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Number of times to retry a dns entry update/delete operation.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 21.1.4.
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
                    <b> update_dns_entry_timeout </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Timeout period for a dns entry update/delete operation.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 21.1.4.
                </div>
                                <div style="font-size: small">
                  - Unit is sec.
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
                    <b> upgrade_dns_ttl </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Time to account for dns ttl during upgrade.
                </div>
                                <div style="font-size: small">
                  - This is in addition to vs_scalein_timeout_for_upgrade in se_group.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 17.1.1.
                </div>
                                <div style="font-size: small">
                  - Unit is sec.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Allowed in essentials (allowed values- 5), basic (allowed values- 5) edition.
                </div>
                                            </td>     
        </tr>
                    <td class="elbow-placeholder"></td>
            <td class="elbow-placeholder"></td>
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> upgrade_fat_se_lease_time </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Amount of time controller waits for a large-sized se (>=128gb memory) to reconnect after it is rebooted during upgrade.
                </div>
                                <div style="font-size: small">
                  - Please refer to upgradeprofile for equivalent fields.
                </div>
                                <div style="font-size: small">
                  - Field deprecated in 31.1.1.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 18.2.10, 20.1.1.
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
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> upgrade_lease_time </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Amount of time controller waits for a regular-sized se (<128gb memory) to reconnect after it is rebooted during upgrade.
                </div>
                                <div style="font-size: small">
                  - Starting 18.2.10/20.1.1, the default time has increased from 360 seconds to 600 seconds.
                </div>
                                <div style="font-size: small">
                  - Please refer to upgradeprofile for equivalent fields.
                </div>
                                <div style="font-size: small">
                  - Field deprecated in 31.1.1.
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
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> upgrade_se_per_vs_scale_ops_txn_time </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - This parameter defines the upper-bound value of the vs scale-in or vs scale-out operation executed in the sescalein and sescale context.
                </div>
                                <div style="font-size: small">
                  - User can tweak this parameter to a higher value if the segroup gets suspended due to sescalein or sescaleout timeout failure typically associated
                </div>
                                <div style="font-size: small">
                  - with high number of vs(es) scaled out.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 18.2.10, 20.1.1.
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
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> user_agent_cache_config </b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Configuration for user-agent cache used in bot management.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 21.1.1.
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
                    <b> uuid </b>
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
                    <b> vnic_op_fail_time </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
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
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> vs_apic_scaleout_timeout </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Time to wait for the scaled out se to become ready before marking the scaleout done, applies to apic configuration only.
                </div>
                                <div style="font-size: small">
                  - Field deprecated in 21.1.1.
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
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> vs_awaiting_se_timeout </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
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
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> vs_key_rotate_period </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Period for rotate vs keys job.
                </div>
                                <div style="font-size: small">
                  - Allowed values are 1-1051200.
                </div>
                                <div style="font-size: small">
                  - Special values are 0 - disabled.
                </div>
                                <div style="font-size: small">
                  - Unit is min.
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
                    <b> vs_scaleout_ready_check_interval </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Interval for checking scaleout_ready status while controller is waiting for scaleoutready rpc from the service engine.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 18.2.2.
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
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> vs_se_attach_ip_fail </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Time to wait before marking attach ip operation on an se as failed.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 17.2.2.
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
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> vs_se_bootup_fail </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
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
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> vs_se_bootup_fail_patch </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Wait for longer for patch ses to boot up.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 30.2.1.
                </div>
                                <div style="font-size: small">
                  - Unit is sec.
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
                    <b> vs_se_create_fail </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
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
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> vs_se_ping_fail </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
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
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> vs_se_vnic_fail </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
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
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> vs_se_vnic_ip_fail </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
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
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> vsphere_ha_detection_timeout </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Vsphere ha monitor detection timeout.
                </div>
                                <div style="font-size: small">
                  - If vsphere_ha_enabled is true and the controller is not able to reach the se, placement will wait for this duration for vsphere_ha_inprogress to
                </div>
                                <div style="font-size: small">
                  - be marked true before taking corrective action.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 20.1.7, 21.1.3.
                </div>
                                <div style="font-size: small">
                  - Unit is sec.
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
                    <b> vsphere_ha_recovery_timeout </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Vsphere ha monitor recovery timeout.
                </div>
                                <div style="font-size: small">
                  - Once vsphere_ha_inprogress is set to true (meaning host failure detected and vsphere ha will recover the service engine), placement will wait for
                </div>
                                <div style="font-size: small">
                  - at least this duration for the se to reconnect to the controller before taking corrective action.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 20.1.7, 21.1.3.
                </div>
                                <div style="font-size: small">
                  - Unit is sec.
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
                    <b> vsphere_ha_timer_interval </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Vsphere ha monitor timer interval for sending cc_check_se_status to cloud connector.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 20.1.7, 21.1.3.
                </div>
                                <div style="font-size: small">
                  - Unit is sec.
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
                    <b> warmstart_se_reconnect_wait_time </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
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
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> warmstart_vs_resync_wait_time </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Timeout for warmstart vs resync.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 18.1.4, 18.2.1.
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
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> flavor_props </b>
                    <div style="font-size: small">
                                                    <span style="color: purple">list / elements=dictionary </span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Flavor properties specific to this cloud type.
                </div>
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
                    <b> cost </b>
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
                    <b> disk_gb </b>
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
                    <b> enhanced_nw </b>
                    <div style="font-size: small">
                        <span style="color: purple">bool</span>
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
                    <b> id </b>
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
                    <b> is_recommended </b>
                    <div style="font-size: small">
                        <span style="color: purple">bool</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - If a vm flavor is recommended for requested se_usage_type.set to true if the chosen vm flavor is recommended for requested se_usage_type.else set
                </div>
                                <div style="font-size: small">
                  - to false.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 18.1.4, 18.2.1.
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
                    <b> max_ip6s_per_nic </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Maximum number of ipv6 addresses that can be configured per nic.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 18.1.1.
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
                    <b> max_ips_per_nic </b>
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
                    <b> max_nics </b>
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
                    <b> meta </b>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
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
                    <b> name </b>
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
                    <b> public </b>
                    <div style="font-size: small">
                        <span style="color: purple">bool</span>
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
                    <b> ram_mb </b>
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
                    <b> vcpus </b>
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
                    <b> flavor_regex_filter </b>
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
                    <b> htypes </b>
                    <div style="font-size: small">
                                                    <span style="color: purple">list / elements=string </span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Supported hypervisors.
                </div>
                                <div style="font-size: small">
                  - Enum options - DEFAULT, VMWARE_ESX, KVM, VMWARE_VSAN, XEN.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                            <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> vtype </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Cloud type.
                </div>
                                <div style="font-size: small">
                  - Enum options - CLOUD_NONE, CLOUD_VCENTER, CLOUD_OPENSTACK, CLOUD_AWS, CLOUD_VCA, CLOUD_APIC, CLOUD_MESOS, CLOUD_LINUXSERVER, CLOUD_DOCKER_UCP,
                </div>
                                <div style="font-size: small">
                  - CLOUD_RANCHER, CLOUD_OSHIFT_K8S, CLOUD_AZURE, CLOUD_GCP, CLOUD_NSXT.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
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
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
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
        - name: Example to create CloudProperties object
          avi_cloudproperties:
            avi_credentials: "{{ avi_credentials }}"
            state: present
            name: sample_cloudproperties


Authors
~~~~~~~
- Gaurav Rastogi (grastogi@vmware.com)
- Sandeep Bandi (sbandi@vmware.com)
- Amol Shinde (samol@vmware.com)



