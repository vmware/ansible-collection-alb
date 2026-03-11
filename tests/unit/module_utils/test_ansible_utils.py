
############################################################################
# ========================================================================
# Copyright 2021 VMware, Inc.  All rights reserved. VMware Confidential
# ========================================================================
###

# Copyright 2021 VMware, Inc.  All rights reserved. VMware Confidential
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.vmware.alb.plugins.module_utils.utils.ansible_utils import (avi_obj_cmp, ref_n_str_cmp)

new_obj = {
    "name": "testpool1",
    "description": "testpool1",
    "servers": [
        {
            "ip": {
                "addr": "192.168.2.20",
                "type": "V4"
            }
        }
    ]
}


existing_object = {
    "name": "testpool1",
    "description": "testpool1",
    "servers": [
        {
            "ip": {
                "addr": "192.168.2.20",
                "type": "V4"
            }
        }
    ]
}


def test_compare_single_value():
    """
    If both objects are equal then it return true
    If both objects are not equal then it return false
    True if x is subset of y else False
    """
    health_monitor = "https://192.168.11.18:/api/healthmonitor?name=System-HTTPS"
    existing_health_monitor = "https://192.168.11.18:/api/healthmonitor?name=System-HTTP"
    exist = not ref_n_str_cmp(health_monitor, existing_health_monitor)
    assert exist


def test_compare_object():
    """
    If both objects are equal then it return true
    If both objects are not equal then it return false
    """
    exist = avi_obj_cmp(new_obj, existing_object)
    assert exist
