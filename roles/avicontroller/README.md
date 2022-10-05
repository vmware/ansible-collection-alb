# avinetworks.avicontroller


Using this module you are able to install the Avi Vantage Controlller, to your system. However, minimum requirements must be met.

> **Warning:**  
> This Ansible role is not meant to be ran repeatedly on the host. It's meant for deployment only. Once deployed the configuration for Avi is managed by Avi.

## Requirements

Requires Docker to be installed. We have created `avinetworks.docker` to install Docker on a host. Please run that role first, or manually install Docker.

## Role Variables

### Setting Deployment type

| Variable          | Required | Default  | Comments                                                                                   |
| ----------------- | -------- | -------- | ------------------------------------------------------------------------------------------ |
| `con_deploy_type` | No       | `docker` | Sets the type of deployment that should be triggered. Valid options: `docker`, `openshift` |

### Standard Parameters

| Variable                | Required | Default | Comments                                             |
| ----------------------- | -------- | ------- | ---------------------------------------------------- |
| `con_skip_requirements` | No       | `false` | Skips any requirements for disk space, ram, and cpu. |

### Package Deploy Variables

| Variable             | Required | Default                      | Comments                                  |
| -------------------- | -------- | ---------------------------- | ----------------------------------------- |
| `con_package_deploy` | No       | `false`                      | Set to true to deploy via package         |
| `con_package_source` | No       | `controller_docker.tgz`      | Source location of the docker tgz         |
| `con_package_dest`   | No       | `/tmp/controller_docker.tgz` | Destination location on the remote server |

### Docker Hub and Docker Repo Variables

| Variable                   | Required | Default                                    | Comments                                                  |
| -------------------------- | -------- | ------------------------------------------ | --------------------------------------------------------- |
| `con_docker_repo`          | No       | `None`                                     | If using a local repository please enter it here.         |
| `con_version`              | No       | `17.2.4-9024-20171127.023607`              | Version of the Avi Controller package you want to deploy. |
| `con_image`                | No       | `avinetworks/controller:{{ con_version }}` | Full name of the controller image.                        |
| `con_docker_repo_user`     | No       | `None`                                     | User to be used for repository authentication.            |
| `con_docker_repo_password` | No       | `None`                                     | Password to be used for repository authentication.        |

### Docker Deployment Variables

| Variable                     | Required | Default                                                   | Comments                                                                               |
| ---------------------------- | -------- | --------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `con_cores`                  | No       | `{{ ansible_processor_cores * ansible_processor_count }}` | How many cores the controller will use.                                                |
| `con_memory_gb`              | No       | `{{ ansible_memtotal_mb // 1024 }}`                       | How much memory the controller will use.                                               |
| `con_destination_disk`       | No       | `auto-detect based on ansible_mounts largest sized disk`  | The disk that the controller data will be installed                                    |
| `con_disk_path`              | No       | `{{ destination_disk }}opt/avi/controller/data`           | The path that the controller data will be installed.                                   |
| `con_disk_gb`                | No       | `30`                                                      | The size of the disk that will be used by controller data.                             |
| `con_metrics_disk_path`      | No       | `None`                                                    | The path that the controller metric data will be stored.                               |
| `con_metrics_disk_gb`        | No       | `None`                                                    | The size of the disk that will be used by metric data.                                 |
| `con_logs_disk_path`         | No       | `None`                                                    | The path that the controller log data will be stored.                                  |
| `con_logs_disk_gb`           | No       | `None`                                                    | The size of the disk that will be used by log data.                                    |
| `con_controller_ip`          | No       | `{{ ansible_default_ipv4.address }}`                      | The IP address of the controller.                                                      |
| `con_dev_name`               | No       | `auto-detect based on con_controller_ip`                  | The device name that will be used by the controller.                                   |
| `con_setup_json`             | No       | `None`                                                    | The source location of the setup.json file. Used to auto-configure a controller.       |
| `con_setup_json_raw`         | No       | `None`                                                    | Allows a user to input the setup.json data in YAML or JSON format directly in Ansible. |
| `con_fresh_install`          | No       | `false`                                                   | Erases any pre-existing directories associated with the controller.                    |
| `con_portal_http_port`       | No       | `80`                                                      | Port used for the controllers unsecured web interface.                                 |
| `con_portal_https_port`      | No       | `443`                                                     | Port used for the controllers secured web interface.                                   |
| `con_sysint_port`            | No       | `8443`                                                    | Port to be used by the controller communication interface.                             |
| `con_ssh_port`               | No       | `5098`                                                    | Port used to connect directly to the controllers ssh port.                             |
| `con_serviceengine_ssh_port` | No       | `5099`                                                    | Port used to connect directly to the service engines ssh port.                         |
| `con_cli_port`               | No       | `5054`                                                    | Port used to access the command line interface of the controller.                      |
| `con_snmp_port`              | No       | `161`                                                     | UDP port used to access the SNMP service on the controller.                            |
| `con_mounts_extras`          | No       | `[]`                                                      | Extra mounting points to be used by the controller.                                    |
| `con_env_variables_extras`   | No       | `[]`                                                      | Extra environment variables to be used by the controller.                              |
| `con_ports_list_extras`      | No       | `[]`                                                      | Extra ports to be used by the controller.                                              |
| `con_force_deploy`           | No       | `false`                                                   | Forces Ansible to run on the host, does not skip tasks.                                |

## Example Playbook

> **WARNING:**  
> Before using this example please make the correct changes required for your server.  
> For more information please visit <https://kb.avinetworks.com/avi-controller-sizing/>  
> It is recommended you adjust these parameters based on the implementation desired.

### Docker Deployment Examples

```yaml
- hosts: servers
  collections:
    - vmware.alb
  tasks:
    - name: Deploy Avi Controller 
      import_role:
        name: avicontroller
      vars:
        con_controller_ip: 10.10.27.101
        con_cores: 4                     # If not specified core count is 4
        con_memory_gb: 12                 # If not specified memory count is 12
```

The following is an example with minimum parameters.

```yaml
- hosts: servers
  collections:
    - vmware.alb
  tasks:
    - name: Deploy Avi Controller 
      import_role:
        name: avicontroller
```

The following is an example with specific 18.1.2 release

```yaml
---
- hosts: bm
  collections:
    - vmware.alb
  vars:
    avi_con_version: 18.1.2-9058-20180623.025526
  tasks:
    - name: Avi Controller | Setup docker
      include_role:
        name: avinetworks.docker
      become: yes
    - name: Avi Controller | Setup Controller
      include_role:
        name: avicontroller
      vars:
        con_controller_ip: "xxx"
        con_memory_gb: 20
        con_cores: 4|int
        con_fresh_install: True
        con_package_deploy: False
        con_version: "{{avi_con_version}}"
        con_image: avinetworks/controller:{{ con_version }}
        con_disk_gb: 50
```

## License

Apache 2.0

## Author Information

[Avi Networks](http://avinetworks.com)
