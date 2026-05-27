# TEST PLAN: Watchguard Desktop Surveillance & Camera Management System

---

## 1. Test Plan Identifier

- **Test Plan ID:** TP-WG-2026-001
- **Version:** 1.0
- **Prepared By:** QA Test Architect
- **Reviewed By:** [To be completed]
- **Approved By:** [To be completed]
- **Date:** May 26, 2026
- **Product Name:** Watchguard - Desktop Surveillance & Camera Management System
- **Release Version:** 1.2.0

---

## 2. Project Overview

### Executive Summary

Watchguard is a desktop-based surveillance management system designed to support end-to-end camera operations including device onboarding, live monitoring, recording, playback, and audit management.

### Business Objectives

**Primary Objectives:**
- Enable centralized surveillance management across multiple stores
- Support ONVIF-based device onboarding and reuse
- Provide real-time live monitoring of camera feeds
- Enable recording, playback, and evidence management
- Ensure secure role-based access to surveillance operations

**Secondary Objectives:**
- Improve incident traceability through audit logs
- Reduce operational dependency on cloud connectivity
- Support scalable multi-store camera deployments
- Improve camera fault detection (e.g., IP change detection alerts)

### Key Stakeholders

| Stakeholder | Role |
|---|---|
| Store Owner | Business owner / decision maker |
| Security Operator | Monitors live feeds and recordings |
| Store Admin | Manages devices and configurations |
| IT/Admin Team | System setup, onboarding, and maintenance |
| Compliance/Audit Team | Reviews logs and evidence |
| Central Services Team | Provides authentication and core services |

### System Design Philosophy

- Desktop-first application with strong local orchestration
- Offline-capable operations
- ONVIF-compatible device management
- Audit-ready evidence storage and retrieval

---

## 3. Scope

### In Scope

**Functional Modules:**
1. Login & Session Management
2. Dashboard
3. Device Onboarding (ONVIF / Manual / RTSP)
4. Live Monitoring (Camera Wall)
5. Recording Management
6. Playback & Evidence Management
7. Settings & Configuration
8. Device Assignment
9. Audit Logs
10. User Management
11. Shopper Profile Module
12. AI Camera Viewer
13. Application Update Manager

**Functional Requirements Covered:**
- Device Management (ONVIF, manual, RTSP onboarding; reusable device storage; max 2 AI cameras per device)
- Live Monitoring (multi-camera display; main/sub stream switching; screenshot capture; configurable storage paths)
- Recording Management (live recording initiation; local storage; metadata indexing; deletion support)
- Playback & Evidence Management (recording list; playback; deletion)
- Device Assignment & Governance (role-based assignment; access restriction; audit tracking)
- Shopper Profile Module (data storage; mapping to shopper ID; historical activity tracking)
- Settings & Configuration (storage path configuration; application updates)
- Device Health & IP Change Handling (IP failure detection; owner/admin notification; false damage prevention)
- Audit & Governance (role-based access control; access/recording/playback action tracking)

**Non-Functional Requirements Covered:**
- Reliability (stable desktop-first operation)
- Data Persistence (local data continuity across sessions)
- Security (strong role-based access control)
- Storage Safety (safe and predictable local file handling)
- Performance (stable stream handling under repeated usage)
- Availability (offline-capable core operations)

### Out of Scope

- Browser-only surveillance model (desktop application only)
- Cloud-only surveillance model without local operation capability

---

## 4. Test Objectives

Define what the testing activity aims to validate:

1. **Functional Correctness**
   - Validate all functional requirements are implemented as specified
   - Verify business workflows execute correctly
   - Ensure data consistency across modules

2. **Integration Validation**
   - Verify ONVIF device integration
   - Validate manual and RTSP-based device onboarding
   - Verify central services authentication
   - Validate local storage integration

3. **Security & Access Control**
   - Verify role-based access control enforcement
   - Validate unauthorized access is blocked
   - Ensure audit logs track all actions

4. **UI & User Experience**
   - Validate responsive behavior
   - Verify navigation workflows
   - Ensure user actions trigger expected system behavior

5. **Data Management**
   - Validate local data storage
   - Verify data persistence across sessions
   - Ensure data integrity during operations

6. **Reliability & Stability**
   - Verify stable desktop-first operation
   - Validate offline capability
   - Ensure graceful error handling

