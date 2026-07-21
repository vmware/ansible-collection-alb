
.. vmware.alb.avi_authprofile:


**********************************************
vmware.alb.avi_authprofile
**********************************************

**Module for setup of AuthProfile Avi RESTful Object**


.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module is used to configure AuthProfile object.
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
                <b>client_cert</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                            <span style="color: purple">dict / elements=dictionary </span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Client cert settings.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 32.1.1.
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
                <b>client_cert_refs</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">list / elements=string </span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Client certs to be used for authentication.
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type sslkeyandcertificate.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 32.1.1.
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
                <b>created_by</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Identifies the user type that created the configuration.
                </div>
                                <div style="font-size: small">
                  - Nil for non-service users.
                </div>
                                <div style="font-size: small">
                  - Enum options - SERVICE_USER.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 32.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
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
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                                            <td colspan="7">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>http</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                            <span style="color: purple">dict / elements=dictionary </span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Http user authentication params.
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
                <b>cache_expiration_time</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">int</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - The max allowed length of time a clients authentication is cached.
                </div>
                                <div style="font-size: small">
                  - Allowed values are 1-30.
                </div>
                                <div style="font-size: small">
                  - Unit is sec.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as 5.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>group_member_is_full_dn</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">bool</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Group member entries contain full dns instead of just user id attribute values.
                </div>
                                <div style="font-size: small">
                  - This should now be configured using the ldapdirectorysettings field instead.
                </div>
                                <div style="font-size: small">
                  - Field deprecated in 18.2.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>request_header</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Insert an http header.
                </div>
                                <div style="font-size: small">
                  - This field is used to define the header name.
                </div>
                                <div style="font-size: small">
                  - The value of the header is set to the client's http auth user id.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>require_user_groups</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">list / elements=string </span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - A user should be a member of these groups.
                </div>
                                <div style="font-size: small">
                  - Each group is defined by the dn.
                </div>
                                <div style="font-size: small">
                  - For example, cn=testgroup,ou=groups,dc=example,dc=avinetworks,dc=com.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
        
                                                <td colspan="7">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>jwt_profile_ref</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Jwtserverprofile to be used for authentication.
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type jwtserverprofile.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 20.1.3.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                                            <td colspan="7">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>ldap</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                            <span style="color: purple">dict / elements=dictionary </span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Ldap server and directory settings.
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
                <b>base_dn</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - The ldap base dn.
                </div>
                                <div style="font-size: small">
                  - For example, avinetworks.com would be dc=avinetworks,dc=com.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>bind_as_administrator</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">bool</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Ldap administrator credentials are used to search for users and group memberships.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as True.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>email_attribute</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Ldap attribute that refers to user email.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as email.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>full_name_attribute</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Ldap attribute that refers to user's full name.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as name.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>port</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">int</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Query the ldap servers on this port.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as 389.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>security_mode</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Ldap connection security mode.
                </div>
                                <div style="font-size: small">
                  - Enum options - AUTH_LDAP_SECURE_NONE, AUTH_LDAP_SECURE_USE_LDAPS.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as AUTH_LDAP_SECURE_USE_LDAPS.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>server</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">list / elements=string </span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Ldap server ip(v4/v6) address or fqdn.
                </div>
                                <div style="font-size: small">
                  - Use ip address if an auth profile is used to configure virtual service.
                </div>
                                <div style="font-size: small">
                  - Minimum of 1 items required.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>settings</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                            <span style="color: purple">dict / elements=dictionary </span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Ldap full directory configuration with administrator credentials.
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
                <b>admin_bind_dn</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Ldap admin user dn.
                </div>
                                <div style="font-size: small">
                  - Administrator credentials are required to search for users under user search dn or groups under group search dn.
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
                <b>group_filter</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Group filter is used to identify groups during search.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as (objectClass=*).
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                            <td class="elbow-placeholder"></td>
                                    <td colspan="5">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>group_member_attribute</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Ldap group attribute that identifies each of the group members.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as member.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                            <td class="elbow-placeholder"></td>
                                    <td colspan="5">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>group_member_is_full_dn</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">bool</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Group member entries contain full dns instead of just user id attribute values.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as True.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                            <td class="elbow-placeholder"></td>
                                    <td colspan="5">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>group_search_dn</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Ldap group search dn is the root of search for a given group in the ldap directory.
                </div>
                                <div style="font-size: small">
                  - Only matching groups present in this ldap directory sub-tree will be checked for user membership.
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
                <b>group_search_scope</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Ldap group search scope defines how deep to search for the group starting from the group search dn.
                </div>
                                <div style="font-size: small">
                  - Enum options - AUTH_LDAP_SCOPE_BASE, AUTH_LDAP_SCOPE_ONE, AUTH_LDAP_SCOPE_SUBTREE.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as AUTH_LDAP_SCOPE_SUBTREE.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                            <td class="elbow-placeholder"></td>
                                    <td colspan="5">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>ignore_referrals</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">bool</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - During user or group search, ignore searching referrals.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as False.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                            <td class="elbow-placeholder"></td>
                                    <td colspan="5">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>password</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Ldap admin user password.
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
                <b>user_attributes</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">list / elements=string </span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Ldap user attributes to fetch on a successful user bind.
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
                <b>user_id_attribute</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Ldap user id attribute is the login attribute that uniquely identifies a single user record.
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
                <b>user_search_dn</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Ldap user search dn is the root of search for a given user in the ldap directory.
                </div>
                                <div style="font-size: small">
                  - Only user records present in this ldap directory sub-tree will be validated.
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
                <b>user_search_scope</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Ldap user search scope defines how deep to search for the user starting from user search dn.
                </div>
                                <div style="font-size: small">
                  - Enum options - AUTH_LDAP_SCOPE_BASE, AUTH_LDAP_SCOPE_ONE, AUTH_LDAP_SCOPE_SUBTREE.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as AUTH_LDAP_SCOPE_ONE.
                </div>
                                            </td>
    </tr>
        
                                        <td class="elbow-placeholder"></td>
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>tls_config</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                            <span style="color: purple">dict / elements=dictionary </span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Tls configuration for outbound ldap connections.
                </div>
                                <div style="font-size: small">
                  - Effective only when security_mode is auth_ldap_secure_use_ldaps.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 32.2.1.
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
                <b>client_cert_ref</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Client certificate for mutual tls connection.
                </div>
                                <div style="font-size: small">
                  - Required when tls mode is mutual tls.
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type sslkeyandcertificate.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 32.2.1.
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
                <b>tls_mode</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Select how tls is used to establish a secure connection.
                </div>
                                <div style="font-size: small">
                  - Enum options - TLS_MODE_NO_VERIFY, TLS_MODE_TLS, TLS_MODE_MTLS, TLS_MODE_SKIP_HOSTNAME_VERIFY.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 32.2.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
        
                                        <td class="elbow-placeholder"></td>
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>user_bind</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                            <span style="color: purple">dict / elements=dictionary </span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Ldap anonymous bind configuration.
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
                <b>dn_template</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Ldap user dn pattern is used to bind ldap user after replacing the user token with real username.
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
                <b>token</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Ldap token is replaced with real user name in the user dn pattern.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as <user>.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                            <td class="elbow-placeholder"></td>
                                    <td colspan="5">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>user_attributes</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">list / elements=string </span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Ldap user attributes to fetch on a successful user bind.
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
                <b>user_id_attribute</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Ldap user id attribute is the login attribute that uniquely identifies a single user record.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
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
                  - Field introduced in 20.1.6.
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
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
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
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
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
                  - Name of the auth profile.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                                            <td colspan="7">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>oauth_profile</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                            <span style="color: purple">dict / elements=dictionary </span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Oauth profile - common endpoint information.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 21.1.3.
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
                <b>audience</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Audience parameter used for jwt token validation.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 32.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>authorization_endpoint</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Url of authorization server.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 21.1.3.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>end_session_endpoint</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Logout uri of idp server.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 22.1.3.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>instance_id</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Instance uuid of the csp service.
                </div>
                                <div style="font-size: small">
                  - Field deprecated in 32.1.1.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 30.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>introspection_endpoint</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Url of token introspection server.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 21.1.3.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>issuer</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Uniquely identifiable name of the token issuer.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 21.1.3.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>jwks_timeout</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">int</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Lifetime of the cached jwks keys.
                </div>
                                <div style="font-size: small">
                  - Allowed values are 0-1440.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 21.1.3.
                </div>
                                <div style="font-size: small">
                  - Unit is min.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as 0.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>jwks_uri</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Jwks url of the endpoint that hosts the public keys that can be used to verify any jwt issued by the authorization server.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 21.1.3.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>oauth_controller_settings</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                            <span style="color: purple">dict / elements=dictionary </span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Oauth app settings for controller authentication.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 30.1.1.
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
                <b>client_id</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Application specific identifier.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 21.1.3.
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
                <b>client_secret</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Application specific identifier secret.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 21.1.3.
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
                <b>oidc_config</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                            <span style="color: purple">dict / elements=dictionary </span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Openid connect specific configuration.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 21.1.3.
                </div>
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
                <b>oidc_enable</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">bool</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Adds openid as one of the scopes enabling openid connect flow.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 21.1.3.
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
                <b>profile</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">bool</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Fetch profile information by enabling profile scope.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 21.1.3.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as True.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                            <td class="elbow-placeholder"></td>
                            <td class="elbow-placeholder"></td>
                                    <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>userid_claim_name</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Claim name from id token to be used as user id.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 31.2.1.
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
                <b>userinfo</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">bool</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Fetch profile information from userinfo endpoint.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 21.1.3.
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
                <b>scopes</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">list / elements=string </span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Scope specified to give limited access to the app.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 21.1.3.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
        
                                        <td class="elbow-placeholder"></td>
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>oauth_profile_type</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Type of oauth profile which defines the usage type.
                </div>
                                <div style="font-size: small">
                  - Enum options - CLIENT_OAUTH, CONTROLLER_OAUTH.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 30.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as CLIENT_OAUTH.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>oauth_provider</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Type of oauth provider when using controller oauth as oauth profile type.
                </div>
                                <div style="font-size: small">
                  - Enum options - OAUTH_CSP, OAUTH_VCF.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 30.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>oauth_resp_buffer_sz</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">int</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Buffering size for the responses from the oauth enpoints.
                </div>
                                <div style="font-size: small">
                  - Allowed values are 0-32768000.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 21.1.3.
                </div>
                                <div style="font-size: small">
                  - Unit is bytes.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as 102400.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>org_id</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Organization id for oauth.
                </div>
                                <div style="font-size: small">
                  - Field deprecated in 32.1.1.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 30.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>pool_ref</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Pool object to interface with authorization server endpoints.
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type pool.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 21.1.3.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>redirect_uri</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Redirect uri specified in the request to authorization server.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 30.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>service_id</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Uuid value of csp service.
                </div>
                                <div style="font-size: small">
                  - Field deprecated in 32.1.1.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 30.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>service_name</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Name of the csp service.
                </div>
                                <div style="font-size: small">
                  - Field deprecated in 32.1.1.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 30.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>tls_config</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                            <span style="color: purple">dict / elements=dictionary </span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Tls configuration for outbound jwks connections during oauth token validation.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 32.2.1.
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
                <b>client_cert_ref</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Client certificate for mutual tls connection.
                </div>
                                <div style="font-size: small">
                  - Required when tls mode is mutual tls.
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type sslkeyandcertificate.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 32.2.1.
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
                <b>tls_mode</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Select how tls is used to establish a secure connection.
                </div>
                                <div style="font-size: small">
                  - Enum options - TLS_MODE_NO_VERIFY, TLS_MODE_TLS, TLS_MODE_MTLS, TLS_MODE_SKIP_HOSTNAME_VERIFY.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 32.2.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
        
                                        <td class="elbow-placeholder"></td>
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>token_endpoint</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Url of token exchange server.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 21.1.3.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>userinfo_endpoint</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Url of the userinfo endpoint.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 21.1.3.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
        
                                                <td colspan="7">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>saml</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                            <span style="color: purple">dict / elements=dictionary </span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Saml settings.
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
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>idp</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                            <span style="color: purple">dict / elements=dictionary </span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Configure remote identity provider settings.
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
                                    <td colspan="5">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>meta_data_download_interval</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">int</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - The interval to query and download saml idp metadata using the metadata url.
                </div>
                                <div style="font-size: small">
                  - Allowed values are 1-10080.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 30.2.1.
                </div>
                                <div style="font-size: small">
                  - Unit is min.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as 60.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                            <td class="elbow-placeholder"></td>
                                    <td colspan="5">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>metadata</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Saml idp metadata.
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
                                    <td colspan="5">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>metadata_url</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Saml idp federation metadata url.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 30.1.1.
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
                <b>periodic_download</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">bool</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Enable periodic metadata download.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 30.2.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as False.
                </div>
                                            </td>
    </tr>
        
                                        <td class="elbow-placeholder"></td>
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>sp</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                            <span style="color: purple">dict / elements=dictionary </span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Configure service provider settings for the controller.
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
                                    <td colspan="5">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>fqdn</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Fqdn if entity type is dns_fqdn.
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
                                    <td colspan="5">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>org_display_name</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Service provider organization display name.
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
                                    <td colspan="5">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>org_name</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Service provider organization name.
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
                                    <td colspan="5">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>org_url</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Service provider organization url.
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
                                    <td colspan="5">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>saml_entity_type</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Type of saml endpoint.
                </div>
                                <div style="font-size: small">
                  - Enum options - AUTH_SAML_CLUSTER_VIP, AUTH_SAML_DNS_FQDN, AUTH_SAML_APP_VS.
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
                                    <td colspan="5">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>sp_nodes</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">list / elements=dictionary </span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Service provider node information.
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
                            <td class="elbow-placeholder"></td>
                                    <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>entity_id</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Globally unique entityid for this node.
                </div>
                                <div style="font-size: small">
                  - Entity id on the idp should match this.
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
                            <td class="elbow-placeholder"></td>
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
                  - Refers to the cluster name identifier (virtual ip or fqdn).
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
                            <td class="elbow-placeholder"></td>
                                    <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>signing_cert</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Service provider signing certificate for metadata.
                </div>
                                <div style="font-size: small">
                  - Field deprecated in 18.2.1.
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
                            <td class="elbow-placeholder"></td>
                                    <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>signing_key</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Service provider signing key for metadata.
                </div>
                                <div style="font-size: small">
                  - Field deprecated in 18.2.1.
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
                            <td class="elbow-placeholder"></td>
                                    <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>signing_ssl_key_and_certificate_ref</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Service engines will use this ssl certificate to sign assertions going to the idp.
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type sslkeyandcertificate.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 18.2.1.
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
                <b>single_signon_url</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Single signon url to be programmed on the idp.
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
                                    <td colspan="5">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>tech_contact_email</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Service provider technical contact email.
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
                                    <td colspan="5">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>tech_contact_name</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Service provider technical contact name.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 17.2.3.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
        
            
                                                <td colspan="7">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>tacacs_plus</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                            <span style="color: purple">dict / elements=dictionary </span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Tacacs+ settings.
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
                <b>authorization_attrs</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">list / elements=dictionary </span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Tacacs+ authorization attribute value pairs.
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
                <b>mandatory</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">bool</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Mandatory.
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
                  - Attribute name.
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
                <b>value</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Attribute value.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
        
                                        <td class="elbow-placeholder"></td>
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>password</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Tacacs+ server shared secret.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>port</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">int</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Tacacs+ server listening port.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as 49.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>server</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">list / elements=string </span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Tacacs+ server ip address or fqdn.
                </div>
                                <div style="font-size: small">
                  - Minimum of 1 items required.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
    </tr>
                                    <td class="elbow-placeholder"></td>
                                    <td colspan="6">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>service</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                                                                        <span style="color: purple">str</span>
                                                            </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Tacacs+ service.
                </div>
                                <div style="font-size: small">
                  - Enum options - AUTH_TACACS_PLUS_SERVICE_NONE, AUTH_TACACS_PLUS_SERVICE_LOGIN, AUTH_TACACS_PLUS_SERVICE_ENABLE, AUTH_TACACS_PLUS_SERVICE_PPP,
                </div>
                                <div style="font-size: small">
                  - AUTH_TACACS_PLUS_SERVICE_ARAP, AUTH_TACACS_PLUS_SERVICE_PT, AUTH_TACACS_PLUS_SERVICE_RCMD, AUTH_TACACS_PLUS_SERVICE_X25,
                </div>
                                <div style="font-size: small">
                  - AUTH_TACACS_PLUS_SERVICE_NASI, AUTH_TACACS_PLUS_SERVICE_FWPROXY.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as AUTH_TACACS_PLUS_SERVICE_LOGIN.
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
                <b>type</b>
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
                  - Type of the auth profile.
                </div>
                                <div style="font-size: small">
                  - Enum options - AUTH_PROFILE_LDAP, AUTH_PROFILE_TACACS_PLUS, AUTH_PROFILE_SAML, AUTH_PROFILE_PINGACCESS, AUTH_PROFILE_JWT, AUTH_PROFILE_OAUTH,
                </div>
                                <div style="font-size: small">
                  - AUTH_PROFILE_CLIENT_CERT.
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
                  - Uuid of the auth profile.
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
          username: "{{ username }}"
          password: "{{ password }}"
          controller: "{{ controller }}"
          api_version: "{{ api_version }}"
          tenant: "{{ admin }}"
      tasks:        
        - name: Create user authorization profile based on the LDAP
          avi_authprofile:
            avi_credentials: "{{ avi_credentials }}"

            ldap:
              base_dn: dc=avi,dc=local
              bind_as_administrator: true
              port: 389
              security_mode: AUTH_LDAP_SECURE_NONE
              server:
                - 192.168.12.18
              settings:
                admin_bind_dn: user@avi.local
                group_filter: (objectClass=*)
                group_member_attribute: member
                group_member_is_full_dn: true
                group_search_dn: dc=avi,dc=local
                group_search_scope: AUTH_LDAP_SCOPE_SUBTREE
                ignore_referrals: true
                password: password
                user_id_attribute: samAccountname
                user_search_dn: dc=avi,dc=local
                user_search_scope: AUTH_LDAP_SCOPE_ONE
            name: ProdAuth
            tenant_ref: /api/tenant?name=admin
            type: AUTH_PROFILE_LDAP



Authors
~~~~~~~
- Anurag Palsule (anurag.palsule@broadcom.com)
- Parikshit Manur (parikshit.manur@broadcom.com)
- Rohan Suryavanshi (rohan.suryavanshi@broadcom.com)
