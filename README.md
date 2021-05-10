# Advanced Load Balancer (formerly Avi) Ansible Collection

<!--start requires_ansible-->
## Ansible version compatibility

This collection has been tested against following Ansible versions: **>=2.9.10**.

<!--end requires_ansible-->

## Installation and Usage

Ansible must be installed
```
pip install ansible
```

Install ALB collection using `ansible-galaxy` CLI:
```
ansible-galaxy collection install vmware.alb
```

Install ALB collection using `requirements.yml` file:

Create `requirements.yml` file using below contents
```yaml
collections:
- name: vmware.alb
```

Install the collection:
```
ansible-galaxy collection install -r requirements.yml
```

### Required Python libraries

ALB collection depends upon following third party libraries:

* requests

### Installing required libraries

After ALB collection installation we need to install the required python libraries using following command:
```
pip install requests
```

### Modules
Name | Description
--- | ---
[vmware.alb.avi_labelgroup](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_labelgroup.rst)|Module to create update or delete LabelGroup
[vmware.alb.avi_albservicesconfig](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_albservicesconfig.rst)|Module to create update or delete ALBServicesConfig
[vmware.alb.avi_systemlimits](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_systemlimits.rst)|Module to create update or delete SystemLimits
[vmware.alb.avi_licenseledgerdetails](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_licenseledgerdetails.rst)|Module to create update or delete LicenseLedgerDetails
[vmware.alb.avi_controllerproperties](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_controllerproperties.rst)|Module to create update or delete ControllerProperties
[vmware.alb.avi_useraccountprofile](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_useraccountprofile.rst)|Module to create update or delete UserAccountProfile
[vmware.alb.avi_cloudproperties](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_cloudproperties.rst)|Module to create update or delete CloudProperties
[vmware.alb.avi_seproperties](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_seproperties.rst)|Module to create update or delete SeProperties
[vmware.alb.avi_tenant](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_tenant.rst)|Module to create update or delete Tenant
[vmware.alb.avi_cloudconnectoruser](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_cloudconnectoruser.rst)|Module to create update or delete CloudConnectorUser
[vmware.alb.avi_hardwaresecuritymodulegroup](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_hardwaresecuritymodulegroup.rst)|Module to create update or delete HardwareSecurityModuleGroup
[vmware.alb.avi_alertscriptconfig](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_alertscriptconfig.rst)|Module to create update or delete AlertScriptConfig
[vmware.alb.avi_customipamdnsprofile](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_customipamdnsprofile.rst)|Module to create update or delete CustomIpamDnsProfile
[vmware.alb.avi_networkprofile](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_networkprofile.rst)|Module to create update or delete NetworkProfile
[vmware.alb.avi_stringgroup](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_stringgroup.rst)|Module to create update or delete StringGroup
[vmware.alb.avi_ipaddrgroup](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_ipaddrgroup.rst)|Module to create update or delete IpAddrGroup
[vmware.alb.avi_pkiprofile](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_pkiprofile.rst)|Module to create update or delete PKIProfile
[vmware.alb.avi_sslprofile](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_sslprofile.rst)|Module to create update or delete SSLProfile
[vmware.alb.avi_applicationpersistenceprofile](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_applicationpersistenceprofile.rst)|Module to create update or delete ApplicationPersistenceProfile
[vmware.alb.avi_alertemailconfig](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_alertemailconfig.rst)|Module to create update or delete AlertEmailConfig
[vmware.alb.avi_snmptrapprofile](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_snmptrapprofile.rst)|Module to create update or delete SnmpTrapProfile
[vmware.alb.avi_autoscalelaunchconfig](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_autoscalelaunchconfig.rst)|Module to create update or delete AutoScaleLaunchConfig
[vmware.alb.avi_fileobject](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_fileobject.rst)|Module to create update or delete FileObject
[vmware.alb.avi_securitypolicy](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_securitypolicy.rst)|Module to create update or delete SecurityPolicy
[vmware.alb.avi_protocolparser](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_protocolparser.rst)|Module to create update or delete ProtocolParser
[vmware.alb.avi_jwtserverprofile](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_jwtserverprofile.rst)|Module to create update or delete JWTServerProfile
[vmware.alb.avi_wafprofile](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_wafprofile.rst)|Module to create update or delete WafProfile
[vmware.alb.avi_wafapplicationsignatureprovider](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_wafapplicationsignatureprovider.rst)|Module to create update or delete WafApplicationSignatureProvider
[vmware.alb.avi_errorpagebody](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_errorpagebody.rst)|Module to create update or delete ErrorPageBody
[vmware.alb.avi_testsedatastorelevel3](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_testsedatastorelevel3.rst)|Module to create update or delete TestSeDatastoreLevel3
[vmware.alb.avi_botconfigconsolidator](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_botconfigconsolidator.rst)|Module to create update or delete BotConfigConsolidator
[vmware.alb.avi_federationcheckpoint](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_federationcheckpoint.rst)|Module to create update or delete FederationCheckpoint
[vmware.alb.avi_gslbgeodbprofile](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_gslbgeodbprofile.rst)|Module to create update or delete GslbGeoDbProfile
[vmware.alb.avi_siteversion](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_siteversion.rst)|Module to create update or delete SiteVersion
[vmware.alb.avi_image](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_image.rst)|Module to create update or delete Image
[vmware.alb.avi_controllerportalregistration](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_controllerportalregistration.rst)|Module to create update or delete ControllerPortalRegistration
[vmware.alb.avi_dynamicdnsrecord](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_dynamicdnsrecord.rst)|Module to create update or delete DynamicDnsRecord
[vmware.alb.avi_controllersite](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_controllersite.rst)|Module to create update or delete ControllerSite
[vmware.alb.avi_role](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_role.rst)|Module to create update or delete Role
[vmware.alb.avi_albservicesfileupload](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_albservicesfileupload.rst)|Module to create update or delete ALBServicesFileUpload
[vmware.alb.avi_webhook](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_webhook.rst)|Module to create update or delete Webhook
[vmware.alb.avi_securitymanagerdata](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_securitymanagerdata.rst)|Module to create update or delete SecurityManagerData
[vmware.alb.avi_cluster](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_cluster.rst)|Module to create update or delete Cluster
[vmware.alb.avi_poolgroupdeploymentpolicy](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_poolgroupdeploymentpolicy.rst)|Module to create update or delete PoolGroupDeploymentPolicy
[vmware.alb.avi_jwtprofile](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_jwtprofile.rst)|Module to create update or delete JWTProfile
[vmware.alb.avi_backupconfiguration](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_backupconfiguration.rst)|Module to create update or delete BackupConfiguration
[vmware.alb.avi_clusterclouddetails](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_clusterclouddetails.rst)|Module to create update or delete ClusterCloudDetails
[vmware.alb.avi_certificatemanagementprofile](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_certificatemanagementprofile.rst)|Module to create update or delete CertificateManagementProfile
[vmware.alb.avi_ipamdnsproviderprofile](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_ipamdnsproviderprofile.rst)|Module to create update or delete IpamDnsProviderProfile
[vmware.alb.avi_analyticsprofile](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_analyticsprofile.rst)|Module to create update or delete AnalyticsProfile
[vmware.alb.avi_wafpolicypsmgroup](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_wafpolicypsmgroup.rst)|Module to create update or delete WafPolicyPSMGroup
[vmware.alb.avi_botmapping](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_botmapping.rst)|Module to create update or delete BotMapping
[vmware.alb.avi_natpolicy](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_natpolicy.rst)|Module to create update or delete NatPolicy
[vmware.alb.avi_applicationprofile](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_applicationprofile.rst)|Module to create update or delete ApplicationProfile
[vmware.alb.avi_microservicegroup](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_microservicegroup.rst)|Module to create update or delete MicroServiceGroup
[vmware.alb.avi_ipreputationdb](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_ipreputationdb.rst)|Module to create update or delete IPReputationDB
[vmware.alb.avi_geodb](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_geodb.rst)|Module to create update or delete GeoDB
[vmware.alb.avi_errorpageprofile](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_errorpageprofile.rst)|Module to create update or delete ErrorPageProfile
[vmware.alb.avi_testsedatastorelevel2](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_testsedatastorelevel2.rst)|Module to create update or delete TestSeDatastoreLevel2
[vmware.alb.avi_gslb](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_gslb.rst)|Module to create update or delete Gslb
[vmware.alb.avi_upgradestatusinfo](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_upgradestatusinfo.rst)|Module to create update or delete UpgradeStatusInfo
[vmware.alb.avi_upgradestatussummary](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_upgradestatussummary.rst)|Module to create update or delete UpgradeStatusSummary
[vmware.alb.avi_scheduler](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_scheduler.rst)|Module to create update or delete Scheduler
[vmware.alb.avi_sslkeyandcertificate](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_sslkeyandcertificate.rst)|Module to create update or delete SSLKeyAndCertificate
[vmware.alb.avi_networksecuritypolicy](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_networksecuritypolicy.rst)|Module to create update or delete NetworkSecurityPolicy
[vmware.alb.avi_botdetectionpolicy](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_botdetectionpolicy.rst)|Module to create update or delete BotDetectionPolicy
[vmware.alb.avi_testsedatastorelevel1](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_testsedatastorelevel1.rst)|Module to create update or delete TestSeDatastoreLevel1
[vmware.alb.avi_backup](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_backup.rst)|Module to create update or delete Backup
[vmware.alb.avi_cloud](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_cloud.rst)|Module to create update or delete Cloud
[vmware.alb.avi_healthmonitor](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_healthmonitor.rst)|Module to create update or delete HealthMonitor
[vmware.alb.avi_alertsyslogconfig](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_alertsyslogconfig.rst)|Module to create update or delete AlertSyslogConfig
[vmware.alb.avi_vrfcontext](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_vrfcontext.rst)|Module to create update or delete VrfContext
[vmware.alb.avi_vcenterserver](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_vcenterserver.rst)|Module to create update or delete VCenterServer
[vmware.alb.avi_prioritylabels](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_prioritylabels.rst)|Module to create update or delete PriorityLabels
[vmware.alb.avi_nsxtsegmentruntime](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_nsxtsegmentruntime.rst)|Module to create update or delete NsxtSegmentRuntime
[vmware.alb.avi_gslbservice](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_gslbservice.rst)|Module to create update or delete GslbService
[vmware.alb.avi_actiongroupconfig](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_actiongroupconfig.rst)|Module to create update or delete ActionGroupConfig
[vmware.alb.avi_availabilityzone](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_availabilityzone.rst)|Module to create update or delete AvailabilityZone
[vmware.alb.avi_alertconfig](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_alertconfig.rst)|Module to create update or delete AlertConfig
[vmware.alb.avi_serverautoscalepolicy](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_serverautoscalepolicy.rst)|Module to create update or delete ServerAutoScalePolicy
[vmware.alb.avi_network](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_network.rst)|Module to create update or delete Network
[vmware.alb.avi_serviceenginegroup](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_serviceenginegroup.rst)|Module to create update or delete ServiceEngineGroup
[vmware.alb.avi_pool](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_pool.rst)|Module to create update or delete Pool
[vmware.alb.avi_trafficcloneprofile](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_trafficcloneprofile.rst)|Module to create update or delete TrafficCloneProfile
[vmware.alb.avi_vsvip](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_vsvip.rst)|Module to create update or delete VsVip
[vmware.alb.avi_serviceengine](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_serviceengine.rst)|Module to create update or delete ServiceEngine
[vmware.alb.avi_networkservice](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_networkservice.rst)|Module to create update or delete NetworkService
[vmware.alb.avi_poolgroup](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_poolgroup.rst)|Module to create update or delete PoolGroup
[vmware.alb.avi_pingaccessagent](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_pingaccessagent.rst)|Module to create update or delete PingAccessAgent
[vmware.alb.avi_httppolicyset](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_httppolicyset.rst)|Module to create update or delete HTTPPolicySet
[vmware.alb.avi_dnspolicy](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_dnspolicy.rst)|Module to create update or delete DnsPolicy
[vmware.alb.avi_vsdatascriptset](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_vsdatascriptset.rst)|Module to create update or delete VSDataScriptSet
[vmware.alb.avi_l4policyset](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_l4policyset.rst)|Module to create update or delete L4PolicySet
[vmware.alb.avi_icapprofile](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_icapprofile.rst)|Module to create update or delete IcapProfile
[vmware.alb.avi_authprofile](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_authprofile.rst)|Module to create update or delete AuthProfile
[vmware.alb.avi_ssopolicy](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_ssopolicy.rst)|Module to create update or delete SSOPolicy
[vmware.alb.avi_systemconfiguration](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_systemconfiguration.rst)|Module to create update or delete SystemConfiguration
[vmware.alb.avi_virtualservice](https://github.com/vmware/ansible-collection-alb/blob/main/docs/avi_virtualservice.rst)|Module to create update or delete VirtualService
<!--end collection content-->

### Testing with `ansible-test`

Refer [testing](testing.md) for more information.

## Publishing New Version

Examples
--------

    - hosts: localhost
      connection: local
      collections:
        - vmware.alb
      tasks:
        - name: Example to create create Pool object
          avi_pool:
            controller: "192.168.15.18"
            username: "admin"
            password: "password"
            name: app1-pool
            lb_algorithm: LB_ALGORITHM_LEAST_LOAD
            servers:
            - ip:
                 addr: "192.168.12.15"
                 type: 'V4'

Example using config role:
```
# config.yml
avi_config:
  pool:
    - name: role1-pool
      lb_algorithm: LB_ALGORITHM_LEAST_LOAD
      servers:
        - ip:
             addr: 192.160.1.10
             type: 'V4'
```
```
# creds.yml
avi_credentials:
    controller: "192.168.1.11"
    username: "admin"
    password: "password"
    api_version: 20.1.5
```
```
# collection.yml
---
- hosts: localhost
  connection: local
  collections:
    - vmware.alb
  tasks:
    - name: Create pool using aviconfig role
      import_role:
        name: aviconfig
      vars:
          avi_config_file: "config.yml"
          avi_creds_file: "creds.yml"