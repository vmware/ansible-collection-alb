# avinetworks.avise-csp


Using this module you are able to install the Avi Vantage Service Engine, to your system. However, minimum requirements must be met. Please visit the Avi SE Requirements webpage: https://kb.avinetworks.com/docs/latest/system-requirements-hardware/

## Requirements

- A CSP device
- `avisdk` python library, which can be installed by `pip install avisdk --upgrade`

## Role Dependencies

- avinetworks.avisdk
  To install use the following command: `ansible-galaxy install -f avinetworks.avisdk`

## Role Variables

### Standard Parameters
| Variable | Required | Default | Comments |
|----------|----------|---------|----------|
| `se_skip_requirements` | No | `false` | Skips any requirements for disk space, ram, and cpu. |

### Auto-registration parameters
| Variable | Required | Default | Comments |
|----------|----------|---------|----------|
| `se_autoregister` | No | `true` | Autoregister the service engine to the specified controller. |
| `se_auth_token` | No | `None`|  If defined it will be the token used to register the service engine to the controller |
| `se_master_ctl_ip` | No | `None` | The IP address of the controller. |
| `se_master_ctl_username` | No | `None` | The username to login into controller api. <br>**Not required when `se_autoregister: false`** |
| `se_master_ctl_password` | No | `None` | The passowrd to login into the controller api. <br>**Not required when `se_autoregister: false`** |
| `se_cloud_name` | No | `Default-Cloud` | Name of cloud the SE should auto-register with. |
| `se_tenant` | No | `admin` | Name of se_tenant the SE should auto-register with. |


### CSP Deployment Variables
These are only marked required, for when you are using CSP Deployment.

| Variable | Required | Default | Comments |
|----------|----------|---------|----------|
| `se_csp_user` | Yes | `None` | Username that will be used to connect to the CSP server. |
| `se_csp_password` | Yes | `None` | Password required to authenticate the user. |
| `se_csp_qcow_image_file` | No | `se.qcow2` | SE qcow2 file name to be searched for on the controller. |
| `se_csp_qcow_image_name` | No | `None` | SE qcow2 file name to be downloaded as or used from local. When copied to CSP host, it defaults to se-(controller_version)-(build)-(cluster_uuid).qcow2 eg. se-17.2.14-9014-0f9449f5.qcow2 |
| `se_csp_mgmt_ip` | Yes | `None` | IP of the SE on the management network. |
| `se_csp_mgmt_mask` | Yes | `None` | Subnet mask that the SE will require. |
| `se_csp_default_gw` | Yes | `None` | Default gateway for the SE. |
| `se_csp_authtoken` | No | Auto | Token which will authenticate the SE to the controller. |
| `se_csp_tenant_uuid` | No | `None` | UUID of the Tenant the SE will use. If left as `None` will use Admin se_tenant. |
| `se_csp_disk_size` | No | `10` | Amount of disk space in GB for the SE. |
| `se_csp_service_name` | No | `avi-se` | Name of the service to be created on the CSP. |
| `se_csp_num_cpu` | No | `1` | Number of CPUs to be allocated to the SE. |
| `se_csp_memory_gb` | No | `1` | Amount of memory in GB allocated to the SE. |
| `se_csp_vnics` | No | See `defaults/main.yml` | Sets the interfaces for the SE service |
| `se_csp_hsm_ip` | No | `None` | IP Address and Subnet for Dedicated HSM interface, ex. 10.160.100.221/24 |
| `se_csp_hsm_mask` | No | `None` | Netmask of the interface that will talk to HSM |
| `se_csp_hsm_static_routes` | No | `None` | Static routes for HSM, ex. 10.128.1.0/24 via 10.160.100.1 |
| `se_csp_hsm_vnic_id` | No | `None` | VNIC id, of the HSM interface configured on this interface ex. 1 |
| `se_csp_asm_ip` | No | `None` | IP Address and Subnet for Dedicated ASM interface, ex. 10.160.100.221/24|
| `se_csp_asm_mask` | No | `None` | Netmask of the interface that will talk to ASM |
| `se_csp_asm_static_routes` | No | `None` | Static routes for ASM, ex. 10.128.1.0/24 via 10.160.100.1 |
| `se_csp_asm_vnic_id` | No | `None` | VNIC id, of the ASM interface configured on this interface ex. 1 |
| `se_csp_bond_ifs` | No | `None` | The bond parameters for the service |


### CSP Deployment Example
```

---
- hosts: csp_devices
  gather_facts: false
  collections:
    - vmware.alb
  tasks:
    - name: Deploy Avi SE csp
      import_role:
        name: avise_csp
      vars:
        se_csp_user: admin
        se_csp_password: password
        se_master_ctl_ip: 10.128.2.20
        se_master_ctl_username: admin
        se_master_ctl_password: password
        se_csp_qcow_image_file: avi-se.qcow2
        se_csp_mgmt_ip: 10.128.2.20
        se_csp_mgmt_mask: 255.255.255.0
        se_csp_default_gw: 10.128.2.1
        se_csp_service_name: avi-se
        se_csp_disk_size: 10
        se_csp_num_cpu: 2
        se_csp_memory_gb: 4
        se_csp_vnics:
          - nic: "0"
            type: access
            tagged: "false"
            network_name: enp1s0f0
          - nic: 1
            type: passthrough
            passthrough_mode: sriov
            vlan: 200
            network_name: enp7s0f0
          - nic: 2
            type: passthrough
            passthrough_mode: sriov
            vlan: 201
            network_name: enp7s0f1
        se_csp_bond_ifs: '1,2'
```

### CSP Example without Auto-registration
```

---
- hosts: csp_devices
  gather_facts: false
  collections:
    - vmware.alb
  tasks:
    - name: Deploy Avi SE csp
      import_role:
        name: avise_csp
      vars:
        se_autoregister: false
        se_auth_token: "auth token here"
        se_cloud_name: Default-Cloud
        se_tenant: admin
        se_csp_user: admin
        se_csp_password: password
        se_master_ctl_ip: 10.128.2.20
        se_csp_qcow_image_file: avi-se.qcow2 #please put relative/direct location of qcow image
        se_csp_mgmt_ip: 10.128.2.20
        se_csp_mgmt_mask: 255.255.255.0
        se_csp_default_gw: 10.128.2.1
        se_csp_service_name: avi-se
        se_csp_disk_size: 10
        se_csp_num_cpu: 2
        se_csp_memory_gb: 4
        se_csp_vnics:
          - nic: "0"
            type: access
            tagged: "false"
            network_name: enp1s0f0
          - nic: 1
            type: passthrough
            passthrough_mode: sriov
            vlan: 200
            network_name: enp7s0f0
          - nic: 2
            type: passthrough
            passthrough_mode: sriov
            vlan: 201
            network_name: enp7s0f1
        se_csp_bond_ifs: '1,2'
```

## License

Apache 2.0

## Author Information

contact: Avi Networks [avi-sdk@avinetworks.com]
