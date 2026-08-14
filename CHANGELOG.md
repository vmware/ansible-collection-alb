# Changelog

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

## 31.1.2
- Added the installation of bs4 as a requirement to fix failure of auto… sync pr
- Fixes ansible module doc


## 30.2.6
### Major Changes
- **Ansible 2.18 Support**: Added support for Ansible 2.18 version
- **Red Hat Certification**: Enhanced collection for Red Hat Ansible Certified Content compliance
- **Code Quality Improvements**: Comprehensive fixes for ansible-lint, pylint, pep8, and sanity tests

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

  - **Role Enhancements**:
  - **avicontroller**: Enhanced Docker deployment, service management, and systemd integration
  - **avise**: Improved SE deployment with better autoregistration, disk checks, and DPDK support
  - **aviconfig**: Enhanced configuration management with better error handling
  - **avicontroller_csp**: Improved CSP deployment and validation
  - **avicontroller_kvm**: Enhanced KVM controller deployment
  - **avicontroller_vmware**: Improved VMware controller deployment

- **SDK Updates**:
  - Updated avi_api.py with improved error handling and API interactions
  - Enhanced saml_avi_api.py for better SAML authentication
  - Improved ansible_utils.py with better utility functions
  - Updated csp_avi_api.py for CSP integration

### Bug Fixes
- Fixed multiple ansible-lint issues across all modules and roles
- Resolved ansible-test sanity validation-module errors
- Fixed doc-default-does-not-match-spec issues
- Corrected shellcheck issues in shell scripts
- Fixed shebang issues in templates and scripts
- Resolved pep8 and pylint compliance issues
- Fixed import-3.8 compatibility issues
- Corrected line-ending issues in configuration files
- Fixed production profile lint issues

### Testing
- Enhanced molecule test scenarios with updated configurations
- Improved test playbooks for better coverage
- Updated integration tests for Jenkins CI/CD
- Enhanced verification and cleanup procedures

### Infrastructure
- Updated requirements.txt with latest dependencies
- Improved meta files for better Ansible Galaxy integration
- Enhanced runtime.yml for collection metadata
- Updated ignore.txt template for Ansible 2.18 compatibility

### Module Updates
The following modules received lint fixes and improvements:
- avi_federationcheckpoint
- avi_pingaccessagent
- avi_saml_api_session
- avi_bootstrap_controller
- avi_serviceenginegroup
- avi_serviceenginegroup_advanced
- avi_user
- avi_useraccount
- avi_api_image
- avi_api_version
- avi_api_session
- avi_api_fileservice
- avi_pulse_registration
- avi_update_se_data_vnics
- avi_gslbservice_patch_member
- deploy_se
- verify_se

### Template and Example Updates
- Updated all ansible example files with proper formatting and lint compliance
- Enhanced role task templates with better error handling
- Improved collection documentation templates
- Updated systemd service files and installation scripts

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
