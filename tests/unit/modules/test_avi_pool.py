
############################################################################
# ========================================================================
# Copyright 2021 VMware, Inc.  All rights reserved. VMware Confidential
# ========================================================================
###

# Copyright 2021 VMware, Inc.  All rights reserved. VMware Confidential
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import json
import os
import unittest
from ansible.module_utils import basic
from ansible.module_utils.common.text.converters import to_bytes
from ansible_collections.vmware.alb.plugins.modules import avi_pool

try:
    from unittest.mock import MagicMock
except ImportError:
    from mock import MagicMock

fixture_path = os.path.join(os.path.dirname(__file__), 'fixtures')
with open(fixture_path + '/avi_pool.json') as json_file:
    data = json.load(json_file)


def set_module_args(args):
    args = json.dumps({'ANSIBLE_MODULE_ARGS': args})
    basic._ANSIBLE_ARGS = to_bytes(args)


class TestAviCloud(unittest.TestCase):

    def test_create_pool(self):
        set_module_args({
            "avi_credentials": {
                "controller": "192.168.15.18",
                "username": "admin",
                "password": "password",
                "api_version": "21.1.1"
            },
            "state": "present",
            "name": "testpool1",
            "description": "testpool1",
            "health_monitor_refs": [
                "/api/healthmonitor?name=System-HTTP"
            ],
            "servers": [
                {
                    "ip": {
                        "addr": "192.168.15.19",
                        "type": "V4"
                    }
                },
                {
                    "ip": {
                        "addr": "192.168.15.20",
                        "type": "V4"
                    }
                }
            ]
        })
        avi_pool.avi_ansible_api = MagicMock(return_value=data['mock_create_resp'])
        response = avi_pool.main()
        assert response['changed']

    def test_put_on_pool(self):
        set_module_args({
            "avi_credentials": {
                "controller": "192.168.15.18",
                "username": "admin",
                "password": "password",
                "api_version": "21.1.1"
            },
            "state": "present",
            "avi_api_update_method": "patch",
            "avi_api_patch_op": "replace",
            "uuid": "pool-7d5dc50b-5624-4992-a69a-eb2f0770cd65",
            "name": "testpool1",
            "description": "testpool1",
            "health_monitor_refs": [
                "/api/healthmonitor?name=System-HTTP"
            ],
            "servers": [
                {
                    "ip": {
                        "addr": "192.168.15.19",
                        "type": "V4"
                    }
                },
                {
                    "ip": {
                        "addr": "192.168.15.21",
                        "type": "V4"
                    }
                }
            ]
        })
        avi_pool.avi_ansible_api = MagicMock(return_value=data['mock_update_resp'])
        response = avi_pool.main()
        print(response)
        assert response['changed']
        assert response['obj']
        assert response['old_obj']

    def test_delete_pool(self):
        set_module_args({
            "avi_credentials": {
                "controller": "192.168.15.18",
                "username": "admin",
                "password": "password",
                "api_version": "21.1.1"

            },
            "uuid": "pool-7d5dc50b-5624-4992-a69a-eb2f0770cd65",
            "state": "absent",
            "name": "testpool1"
        })
        avi_pool.avi_ansible_api = MagicMock(return_value=data['mock_delete_resp'])
        response = avi_pool.main()
        assert response['changed']
        assert not response['obj']
        assert response['old_obj']
