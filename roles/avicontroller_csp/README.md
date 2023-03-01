# avinetworks.avicontroller-csp

Using this module you are able to install the Avi Vantage Controlller, to your system. However, minimum requirements must be met.

> **Warning:**  
> This Ansible role is not meant to be ran repeatedly on the host. It's meant for deployment only. Once deployed the configuration for Avi is managed by Avi.

## Requirements

A Cisco CSP Device

## Role Variables

### CSP Deployment Variables

These are only marked required, for when you are using CSP Deployment.

| Variable                    | Required | Default           | Comments                                                                         |
| --------------------------- | -------- | ----------------- | -------------------------------------------------------------------------------- |
| `con_csp_user`              | Yes      | `None`            | Username that will be used to connect to the CSP server                          |
| `con_csp_password`          | Yes      | `None`            | Password required to authenticate the user                                       |
| `con_csp_qcow_image_file`   | No       | `controller.qcow` | Relative or absolute location of the controller qcow                             |
| `con_csp_mgmt_ip`           | Yes      | `None`            | IP of the controller on the management network.                                  |
| `con_csp_mgmt_mask`         | Yes      | `None`            | Subnet mask that the controller will require.                                    |
| `con_csp_default_gw`        | Yes      | `None`            | Default gateway for the controller.                                              |
| `con_csp_disk_size`         | No       | `64`              | Amount of disk space in GB for the controller.                                   |
| `con_csp_disk_type`         | No       | `virtio`          | Disk type in CSP. Recommended to use the default.                                |
| `con_csp_service_name`      | No       | `avi-controller`  | Name of the service to be created on the CSP.                                    |
| `con_csp_num_cpu`           | No       | `4`               | Number of CPUs to be allocated to the Controller                                 |
| `con_csp_memory_gb`         | No       | `16`              | Amount of memory in GB allocated to the Controller                               |
| `con_csp_hsm_ip`            | No       | `None`            | IP Address and Subnet for Dedicated HSM interface, ex. 10.160.100.221/24         |
| `con_csp_hsm_mask`          | No       | `None`            | Netmask of the interface that will talk to HSM                                   |
| `con_csp_hsm_static_routes` | No       | `None`            | Static routes for HSM, ex. 10.128.1.0/24 via 10.160.100.1                        |
| `con_csp_hsm_vnic_id`       | No       | `None`            | VNIC id, of the HSM interface configured on this interface ex. 1                 |
| `con_csp_bond_ifs`          | No       | `None`            | Bonds the listed interfaces together. Ex. '1,2 3,4' bonds 1 with 2, and 3 with 4 |
| `con_csp_platform`          | No       | `csp-2100`        | CSP platform model.                                                              |

## Example Playbook

> **WARNING:**  
> Before using this example please make the correct changes required for your server.  
> For more information please visit <https://kb.avinetworks.com/avi-controller-sizing/>  
> It is recommended you adjust these parameters based on the implementation desired.

### CSP Deployment Example

> **Note:**  
> When running. `gather_facts` needs to be set to `false`, failure to do so will cause Ansible failure on first step.

```yaml
---
- hosts: csp_devices
  gather_facts: false
  collections:
    - vmware.alb
  tasks:
    - name: Deploy Avi Controller csp
      import_role:
        name: avicontroller_csp
      vars:
        con_deploy_type: csp
        con_csp_user: admin
        con_csp_password: password
        con_csp_qcow_image_file: avi-controller.qcow2
        con_csp_mgmt_ip: 10.128.2.20
        con_csp_mgmt_mask: 255.255.255.0
        con_csp_default_gw: 10.128.2.1
        con_csp_service_name: avi-controller
        con_csp_memory_gb: 32
        con_csp_num_cpu: 16
        con_csp_vnics:
          - nic: '0'
            type: access
            tagged: 'false'
            network_name: enp1s0f0
        con_csp_bond_ifs: '1,2'   
```

## License

Apache 2.0

## Author Information

[Avi Networks](https://avinetworks.com)

Avi SDK Team
avi-sdk@avinetworks.com
