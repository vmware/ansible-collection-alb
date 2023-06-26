# vmware.alb.avise

Using this module you are able to install the Avi Vantage Service Engine, to your system. However, minimum requirements must be met. Please visit the Avi SE Requirements webpage: https://kb.avinetworks.com/docs/latest/system-requirements-hardware/

## Requirements

- Docker is required, and can be installed using `avinetworks.docker` or manually installed.  

- `avisdk` python library is required and can be installed by:  
`pip install avisdk --upgrade`  

## Role Dependencies

- avinetworks.avisdk
  - To install these use the following command: `ansible-galaxy install -f avinetworks.avisdk`  

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
| `se_leader_ctl_ip` | No | `None` | The IP address of the controller. |
| `se_leader_ctl_username` | No | `None` | The username to login into controller api. <br>**Not required when `se_autoregister: false`** |
| `se_leader_ctl_password` | No | `None` | The passowrd to login into the controller api. <br>**Not required when `se_autoregister: false`** |
| `se_cloud_name` | No | `Default-Cloud` | Name of cloud the SE should auto-register with. |
| `se_tenant` | No | `admin` | Name of se_tenant the SE should auto-register with. |
| `segroup_uuid` | No | `None` | Uuid of segroup_uuid the SE should auto-register with. |

### Package Deploy Variables
| Variable | Required | Default | Comments |
|----------|----------|---------|----------|
| `se_package_deploy` | No | `false` | Set to true to deploy via package. |
| `se_package_source` | No | `se_docker.tgz` | Source location of the docker tgz |
| `se_package_dest` | No | `/tmp/se_docker.tgz` | Destination location on the remote server |

### Docker Hub and Docker Repo Variables
| Variable | Required | Default | Comments |
|----------|----------|---------|----------|
| `se_docker_repo` | No | `None` | If using a local repository please enter it here. |
| `se_version` | No | `latest` | Version of the Avi Service Engine package you want to deploy. |
| `se_image` | No | `avinetworks/se:{{ se_version }}` | Full name of the service engine image. |
| `se_docker_repo_user` | No | `None` | User to be used for repository authentication. |
| `se_docker_repo_password` | No | `None` | Password to be used for repository authentication. |

### Docker Deployment Variables
| Variable | Required | Default | Comments |
|-----------------------|----------|-----------|---------|
| `se_dpdk` | No | `false` | When set to true performs se_dpdk installation. |
| `se_inband_mgmt` | No | `false` | Enables inband management interface for this Service Engine (i.e. Use Management interface for data traffic as well). |
| `se_cores` | No | `{{ ansible_processor_cores * ansible_processor_count }}` | How many cores the service engine will use. |
| `se_memory_gb` | No | `{{ ansible_memtotal_mb / 1024 }}` | How much memory the service engine will use.  |
| `se_destination_disk` | No | auto-detect based on `ansible_mounts` largest sized disk | The disk that the service engine data will be installed |
| `se_disk_path` | No | `{{ se_destination_disk }}opt/avi/se/data` | The path that the service engine data will be installed. |
| `se_disk_gb` | No | `10` | The size of the disk that will be used by service engine data. |
| `se_logs_disk_path` | No | `None` | The path that the service engine log data will be stored. |
| `se_logs_disk_gb` | No | `None` | The size of the disk that will be used by log data. |
| `se_fresh_install` | No | `false` | Erases any pre-existing directories associated with the service engine. |
| `se_mounts_extras` | No | `[]` | Extra mounting points to be used by the service engine. <br>No need to include the `-v` |
| `se_env_variables_extras` | No | `[]` | Extra environment variables to be used by the service engine. <br>No need to include `-e` |

## Example Playbooks

**WARNING:**
**Before using this example please make the correct changes required for your server. For more information please visit [https://kb.avinetworks.com/sizing-service-engines/] (https://kb.avinetworks.com/sizing-service-engines/)**

**It is recommended you adjust these parameters based on the implementation desired.**
### Standard Example
```

- hosts: service_engines
  gather_facts: false
  collections:
    - vmware.alb
  tasks:
    - name: Deploy Avi dockersied SE
      import_role:
        name: avise
      vars:
        se_leader_ctl_ip: 10.10.27.101
        se_leader_ctl_username: admin
        se_leader_ctl_password: avi123
        se_disk_gb: 60
        se_cores: 4
        se_memory_gb: 12
```

### Minimum Example
```

- hosts: service_engines
  gather_facts: false
  collections:
    - vmware.alb
  tasks:
    - name: Deploy Avi dockersied SE
      import_role:
        name: avise
      vars:
        se_leader_ctl_ip: 10.10.27.101
        se_leader_ctl_username: admin
        se_leader_ctl_password: avi123
```

### Example without Auto-registration
```

- hosts: all
  gather_facts: false
  collections:
    - vmware.alb
  tasks:
    - name: Deploy Avi dockersied SE
      import_role:
        name: avicontroller_csp
      vars:
        se_leader_ctl_ip: 10.10.27.101
        se_auth_token: "{{ se_auth_token }}"
```

