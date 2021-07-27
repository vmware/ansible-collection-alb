## Integration Testing With Ansible Collection: vmware.alb

##### How to install collection
```
$ ansible-galaxy collection install vmware.alb
$ cd ~/.ansible/collections/ansible_collections/vmware/alb
```

#### Configure integration_config.yml
Update integration_config.yml with live controller details.

```
---
avi_credentials:
  controller: "<controller_ip>"
  username: "<controller_username>"
  password: "<controller_password>"
  api_version: "<api_version>"
```

#### Install the requirements
```
$ pip install -r requirements.txt
```

##### Run ansible tests
Run all the integration targets

```
$ sudo ansible-test integration --exclude test_avi_serviceenginegroup --docker
```

Run the specific integration target
```
$ sudo ansible-test integration test_avi_healthmonitor --docker
```
Run all the integration targets with specific python version
```
$ sudo ansible-test integration --python 3.8 --docker
```
Run specific integration targets with specific python version
```
$ sudo ansible-test integration test_avi_serviceenginegroup --python 3.8 --docker
```
Run excluding specific integration targets with specific python version
```
$ sudo ansible-test integration --exclude test_avi_serviceenginegroup --python 3.6 --docker
```

Run all tests with different python matrix
```
$ cd ~/.ansible/collections/ansible_collections/vmware/alb
$ ./tests/integration/run_tests.sh
```


**Notes**
- Target test_avi_serviceenginegroup will pass only for python version 3.8 (Known error: Unable to import avi_serviceenginegroup due to more than 255 arguments)