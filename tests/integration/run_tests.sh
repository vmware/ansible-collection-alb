#/bin/bash
echo "Started ansible integration tests execution."
python38=3.8
for version in 3.5 3.6 3.7 3.8 3.9
do
  cd ~/.ansible/collections/ansible_collections/vmware/alb
  echo "Ansible test runing on python version: $version"
  st=$((`echo "$version < $python38"| bc`))
  if [ $st -eq 1 ]
  then
    sudo ansible-test integration --exclude test_avi_serviceenginegroup --python $version --docker
  else
    sudo ansible-test integration --python $version --docker
  fi
done
echo "Ansible tests integration tests execution completed."
