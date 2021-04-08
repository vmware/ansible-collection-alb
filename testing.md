# Testing Ansible Collection: vmware.alb

### Testing with `ansible-test`

##### Install collection tar

```
$ ansible-galaxy collection install vmware-alb-1.0.0.tar.gz
$ cd ~/.ansible/collections/ansible_collections/vmware/alb
```
##### Run ansible tests

```
$ sudo ansible-test units --requirements -vvvv --docker
$ sudo ansible-test sanity --requirements -vvvv --docker
