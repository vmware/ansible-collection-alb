
.. vmware.alb.avi_saml_api_session:


**********************************************
vmware.alb.avi_saml_api_session
**********************************************

**Module for setup of SamlApiSession Avi RESTful Object**


.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module is used to configure SamlApiSession object.
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
                <b>idp_class</b>
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
                  - IDP class which will be used to authenticate session with that corresponding IDP such as Okta,
                </div>
                                <div style="font-size: small">
                  - Onelogin and Pingfederate. Currently, we support two idp classes OktaSAMLApiSession, OneloginSAMLApiSession.
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
        - name: Example to create SamlApiSession object
          avi_saml_api_session:
            avi_credentials: "{{ avi_credentials }}"
            state: present
            name: sample_saml_api_session


Authors
~~~~~~~
- Anurag Palsule (anurag.palsule@broadcom.com)
- Parikshit Manur (parikshit.manur@broadcom.com)
- Rohan Suryavanshi (rohan.suryavanshi@broadcom.com)
