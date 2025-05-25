# 🧪 Test Plan: Multi-Platform Backup Application

## 1. Overview
This test plan describes the scope, strategy, resources, and schedule for testing the backup application across Windows and Linux environments.

## 2. Objectives
- Ensure application performs backups successfully across platforms
- Verify API endpoints and system responses
- Validate user interface behavior through automated tests
- Identify critical bugs before release

## 3. Scope
### In Scope:
- Manual functional testing
- API testing via Postman
- UI automation (Selenium)
- DNS/DHCP configuration checks

### Out of Scope:
- Performance and load testing
- Security penetration testing

## 4. Test Items
- Backup functionality (incremental, full)
- Restore functionality
- API (GET, POST requests)
- System configuration validations

## 5. Testing Types
- Functional testing
- UI automation
- Configuration verification

## 6. Test Deliverables
- `test-cases.xlsx`
- `bug-reports/`
- Postman collections
- Selenium test results

## 7. Entry and Exit Criteria
### Entry:
- Test environment ready
- Application build deployed
- Access to systems and test accounts

### Exit:
- All critical test cases passed
- No blocker or critical bugs open

## 8. Risks
- Incomplete requirements
- OS compatibility issues
- Limited access to test environments

## 9. Team
| Role         | Name            |
|--------------|-----------------|
| QA Engineer  | [Almazova A.]   |

## 10. Tools
- Postman
- Selenium
- Excel / Google Sheets
- Windows / Linux
# Test Plan – Backup Application

## Goal
To verify the core functionality of a multi-platform backup utility.

## Functionalities to Test
- File selection
- Backup execution
- Restore operation
- Log file verification

## Types of Testing
- Smoke testing
- Functional testing
- UI/UX validation

## Environment
- Windows 10, Ubuntu Linux
