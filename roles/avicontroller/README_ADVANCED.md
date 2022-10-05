# avinetworks.avicontroller

This readme covers the advanced features of this role. These notes are for advanced users or customizing this role to use in unique environments including Development environments. Please use the following with extreme caution.

## Role Variables

### Parameter Override Variables
However, you are able to provide these parameters another way. Using the following variables. This will allow the user to customize all values.  
**!!!BEWARE: USING THIS WILL ERASE DEFAULTS - USE WITH CAUTION!!!**


```

con_env_variables_all:
  - "CONTAINER_NAME=avicontroller"
  - "MANAGEMENT_IP={{ con_controller_ip | string}}"
  - "NUM_CPU={{ con_cores }}"
  - "NUM_MEMG={{ con_memory_gb }}"
  - "DISK_GB={{ con_disk_gb }}"

con_mounts_all:
  - "/:/hostroot/"
  - "/var/run/docker.sock:/var/run/docker.sock"
  - "{{ con_disk_path }}:/vol/"

con_ports_list_all:
  - "5098:5098"
  - "80:80"
  - "443:443"
  - "8443:8443"
  - "5054:5054"
  - "161:161/udp"
```