7. **Non-Functional Compliance**
   - Verify performance under repeated usage
   - Validate stream handling stability
   - Ensure safe file handling practices

---

## 5. Test Strategy

### Functional Testing Approach

- **Requirements-Based Testing:** Test all explicitly defined functional requirements
- **Business Workflow Testing:** Validate end-to-end business flows (e.g., device onboarding → live monitoring → recording → playback)
- **Module Testing:** Systematic testing of each functional module in isolation and integration
- **Boundary Testing:** Test limits (e.g., max 2 AI cameras per device; multi-store deployments)
- **User Role Testing:** Validate workflows for each user role (Store Owner, Security Operator, Store Admin, IT/Admin Team, Compliance/Audit Team)

### API/Integration Testing Approach

- **ONVIF Integration:** Validate device discovery and onboarding
- **Manual/RTSP Onboarding:** Validate manual device addition and RTSP credential configuration
- **Central Services Integration:** Validate authentication and credential validation
- **Local Storage Integration:** Validate recording storage and retrieval
- **Device Health Monitoring:** Validate IP change detection and notification mechanisms

### UI Testing Approach

- **Navigation Flow:** Validate menus and page transitions
- **Form Validation:** Verify input validation and error messages
- **Visual Consistency:** Ensure UI layout and styling correctness
- **Action Responsiveness:** Verify UI updates on user actions
- **Configuration UI:** Validate settings screens and parameter updates

### Automation Strategy

- **High Priority:** Device onboarding, authentication, live monitoring, recording/playback flows
- **Medium Priority:** UI navigation, form validations, configuration changes
- **Manual Testing:** Exploratory testing, usability validation, multi-device scenarios

### Regression Testing Approach

- **Core Workflows:** Regression suite covering critical paths (login → device management → monitoring → recording)
- **Module Integration:** Test module interactions after changes
- **Version Updates:** Validate application update functionality and post-update operations

### Risk-Based Testing Approach

- **High-Risk Areas:** Authentication, access control, data persistence, offline operations, device connectivity
- **Medium-Risk Areas:** UI navigation, configuration management, multi-user scenarios
- **Mitigation:** Extended testing for high-risk areas; early detection of critical issues

---

## 6. Test Types

| Test Type | Applicable | Remarks |
|---|---|---|
| Functional Testing | Yes | Core functionality validation for all modules and workflows |
| UI Testing | Yes | Navigation, form validation, and user interaction validation |
| API Testing | Yes | ONVIF integration, manual onboarding, and central services validation |
| Integration Testing | Yes | Module interaction and system component integration |
| Regression Testing | Yes | Existing functionality validation post-build |
| Security Testing | Yes | Role-based access control, authentication, audit logging |
| Data Persistence Testing | Yes | Local storage continuity across sessions |
| Performance Testing | Optional | Stream handling stability; applicable for repeated usage scenarios |
| Reliability Testing | Yes | Offline capability, error handling, graceful failure modes |
| Acceptance Testing | Yes | Stakeholder validation against business requirements |

---

## 7. Test Environment

### Application Environment
- **Application Name:** Watchguard
- **Application Type:** Desktop Application
- **Current Release:** Version 1.2.0

### System Requirements
- **Operating System:** Windows (inferred from desktop application)
- **Required Permissions:** Local storage write access; network access for device communication

### Testing Infrastructure
- **QA Environment:** Desktop with local network access
- **Test Stores:** Multiple test store configurations
- **Mock Devices:** ONVIF-compatible test devices or device simulators
- **Network:** Local network with ONVIF device connectivity
- **Storage:** Dedicated test storage paths for recording validation

### Device/Integration Testing Requirements
- **ONVIF Devices:** Test ONVIF-compatible camera devices
- **Manual Onboarding:** Test IP addresses, ports, store names, store IDs, locations, manufacturers, models
- **RTSP Credentials:** Test RTSP stream credentials and configuration
- **Central Services:** Authentication service availability
- **Local Storage:** Verified writable paths for screenshots and recordings

### Assumptions
- ONVIF devices must be reachable within network
- Local machines must have write permissions for storage paths
- Required ports must be available
- Central authentication services must be accessible for login
- RTSP streams must be valid and accessible

---

## 8. Test Objectives Summary

