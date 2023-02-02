# ansible-role-avise-kvm
Ansible Role to setup Avi Service Engines in KVM environment.

Requirements
------------
 - python >= 2.6
 - avisdk : It can be installed by `pip install avisdk --upgrade`
 - avinetworks.avisdk : It can be installed by `ansible-galaxy install -f avinetworks.avisdk`

Role Variables
--------------

| Variable | Required | Default | Comments |
|----------|----------|---------|----------|
|kvm_vm_hostname|Yes||Name for VM|
|kvm_vm_base_img|No||se.qcow2 file|
|kvm_vm_vcpus|No|2|How many cpus the service engine will use.|
|kvm_vm_ram|No|2048|How much memory the service engine will use.|
|kvm_vm_os_disk_size|No|20|How much disk size the service engine will use.|
|kvm_host_mgmt_intf|Yes||host management interface name|
|se_kvm_ctrl_ip|Yes||The IP address of the controller.|
|se_kvm_ctrl_username|Yes||The username to login into the controller.|
|se_kvm_ctrl_password|Yes||The password to login into the controller.|
|se_kvm_ctrl_version|Yes||The controller version.|
|state|No|create|If create then create service engine and for delete it will delete the service engine.|
|se_auth_token|No||If defined it will be the token used to register the service engine to the controller|
|kvm_force_mode|No|true|If VM with the given name exist then it will overwrite to that VM and for false it will stop the execution.|
|se_bond_seq|Yes||Bonding sequence|
|se_kvm_mgmt_ip|Yes||Management Ip for the service engine|
|se_kvm_mgmt_mask|Yes||Subnet mask|
|se_kvm_default_gw|Yes||Default gateway for service engine|
|kvm_pinning|Yes||If you want to enable pinning CPU for the VM|
|kvm_total_num_vfs|Yes||Numbers VFs will be pass-through to VM|
|kvm_virt_intf_name|Yes||Virtual Function name will be pass-through to VM|
|se_image_gen_timeout|No|700|Timeout value for SE image generation|


### Standard Example
<b>Kvm host (inventory) file </b>

```
[kvm]
10.170.5.51
[kvm:vars]
ansible_ssh_user=root
ansible_ssh_pass=<password>
```

```
- hosts: all
  collections:
    - vmware.alb
  tasks:
    - name: Avi SE | KVM | Create SE VM on KVM
      include_role:
        name: avise_kvm
      vars:
        state: create
        kvm_vm_hostname: "se1"
        kvm_vm_vcpus: "2"
        kvm_vm_ram: "2048"
        kvm_host_mgmt_intf: eno1.100
        se_kvm_ctrl_ip: "10.170.5.21"
        se_kvm_ctrl_username: "admin"
        se_kvm_ctrl_password: "<controller password>"
        se_kvm_ctrl_version: "18.2.2"
        se_bond_seq: "1,2,3,4"
        se_kvm_mgmt_ip: "10.170.5.15"
        se_kvm_mgmt_mask: "255.255.255.0"
        se_kvm_default_gw: "10.170.5.1"
        kvm_pinning: true
        kvm_total_num_vfs: 4
        kvm_virt_intf_name:
          - enp24s17f1
          - enp24s17f3
          - enp24s17f5
          - enp24s17f7

```
<b>Command to run the playbook </b>
```
ansible-playbook kvm.yml -i <inventory file> -vv
```

