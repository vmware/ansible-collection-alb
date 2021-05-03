# avinetworks.aviconfig

[![Build Status](https://travis-ci.org/avinetworks/ansible-role-aviconfig.svg?branch=master)](https://travis-ci.org/avinetworks/ansible-role-aviconfig)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-avinetworks.aviconfig-blue.svg)](https://galaxy.ansible.com/avinetworks/aviconfig/)


This role provides ability for user to configure Avi by simply providing a dictionary of avi configuration objects.
This role invokes the right Avi Ansible modules as tasks in correct order ensuring consistent and successful configuration.

## Requirements

 - python >= 2.7
 - avisdk

This role requires Ansible 2.2 or higher. Requirements are listed in the metadata file.

Please install avisdk from pip prior to running this module.
```bash

pip install avisdk --upgrade
```

## Installation

To install the aviconfig Ansible Module, please issue the command on the machine you will run Ansible from.
```bash

ansible-galaxy install avinetworks.aviconfig
```

For more information please visit http://docs.ansible.com/ansible/galaxy.html

## Role Variables

### avi_config ###
This is dictionary of all the Avi REST resources user wants to setup. Aviconfig role calls the Avi Ansible Modules to configure these settings in Avi Controller.
Eg.

```yaml

- name: defining avi config
  set_fact:
    avi_config:
      pool:
        - name: "foo-pool"
          lb_algorithm: LB_ALGORITHM_ROUND_ROBIN
          servers:
            - ip:
                 addr: "42.42.42.42"
                 type: 'V4'
      virtualservice:
        - name: foo
          services:
            - port: 80
          pool_ref: "/api/pool?name=foo-pool"
          vip:
            - ip_address:
                addr: "10.10.10.10"
                type: 'V4'
              vip_id: '1'

- name: Avi Application | Setup Foo
  import_role:
    name: avinetworks.aviconfig
  vars:
    avi_config: "{{avi_config}}"
```

### avi_config_file ###
This provides location to the role to read the Avi configuration objects. It loads variable avi_config from this file if defined. Eg.

```yaml

- name: Avi Application | Setup VMWare Cloud with Write Access
  import_role:
    name: avinetworks.aviconfig
  vars:
    avi_config_file: application/config.yml
```

### avi_creds_file ###
This provides location of credential variables for Avi Controller. Typically this should be an Ansible vault file.
Eg.

```yaml

- name: Avi Application | Setup VMWare Cloud with Write Access
  import_role:
    name: avinetworks.aviconfig
  vars:
    avi_config_file: application/config.yml
    avi_creds_file: credentials/creds.yml
```


### avi_config_state ###
This is a global override to delete all Avi REST objects that are listed in the avi_config directory. This is useful to create a full configuration and then delete all objects.

```yaml

avi_config_state=absent
Eg. ansible-playbook site_applications.yml --extra-vars "site_dir=`pwd` avi_config_state=absent"
```


## Example Playbooks

```yaml
---
- hosts: localhost
  connection: local
  roles:
    - role: avinetworks.avisdk
  tasks:
    - name: Avi Application | Setup foo
      import_role:
        name: avinetworks.aviconfig
      vars:
        avi_config_file: "foo/config.yml"
        avi_creds_file: "vars/creds.yml"
```

This example shows usage of how to create avi_config as part of task and pass it to role.

```yaml
---
- hosts: localhost
  connection: local
  roles:
    - role: avinetworks.avisdk
  tasks:
    - name: defining avi config
      set_fact:
        avi_config:
          pool:
            - name: foo-pool
              lb_algorithm: LB_ALGORITHM_ROUND_ROBIN
              servers:
                - ip:
                     addr: 42.42.42.42
                     type: V4
          virtualservice:
            - name: foo
              services:
                - port: 80
              pool_ref: "/api/pool?name=foo-pool"
              vip:
                - ip_address:
                    addr: 10.10.10.10
                    type: V4
                  vip_id: '1'

    - name: Avi Application | Setup foo
      import_role:
        name: avinetworks.aviconfig
      vars:
        avi_config: "{{avi_config}}"
        avi_creds_file: "vars/creds.yaml"
```

There are many more examples located at [https://github.com/avinetworks/devops/tree/master/ansible](https://github.com/avinetworks/devops/tree/master/ansible).

## License

Apache 2.0

## Author Information

Gaurav Rastogi

github: grastogi23

[https://www.linkedin.com/in/grrastogi]