**Primary Testing Goals:**
1. Validate all explicitly defined functional requirements
2. Verify secure role-based access control
3. Ensure data persistence and offline capability
4. Validate multi-store surveillance workflows
5. Verify reliable error handling and recovery

**Verification Focus:**
- All business use cases execute as documented
- Device onboarding (ONVIF/Manual/RTSP) functions correctly
- Live monitoring displays cameras across multiple stores
- Recording and playback workflows work reliably
- Access control prevents unauthorized operations
- Audit logs track all user actions
- Application handles network/device failures gracefully

---

## 9. Risks and Mitigation

| Risk | Impact | Probability | Mitigation |
|---|---|---|---|
| ONVIF device unavailability | High | Medium | Use device simulators; maintain test device pool; early procurement |
| Requirement interpretation ambiguity | Medium | Medium | Document explicit requirements; frequent requirement review meetings |
| Central services unavailability | High | Low | Maintain stable test environment; coordinate with central services team |
| Test data availability | Medium | Medium | Pre-populate test stores and devices; automated data setup |
| Environment instability | Medium | Medium | Backup test environment; documented recovery procedures |
| Local storage access issues | Medium | Low | Verify permissions early; test environment setup validation |
| Offline capability testing challenges | Medium | Medium | Simulate network disconnection scenarios; document test procedures |
| Multi-store scenario complexity | Medium | Medium | Phased testing approach; clear test case documentation |

---

## 10. Entry Criteria

Testing can commence when the following conditions are met:

1. **Build Requirements:**
   - Application build deployed to QA environment
   - Build is stable and executable
   - All critical build issues resolved

2. **Requirement Clarity:**
   - Requirements document reviewed and approved
   - Functional specifications finalized
   - Ambiguities clarified with stakeholders

3. **Environment Readiness:**
   - Test environment configured with required devices
   - ONVIF test devices accessible and functional
   - Central authentication services available
   - Local storage paths configured with proper permissions
   - Network connectivity verified

4. **Test Preparation:**
   - Test plan approved
   - Test cases designed and reviewed
   - Test data prepared
   - Automation framework ready (if applicable)

5. **Resource Availability:**
   - QA team assigned and available
   - Business analyst available for requirement clarification
   - Dev team available for defect triage

---

## 11. Exit Criteria

Testing phase is complete when:

1. **Test Coverage:**
   - All test cases executed
   - Minimum 90% functional requirement coverage achieved
   - All critical and high-priority areas tested

2. **Defect Management:**
   - All critical defects resolved
   - High-priority defects resolved or deferred with documented justification
   - Remaining defects logged and prioritized

3. **Regression Validation:**
   - Regression test suite executed with passing results
   - Post-fix testing completed
   - No new defects introduced

4. **Quality Gates:**
   - Security testing completed successfully
   - Data persistence validation passed
   - Offline capability verified
   - Audit logging validated

5. **Documentation:**
   - Test execution report completed
   - Defect report finalized
   - Requirements Traceability Matrix updated
   - Known issues documented

6. **Sign-off:**
   - QA lead approval obtained
   - Product owner acceptance sign-off received
   - Stakeholder approval documented

---

## 12. Test Deliverables

| Deliverable | Description | Owner | Timeline |
|---|---|---|---|
| Test Plan | This document | QA Lead | Before testing starts |
| Test Strategy | Detailed test approach | QA Lead | Before testing starts |
| Test Scenarios | High-level business scenarios | QA Architect | Week 1 |
| Test Cases | Detailed step-by-step test cases | QA Engineers | Week 1-2 |
| Test Data Requirements | Data setup specifications | QA Engineer | Week 1 |
| Automation Scripts | Automated test scripts (if applicable) | Automation Engineer | Week 2-3 |
| Test Execution Report | Summary of test execution | QA Lead | End of testing |
| Defect Report | Detailed defect logs and analysis | QA Lead | End of testing |
| Regression Report | Regression testing results | QA Engineer | End of testing |
| Traceability Matrix | Requirements to test case mapping | QA Lead | End of testing |
| Known Issues List | Documented known issues | QA Lead | End of testing |

---

## 13. Roles and Responsibilities

