
.. vmware.alb.avi_alertsyslogconfig:


**********************************************
vmware.alb.avi_alertsyslogconfig
**********************************************

**Module for setup of AlertSyslogConfig Avi RESTful Object**


.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module is used to configure AlertSyslogConfig object.
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
                  - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
                </div>
                                <div style="font-size: small">
                  - edition.
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
                  - Protobuf version number.
                </div>
                                <div style="font-size: small">
                  - Gets incremented if there is se diff of federated diff in config pbs.this field will be a monotonically increasing number indicating the number
                </div>
                                <div style="font-size: small">
                  - of config update operations.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 21.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
                </div>
                                <div style="font-size: small">
                  - edition.
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
                  - User defined description for alert syslog config.
                </div>
                                <div style="font-size: small">
                  - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
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
                  - A user-friendly name of the syslog notification.
                </div>
                                <div style="font-size: small">
                  - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                                            <td colspan="7">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>sender_hostname</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - User defined sender hostname in syslog message.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 30.2.1.
                </div>
                                <div style="font-size: small">
                  - Allowed in enterprise edition with any value, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                                            <td colspan="7">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>syslog_servers</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">list / elements=dictionary </span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - The list of syslog servers.
                </div>
                                <div style="font-size: small">
                  - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                <tr>
                                    <td class="elbow-placeholder"></td>
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>anon_auth</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">bool</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Enable anonymous authentication of syslog serverwhich will disable server certificate authentication.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 17.2.17, 18.2.5.
                </div>
                                <div style="font-size: small">
                  - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as False.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>format</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Syslog output format - legacy, rfc 5424, json.
                </div>
                                <div style="font-size: small">
                  - Enum options - SYSLOG_LEGACY, SYSLOG_RFC5424, SYSLOG_JSON, SYSLOG_RFC5425_ENHANCED.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 17.2.8.
                </div>
                                <div style="font-size: small">
                  - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as SYSLOG_LEGACY.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>pkiprofile_ref</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Select the pkiprofile containing a ca or list of ca chainswhich will validate the certificate of the syslog server.
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type pkiprofile.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 17.2.17, 18.2.5.
                </div>
                                <div style="font-size: small">
                  - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>ssl_key_and_certificate_ref</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Select a certificate and key which will be used to authenticate to the syslog server.
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type sslkeyandcertificate.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 17.2.17, 18.2.5.
                </div>
                                <div style="font-size: small">
                  - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>strict_cert_verify</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">bool</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Strict verificiation of certificate given by the server.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 30.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed in enterprise edition with any value, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as False.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>syslog_server</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - The destination syslog server ip(v4/v6) address or fqdn.
                </div>
                                <div style="font-size: small">
                  - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>syslog_server_port</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">int</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - The destination syslog server's service port.
                </div>
                                <div style="font-size: small">
                  - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as 514.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>tls_enable</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">bool</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Enable tls to the syslog server.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 17.2.16, 18.2.3.
                </div>
                                <div style="font-size: small">
                  - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as False.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>udp</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">bool</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Network protocol to establish syslog session.
                </div>
                                <div style="font-size: small">
                  - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as True.
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
                  - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
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
                  - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
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
          username: "{{ username }}"
          password: "{{ password }}"
          controller: "{{ controller }}"
          api_version: "{{ api_version }}"
          tenant: "{{ admin }}"
      tasks:        
        - name: Create Alert Syslog object to forward all events to external syslog server
          avi_alertsyslogconfig:
            avi_credentials: "{{ avi_credentials }}"
            name: Roberts-syslog
            syslog_servers:
            - syslog_server: 192.168.15.11
              syslog_server_port: 514
              udp: true
            tenant_ref: /api/tenant?name=admin



Authors
~~~~~~~
- Anurag Palsule (anurag.palsule@broadcom.com)
- Parikshit Manur (parikshit.manur@broadcom.com)
- Rohan Suryavanshi (rohan.suryavanshi@broadcom.com)
