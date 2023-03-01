# avinetworks.avise_vmware


Using this module you are able to install the Avi Vantage Service Engine, to your system. However, minimum requirements must be met. Please visit the Avi SE Requirements webpage: https://kb.avinetworks.com/docs/latest/system-requirements-hardware/

## Requirements

- `avisdk` python library, which can be installed by `pip install avisdk --upgrade`
- `pyvmomi` python library, which can be installed by  `pip install pyvmomi --upgrade`
- `requests_toolbelt` python library, which can be installed by `pip install requests_toolbelt --upgrade`

## Role Dependencies

- avinetworks.avisdk
  To install use the following command: `ansible-galaxy install -f avinetworks.avisdk`

## Role Variables

### Standard Parameters
| Variable | Required | Default | Comments |
|----------|----------|---------|----------|
| `se_skip_requirements` | No | `false` | Skips any requirements for disk space, ram, and cpu. |

### Auto-registration and Controller specific parameters
| Variable | Required | Default | Comments |
|----------|----------|---------|----------|
| `se_autoregister` | No | `true` | Autoregister the service engine to the specified controller. |
| `se_auth_token` | No | `None`|  If defined it will be the token used to register the service engine to the controller |
| `se_cluster_uuid` | No | `None`|  If defined it will be the cluster UUID used to register the service engine to the controller |
| `se_leader_ctl_ip` | Yes | `None` | The IP address of the controller. |
| `se_leader_ctl_username` | No | `None` | The username to login into controller api. |
| `se_leader_ctl_password` | No | `None` | The passowrd to login into the controller api. |
| `se_tenant` | No | `admin` | Name of se_tenant the SE should auto-register with. |
| `se_cloud_name` | No | `Default-Cloud` | Name of cloud the SE should auto-register with. |
| `se_group_name` | No | `Default-Group` | Name of SE group the SE should reside in. |


### VMware Deployment Variables
These are only marked required, for when you are using VMware Deployment.

| Variable | Required | Default | Comments |
|----------|----------|---------|----------|
| `vcenter_host` | Yes | `None` | VMWare host IP |
| `vcenter_user` | Yes | `None` | VMWare user name |
| `vcenter_password` | Yes | `None` | VMWare password |
| `ssl_verify` | No | False | ovftool sslverify option |
| `state` | No | present | Option to specify create or destroy the infra |
| `se_vmw_datacenter` | No | Picked first from the list | Name of VMWare datacenter |
| `se_vmw_cluster` | No | Picked from the first in the list of given datacenters clusters | Name of a cluster in the datacenter |
| `se_vmw_datastore` | No | Picked up the datastore having max free space | Name of datastore on which VM to be deployed |
| `se_vmw_ovf_networks` | No | `None` | Key-Value object for specifying OVF network names |
| `se_vmw_disk_mode` | No | thin | Deployment disk mode |
| `se_vmw_ova_image_file` | No | `se.ova` | SE ova file name to be searched for on the controller. |
| `se_vmw_ova_image_name` | No | `None` | SE ova file name to be downloaded as or used from local. When downloaded, it defaults to se-(controller_version)-(build)-(cluster_uuid).ova eg. se-17.2.7-9014-0f9449f5.ova |
| `se_vmw_ova_path` | No | `None` | Relative or absolute location of the SE ova (includes ova filename). If specified the OVA file will not be downloaded. |
| `se_vmw_ova_download_path` | No | `.` | Relative or absolute location to download SE ova (excludes ova filename). |
| `se_vmw_vm_name` | Yes | `None` | Name of a controller VM on VMWare |
| `se_vmw_power_on` | No | True | VM to be powered on after provisioning |
| `se_vmw_vcenter_folder` | No | Datacenter root | Folder path to deploy VM |
| `se_vmw_mgmt_ip` | No | `None` | Static IP for the controller |
| `se_vmw_mgmt_mask` | No | `None` | Management IP Mask |
| `se_vmw_default_gw` | No | `None` | Default gateway of management network |
| `se_vmw_sysadmin_public_key` | No | `None` | Public key file path |
| `se_vmw_number_of_cpus` | No | `None` | Number of CPUs for controller |
| `se_vmw_cpu_reserved` | No | `None` | CPU reservation in megahertz |
| `se_vmw_memory` | No | `None` | Controller memory in MB |
| `se_vmw_memory_reserved` | No | `None` | Controller memory reservation in MB |
| `se_vmw_disk_size` | No | `None` | Controller disk size in GB |
| `se_vmw_ovf_properties` | No | `None` | Other Controller ovf properties in key value format |