| Role | Responsibility |
|---|---|
| QA Lead | Test planning, reporting, stakeholder communication, exit criteria approval |
| QA Test Architect | Test strategy definition, test scenario creation, risk assessment |
| QA Test Engineer | Test case creation, manual test execution, defect logging |
| Automation Engineer | Automation framework setup, script development, test execution |
| Business Analyst | Requirement clarification, acceptance criteria validation |
| Developer | Defect investigation and resolution, question clarification |
| Product Owner | Requirement approval, acceptance testing, signoff |
| IT/Infrastructure | Test environment setup and maintenance |

---

## 14. Test Schedule

**Tentative Project Timeline:**

| Activity | Duration | Start | End |
|---|---|---|---|
| Test Planning | 2 days | TBD | TBD |
| Test Case Design | 5 days | TBD | TBD |
| Test Environment Setup | 3 days | TBD | TBD |
| Manual Test Execution (Phase 1) | 10 days | TBD | TBD |
| Automation Script Development | 7 days | TBD | TBD |
| Automation Test Execution | 5 days | TBD | TBD |
| Defect Triage & Retesting | 5 days | TBD | TBD |
| Regression Testing | 3 days | TBD | TBD |
| UAT Support | 3 days | TBD | TBD |
| **Total Estimated Duration** | **43 days** | | |

---

## 15. Defect Management Process

### Defect Classification

**Severity Levels:**
- **Critical:** Core functionality broken; system unusable; security vulnerability; data loss
- **High:** Major functionality impaired; workaround available
- **Medium:** Minor functionality issue; low user impact
- **Low:** UI/UX issue; no functional impact; cosmetic

**Priority Levels:**
- **P1 (Critical):** Resolve before release
- **P2 (High):** Resolve in current sprint
- **P3 (Medium):** Resolve in next sprint
- **P4 (Low):** Backlog; resolve as resources permit

### Defect Lifecycle

1. **Identification:** QA identifies and logs defect
2. **Triage:** QA Lead triages and assigns severity/priority
3. **Assignment:** Developer assigned for fix
4. **Resolution:** Developer fixes and marks resolved
5. **Verification:** QA verifies fix and closes
6. **Regression:** Ensure fix doesn't break other functionality

### Defect Documentation

- Defect ID (auto-generated)
- Title (concise description)
- Severity/Priority
- Module affected
- Environment details
- Steps to reproduce
- Expected vs. Actual behavior
- Screenshots/logs attached
- Status and resolution notes

---

## 16. Requirements Traceability Approach

A Requirements Traceability Matrix (RTM) will be maintained to:

1. **Map Requirements to Test Cases:** Each functional requirement mapped to corresponding test cases
2. **Ensure Complete Coverage:** Verify all requirements have associated test cases
3. **Track Test Execution:** Link test case results to requirements
4. **Defect Linkage:** Link defects to requirements and test cases
5. **Coverage Metrics:** Track percentage of requirements tested

**RTM Structure:**
| Req ID | Requirement | Test Case ID | Test Status | Defect ID (if any) | Remarks |
|---|---|---|---|---|---|
| FR-001 | Device onboarding via ONVIF | TC-001, TC-002 | Pass/Fail | [If applicable] | |
| FR-002 | Manual device addition | TC-003 | Pass/Fail | | |
| ... | ... | ... | ... | ... | ... |

---

## 17. Test Scenarios (High-Level)

### Scenario 1: Device Onboarding and Multi-Store Deployment
**Objective:** Validate devices can be onboarded and assigned across multiple stores

**High-Level Steps:**
1. User logs in with appropriate role
2. Admin scans/adds ONVIF camera devices
3. System captures device details (IP, port, store info, etc.)
4. Device is stored for reuse
5. Device is assigned to appropriate store(s)
6. Verify device availability and assignment

**Expected Outcome:** Device successfully onboarded and accessible from assigned store

---

### Scenario 2: Live Monitoring and Recording
**Objective:** Validate live camera monitoring and recording functionality

**High-Level Steps:**
1. Security operator logs in
2. Dashboard displays all cameras across assigned stores
3. Operator selects camera feed
4. Livestream displays (main and sub-streams available)
5. Operator initiates recording
6. System stores recording locally
7. Metadata is indexed for playback

**Expected Outcome:** Recording successfully captured and indexed

---

### Scenario 3: Playback and Evidence Management
**Objective:** Validate recorded footage playback and evidence retention

