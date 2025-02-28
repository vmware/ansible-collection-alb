.. vmware.alb.avi_wafapplicationsignatureprovider:


**********************************************
vmware.alb.avi_wafapplicationsignatureprovider
**********************************************

**Module for setup of WafApplicationSignatureProvider Avi RESTful Object**


.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module is used to configure WafApplicationSignatureProvider object.
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
                <b>available_applications</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Available application names and the ruleset version, when the rules for an application changed the last time.
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
                    <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> application </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Name of an application in the rule set.
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
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> last_changed_ruleset_version </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - The last version of the rule set when the rules corresponding to the application changed.
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
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> number_of_rules </b>
                    <div style="font-size: small">
                                                <span style="color: purple">integer</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - The number of rules available for this application.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 20.1.3.
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
                <b>filter_rules_on_import</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - If this is set to false, all provided rules are imported when updating this object.
                </div>
                                <div style="font-size: small">
                  - If this is set to true, only newer rules are considered for import.
                </div>
                                <div style="font-size: small">
                  - Newer rules are rules where the rule id is not in the range of 2,000,000 to 2,080,000 or where the rule has a tag with a cve from 2013 or newer.
                </div>
                                <div style="font-size: small">
                  - All other rules are ignored on rule import.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 30.2.1.
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
                  - Name of application specific ruleset provider.
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
                <b>ruleset_version</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Version of signatures.
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
                <b>service_status</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - If this object is managed by the application signatures update service, this field contain the status of this syncronization.
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
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> error </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - If the last attempted update failed, this is a more detailed error message.
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
                    <b> last_successful_update_check </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - The time when the application signature service last successfull attemped to update this object.
                </div>
                                <div style="font-size: small">
                  - It will be not update, if an error occurs during an update attempt.
                </div>
                                <div style="font-size: small">
                  - In this case, the error will be set.
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
                    <b> upstream_sync_timestamp </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - A timestamp field.
                </div>
                                <div style="font-size: small">
                  - It is used by the application signature sync service to keep track of the current version.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 21.1.1, 20.1.5.
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
                                                <tr>
            <td colspan="4">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>signatures</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - The waf rules.
                </div>
                                <div style="font-size: small">
                  - Not visible in the api.
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
                  - Enable or disable waf rule group.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 17.2.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                            <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> exclude_list </b>
                    <div style="font-size: small">
                                                    <span style="color: purple">list / elements=dictionary </span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Exclude list for the waf rule.
                </div>
                                <div style="font-size: small">
                  - The fields in the exclude list entry are logically and'ed to deduce the exclusion criteria.
                </div>
                                <div style="font-size: small">
                  - If there are multiple excludelist entries, it will be 'logical or' of them.
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
                    <b> client_subnet </b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Client ip subnet to exclude for waf rules.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 17.2.1.
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
                    <b> description </b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Free-text comment about this exclusion.
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
                    <b> match_element </b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - The match_element can be 'args xxx', 'args_get xxx', 'args_post xxx', 'args_names xxx', 'files xxx', 'query_string', 'request_basename',
                </div>
                                <div style="font-size: small">
                  - 'request_body', 'request_uri', 'request_uri_raw', 'request_cookies xxx', 'request_cookies_names xxx', 'request_headers xxx',
                </div>
                                <div style="font-size: small">
                  - 'request_headers_names xxx', 'response_headers xxx' or xml xxx.
                </div>
                                <div style="font-size: small">
                  - These match_elements in the http transaction (if present) will be excluded when executing waf rules.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 17.2.1.
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
                    <b> match_element_criteria </b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Criteria for match_element matching.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 18.2.2.
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
                    <b> uri_match_criteria </b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Criteria for uri matching.
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
                    <b> uri_path </b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
            </td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Uri path to exclude for waf rules.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 17.2.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>     
        </tr>
                                    <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> force_detection </b>
                    <div style="font-size: small">
                                                <span style="color: purple">bool</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - When set to 'true', this rule will not cause 'deny' or 'redirect' actions to run, even if waf policy is set to enforcement mode.
                </div>
                                <div style="font-size: small">
                  - The behavior would be as if this rule operated in detection mode regardless of waf policy setting.
                </div>
                                <div style="font-size: small">
                  - Field deprecated in 18.1.5.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 18.1.4.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                            <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> index </b>
                    <div style="font-size: small">
                                                <span style="color: purple">integer</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Field introduced in 17.2.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                            <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> is_sensitive </b>
                    <div style="font-size: small">
                                                <span style="color: purple">bool</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - The rule field is sensitive and will not be displayed.
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
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> mode </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Waf rule mode.
                </div>
                                <div style="font-size: small">
                  - This can be detection or enforcement.
                </div>
                                <div style="font-size: small">
                  - If this is not set, the policy mode is used.
                </div>
                                <div style="font-size: small">
                  - This only takes effect if the policy allows delegation.
                </div>
                                <div style="font-size: small">
                  - Enum options - WAF_MODE_DETECTION_ONLY, WAF_MODE_ENFORCEMENT.
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
                  - User-friendly optional name for a rule.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 17.2.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                            <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> paranoia_level </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Waf rule paranoia level.
                </div>
                                <div style="font-size: small">
                  - This field is informative, like rule_id and tags, it is generated by the system from the rule text.
                </div>
                                <div style="font-size: small">
                  - This field is filled for crs rules.
                </div>
                                <div style="font-size: small">
                  - Enum options - WAF_PARANOIA_LEVEL_LOW, WAF_PARANOIA_LEVEL_MEDIUM, WAF_PARANOIA_LEVEL_HIGH, WAF_PARANOIA_LEVEL_EXTREME.
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
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> phase </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - The execution phase where this rule will be executed.
                </div>
                                <div style="font-size: small">
                  - Enum options - WAF_PHASE_CONNECTION, WAF_PHASE_REQUEST_HEADER, WAF_PHASE_REQUEST_BODY, WAF_PHASE_RESPONSE_HEADER, WAF_PHASE_RESPONSE_BODY,
                </div>
                                <div style="font-size: small">
                  - WAF_PHASE_LOGGING.
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
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> rule </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Rule as per modsec language.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 17.2.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>             
        </tr>
                            <td class="elbow-placeholder"></td>
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> rule_id </b>
                    <div style="font-size: small">
                                                <span style="color: purple">string</span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Identifier (id) for a rule per modsec language.
                </div>
                                <div style="font-size: small">
                  - All secrule and secaction directives require an id.
                </div>
                                <div style="font-size: small">
                  - It is extracted from the id action in a modsec rule.
                </div>
                                <div style="font-size: small">
                  - Rules within a single waf policy are required to have unique rule_ids.
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
            <td collspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b> tags </b>
                    <div style="font-size: small">
                                                    <span style="color: purple">list / elements=string </span>
                                            </div>
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                                                <div style="font-size: small">
                  - Tags for waf rule as per modsec language.
                </div>
                                <div style="font-size: small">
                  - They are extracted from the tag action in a modsec rule.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 18.1.3.
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
                  - Field introduced in 20.1.1.
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
        - name: Example to create WafApplicationSignatureProvider object
          avi_wafapplicationsignatureprovider:
            avi_credentials: "{{ avi_credentials }}"
            state: present
            name: sample_wafapplicationsignatureprovider


Authors
~~~~~~~
- Gaurav Rastogi (grastogi@vmware.com)
- Sandeep Bandi (sbandi@vmware.com)
- Amol Shinde (samol@vmware.com)



