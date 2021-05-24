# Testing Ansible Collection: vmware.alb

##### Generate ansible collections artifacts
To test the vmware.alb collection first you need to setup the develop environment inside the dev machine
after that hit the following command in build directory to generate collections artifacts

```
$ make ansible_code_gen
```


##### Testing with `ansible-test`

##### Build & Install collection tar

```
$ cd /path/to/generated/collections/directory
$ ansible-galaxy collection build
$ ansible-galaxy collection install vmware-alb-1.0.0.tar.gz
$ cd ~/.ansible/collections/ansible_collections/vmware/alb
```
##### Run ansible tests

```
$ sudo ansible-test units --requirements -vvvv --docker
$ sudo ansible-test sanity --requirements -vvvv --docker