**High-Level Steps:**
1. User accesses Playback & Evidence module
2. Available/unavailable recordings listed
3. User selects recording for playback
4. Video plays correctly
5. User can delete evidence (with appropriate permissions)
6. Audit log tracks deletion action

**Expected Outcome:** Playback works; evidence management is audited

---

### Scenario 4: Role-Based Access Control
**Objective:** Validate only authorized users can perform specific actions

**High-Level Steps:**
1. Users with different roles log in
2. Attempt access to role-restricted features
3. Unauthorized access is prevented
4. Authorized actions are allowed
5. All actions are logged in audit trail

**Expected Outcome:** Access control enforced; audit logs accurate

---

### Scenario 5: Device Health and Failure Handling
**Objective:** Validate system detects and responds to device failures

**High-Level Steps:**
1. IP change detection triggers failure alert
2. Notification sent to owner/admin
3. False camera damage assumption prevented
4. System maintains availability of other cameras

**Expected Outcome:** Graceful failure handling; accurate notifications

---

### Scenario 6: Offline Capability
**Objective:** Validate system maintains operations during network disconnection

**High-Level Steps:**
1. System connected; normal operations
2. Network disconnected
3. Local operations (local recordings, playback) continue
4. Network reconnected
5. System synchronizes state

**Expected Outcome:** Local operations unaffected by network; graceful recovery

---

## 18. High-Level Test Cases (Representative Sample)

### TC-001: ONVIF Device Onboarding

**Precondition:** User logged in with Admin role; ONVIF device available

**Steps:**
1. Navigate to Device Onboarding
2. Select "ONVIF" option
3. System discovers ONVIF device
4. Verify device details (IP, port, manufacturer, model)
5. Enter store name, store ID, location
6. Verify max 2 AI cameras configured (if applicable)
7. Save device

**Expected Result:** Device onboarded successfully; stored for reuse

**Test Data:** Valid ONVIF device IP, valid store information

---

### TC-002: Manual Device Addition

**Precondition:** User logged in with Admin role

**Steps:**
1. Navigate to Device Onboarding
2. Select "Manual" option
3. Enter IP address, port
4. Enter store name, store ID, location, manufacturer, model
5. Configure AI camera count (max 2)
6. Save device

**Expected Result:** Device added successfully; available for assignment

---

### TC-003: Device Assignment by Role/Store

**Precondition:** Device onboarded; multiple users with different roles

**Steps:**
1. Admin assigns device to specific store
2. Security operator attempts to view only assigned devices
3. Verify unauthorized access to other stores blocked
4. Verify audit log records assignment action

**Expected Result:** Devices correctly restricted by role/store

---

### TC-004: Live Monitoring - Multi-Camera Display

**Precondition:** User logged in; devices assigned; cameras accessible

**Steps:**
1. Navigate to Camera Wall
2. Verify all cameras across assigned stores displayed
3. Select individual camera feed
4. Verify main stream displays
5. Switch to sub-stream
6. Capture screenshot
7. Verify screenshot stored in configured path

**Expected Result:** All cameras visible; stream switching works; screenshots captured

---

### TC-005: Recording Initiation and Storage

**Precondition:** Live feed active; storage path configured

**Steps:**
1. Select camera in live view
2. Click "Start Recording"
3. Recording status indicator shows active
4. Wait for defined duration
5. Stop recording
6. Verify recording stored in local path
7. Verify metadata indexed

**Expected Result:** Recording saved locally; metadata indexed for playback

---

### TC-006: Playback of Recorded Footage

**Precondition:** Recordings exist; user logged in

**Steps:**
1. Navigate to Playback & Evidence
2. Select available recording
3. Click play
4. Video plays correctly
5. Verify playback controls (pause, stop, seek)
6. View metadata

**Expected Result:** Recording plays correctly; controls functional

---

### TC-007: Role-Based Access Control - Unauthorized Access

**Precondition:** Users with different roles

**Steps:**
1. Log in as Security Operator
2. Attempt to access User Management (Admin-only feature)
3. Verify access denied

**Expected Result:** Unauthorized access blocked; error message displayed

---

### TC-008: Audit Log - Action Tracking

**Precondition:** Actions performed in system

**Steps:**
1. Perform various actions (login, device assignment, recording, playback, deletion)
2. Navigate to Audit Logs
3. Verify all actions logged with timestamp
4. Verify user, action type, and affected resource recorded

