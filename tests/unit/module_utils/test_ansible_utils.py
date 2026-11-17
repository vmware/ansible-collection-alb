
############################################################################
# ========================================================================
# Copyright 2021 VMware, Inc.  All rights reserved. VMware Confidential
# ========================================================================
###

# Copyright 2021 VMware, Inc.  All rights reserved. VMware Confidential
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.vmware.alb.plugins.module_utils.utils.ansible_utils import (avi_obj_cmp, ref_n_str_cmp,
                                                                                     merge_with_existing)

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


# AV-298730: a PUT fills in what the playbook leaves out, also inside sub-objects
EXISTING_SYSCONF = {
    "uuid": "default",
    "default_license_tier": "ENTERPRISE",
    "portal_configuration": {
        "http_port": 8080,
        "https_port": 8443,
        "api_force_timeout": 24,
        "allow_basic_authentication": True,
        "sslkeyandcertificate_refs": ["/api/sslkeyandcertificate/cert-1#cert1",
                                      "/api/sslkeyandcertificate/cert-2#cert2"],
        "sslprofile_ref": "/api/sslprofile/profile-1#System-Standard-Portal",
    },
    "dns_configuration": {"server_list": [{"addr": "10.10.10.10", "type": "V4"}]},
}


def test_put_keeps_sub_fields_the_playbook_leaves_out():
    new = {"portal_configuration": {"api_force_timeout": 30}}
    merged = merge_with_existing(new, EXISTING_SYSCONF)
    expected_portal = dict(EXISTING_SYSCONF["portal_configuration"], api_force_timeout=30)
    assert merged["portal_configuration"] == expected_portal
    assert merged["default_license_tier"] == "ENTERPRISE"
    assert merged["dns_configuration"] == EXISTING_SYSCONF["dns_configuration"]


def test_put_uses_the_playbook_values():
    new = {"portal_configuration": {"http_port": 80, "https_port": 443}}
    merged = merge_with_existing(new, EXISTING_SYSCONF)
    assert merged["portal_configuration"]["http_port"] == 80
    assert merged["portal_configuration"]["https_port"] == 443
    assert merged["portal_configuration"]["api_force_timeout"] == 24


def test_put_merges_every_level():
    existing = {"a": {"b": {"c": 1, "d": 2}, "e": 3}}
    merged = merge_with_existing({"a": {"b": {"c": 10}}}, existing)
    assert merged == {"a": {"b": {"c": 10, "d": 2}, "e": 3}}


def test_put_replaces_lists_as_a_whole():
    new = {"portal_configuration": {"sslkeyandcertificate_refs": ["/api/sslkeyandcertificate/?name=cert3"]}}
    merged = merge_with_existing(new, EXISTING_SYSCONF)
    assert merged["portal_configuration"]["sslkeyandcertificate_refs"] == ["/api/sslkeyandcertificate/?name=cert3"]
    new = {"dns_configuration": {"server_list": [{"addr": "10.10.10.20"}]}}
    merged = merge_with_existing(new, EXISTING_SYSCONF)
    assert merged["dns_configuration"]["server_list"] == [{"addr": "10.10.10.20"}]


def test_put_none_keeps_the_controller_value():
    new = {"default_license_tier": None, "portal_configuration": {"http_port": None}}
    merged = merge_with_existing(new, EXISTING_SYSCONF)
    assert merged["default_license_tier"] == "ENTERPRISE"
    assert merged["portal_configuration"]["http_port"] == 8080


def test_put_new_sub_object_and_value_type_change():
    existing = {"a": "x", "b": {"c": 1}}
    merged = merge_with_existing({"a": {"k": 1}, "b": "y", "n": {"m": 2}}, existing)
    assert merged == {"a": {"k": 1}, "b": "y", "n": {"m": 2}}


def test_put_state_absent_still_removes_a_sub_object():
    from ansible_collections.vmware.alb.plugins.module_utils.utils.ansible_utils import cleanup_absent_fields
    new = {"dns_configuration": {"state": "absent"}}
    merged = cleanup_absent_fields(merge_with_existing(new, EXISTING_SYSCONF))
    assert "dns_configuration" not in merged
    assert merged["portal_configuration"] == EXISTING_SYSCONF["portal_configuration"]


def test_put_merge_does_not_change_its_inputs():
    import copy
    existing = copy.deepcopy(EXISTING_SYSCONF)
    new = {"portal_configuration": {"api_force_timeout": 30}}
    merged = merge_with_existing(new, existing)
    merged["portal_configuration"]["http_port"] = 1
    assert existing == EXISTING_SYSCONF
    assert new == {"portal_configuration": {"api_force_timeout": 30}}
