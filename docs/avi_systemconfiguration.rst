.. vmware.alb.avi_systemconfiguration:


**********************************************
vmware.alb.avi_systemconfiguration
**********************************************

**Module for setup of SystemConfiguration Avi RESTful Object**


.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module is used to configure SystemConfiguration object.
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
                <b>admin_auth_configuration</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
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
                    <b> allow_local_user_login </b>
                    <div style="font-size: small">
                                                <span style="color: purple">bool</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Allow any user created locally to login with local credentials.
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
                    <b> alternate_auth_configurations </b>
                    <div style="font-size: small">
                                                    <span style="color: purple">list / elements=dictionary </span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Secondary authentication mechanisms to be used.
                </div>
                                <div style="font-size: small">
                  - Field deprecated in 22.1.1.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 20.1.6.
                </div>
                                <div style="font-size: small">
                  - Maximum of 1 items allowed.
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
                    <b> auth_profile_ref </b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Uuid of the authprofile.
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type authprofile.
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
                    <b> index </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Index used for maintaining order of alternateauthconfiguration.
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
                    <b> mapping_rules </b>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Rules list for tenant or role mapping.
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
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> auth_profile_ref </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - It is a reference to an object of type authprofile.
                </div>
                                <div style="font-size: small">
                  - Field deprecated in 22.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                            <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> mapping_rules </b>
                    <div style="font-size: small">
                                                    <span style="color: purple">list / elements=dictionary </span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Rules list for tenant or role mapping.
                </div>
                                <div style="font-size: small">
                  - Field deprecated in 22.1.1.
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
                    <b> assign_policy </b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Assignment rule for the object access policy.
                </div>
                                <div style="font-size: small">
                  - Enum options - ASSIGN_ALL, ASSIGN_FROM_SELECT_LIST, ASSIGN_MATCHING_GROUP_NAME, ASSIGN_MATCHING_ATTRIBUTE_VALUE, ASSIGN_MATCHING_GROUP_REGEX,
                </div>
                                <div style="font-size: small">
                  - ASSIGN_MATCHING_ATTRIBUTE_REGEX, ASSIGN_CONFIG_CONTAINS_ATTRIBUTE_VALUE.
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
                    <b> assign_role </b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Enum options - ASSIGN_ALL, ASSIGN_FROM_SELECT_LIST, ASSIGN_MATCHING_GROUP_NAME, ASSIGN_MATCHING_ATTRIBUTE_VALUE, ASSIGN_MATCHING_GROUP_REGEX,
                </div>
                                <div style="font-size: small">
                  - ASSIGN_MATCHING_ATTRIBUTE_REGEX, ASSIGN_CONFIG_CONTAINS_ATTRIBUTE_VALUE.
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
                    <b> assign_tenant </b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Enum options - ASSIGN_ALL, ASSIGN_FROM_SELECT_LIST, ASSIGN_MATCHING_GROUP_NAME, ASSIGN_MATCHING_ATTRIBUTE_VALUE, ASSIGN_MATCHING_GROUP_REGEX,
                </div>
                                <div style="font-size: small">
                  - ASSIGN_MATCHING_ATTRIBUTE_REGEX, ASSIGN_CONFIG_CONTAINS_ATTRIBUTE_VALUE.
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
                    <b> assign_userprofile </b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Assignment rule for the user account profile.
                </div>
                                <div style="font-size: small">
                  - Enum options - ASSIGN_ALL, ASSIGN_FROM_SELECT_LIST, ASSIGN_MATCHING_GROUP_NAME, ASSIGN_MATCHING_ATTRIBUTE_VALUE, ASSIGN_MATCHING_GROUP_REGEX,
                </div>
                                <div style="font-size: small">
                  - ASSIGN_MATCHING_ATTRIBUTE_REGEX, ASSIGN_CONFIG_CONTAINS_ATTRIBUTE_VALUE.
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
                    <b> attribute_match </b>
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
                    <b> default_tenant_ref </b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Default tenant ref to assign to user.
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type tenant.
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
                    <b> group_match </b>
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
                    <b> index </b>
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
                    <b> is_superuser </b>
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
                    <b> object_access_policy_refs </b>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Object access policies to assign to user on successful match.
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type objectaccesspolicy.
                </div>
                                <div style="font-size: small">
                  - Field deprecated in 20.1.2.
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
                    <b> policy_attribute_name </b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Attribute name for object access policy assignment.
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
                    <b> role_attribute_name </b>
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
                    <b> role_refs </b>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - It is a reference to an object of type role.
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
                    <b> tenant_attribute_name </b>
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
                    <b> tenant_refs </b>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - It is a reference to an object of type tenant.
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
                    <b> userprofile_attribute_name </b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Attribute name for user account profile assignment.
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
                    <b> userprofile_ref </b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - User account profile to assign to user on successful match.
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type useraccountprofile.
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
                    <b> remote_auth_configurations </b>
                    <div style="font-size: small">
                                                    <span style="color: purple">list / elements=dictionary </span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Remote auth configurations.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 22.1.1.
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
                    <b> auth_mapping_profile_ref </b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Uuid of the authmappingprofile(set of auth mapping rules) to be assigned to a user on successful match.
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type authmappingprofile.
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
                    <b> auth_profile_ref </b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Uuid of the auth profile.
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type authprofile.
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
                    <b> index </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Index used for maintaining order of remoteauthconfiguration.
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
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> service_auth_configurations </b>
                    <div style="font-size: small">
                                                    <span style="color: purple">list / elements=dictionary </span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Service auth configurations.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 30.1.1.
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
                    <b> index </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Index used for maintaining order of serviceauthconfiguration.
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
                    <b> service_auth_mapping_profile_ref </b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Uuid of the authmappingprofile(set of auth mapping rules) to be assigned to a user on successful match.
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type authmappingprofile.
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
                    <b> service_auth_profile_ref </b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Uuid of the service auth profile.
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type serviceauthprofile.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 30.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, enterprise with cloud services edition.
                </div>
                                            </td>     
        </tr>
                                                <tr>
            <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>common_criteria_mode</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Common criteria mode's current state.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 20.1.3.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as False.
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
                <b>controller_analytics_policy</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Controller metrics event dynamic thresholds can be set here.
                </div>
                                <div style="font-size: small">
                  - Controller_cpu_high and controller_mem_high evets can take configured dynamic thresholds.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 21.1.3.
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
                    <b> metrics_event_thresholds </b>
                    <div style="font-size: small">
                                                    <span style="color: purple">list / elements=dictionary </span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Thresholds for various events generated by metrics system.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 21.1.3.
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
                    <b> metrics_event_threshold_type </b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Type of the metrics event threshold.
                </div>
                                <div style="font-size: small">
                  - This value will decide which metric rule (or rules) use configured thresholds.
                </div>
                                <div style="font-size: small">
                  - Enum options - THRESHOLD_TYPE_STATIC, SE_CPU_THRESHOLD, SE_MEM_THRESHOLD, SE_DISK_THRESHOLD, CONTROLLER_CPU_THRESHOLD, CONTROLLER_MEM_THRESHOLD,
                </div>
                                <div style="font-size: small">
                  - CONTROLLER_DISK_THRESHOLD.
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
                    <b> reset_threshold </b>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - This value is used to reset the event state machine.
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
                    <b> watermark_thresholds </b>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Threshold value for which event in raised.
                </div>
                                <div style="font-size: small">
                  - There can be multiple thresholds defined.health score degrades when the the target is higher than this threshold.
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
                                                <tr>
            <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>default_license_tier</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Specifies the default license tier which would be used by new clouds.
                </div>
                                <div style="font-size: small">
                  - Enum options - ENTERPRISE_16, ENTERPRISE, ENTERPRISE_18, BASIC, ESSENTIALS, ENTERPRISE_WITH_CLOUD_SERVICES.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 17.2.5.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Special default for essentials edition is essentials, basic edition is basic, enterprise edition is enterprise_with_cloud_services.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as ENTERPRISE_WITH_CLOUD_SERVICES.
                </div>
                                            </td>
        </tr>
                        <tr>
            <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>dns_configuration</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
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
                    <b> search_domain </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Search domain to use in dns lookup, multiple domains must be delimited by space only.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                            <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> server_list </b>
                    <div style="font-size: small">
                                                    <span style="color: purple">list / elements=dictionary </span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - List of dns server ip(v4/v6) addresses or fqdns.
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
                    <b> addr </b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
            </td>
            <td></td>
            <td></td>
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
                  - Enum options - V4, DNS, V6.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>     
        </tr>
                                                <tr>
            <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>dns_virtualservice_refs</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Dns virtualservices hosting fqdn records for applications across avi vantage.
                </div>
                                <div style="font-size: small">
                  - If no virtualservices are provided, avi vantage will provide dns services for configured applications.
                </div>
                                <div style="font-size: small">
                  - Switching back to avi vantage from dns virtualservices is not allowed.
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type virtualservice.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, enterprise with cloud services edition.
                </div>
                                            </td>
        </tr>
                        <tr>
            <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>docker_mode</b>
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
                        <tr>
            <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>email_configuration</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
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
                    <b> auth_password </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Password for mail server.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                            <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> auth_username </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Username for mail server.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                            <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> disable_tls </b>
                    <div style="font-size: small">
                                                <span style="color: purple">bool</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - When set, disables tls on the connection to the mail server.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 17.2.12, 18.1.3, 18.2.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                            <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> email_timezone </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Timezone for timestamps in alert emails.
                </div>
                                <div style="font-size: small">
                  - Enum options - UTC, AFRICA_ABIDJAN, AFRICA_ACCRA, AFRICA_ADDIS_ABABA, AFRICA_ALGIERS, AFRICA_ASMARA, AFRICA_ASMERA, AFRICA_BAMAKO, AFRICA_BANGUI,
                </div>
                                <div style="font-size: small">
                  - AFRICA_BANJUL, AFRICA_BISSAU, AFRICA_BLANTYRE, AFRICA_BRAZZAVILLE, AFRICA_BUJUMBURA, AFRICA_CAIRO, AFRICA_CASABLANCA, AFRICA_CEUTA,
                </div>
                                <div style="font-size: small">
                  - AFRICA_CONAKRY, AFRICA_DAKAR, AFRICA_DAR_ES_SALAAM...
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
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> from_email </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Email address in from field.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                            <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> from_name </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Friendly name in from field.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 21.1.4, 22.1.3.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                            <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> mail_server_name </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Mail server fqdn or ip(v4/v6) address.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                            <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> mail_server_port </b>
                    <div style="font-size: small">
                                                <span style="color: purple">integer</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Mail server port.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                            <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> smtp_type </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Type of smtp mail service.
                </div>
                                <div style="font-size: small">
                  - Enum options - SMTP_NONE, SMTP_LOCAL_HOST, SMTP_SERVER, SMTP_ANONYMOUS_SERVER.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                                        <tr>
            <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>enable_cors</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Enable cors header.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 20.1.3.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as False.
                </div>
                                            </td>
        </tr>
                        <tr>
            <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>enable_host_header_check</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Validates the host header against a list of trusted domains.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 31.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as False.
                </div>
                                            </td>
        </tr>
                        <tr>
            <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>fips_mode</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Fips mode current state.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 20.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as False.
                </div>
                                            </td>
        </tr>
                        <tr>
            <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>global_tenant_config</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
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
                    <b> se_in_provider_context </b>
                    <div style="font-size: small">
                                                <span style="color: purple">bool</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Controls the ownership of serviceengines.
                </div>
                                <div style="font-size: small">
                  - Service engines can either be exclusively owned by each tenant or owned by the administrator and shared by all tenants.
                </div>
                                <div style="font-size: small">
                  - When serviceengines are owned by the administrator, each tenant can have either read access or no access to their service engines.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                            <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> tenant_access_to_provider_se </b>
                    <div style="font-size: small">
                                                <span style="color: purple">bool</span>
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
                    <b> tenant_vrf </b>
                    <div style="font-size: small">
                                                <span style="color: purple">bool</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - When 'per tenant ip domain' is selected, each tenant gets its own routing domain that is not shared with any other tenant.
                </div>
                                <div style="font-size: small">
                  - When 'share ip domain across all tenants' is selected, all tenants share the same routing domain.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                                        <tr>
            <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>host_key_algorithm_exclude</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Users can specify comma separated list of deprecated host key algorithm.if nothing is specified, all known algorithms provided by openssh will be
                </div>
                                <div style="font-size: small">
                  - supported.this change could only apply on the controller node.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 22.1.3.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
        </tr>
                        <tr>
            <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>kex_algorithm_exclude</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Users can specify comma separated list of deprecated key exchange algorithm.if nothing is specified, all known algorithms provided by openssh
                </div>
                                <div style="font-size: small">
                  - will be supported.this change could only apply on the controller node.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 22.1.3.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
        </tr>
                        <tr>
            <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>legacy_ssl_support</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Allow outgoing connections from controller to servers using tls 1.0/1.1.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 31.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as False.
                </div>
                                            </td>
        </tr>
                        <tr>
            <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>linux_configuration</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
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
                    <b> banner </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Banner displayed before login to ssh, and ui.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                            <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> cis_mode </b>
                    <div style="font-size: small">
                                                <span style="color: purple">bool</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Enforce cis benchmark recommendations for avi controller and service engines.
                </div>
                                <div style="font-size: small">
                  - The enforcement is as per cis dil 1.0.1 level 2, for applicable controls.
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
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> motd </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Message of the day, shown to users on login via the command line interface, web interface, or ssh.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                                        <tr>
            <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>mgmt_ip_access_control</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Configure ip access control for controller to restrict open access.
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
                    <b> api_access </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Configure ip addresses to access controller using api.
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
                    <b> addrs </b>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Ip address(es).
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
                    <b> group_refs </b>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Uuid of ip address group(s).
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type ipaddrgroup.
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
                    <b> match_criteria </b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Criterion to use for ip address matching the http request.
                </div>
                                <div style="font-size: small">
                  - Enum options - IS_IN, IS_NOT_IN.
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
                    <b> prefixes </b>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Ip address prefix(es).
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
                    <b> ranges </b>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Ip address range(s).
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>     
        </tr>
                                    <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> shell_server_access </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Configure ip addresses to access controller using cli shell.
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
                    <b> addrs </b>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Ip address(es).
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
                    <b> group_refs </b>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Uuid of ip address group(s).
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type ipaddrgroup.
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
                    <b> match_criteria </b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Criterion to use for ip address matching the http request.
                </div>
                                <div style="font-size: small">
                  - Enum options - IS_IN, IS_NOT_IN.
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
                    <b> prefixes </b>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Ip address prefix(es).
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
                    <b> ranges </b>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Ip address range(s).
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>     
        </tr>
                                    <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> snmp_access </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Configure ip addresses to access controller using snmp.
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
                    <b> addrs </b>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Ip address(es).
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
                    <b> group_refs </b>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Uuid of ip address group(s).
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type ipaddrgroup.
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
                    <b> match_criteria </b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Criterion to use for ip address matching the http request.
                </div>
                                <div style="font-size: small">
                  - Enum options - IS_IN, IS_NOT_IN.
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
                    <b> prefixes </b>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Ip address prefix(es).
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
                    <b> ranges </b>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Ip address range(s).
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>     
        </tr>
                                    <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> ssh_access </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Configure ip addresses to access controller using ssh.
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
                    <b> addrs </b>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Ip address(es).
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
                    <b> group_refs </b>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Uuid of ip address group(s).
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type ipaddrgroup.
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
                    <b> match_criteria </b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Criterion to use for ip address matching the http request.
                </div>
                                <div style="font-size: small">
                  - Enum options - IS_IN, IS_NOT_IN.
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
                    <b> prefixes </b>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Ip address prefix(es).
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
                    <b> ranges </b>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Ip address range(s).
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>     
        </tr>
                                    <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> sysint_access </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Configure ip addresses to access controller using sysint access.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 18.1.3, 18.2.1.
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
                    <b> addrs </b>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Ip address(es).
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
                    <b> group_refs </b>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Uuid of ip address group(s).
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type ipaddrgroup.
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
                    <b> match_criteria </b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Criterion to use for ip address matching the http request.
                </div>
                                <div style="font-size: small">
                  - Enum options - IS_IN, IS_NOT_IN.
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
                    <b> prefixes </b>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Ip address prefix(es).
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
                    <b> ranges </b>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Ip address range(s).
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>     
        </tr>
                                                <tr>
            <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>ntp_configuration</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
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
                    <b> ntp_authentication_keys </b>
                    <div style="font-size: small">
                                                    <span style="color: purple">list / elements=dictionary </span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Ntp authentication keys.
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
                    <b> algorithm </b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Message digest algorithm used for ntp authentication.
                </div>
                                <div style="font-size: small">
                  - Default is ntp_auth_algorithm_md5.
                </div>
                                <div style="font-size: small">
                  - Enum options - NTP_AUTH_ALGORITHM_MD5, NTP_AUTH_ALGORITHM_SHA1.
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
                    <b> key </b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Ntp authentication key.
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
                    <b> key_number </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Key number to be assigned to the authentication-key.
                </div>
                                <div style="font-size: small">
                  - Allowed values are 1-65534.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>     
        </tr>
                                    <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> ntp_server_list </b>
                    <div style="font-size: small">
                                                    <span style="color: purple">list / elements=dictionary </span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - List of ntp server fqdns or ip(v4/v6) addresses.
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
                    <b> addr </b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
            </td>
            <td></td>
            <td></td>
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
                  - Enum options - V4, DNS, V6.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>     
        </tr>
                                    <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> ntp_servers </b>
                    <div style="font-size: small">
                                                    <span style="color: purple">list / elements=dictionary </span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - List of ntp servers.
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
                    <b> key_number </b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Key number from the list of trusted keys used to authenticate this server.
                </div>
                                <div style="font-size: small">
                  - Allowed values are 1-65534.
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
                    <b> server </b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Ip address of the ntp server.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>     
        </tr>
                                                <tr>
            <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>portal_configuration</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
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
                    <b> allow_basic_authentication </b>
                    <div style="font-size: small">
                                                <span style="color: purple">bool</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Enable/disable http basic authentication.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                            <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> api_force_timeout </b>
                    <div style="font-size: small">
                                                <span style="color: purple">integer</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Force api session timeout after the specified time (in hours).
                </div>
                                <div style="font-size: small">
                  - Allowed values are 1-24.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 18.2.3.
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
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> disable_remote_cli_shell </b>
                    <div style="font-size: small">
                                                <span style="color: purple">bool</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Disable remote cli shell client access.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                            <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> disable_swagger </b>
                    <div style="font-size: small">
                                                <span style="color: purple">bool</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Disable swagger access.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 18.2.3.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                            <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> enable_clickjacking_protection </b>
                    <div style="font-size: small">
                                                <span style="color: purple">bool</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Enable/disable clickjacking protection.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                            <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> enable_http </b>
                    <div style="font-size: small">
                                                <span style="color: purple">bool</span>
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
                    <b> enable_https </b>
                    <div style="font-size: small">
                                                <span style="color: purple">bool</span>
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
                    <b> http_port </b>
                    <div style="font-size: small">
                                                <span style="color: purple">integer</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Http port.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                            <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> https_port </b>
                    <div style="font-size: small">
                                                <span style="color: purple">integer</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Https port.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                            <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> legacy_ssl_support </b>
                    <div style="font-size: small">
                                                <span style="color: purple">bool</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Allow incoming connections from clients using tls 1.0/1.1 to controller.
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
                    <b> minimum_password_length </b>
                    <div style="font-size: small">
                                                <span style="color: purple">integer</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Minimum password length for user accounts.
                </div>
                                <div style="font-size: small">
                  - Allowed values are 6-32.
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
                    <b> password_strength_check </b>
                    <div style="font-size: small">
                                                <span style="color: purple">bool</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Strict checking of password strength for user accounts.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                            <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> pkiprofile_ref </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Reference to pkiprofile config used for crl validation.
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type pkiprofile.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 30.1.2.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                            <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> redirect_to_https </b>
                    <div style="font-size: small">
                                                <span style="color: purple">bool</span>
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
                    <b> sslkeyandcertificate_refs </b>
                    <div style="font-size: small">
                                                    <span style="color: purple">list / elements=string </span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Certificates for system portal.
                </div>
                                <div style="font-size: small">
                  - Maximum 2 allowed.
                </div>
                                <div style="font-size: small">
                  - Leave list empty to use system default certs.
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type sslkeyandcertificate.
                </div>
                                <div style="font-size: small">
                  - Maximum of 2 items allowed.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                            <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> sslprofile_ref </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - It is a reference to an object of type sslprofile.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                            <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> use_uuid_from_input </b>
                    <div style="font-size: small">
                                                <span style="color: purple">bool</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Use uuid in post object data as uuid of the new object, instead of a generated uuid.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                                        <tr>
            <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>proxy_configuration</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
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
                    <b> host </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Proxy hostname or ip address.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                            <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> password </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Password for proxy.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                            <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> port </b>
                    <div style="font-size: small">
                                                <span style="color: purple">integer</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Proxy port.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                            <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> username </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Username for proxy.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                                        <tr>
            <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>rekey_time_limit</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Users can specify and update the time limit of rekeylimit in sshd_config.if nothing is specified, the default setting will be none.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 30.2.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as none.
                </div>
                                            </td>
        </tr>
                        <tr>
            <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>rekey_volume_limit</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Users can specify and update the size/volume limit of rekeylimit in sshd_config.if nothing is specified, the default setting will be default.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 30.2.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as default.
                </div>
                                            </td>
        </tr>
                        <tr>
            <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>sddcmanager_fqdn</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Fqdn of sddc manager in vcf responsible for management of this alb controller cluster.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 22.1.6,31.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
        </tr>
                        <tr>
            <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>secure_channel_configuration</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Configure secure channel properties.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 18.1.4, 18.2.1.
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
                    <b> bypass_secure_channel_must_checks </b>
                    <div style="font-size: small">
                                                <span style="color: purple">bool</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Boolean which allowed force update of secure channel certificate.
                </div>
                                <div style="font-size: small">
                  - Forced updating has been disallowed.
                </div>
                                <div style="font-size: small">
                  - Field deprecated in 18.2.8.
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
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> sslkeyandcertificate_refs </b>
                    <div style="font-size: small">
                                                    <span style="color: purple">list / elements=string </span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Certificate for secure channel.
                </div>
                                <div style="font-size: small">
                  - Leave list empty to use system default certs.
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type sslkeyandcertificate.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 18.1.4, 18.2.1.
                </div>
                                <div style="font-size: small">
                  - Maximum of 1 items allowed.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                                        <tr>
            <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>snmp_configuration</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
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
                    <b> community </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Community string for snmp v2c.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                            <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> large_trap_payload </b>
                    <div style="font-size: small">
                                                <span style="color: purple">bool</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Support for 4096 bytes trap payload.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 17.2.13,18.1.4,18.2.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                            <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> snmp_v3_config </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Snmp version 3 configuration.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 17.2.3.
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
                    <b> engine_id </b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Engine id of the avi controller snmp.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 17.2.3.
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
                    <b> user </b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Snmp ver 3 user definition.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 17.2.3.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>     
        </tr>
                                    <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> sys_contact </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Sets the syscontact in system mib.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                            <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> sys_location </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Sets the syslocation in system mib.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                            <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> version </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Snmp version support.
                </div>
                                <div style="font-size: small">
                  - V2 or v3.
                </div>
                                <div style="font-size: small">
                  - Enum options - SNMP_VER2, SNMP_VER3.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 17.2.3.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                                        <tr>
            <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>ssh_ciphers</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Allowed ciphers list for ssh to the management interface on the controller and service engines.
                </div>
                                <div style="font-size: small">
                  - If this is not specified, all the default ciphers are allowed.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
        </tr>
                        <tr>
            <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>ssh_hmacs</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Allowed hmac list for ssh to the management interface on the controller and service engines.
                </div>
                                <div style="font-size: small">
                  - If this is not specified, all the default hmacs are allowed.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
        </tr>
                        <tr>
            <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>telemetry_configuration</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Telemetry configuration.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 31.1.1.
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
                    <b> enable </b>
                    <div style="font-size: small">
                                                <span style="color: purple">bool</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Enables vmware customer experience improvement program ( ceip ).
                </div>
                                <div style="font-size: small">
                  - Field introduced in 31.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                            <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> url </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - The fqdn or ip address of the telemetry server.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 31.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                                        <tr>
            <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>trusted_host_profiles_refs</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Trusted host profiles for host header validation.
                </div>
                                <div style="font-size: small">
                  - Only works when host_header_check is set to true.
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type trustedhostprofile.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 31.1.1.
                </div>
                                <div style="font-size: small">
                  - Maximum of 20 items allowed.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, enterprise with cloud services edition.
                </div>
                                            </td>
        </tr>
                        <tr>
            <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>truststore_pkiprofile_ref</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Reference to pkiprofile used for validating the ca certificates for external comminications from avi load balancer controller  this acts as trust
                </div>
                                <div style="font-size: small">
                  - store for avi load balancer controller.
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type pkiprofile.
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
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
        </tr>
                        <tr>
            <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>welcome_workflow_complete</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - This flag is set once the initial controller setup workflow is complete.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 18.2.3.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as False.
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
          username: "{{ username }}"
          password: "{{ password }}"
          controller: "{{ controller }}"
          api_version: "{{ api_version }}"
      tasks:        
        - hosts: all
          vars:
            avi_credentials:
              username: "admin"
              password: "something"
              controller: "192.168.15.18"
              api_version: "21.1.1"
          tasks:
            - name: Example to create SystemConfiguration object
              vmware.alb.avi_systemconfiguration:
                avi_credentials: "{{ avi_credentials }}"
                state: present
                welcome_workflow_complete: True
                dns_configuration:
                  search_domain: ''
                  server_list:
                    - type: V4
                      addr: "8.8.8.8"
                    - type: DNS
                      addr: "dns.rainpole.com"



Authors
~~~~~~~
- Gaurav Rastogi (grastogi@vmware.com)
- Sandeep Bandi (sbandi@vmware.com)
- Amol Shinde (samol@vmware.com)



