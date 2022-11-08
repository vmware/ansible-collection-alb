############################################################################
# ========================================================================
# Copyright 2022 VMware, Inc.  All rights reserved. VMware Confidential
# ========================================================================
###
# SPDX-License-Identifier: Apache License 2.0

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
try:
    import sys
    from pyVmomi import vim
    HAS_IMPORT = True
except ImportError:
    HAS_IMPORT = False


def add_nic(vm, network_name):
    if not HAS_IMPORT:
        sys.exit("Import failed")
    spec = vim.vm.ConfigSpec()
    nic_changes = []
    nic_spec = vim.vm.device.VirtualDeviceSpec()
    nic_spec.operation = vim.vm.device.VirtualDeviceSpec.Operation.add
    nic_spec.device = vim.vm.device.VirtualE1000()
    nic_spec.device.deviceInfo = vim.Description()
    nic_spec.device.backing = \
        vim.vm.device.VirtualEthernetCard.NetworkBackingInfo()
    nic_spec.device.backing.useAutoDetect = False
    nic_spec.device.backing.deviceName = network_name
    nic_spec.device.connectable = vim.vm.device.VirtualDevice.ConnectInfo()
    nic_spec.device.connectable.startConnected = True
    nic_spec.device.connectable.allowGuestControl = True
    nic_spec.device.connectable.connected = True
    nic_spec.device.connectable.status = 'untried'
    nic_spec.device.wakeOnLanEnabled = True
    nic_spec.device.addressType = 'assigned'
    nic_changes.append(nic_spec)
    spec.deviceChange = nic_changes
    vm.ReconfigVM_Task(spec=spec)
