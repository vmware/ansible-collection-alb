# vmware.alb.avicontroller_vmware

Using this module you are able to install the Avi Vantage Controlller, to Vmware cloud.

Requirements
------------
 - python >= 2.6
 - pyVmomi
 - pyVim
 - ovftool (Installation bundle packaged with the role please run command '<roles_dir>/avinetworks.avicontroller-vmware/files/VMware-ovftool-4.1.0-2459827-lin.x86_64.bundle' to install ovftool)

Role Variables
--------------

| Variable | Required | Default | Comments |
|----------|----------|---------|----------|
|ovftool_path|Yes||Path for VMWare ovftool|
|vcenter_host|Yes||VMWare host IP|
|vcenter_user|Yes||VMWare user name|
|vcenter_password|Yes||VMWare password|
|ssl_verify|No|False|ovftool sslverify option|
|state|No|present|Option to specify create or destroy the infra|
|con_datacenter|No|Picked first from the list|Name of VMWare datacenter|
|con_cluster|No|Picked from the first in the list of given datacenters clusters|Name of a cluster in the datacenter|
|con_datastore|No|Picked up the datastore having max free space|Name of datastore on which VM to be deployed|
|con_mgmt_network|Yes||Management network name|
|con_disk_mode|No|thin|Deployment disk mode|
|con_ova_path|Yes||Path to controller OVA file|
|con_vm_name|Yes||Name of a controller VM on VMWare|
|con_power_on|No|True|VM to be powered on after provisioning|
|con_vcenter_folder|No|Datacenter root|Folder path to deploy VM|
|con_mgmt_ip|No||Static IP for the controller|
|con_mgmt_mask|No||Management IP Mask|
|con_default_gw|No||Default gateway of management network|
|con_sysadmin_public_key|No||Public key file path|
|con_number_of_cpus|No||Number of CPUs for controller|
|con_cpu_reserved|No||CPU reservation in megahertz|
|con_memory|No||Controller memory in MB|
|con_memory_reserved|No||Controller memory reservation in MB|
|con_disk_size|No||Controller disk size in GB|
|con_ovf_properties|No||Other Controller ovf properties in key value format|

Dependencies
------------



Example Playbook
----------------

Including an example of how to use your role:

```
- hosts: localhost
  connection: local
  collections:
    - vmware.alb
  tasks:
    - name: Deploy Avi Controller
      avi_deploy_controller:
        ovftool_path: /usr/lib/vmware-ovftool
        vcenter_host: '{{ vcenter_host }}'
        vcenter_user: '{{ vcenter_user }}'
        vcenter_password: '{{ vcenter_password }}'
        con_datacenter: 10GTest
        con_cluster: Arista
        con_mgmt_network: Mgmt_Ntwk_3
        con_ova_path: ./controller.ova
        con_vm_name: ansible-test-controller
        con_power_on: true
        con_vcenter_folder: network/avi
```
Example using including role [version parameter is required while including the role]
```
- hosts: localhost
  connection: local
  collections:
    - vmware.alb
  tasks:
    - name: Avi Controller | Vmware | Configure VMware controller
      include_role:
        name: avicontroller_vmware
      vars:
        ovftool_path: /usr/bin/
        vcenter_host: '{{ vcenter_host }}'
        vcenter_user: '{{ vcenter_user }}'
        vcenter_password: '{{ vcenter_password }}'
        con_datacenter: '{{ con_datacenter }}'
        con_cluster: '{{ con_cluster }}'
        con_mgmt_network: '{{ con_mgmt_network }}'
        con_ova_path: ./controller.ova
        con_vm_name: ansible_ctr
        con_power_on: false
        con_number_of_cpus: 8
        con_memory: 30720
        con_cpu_reserved: 1028
        con_memory_reserved: 2048
        con_disk_size: 128
        con_vcenter_folder: /folder/path
        state: present
        con_datastore: '{{ con_datastore }}'
```

License
-------

Apache 2.0

Author Information
------------------

contact: Avi Networks [avi-sdk@avinetworks.com]
