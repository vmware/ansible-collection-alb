# Changelog

## 30.2.7

### Enhancements
- Upgraded Python version from 3.9 to 3.12 in CI workflow
- Upgraded Ansible version from 2.15.0 to 2.16.0 in CI matrix
- Updated minimum Ansible requirement to `>=2.16.0` in `meta/runtime.yml`

### Bug Fixes
- Fixed `cleanup_absent_fields` in `ansible_utils.py` — function was incorrectly returning `None` instead of the processed object, causing data loss in object cleanup operations
- Fixed `verify_se.py` to import `ApiSession` from the collection module path (`ansible_collections.vmware.alb.plugins.module_utils.avi_api`) instead of the legacy `avi.sdk` path


## 32.1.1

### Enhancements
- Added installation of **bs4** as a required dependency to resolve automation failures
- Auto-updated collection assets for Ansible Collection Engineering
- Performed additional collection asset synchronization updates

### Bug Fixes
- Fixed Ansible sanity issues across the collection modules
- Resolved automation validation and compliance issues

### Contributions
- Added bs4 installation requirement to fix automation failures
- Asset updates by contributors through automated collection engineering workflows
- Ansible sanity issue fixes and collection stabilization improvements

## 31.2.1

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
