
.. vmware.alb.avi_trafficcloneprofile:


**********************************************
vmware.alb.avi_trafficcloneprofile
**********************************************

**Module for setup of TrafficCloneProfile Avi RESTful Object**


.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module is used to configure TrafficCloneProfile object.
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
                <b>clone_servers</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">list / elements=dictionary </span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Field introduced in 17.1.1.
                </div>
                                <div style="font-size: small">
                  - Maximum of 10 items allowed.
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
                <b>ip_address</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                            <span style="color: purple">dict / elements=dictionary </span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Ip address of the clone server.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 17.1.1.
                </div>
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
                <b>addr</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Ip address.
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
                <b>type</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Enum options - V4, DNS, V6.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
        
                                        <td class="elbow-placeholder"></td>
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>mac</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Mac address of the clone server.
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
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>network_ref</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Network to clone the traffic to.
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type network.
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
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>subnet</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                            <span style="color: purple">dict / elements=dictionary </span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Subnet of the network to clone the traffic to.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 17.1.1.
                </div>
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
                <b>ip_addr</b>
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
                <b>addr</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Ip address.
                </div>
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
                <b>type</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Enum options - V4, DNS, V6.
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
                <b>mask</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">int</span>
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
                <b>cloud_ref</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - It is a reference to an object of type cloud.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 17.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
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
                <b>markers</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">list / elements=dictionary </span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - List of labels to be used for granular rbac.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 20.1.5.
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
                <b>key</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Key for filter match.
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
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>values</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">list / elements=string </span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Values for filter match.
                </div>
                                <div style="font-size: small">
                  - Multiple values will be evaluated as or.
                </div>
                                <div style="font-size: small">
                  - Example  key = value1 or key = value2.
                </div>
                                <div style="font-size: small">
                  - Behavior for match is key = * if this field is empty.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 20.1.3.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, enterprise with cloud services edition.
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
                  - Name for the traffic clone profile.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 17.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                                            <td colspan="7">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>preserve_client_ip</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">bool</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Specifies if client ip needs to be preserved to clone destination.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 17.1.1.
                </div>
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
                  - Field introduced in 17.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
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
                  - Uuid of the traffic clone profile.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 17.1.1.
                </div>
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
      connection: local
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
        - name: Example to create TrafficCloneProfile object
          avi_trafficcloneprofile:
            avi_credentials: "{{ avi_credentials }}"
            state: present
            name: sample_trafficcloneprofile


Authors
~~~~~~~
- Anurag Palsule (anurag.palsule@broadcom.com)
- Parikshit Manur (parikshit.manur@broadcom.com)
- Rohan Suryavanshi (rohan.suryavanshi@broadcom.com)
