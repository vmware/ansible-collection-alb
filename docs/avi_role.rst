.. vmware.alb.avi_role:


**********************************************
vmware.alb.avi_role
**********************************************

**Module for setup of Role Avi RESTful Object**


.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module is used to configure Role object.
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
                <b>allow_unlabelled_access</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Allow access to unlabelled objects.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 20.1.5.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as True.
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
                <b>filters</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Filters for granular object access control based on object labels.
                </div>
                                <div style="font-size: small">
                  - Multiple filters are merged using the and operator.
                </div>
                                <div style="font-size: small">
                  - If empty, all objects according to the privileges will be accessible to the user.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 20.1.3.
                </div>
                                <div style="font-size: small">
                  - Maximum of 4 items allowed.
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
                    <b> enabled </b>
                    <div style="font-size: small">
                                                <span style="color: purple">bool</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Enable this filter.
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
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> match_label </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Label key to match against objects for values.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 20.1.3.
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
                    <b> key </b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
            </td>
            <td></td>
            <td></td>
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
            <td class="elbow-placeholder"></td>
            <td collspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> values </b>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                    </div>
            </td>
            <td></td>
            <td></td>
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
                                    <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> match_operation </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Label match operation criteria.
                </div>
                                <div style="font-size: small">
                  - Enum options - ROLE_FILTER_EQUALS, ROLE_FILTER_DOES_NOT_EQUAL, ROLE_FILTER_GLOB_MATCH, ROLE_FILTER_GLOB_DOES_NOT_MATCH.
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
                  - Name for the filter.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 20.1.3.
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
                                <div style="font-size: small">
                <b>required: true</b>
                </div>
                            </td>
            <td>
                                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
        </tr>
                        <tr>
            <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>privileges</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
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
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> resource </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Enum options - PERMISSION_CONTROLLER, PERMISSION_INTERNAL, PERMISSION_VIRTUALSERVICE, PERMISSION_POOL, PERMISSION_HEALTHMONITOR,
                </div>
                                <div style="font-size: small">
                  - PERMISSION_NETWORKPROFILE, PERMISSION_APPLICATIONPROFILE, PERMISSION_HTTPPOLICYSET, PERMISSION_IPADDRGROUP, PERMISSION_STRINGGROUP,
                </div>
                                <div style="font-size: small">
                  - PERMISSION_SSLPROFILE, PERMISSION_SSLKEYANDCERTIFICATE, PERMISSION_NETWORKSECURITYPOLICY, PERMISSION_APPLICATIONPERSISTENCEPROFILE,
                </div>
                                <div style="font-size: small">
                  - PERMISSION_ANALYTICSPROFILE, PERMISSION_VSDATASCRIPTSET, PERMISSION_TENANT, PERMISSION_PKIPROFILE, PERMISSION_AUTHPROFILE, PERMISSION_CLOUD...
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                            <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> subresource </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Limits the scope of write access on the parent resource to modification of only the specified subresources.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 20.1.5.
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
                    <b> exclude_subresources </b>
                    <div style="font-size: small">
                        <span style="color: purple">bool</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Allows modification of all fields except for the specified subresources.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 20.1.5.
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
                    <b> subresources </b>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Subresources user can modify.
                </div>
                                <div style="font-size: small">
                  - Each subresource specifies and individual field.
                </div>
                                <div style="font-size: small">
                  - I.e.
                </div>
                                <div style="font-size: small">
                  - Subresource_pool_enabled allows modification of the enabled field in the pool object.
                </div>
                                <div style="font-size: small">
                  - Enum options - SUBRESOURCE_POOL_ENABLED, SUBRESOURCE_POOL_SERVERS, SUBRESOURCE_POOL_SERVER_ENABLED, SUBRESOURCE_VIRTUALSERVICE_ENABLED,
                </div>
                                <div style="font-size: small">
                  - SUBRESOURCE_VIRTUALSERVICE_AUTO_ALLOCATE_FLOATING_IP, SUBRESOURCE_GSLBSERVICE_ENABLED, SUBRESOURCE_GSLBSERVICE_GROUPS,
                </div>
                                <div style="font-size: small">
                  - SUBRESOURCE_GSLBSERVICE_GROUP_ENABLED, SUBRESOURCE_GSLBSERVICE_GROUP_MEMBERS, SUBRESOURCE_GSLBSERVICE_GROUP_MEMBER_ENABLED.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 20.1.5.
                </div>
                                <div style="font-size: small">
                  - Minimum of 1 items required.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, enterprise with cloud services edition.
                </div>
                                            </td>     
        </tr>
                                    <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> type </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Enum options - NO_ACCESS, READ_ACCESS, WRITE_ACCESS.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
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
                  - It is a reference to an object of type tenant.
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
        - name: Example to create Role object
          avi_role:
            avi_credentials: "{{ avi_credentials }}"
            state: present
            name: sample_role


Authors
~~~~~~~
- Gaurav Rastogi (grastogi@vmware.com)
- Sandeep Bandi (sbandi@vmware.com)
- Amol Shinde (samol@vmware.com)



