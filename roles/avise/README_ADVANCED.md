# vmware.alb.avise

This readme covers the advanced features of this role. These notes are for advanced users or customizing this role to use in unique environments including Development environments. Please use the following with extreme caution.

## Role Variables

### Parameter Override Variables
However, you are able to provide these parameters another way. Using the following variables. This will allow the user to customize all values.  
**!!!BEWARE: USING THIS WILL ERASE DEFAULTS - USE WITH CAUTION!!!**

```

se_env_variables_all:
  - "CONTAINER_NAME=avise"
  - "CONTROLLERIP=10.10.27.101""
  - "NTHREADS=4"
  - "SEMEMMB=4096"
  - "DOCKERNETWORKMODE=HOST"

se_mounts_all:
  - "/mnt:/mnt"
  - "/dev:/dev"
  - "/etc/sysconfig/network-scripts:/etc/sysconfig/network-scripts"
  - "/:/hostroot/"
  - "/etc/hostname:/etc/host_hostname"
  - "/etc/localtime:/etc/localtime"
  - "/var/run/docker.sock:/var/run/docker.sock"
  - "/opt/avi/se/data:/vol/"
```
