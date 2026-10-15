# Changelog

## 32.1.4

- File Upload Support: Introduced a new fileobject_upload module to enable file upload operations through the Ansible collection. This allows users to automate file uploads within their Ansible workflows, reducing the need for manual upload operations.
- REST API Endpoint Updates (AV-293089): Updated REST API paths used by Ansible modules to align with the revised endpoint structure. This helps users execute automation tasks against the correct API endpoints and reduces issues caused by outdated REST paths.
- Enhanced Logging Security (AV-274876): Enhanced logging security by masking all sensitive fields in log output. This helps users troubleshoot module execution more securely while reducing the risk of exposing confidential information in logs.
- Added preflight_check boolean parameter (default true) to the avi_api_session module to gate pre-flight GET requests before POST/PUT operations.


## 32.1.3

### Bug Fixes
- avi_serviceenginegroup_advanced Module is removed. All fields previously only available through avi_serviceenginegroup_advanced are now available directly on vmware.alb.avi_serviceenginegroup. Action required: Playbooks and roles using avi_serviceenginegroup_advanced must be updated to use avi_serviceenginegroup instead, passing all fields (both previously "basic" and "advanced") to that single module.

## 32.1.2

### Security Fixes
- Enforced OVA manifest verification and enabled TLS certificate validation by default to prevent tampered OVA deployments and MITM attacks.
- Fixed vCenter connections to honor the ssl_verify setting instead of always bypassing certificate validation (CWE-295).
- Prevented leakage of session tokens, cookies, CSRF tokens, and other sensitive credentials in Ansible logs, SDK logs, and API error messages (CWE-532, CWE-209).
- Fixed exposure of URL-encoded vCenter passwords in ovftool deployment failure logs by ensuring sensitive values are properly redacted.
- avi_serviceenginegroup_advanced Module is removed. All fields previously only available through avi_serviceenginegroup_advanced are now available directly on vmware.alb.avi_serviceenginegroup. Action required: Playbooks and roles using avi_serviceenginegroup_advanced must be updated to use avi_serviceenginegroup instead, passing all fields. (both previously "basic" and "advanced") to that single module.

## 32.1.1

### Enhancements
- Added installation of **bs4** as a required dependency to resolve automation failures
- Auto-updated collection assets for Ansible Collection Engineering
- Performed additional collection asset synchronization updates

### Bug Fixes
- Fixed Ansible sanity issues across the collection modules
- Resolved automation validation and compliance issues
- avi_serviceenginegroup_advanced Module is removed. All fields previously only available through avi_serviceenginegroup_advanced are now available directly on vmware.alb.avi_serviceenginegroup. Action required: Playbooks and roles using avi_serviceenginegroup_advanced must be updated to use avi_serviceenginegroup instead, passing all fields (both previously "basic" and "advanced") to that single module.

### Contributions
- Added bs4 installation requirement to fix automation failures
- Asset updates by contributors through automated collection engineering workflows
- Ansible sanity issue fixes and collection stabilization improvements

## 31.2.2
- No functional changes; version bump only.

## 31.2.3
- avi_serviceenginegroup_advanced Module is removed. All fields previously only available through avi_serviceenginegroup_advanced are now available directly on vmware.alb.avi_serviceenginegroup. Action required: Playbooks and roles using avi_serviceenginegroup_advanced must be updated to use avi_serviceenginegroup instead, passing all fields (both previously "basic" and "advanced") to that single module.

## 31.1.2
- Added the installation of bs4 as a requirement to fix failure of auto… sync pr
- Fixes ansible module doc

## 30.2.6

### Enhancements
- **Documentation Updates**:
  - Added comprehensive Support section in README with information about Red Hat Ansible Certified Content
  - Updated README with improved examples and better formatting
  - Enhanced collection documentation with support and troubleshooting information
  - Updated LICENSE and NOTICE files for proper compliance

- **Module Improvements**:
  - Fixed Service Engine (SE) creation issues
  - Enhanced SE data vnics update functionality
  - Improved SAML API session handling
  - Updated Federation checkpoint module
  - Enhanced Ping Access Agent module
  - Improved deploy_se and verify_se modules

### Bug Fixes
- Fixed multiple ansible-lint issues across all modules and roles
- Resolved ansible-test sanity validation-module errors
- Fixed doc-default-does-not-match-spec issues
- Corrected shellcheck issues in shell scripts
- Fixed shebang issues in templates and scripts
- Resolved pep8 and pylint compliance issues
- Corrected line-ending issues in configuration files


## 30.2.5
- Initial release of the VMware Avi collection
