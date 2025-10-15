#!/bin/sh
branch_version=${branch_version:-"v1.0"}
controller_ip=${controller_ip:-"127.0.0.1"}
vcenter_host=${vcenter_host:-"vcenter.local"}
vcenter_username=${vcenter_username:-"administrator@vsphere.local"}
vcenter_password=${vcenter_password:-"password"}
datacenter=${datacenter:-"Datacenter1"}
cluster=${cluster:-"Cluster1"}
network=${network:-"VM Network"}
vcenter_folder=${vcenter_folder:-"Folder1"}
ovftool_path=${ovftool_path:-"/usr/bin/ovftool"}
ova_path=${ova_path:-"/tmp/controller.ova"}
config_file="tests/integration/integration_config.yml"

sed -i "s#<<api_version>>#$branch_version#g" "$config_file"
sed -i "s#<<controller>>#$controller_ip#g" "$config_file"
sed -i "s#<<username>>#admin#g" "$config_file"
sed -i "s#<<password>>#admin#g" "$config_file"
sed -i "s#<<vcenter_host>>#$vcenter_host#g" "$config_file"
sed -i "s#<<vcenter_username>>#$vcenter_username#g" "$config_file"
sed -i "s#<<vcenter_password>>#$vcenter_password#g" "$config_file"
sed -i "s#<<datacenter>>#$datacenter#g" "$config_file"
sed -i "s#<<cluster>>#$cluster#g" "$config_file"
sed -i "s#<<network>>#$network#g" "$config_file"
sed -i "s#<<vcenter_folder>>#$vcenter_folder#g" "$config_file"
sed -i "s#<<ovftool_path>>#$ovftool_path#g" "$config_file"
sed -i "s#<<con_ova_path>>#$ova_path#g" "$config_file"
sed -i "s#<<con_vm_name>>#ansible-test-controller#g" "$config_file"

echo "Started ansible integration tests execution."
python38=3.8
for version in 3.5 3.6 3.7 3.8 3.9
do
    collection_dir="$HOME/.ansible/collections/ansible_collections/vmware/alb"

    cd "$collection_dir" || { echo "Failed to cd into $collection_dir"; exit 1; }

    echo "Ansible test running on python version: $version"

    # Compare Python version using bc
    if ( echo "$version < $python38" | bc ); then
        sudo ansible-test integration \
            --exclude test_avi_serviceenginegroup \
            --python "$version" \
            --docker \
            --docker-privileged
    else
        sudo ansible-test integration \
            --python "$version" \
            --docker \
            --docker-privileged
    fi
done

echo "Ansible tests integration tests execution completed."
