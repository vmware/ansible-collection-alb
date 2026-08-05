#!/usr/bin/python
# module_check: supported

# Copyright (c) 2026 Broadcom Inc. and/or its subsidiaries. All Rights Reserved. Broadcom Confidential.
# SPDX-License-Identifier: Apache License 2.0

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_fileobject_upload
author: Parikshit Manur (@pm020058) <parikshit.manur@broadcom.com>
short_description: Upload or register a FileObject via the consolidated upload endpoint (32.2.1+)
description:
    - Uses C(POST /api/fileobject/upload) with the structured B(UploadParams) schema
      introduced in 32.2.1.
    - Supports two upload modes, both routed through the collection's standard
      C(avi_ansible_api) helper (session management, idempotency, API call).
    - B(url) mode -- the controller fetches a CRL from a remote server URL and
      schedules periodic refreshes.  Only the C(CRL_DATA) type is valid here.
      Idempotency is handled by C(avi_ansible_api) comparing the full object.
    - B(file) mode -- a local binary file is streamed to the controller as
      C(multipart/form-data).  C(avi_ansible_api) computes a SHA-1 checksum of
      the local file and skips the upload when it matches the stored checksum.
      Requires the C(requests_toolbelt) Python package on the control node.
    - The response is always a B(FileObject) JSON object.
    - B(Requires API version 32.2.1 or later on the controller.)
    - For controllers older than 32.2.1 use M(vmware.alb.avi_fileobject) for
      metadata and M(vmware.alb.avi_api_fileservice) for file uploads.
options:
    state:
        description:
            - Only C(present) is supported.  Deletion uses M(vmware.alb.avi_fileobject)
              with C(state=absent).
        default: present
        choices: ["present", "absent"]
        type: str
    file_path:
        description:
            - Absolute or relative path to the local file to upload.
        type: str
    name:
        description:
            - Logical name for the FileObject.
        required: true
        type: str
    type:
        description:
            - Kind of file being uploaded.
            - Enum options - OTHER_FILE_TYPES, IP_REPUTATION, GEO_DB, TECH_SUPPORT,
              HSMPACKAGES, IPAMDNSSCRIPTS, CONTROLLER_IMAGE, CRL_DATA,
              IP_REPUTATION_IPV6, GSLB_GEO_DB, CSRF_JS.
        required: true
        type: str
    url:
        description:
            - Remote server URL from which the controller will fetch the CRL.
            - Valid only for C(type=CRL_DATA).
        type: str
    update_interval:
        description:
            - How often (in minutes) the controller re-fetches the CRL.
            - Applicable only when C(type=CRL_DATA).
            - Controller default is 1440 (24 hours) when not specified.
        type: int
    description:
        description:
            - Free-text description stored with the FileObject.
        type: str
    is_federated:
        description:
            - When C(true) the FileObject is replicated across the GSLB federation.
        type: bool
        default: false
    expires_at:
        description:
            - Timestamp after which the file may be garbage-collected.
        type: str
    gslb_geodb_format:
        description:
            - File format for C(GSLB_GEO_DB) files.
            - Enum options - GSLB_GEODB_FILE_FORMAT_AVI,
              GSLB_GEODB_FILE_FORMAT_MAXMIND_CITY,
              GSLB_GEODB_FILE_FORMAT_MAXMIND_CITY_V6,
              GSLB_GEODB_FILE_FORMAT_MAXMIND_CITY_V4_AND_V6,
              GSLB_GEODB_FILE_FORMAT_AVI_V6, GSLB_GEODB_FILE_FORMAT_AVI_V4_AND_V6.
        type: str
    part:
        description:
            - Chunked upload part identifier for very large files.
        type: str
    size:
        description:
            - Declared size of the file in bytes.
        type: int
    compressed:
        description:
            - Set to C(true) if the file body is gzip-compressed.
        type: bool
    read_only:
        description:
            - When C(true) the controller rejects subsequent modification.
        type: bool
    restrict_download:
        description:
            - When C(true) the download endpoint is blocked for this file.
        type: bool
    timeout:
        description:
            - Timeout in seconds for the multipart POST.
            - Increase for large files.
        type: int
        default: 300
extends_documentation_fragment:
    - vmware.alb.avi
'''

EXAMPLES = '''
- name: File Upload
  hosts: all
  vars:
    avi_credentials:
      username: "{{ username }}"
      password: "{{ password }}"
      controller: "{{ controller }}"
      api_version: "{{ api_version }}"

  tasks:
    # URL-based CRL (32.2.1+)
    - name: Create CRL FileObject from remote URL
      vmware.alb.avi_fileobject_upload:
        avi_credentials: ""
        name: "digicert-global-root-crl"
        type: "CRL_DATA"
        url: "http://crl4.digicert.com/DigiCertGlobalRootCA.crl"
        update_interval: 480

    # Binary file upload (32.2.1+)
    - name: Upload MaxMind GeoIP database
      vmware.alb.avi_fileobject_upload:
        avi_credentials: ""
        name: "maxmind-city-db"
        type: "GEO_DB"
        file_path: "/var/data/GeoLite2-City.mmdb"
        timeout: 600
'''

RETURN = '''
obj:
    description: FileObject returned by the controller after the upload.
    returned: success, changed
    type: dict
'''

from ansible.module_utils.basic import AnsibleModule
try:
    from ansible_collections.vmware.alb.plugins.module_utils.utils.ansible_utils import (
        avi_common_argument_spec, avi_ansible_api)
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False


def main():
    UPLOAD_ENDPOINT = 'fileobject/upload'
    argument_specs = dict(
        state=dict(default='present', choices=['present', 'absent']),
        file_path=dict(type='str'),
        name=dict(type='str', required=True),
        type=dict(type='str', required=True),
        url=dict(type='str'),
        update_interval=dict(type='int'),
        description=dict(type='str'),
        is_federated=dict(type='bool', default=False),
        expires_at=dict(type='str'),
        gslb_geodb_format=dict(type='str'),
        part=dict(type='str'),
        size=dict(type='int'),
        compressed=dict(type='bool'),
        read_only=dict(type='bool'),
        restrict_download=dict(type='bool'),
        timeout=dict(type='int', default=300),
        api_context=dict(type='dict'),
        username=dict(type='str', default=''),
        tenant_uuid=dict(type='str', default=''),
        tenant=dict(type='str', default='admin'),
        password=dict(type='str', default='', no_log=True),
        controller=dict(type='str', default=''),
        api_version=dict(type='str', default='20.1.7'),
        avi_credentials=dict(type='dict'),
        avi_deactivate_session_cache_as_fact=dict(type='bool', default=False),
    )
    if HAS_REQUESTS:
        argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs,
        supports_check_mode=True,
    )
    if not HAS_REQUESTS:
        return module.fail_json(msg=(
            'Python requests package is not installed. '
            'For installation instructions, visit https://pypi.org/project/requests.'))

    if module.params['state'] == "absent":
        UPLOAD_ENDPOINT = 'fileobject'

    return avi_ansible_api(module, UPLOAD_ENDPOINT, set())


if __name__ == '__main__':
    main()