**Expected Result:** All actions accurately logged in audit trail

---

## 19. Test Data Requirements

### Device Information
- ONVIF-compatible camera devices (IP addresses, credentials)
- Manual onboarding data (IP, port, store name, store ID, location, manufacturer, model)
- RTSP stream credentials and URLs
- AI camera configurations (max 2 per device)

### User Accounts
- Test accounts with different roles:
  - Store Owner
  - Security Operator
  - Store Admin
  - IT/Admin Team Member
  - Compliance/Audit Team Member

### Store Information
- Multiple test stores with distinct store IDs
- Store location information
- Multi-store deployment configurations

### Recording Data
- Sample RTSP/live streams for recording
- Various recording durations for testing
- Metadata templates for indexed recordings

### Configuration Data
- Screenshot storage paths
- Recording storage paths
- Application settings templates

---

## 20. Automation Scope

### High Priority (Automate)
- Device onboarding workflows (ONVIF, manual, RTSP)
- Login and session management
- User role-based access control validation
- Recording initiation and storage verification
- Playback functionality
- Audit log verification

### Medium Priority (Consider for Automation)
- UI navigation flows
- Configuration management
- Multi-device scenarios
- Data persistence validation

### Low Priority (Manual Testing)
- Exploratory testing
- Usability validation
- Visual design validation
- Complex multi-user concurrent scenarios
- Network failure simulation

---

## 21. Regression Suite Scope

### Core Regression Areas
1. **Authentication & Authorization**
   - Login functionality
   - Session management
   - Role-based access control

2. **Device Management**
   - Device onboarding (all methods)
   - Device assignment
   - Device storage and reuse

3. **Live Monitoring**
   - Camera wall display
   - Stream switching
   - Screenshot capture

4. **Recording & Playback**
   - Recording initiation
   - Local storage
   - Metadata indexing
   - Playback functionality

5. **Audit & Governance**
   - Access control enforcement
   - Audit log accuracy
   - User action tracking

### Regression Trigger Points
- Post-bug-fix testing
- After feature additions
- After configuration changes
- Before release approval

---

## 22. Dependencies

### External Dependencies
- **ONVIF Devices:** Physical or simulated ONVIF-compatible cameras
- **Central Services:** Authentication service availability
- **Network:** Local network connectivity to devices
- **Storage:** Writable local storage for recordings and metadata

### Internal Dependencies
- **Build Availability:** Deployment of application build to QA
- **Requirement Finalization:** Approved requirements document
- **Environment Setup:** Configured test environment with devices and services

### Team Dependencies
- **Business Analyst:** Requirement clarification
- **Development Team:** Defect fixes and question resolution
- **Infrastructure Team:** Environment maintenance
- **Product Owner:** Acceptance validation and approval

---

## 23. Approval Section

| Role | Name | Signature | Date |
|---|---|---|---|
| QA Lead | | | |
| Test Manager | | | |
| Product Owner | | | |
| Project Manager | | | |
| Stakeholder | | | |

---

## Document Version History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | May 26, 2026 | QA Test Architect | Initial Test Plan creation based on BRS requirements |

---

## Appendices

### Appendix A: Anti-Hallucination Verification

**Verification Facts (From BRS Document):**
- Watchguard is a desktop-based surveillance management system
- Supports ONVIF, manual, and RTSP device onboarding
- Supports multi-store camera deployments
- Provides live monitoring with main/sub-stream switching
- Supports local recording and playback
- Includes audit logging
- Supports role-based access control
- Offline-capable design
- Supports screenshot and evidence management
- Includes device health monitoring (IP change detection)
- Version 1.2.0 with enhancements to recording storage and playback
- Specific stakeholders: Store Owner, Security Operator, Store Admin, IT/Admin, Compliance/Audit, Central Services

**Testing Limitations (Not Explicitly Defined):**
- Specific performance benchmarks not defined in BRS
- Load testing thresholds not specified
- Specific error messages/codes not documented
- Exact recovery time objectives not specified
- Detailed UI designs not provided

**Inference Notes:**
- Desktop application type inferred from "desktop-first" design philosophy
- Windows OS inferred from typical enterprise desktop deployment (marked as low confidence)

---

**END OF TEST PLAN DOCUMENT**