### VMware Deployment Example
```

---
- hosts: controller
  gather_facts: no
  collections:
    - vmware.alb
  roles:
    - name: avinetworks.avisdk
  tasks:
    - name: Deploy Avi Service Engines
      include_role:
        name: avise_vmware
      vars:
        se_leader_ctl_ip: '{{ controller_ip }}'
        se_leader_ctl_username: '{{ controller_username }}'
        se_leader_ctl_password: '{{ controller_password }}'
        se_cloud_name: Default-Cloud
        ovftool_path: /usr/bin/
        vcenter_host: '{{ vcenter_host }}'
        vcenter_user: '{{ vcenter_user }}'
        vcenter_password: '{{ vcenter_password }}'
        se_vmw_datacenter: VMW_DC
        se_vmw_cluster: VMW_CL
        se_vmw_ovf_networks:
          'Data Network 1': DPG-80
          'Data Network 2': DPG-100
          'Management': Mgmt_network
        se_vmw_vm_name: ansible-avise-vmware
        se_vmw_power_on: true
        se_vmw_vcenter_folder: network/avi
        se_vmw_number_of_cpus: 2
        se_vmw_memory: 2048
```
### VMware Cloud on AWS (VMC) Example with Auto-registration

- In case of VMware Cloud on AWS (VMC) all the network interfaces require port group to be attached, for unused interfaces the parking port group can be used.

```
---
- hosts: localhost
  gather_facts: no
  connection: local
  roles:
    - name: avinetworks.avisdk
  collections:
    - vmware.alb
  vars:
    avi_credentials:
      api_version: "{{ avi_api_version }}"
      username: "{{ avi_username }}"
      password: "{{ avi_password }}"
      controller: "{{ controllers.0.mgmt_ip }}"
  tasks:
    - name: Deploy Avi Service Engines
      include_role:
        name: avise_vmware
      vars:
        se_leader_ctl_ip: '{{ controllers.0.mgmt_ip }}'
        se_leader_ctl_username: '{{ avi_username }}'
        se_leader_ctl_password: '{{ avi_password }}'
        se_cloud_name: '{{ cloud_name }}'
        se_group_name: '{{ seg_name }}'
        ovftool_path: /usr/bin/
        vcenter_host: '{{ vcenter_host }}'
        vcenter_user: '{{ vcenter_user }}'
        vcenter_password: '{{ vcenter_password }}'
        se_vmw_datacenter: '{{ con_vcenter_datacenter }}'
        se_vmw_cluster: '{{ con_vcenter_cluster }}'
        se_vmw_vcenter_folder: '{{ seg_vcenter_folder }}'
        se_vmw_datastore: '{{ serviceengines.0.se_vcenter_datastore }}'
        se_vmw_vm_name: "{{ serviceengines.0.vm_name }}"
        se_vmw_power_on: '{{ serviceengines.0.power_on }}'
        #se_vmw_mgmt_network: '{{ seg_mgmt_network }}'
        se_vmw_ovf_networks:
          'Data Network 9': '{{ seg_parking_network }}'
          'Data Network 8': '{{ seg_parking_network }}'
          'Data Network 7': '{{ seg_parking_network }}'
          'Data Network 6': '{{ seg_parking_network }}'
          'Data Network 5': '{{ seg_parking_network }}'
          'Data Network 4': '{{ seg_parking_network }}'
          'Data Network 3': '{{ seg_parking_network }}'
          'Data Network 2': '{{ seg_parking_network }}'
          'Data Network 1': '{{ seg_data1_network }}'
          'Management': '{{ seg_mgmt_network }}'
        se_vmw_power_on: true
        se_vmw_number_of_cpus: '{{ seg_cpus }}'
        se_vmw_memory: '{{ seg_memory }}'
        se_vmw_memory_reserved: '{{ seg_memory }}'
        se_vmw_disk_size: '{{ seg_disk }}'
        se_vmw_disk_mode: thick
      loop: "{{ serviceengines }}"

```

### VMware Example without Auto-registration

```
---
- hosts: controller
  roles:
    - name: avinetworks.avisdk
  collections:
    - vmware.alb
  tasks:
    - name: Deploy Avi Service Engines
      include_role:
        name: avise_vmware
      vars:
        se_leader_ctl_ip: '{{ controller_ip }}'
        se_leader_ctl_username: '{{ controller_username }}'
        se_leader_ctl_password: '{{ controller_password }}'
        se_cloud_name: Default-Cloud
        ovftool_path: /usr/bin/
        vcenter_host: '{{ vcenter_host }}'
        vcenter_user: '{{ vcenter_user }}'
        vcenter_password: '{{ vcenter_password }}'
        se_autoregister: false
        se_auth_token: '{{ se_authtoken }}'
        se_cluster_uuid: '{{ se_clusteruuid }}'
        se_vmw_datacenter: VMW_DC
        se_vmw_cluster: VMW_CL
        se_vmw_ovf_networks:
          'Data Network 1': DPG-80
          'Data Network 2': DPG-100
          'Management': Mgmt_network
        se_vmw_vm_name: ansible-avise-vmware
        se_vmw_power_on: true
        se_vmw_vcenter_folder: network/avi
        se_vmw_number_of_cpus: 2
        se_vmw_memory: 2048

```

## License

Apache 2.0

## Author Information

contact: Avi Networks [avi-sdk@avinetworks.com]
