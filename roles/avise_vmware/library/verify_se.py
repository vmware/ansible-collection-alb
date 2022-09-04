#!/usr/bin/python

import json
from ansible.module_utils.basic import AnsibleModule
import time
import requests
import atexit
from pyVim.connect import SmartConnectNoSSL, Disconnect
from pyVmomi import vim
try:
    from __main__ import display
except ImportError:
    from ansible.utils.display import Display
    display = Display()

try:
    from pkg_resources import parse_version
    import avi.sdk
    from avi.sdk.avi_api import (ApiSession, ObjectNotFound, APIError, ApiResponse,
                             avi_timedelta, sessionDict)

    sdk_version = getattr(avi.sdk, '__version__', None)
    if ((sdk_version is None) or
            (sdk_version and
             (parse_version(sdk_version) < parse_version('17.1')))):
        # It allows the __version__ to be '' as that value is used in development builds
        raise ImportError
    HAS_AVI = True
except ImportError:
    HAS_AVI = False



def get_vm_by_name(si, vm_name):
    '''
    Get vm instance by name
    :param si: vcenter conection instance
    :param vm_name: name of the vm
    :return: vm instance
    '''
    container = si.content.viewManager.CreateContainerView(
        si.content.rootFolder, [vim.VirtualMachine], True)
    for vm in container.view:
        if vm.name == vm_name:
            return vm
    return None


def get_vm_ip_by_network(target_vm, network):
    '''
    Try to get the IP for the network on target_vm
    :param target_vm: vm instance
    :param network: VM network name
    :return: IP address for the network if found otherwise empty string
    '''
    ip_address = ''
    for nic in target_vm.guest.net:
        if nic.network == network:
            addresses = nic.ipConfig.ipAddress
            for adr in addresses:
                if adr.state == 'preferred':
                    ip_address = adr.ipAddress
                    break
    return ip_address

def main():
    module = AnsibleModule(
        argument_spec=dict(
            se_master_ctl_ip=dict(required=True, type='str'),
            se_master_ctl_username=dict(required=True, type='str'),
            se_master_ctl_password=dict(required=True, type='str', no_log=True),
            se_master_ctl_version=dict(required=True, type='str'),
            se_cloud_name=dict(required=True, type='str'),
            se_group_name=dict(required=True, type='str'),
            se_tenant=dict(required=True, type='str'),
            se_vmw_vm_name=dict(required=True, type='str'),
            se_vmw_mgmt_ip=dict(required=False, type='str'),
            se_vmw_ovf_networks=dict(required=False, type='dict'),
            vcenter_host=dict(required=True, type='str'),
            vcenter_user=dict(required=True, type='str'),
            vcenter_password=dict(required=True, type='str', no_log=True),
            max_se_up_wait=dict(required=False, type='int', default=600),
        ),
        supports_check_mode=False,
    )

    if not HAS_AVI:
        return module.fail_json(msg=(
            'Avi python API SDK (avisdk>=17.1) is not installed. '
            'For more details visit https://github.com/avinetworks/sdk.'))

    se_mgmt_ip = ''
    se_vm_name = module.params['se_vmw_vm_name']
    my_deployed_se = None
    mgmt_network = None
    se_vm = None

    if module.params.get('se_vmw_mgmt_ip', None):
        se_mgmt_ip = module.params['se_vmw_mgmt_ip']
    elif module.params.get("se_vmw_ovf_networks", None):
        #If there is no  se_vmw_mgmt_ip provided and only se_vmw_ovf_networks is available then
        #get the SE VM instance to find DHCP IP
        ovf_networks = module.params.get("se_vmw_ovf_networks")
        if "Management" in ovf_networks:
            mgmt_network = ovf_networks["Management"]
            try:
                si = SmartConnectNoSSL(host=module.params['vcenter_host'],
                                       user=module.params['vcenter_user'],
                                       pwd=module.params['vcenter_password'])
                atexit.register(Disconnect, si)
            except vim.fault.InvalidLogin:
                return module.fail_json(
                    msg='exception while connecting to vCenter, login failure, '
                        'check username and password')
            except requests.exceptions.ConnectionError:
                return module.fail_json(
                    msg='exception while connecting to vCenter, check hostname, '
                        'FQDN or IP')
            se_vm = get_vm_by_name(si, se_vm_name)
            if not se_vm:
                module.fail_json(msg='No Vm with name %s found' % se_vm)

    api = ApiSession.get_session(
        module.params['se_master_ctl_ip'],
        module.params['se_master_ctl_username'],
        password=module.params['se_master_ctl_password'],
        tenant=module.params['se_tenant'])

    path = 'serviceengine'
    gparams = {
        'cloud_ref.name': module.params['se_cloud_name']
    }

    interval = 5
    retries = module.params.get("max_se_up_wait")/interval
    initial_interval = 10
    step = 0
    time.sleep(initial_interval)
    while step < retries:
        if mgmt_network and not se_mgmt_ip:
            #try to get the mgmt IP(DHCP as no se_vmw_mgmt_ip provided) for the SE if it's not present
            #If no IP found try to get the SE from controller by its name for current iteration
            se_mgmt_ip = get_vm_ip_by_network(se_vm, mgmt_network)
        rsp = api.get(path, tenant=module.params['se_tenant'],
                            params=gparams, api_version=module.params['se_master_ctl_version'])
        rsp_data = rsp.json()
        for item in rsp_data['results']:
            if (item['name'] == se_vm_name or item['name'] == se_mgmt_ip) and item['se_connected']:
                my_deployed_se = item
                break

        if my_deployed_se != None:
            mymsg = 'Service Engine \'%s\' is deployed and is connected to the Controller %s' % (
                my_deployed_se['name'], module.params['se_master_ctl_ip'])
            return module.exit_json(changed=True, msg=(mymsg), se_details=my_deployed_se)
        time.sleep(interval)
        step += 1

    return module.fail_json(msg='Could not verify SE connection to the controller!')

if __name__ == "__main__":
    main()
