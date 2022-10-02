# ansible-role-avicontroller-kvm
Ansible Role to setup Avi Controller on KVM

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
|kvm_vm_base_img|Yes||controller.qcow2 file|
|kvm_vm_vcpus|No|8|How many cpus the controller will use.|
|kvm_vm_ram|No|24576 MB|How much memory the controller will use.|
|kvm_network_type|No|direct|Which network type you have to use.|
|kvm_network_source_mode|No|bridge|Which network bridge you have to use.|
|kvm_network_model|No|virtio|Which network model you have to use.|
|kvm_vm_os_disk_size|No|100|How much disk size the controller will use.|
|kvm_host_mgmt_intf|Yes||host management interface name|
|ctrl_mgmt_ip|Yes||Management Ip for the controller|
|ctrl_mgmt_mask|Yes||Subnet mast for the controller|
|ctrl_default_gw|Yes||Default gateway for controller|
|state|No|create|If create then it will create controller and for delete it will delete the controller.|
|kvm_pinning|Yes||If you want to enable pinning CPU for the VM|
|kvm_force_mode|No|true|If VM with the given name exist then it will overwrite to that VM and for false it will stop the execution.|

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
- hosts: kvm
  collections:
    - vmware.alb
  tasks:
    - name: Create KVM VM
      include_role:
        name: avicontroller_kvm
      vars:
        kvm_vm_hostname: "ctrl1"
        kvm_host_mgmt_intf: eno1.100
        ctrl_mgmt_ip: 10.130.5.12
        ctrl_mgmt_mask: 255.255.255.0
        ctrl_default_gw: 10.130.5.1
        kvm_pinning: true
```

<b>Command to run the playbook </b>

```
ansible-playbook kvm.yml -i <inventory file> -vv
```
