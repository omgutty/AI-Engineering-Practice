# ICARUS - Functional Test Cases (Jira Format)

> Test cases for https://icarus.cloudamber.com/ covering valid and invalid login scenarios and navigation elements.
> 
> Last Updated: May 25, 2026

---

## Test Case Summary

| TC ID  | Test Case Title | Type | Priority | Status |
|--------|-----------------|------|----------|--------|
| TC-001 | Successful Login with Valid Credentials | Functional | High | Active |
| TC-002 | Login with Empty Username | Functional | High | Active |
| TC-003 | Login with Empty Password | Functional | High | Active |
| TC-004 | Login with Invalid Username | Functional | High | Active |
| TC-005 | Login with Invalid Password | Functional | High | Active |
| TC-006 | Keep Me Logged In Checkbox - Valid Login | Functional | Medium | Active |
| TC-007 | Forgot Password Link Navigation | Functional | Medium | Active |
| TC-008 | Social Media Links Navigation | Functional | Low | Active |
| TC-009 | Multiple Failed Login Attempts | Functional | High | Active |
| TC-010 | Logo Navigation to Home Page | Functional | Low | Active |

---

## Detailed Test Cases

### TC-001: Successful Login with Valid Credentials

| Field | Value |
|-------|-------|
| **Test Case ID** | TC-001 |
| **Test Case Title** | Verify successful login with valid credentials |
| **Module/Component** | Authentication - Login Panel |
| **Type** | Functional |
| **Priority** | High |
| **Pre-conditions** | 1. User has a valid account with ICARUS 2. User is not already logged in 3. Browser is open and navigated to https://icarus.cloudamber.com/ |
| **Test Steps** | 1. On the Home Page, locate the Login Panel on the right side 2. Enter valid username in the "User Name" field 3. Enter corresponding valid password in the "Password" field 4. Click the "Login" button 5. Observe the response |
| **Test Data** | Username: [valid admin account] Password: [valid password] |
| **Expected Result** | 1. Login is successful 2. User is redirected to the dashboard or home page 3. Session is created and user remains logged in 4. Login Panel disappears or changes to show logged-in user info |
| **Actual Result** | *(To be filled during execution)* |
| **Status** | Not Executed |
| **Executed By** | [QA Engineer Name] |
| **Execution Date** | *(To be filled during execution)* |
| **Pass/Fail** | *(To be filled during execution)* |
| **Remarks/Comments** | Valid credentials required for execution. Ensure account exists in test environment. |

---

### TC-002: Login with Empty Username Field

| Field | Value |
|-------|-------|
| **Test Case ID** | TC-002 |
| **Test Case Title** | Verify login validation when Username field is left empty |
| **Module/Component** | Authentication - Login Panel |
| **Type** | Functional (Negative Test) |
| **Priority** | High |
| **Pre-conditions** | 1. User is on the Home Page 2. User is not logged in 3. Login Panel is visible |
| **Test Steps** | 1. On the Home Page, locate the Login Panel 2. Leave the "User Name" field empty 3. Enter valid password in the "Password" field 4. Click the "Login" button 5. Observe the validation behavior |
| **Test Data** | Username: [empty] Password: [valid password] |
| **Expected Result** | 1. Login fails 2. An error message is displayed indicating "Username is required" or similar validation message 3. User remains on the same page 4. Login Panel remains visible for retry |
| **Actual Result** | *(To be filled during execution)* |
| **Status** | Not Executed |
| **Executed By** | [QA Engineer Name] |
| **Execution Date** | *(To be filled during execution)* |
| **Pass/Fail** | *(To be filled during execution)* |
| **Remarks/Comments** | Test client-side or server-side validation for empty username. |

---

### TC-003: Login with Empty Password Field

| Field | Value |
|-------|-------|
| **Test Case ID** | TC-003 |
| **Test Case Title** | Verify login validation when Password field is left empty |
| **Module/Component** | Authentication - Login Panel |
| **Type** | Functional (Negative Test) |
| **Priority** | High |
| **Pre-conditions** | 1. User is on the Home Page 2. User is not logged in 3. Login Panel is visible |
| **Test Steps** | 1. On the Home Page, locate the Login Panel 2. Enter valid username in the "User Name" field 3. Leave the "Password" field empty 4. Click the "Login" button 5. Observe the validation behavior |
| **Test Data** | Username: [valid username] Password: [empty] |
| **Expected Result** | 1. Login fails 2. An error message is displayed indicating "Password is required" or similar validation message 3. User remains on the same page 4. Login Panel remains visible for retry |
| **Actual Result** | *(To be filled during execution)* |
| **Status** | Not Executed |
| **Executed By** | [QA Engineer Name] |
| **Execution Date** | *(To be filled during execution)* |
| **Pass/Fail** | *(To be filled during execution)* |
| **Remarks/Comments** | Test client-side or server-side validation for empty password. |

---

### TC-004: Login with Invalid/Non-existent Username

| Field | Value |
|-------|-------|
| **Test Case ID** | TC-004 |
| **Test Case Title** | Verify login fails with non-existent username |
| **Module/Component** | Authentication - Login Panel |
| **Type** | Functional (Negative Test) |
| **Priority** | High |
| **Pre-conditions** | 1. User is on the Home Page 2. User is not logged in 3. Login Panel is visible 4. Username does not exist in the system |
| **Test Steps** | 1. On the Home Page, locate the Login Panel 2. Enter a non-existent username in the "User Name" field 3. Enter a valid password in the "Password" field 4. Click the "Login" button 5. Observe the response |
| **Test Data** | Username: invaliduser123 Password: [valid password format] |
| **Expected Result** | 1. Login fails 2. An error message is displayed (e.g., "Invalid username or password", "User not found", or generic authentication error) 3. User remains on the same page 4. Login Panel remains visible for retry 5. No sensitive information is revealed |
| **Actual Result** | *(To be filled during execution)* |
| **Status** | Not Executed |
| **Executed By** | [QA Engineer Name] |
| **Execution Date** | *(To be filled during execution)* |
| **Pass/Fail** | *(To be filled during execution)* |
| **Remarks/Comments** | Security best practice: Generic error messages prevent username enumeration attacks. Verify the message does not confirm/deny user existence. |

---

### TC-005: Login with Incorrect Password

| Field | Value |
|-------|-------|
| **Test Case ID** | TC-005 |
| **Test Case Title** | Verify login fails with incorrect password for valid username |
| **Module/Component** | Authentication - Login Panel |
| **Type** | Functional (Negative Test) |
| **Priority** | High |
| **Pre-conditions** | 1. User is on the Home Page 2. User is not logged in 3. Login Panel is visible 4. A valid username exists in the system |
| **Test Steps** | 1. On the Home Page, locate the Login Panel 2. Enter a valid username in the "User Name" field 3. Enter an incorrect password in the "Password" field 4. Click the "Login" button 5. Observe the response |
| **Test Data** | Username: [valid username] Password: wrongpassword123 |
| **Expected Result** | 1. Login fails 2. An error message is displayed (e.g., "Invalid username or password", "Authentication failed", or similar) 3. User remains on the same page 4. Login Panel remains visible for retry 5. Session is not created |
| **Actual Result** | *(To be filled during execution)* |
| **Status** | Not Executed |
| **Executed By** | [QA Engineer Name] |
| **Execution Date** | *(To be filled during execution)* |
| **Pass/Fail** | *(To be filled during execution)* |
| **Remarks/Comments** | Security best practice: Error message should not differentiate between invalid username and invalid password. |

---

### TC-006: Keep Me Logged In Checkbox - Valid Login

| Field | Value |
|-------|-------|
| **Test Case ID** | TC-006 |
| **Test Case Title** | Verify "Keep me logged in" checkbox functionality with valid credentials |
| **Module/Component** | Authentication - Login Panel, Session Management |
| **Type** | Functional |
| **Priority** | Medium |
| **Pre-conditions** | 1. User is on the Home Page 2. User is not logged in 3. Login Panel is visible with the "Keep me logged in" checkbox 4. Browser cookies are enabled |
| **Test Steps** | 1. On the Home Page, locate the Login Panel 2. Enter valid username in the "User Name" field 3. Enter valid password in the "Password" field 4. Check the "Keep me logged in" checkbox 5. Click the "Login" button 6. Successfully log in 7. Close the browser completely 8. Reopen the browser and navigate to https://icarus.cloudamber.com/ 9. Verify user session state |
| **Test Data** | Username: [valid username] Password: [valid password] |
| **Expected Result** | 1. Initial login is successful 2. "Keep me logged in" checkbox is checked before login 3. After browser restart, user is automatically logged in without needing to re-enter credentials 4. User dashboard or home page is displayed 5. Session cookie persists across browser sessions |
| **Actual Result** | *(To be filled during execution)* |
| **Status** | Not Executed |
| **Executed By** | [QA Engineer Name] |
| **Execution Date** | *(To be filled during execution)* |
| **Pass/Fail** | *(To be filled during execution)* |
| **Remarks/Comments** | This test verifies persistent session functionality. Clear cookies before test if needed to ensure clean state. Check browser cookie settings and expiration time. |

---

### TC-007: Forgot Password Link Navigation

| Field | Value |
|-------|-------|
| **Test Case ID** | TC-007 |
| **Test Case Title** | Verify "Forgot your password?" link navigates to password reset page |
| **Module/Component** | Authentication - Login Panel, Password Recovery |
| **Type** | Functional |
| **Priority** | Medium |
| **Pre-conditions** | 1. User is on the Home Page (https://icarus.cloudamber.com/) 2. User is not logged in 3. Login Panel is visible 4. "Forgot your password?" link is visible |
| **Test Steps** | 1. On the Home Page, locate the Login Panel 2. Look for the "Forgot your password?" link 3. Click on "Click here" link next to "Forgot your password?" 4. Observe the page that loads 5. Verify the URL and page content |
| **Test Data** | N/A |
| **Expected Result** | 1. Clicking the link navigates to the password reset/recovery page 2. URL changes to http://admin.cloudamber.com/forgotpassword or similar 3. Password recovery form or instructions are displayed 4. User can enter email or username to initiate password reset process 5. Navigation is successful without errors or broken links |
| **Actual Result** | *(To be filled during execution)* |
| **Status** | Not Executed |
| **Executed By** | [QA Engineer Name] |
| **Execution Date** | *(To be filled during execution)* |
| **Pass/Fail** | *(To be filled during execution)* |
| **Remarks/Comments** | Verify that the link points to the correct recovery page. Check for 404 errors or broken redirects. Test in multiple browsers for consistency. |

---

### TC-008: Social Media Links Navigation

| Field | Value |
|-------|-------|
| **Test Case ID** | TC-008 |
| **Test Case Title** | Verify social media links in navigation open correct external pages |
| **Module/Component** | Navigation - Social Media Links |
| **Type** | Functional |
| **Priority** | Low |
| **Pre-conditions** | 1. User is on the Home Page (https://icarus.cloudamber.com/) 2. Internet connection is active 3. External social media pages are accessible 4. Navigation section is visible with social media links |
| **Test Steps** | 1. On the Home Page, locate the navigation section with social media links 2. Verify links are present: Facebook, Twitter, RSS Feeds 3. Click on "Follow us on Facebook" link 4. Verify the page that opens 5. Navigate back to ICARUS Home Page 6. Click on "Follow us on Twitter" link 7. Verify the page that opens 8. Navigate back and repeat for RSS Feeds link |
| **Test Data** | N/A |
| **Expected Result** | 1. Facebook link opens: https://www.facebook.com/idoxgroup 2. Twitter link opens: https://twitter.com/idoxtransport 3. RSS Feeds link opens: http://transport.idoxgroup.com/index.php/news?alttemplate=newseventsRSS 4. Each link opens in a new tab or window (or appropriate behavior) 5. No 404 errors or broken links 6. Pages load successfully |
| **Actual Result** | *(To be filled during execution)* |
| **Status** | Not Executed |
| **Executed By** | [QA Engineer Name] |
| **Execution Date** | *(To be filled during execution)* |
| **Pass/Fail** | *(To be filled during execution)* |
| **Remarks/Comments** | External links may require manual verification if targets are blocked in test environment. Verify links open in appropriate target (new tab, same tab, etc.). |

---

### TC-009: Multiple Failed Login Attempts

| Field | Value |
|-------|-------|
| **Test Case ID** | TC-009 |
| **Test Case Title** | Verify system behavior after multiple failed login attempts |
| **Module/Component** | Authentication - Login Panel, Security |
| **Type** | Functional (Negative Test) |
| **Priority** | High |
| **Pre-conditions** | 1. User is on the Home Page 2. User is not logged in 3. Login Panel is visible 4. No account lockout is currently active |
| **Test Steps** | 1. On the Home Page, locate the Login Panel 2. Attempt login with invalid credentials 3. Click the "Login" button 4. Observe error message (Attempt #1) 5. Enter different invalid credentials 6. Click the "Login" button (Attempt #2) 7. Observe error message 8. Repeat steps 5-7 three more times (Attempts #3, #4, #5) 9. After 5 failed attempts, try logging in with correct credentials 10. Observe system response |
| **Test Data** | 5 combinations of invalid username/password: 1. user1/wrongpass1 2. user2/wrongpass2 3. user3/wrongpass3 4. user4/wrongpass4 5. user5/wrongpass5 Then: validuser/validpass |
| **Expected Result** | 1. First 4 failed attempts show "Invalid username or password" error 2. Login Panel remains visible 3. On 5th attempt, one of the following should occur: a) Account is temporarily locked with message "Account locked due to multiple failed attempts" OR b) CAPTCHA challenge is presented OR c) Additional security prompt is displayed 4. After account restriction, valid credentials do NOT allow login 5. Error messages are consistent and user-friendly |
| **Actual Result** | *(To be filled during execution)* |
| **Status** | Not Executed |
| **Executed By** | [QA Engineer Name] |
| **Execution Date** | *(To be filled during execution)* |
| **Pass/Fail** | *(To be filled during execution)* |
| **Remarks/Comments** | Security best practice: System should implement account lockout or CAPTCHA after multiple failed attempts to prevent brute-force attacks. Record how many attempts trigger security measures. If account is locked, document the unlock mechanism. |

---

### TC-010: ICARUS Logo Navigation to Home Page

| Field | Value |
|-------|-------|
| **Test Case ID** | TC-010 |
| **Test Case Title** | Verify ICARUS logo navigation to home page from different pages |
| **Module/Component** | Navigation - Logo/Branding |
| **Type** | Functional |
| **Priority** | Low |
| **Pre-conditions** | 1. User is on the Home Page (https://icarus.cloudamber.com/Home/Index) 2. ICARUS logo is visible in the page header 3. Logo is clickable (cursor changes to pointer) |
| **Test Steps** | 1. Verify the ICARUS logo is displayed on the home page 2. Hover over the ICARUS logo and verify the cursor changes to pointer (clickable) 3. Click on the ICARUS logo 4. Observe the page that loads 5. Verify the URL and page content 6. If available, navigate to another page within the application 7. Click the ICARUS logo again 8. Verify navigation back to home page |
| **Test Data** | N/A |
| **Expected Result** | 1. ICARUS logo is visible and clickable on all pages 2. Cursor changes to pointer when hovering over the logo 3. Clicking the logo navigates to the home page (https://icarus.cloudamber.com/Home/Index) 4. Home page loads successfully 5. Logo acts as a breadcrumb navigation element 6. URL reflects home page after logo click |
| **Actual Result** | *(To be filled during execution)* |
| **Status** | Not Executed |
| **Executed By** | [QA Engineer Name] |
| **Execution Date** | *(To be filled during execution)* |
| **Pass/Fail** | *(To be filled during execution)* |
| **Remarks/Comments** | Standard UX pattern: Logo should always link to home page. Verify this works consistently across the application. Test in multiple browsers and screen resolutions. |

---

## Test Execution Summary

| TC ID  | Test Case Title | Status | Pass/Fail | Executed By | Execution Date | Remarks |
|--------|-----------------|--------|-----------|-------------|----------------|---------| 
| TC-001 | Successful Login with Valid Credentials | Not Executed | - | - | - | - |
| TC-002 | Login with Empty Username | Not Executed | - | - | - | - |
| TC-003 | Login with Empty Password | Not Executed | - | - | - | - |
| TC-004 | Login with Invalid Username | Not Executed | - | - | - | - |
| TC-005 | Login with Incorrect Password | Not Executed | - | - | - | - |
| TC-006 | Keep Me Logged In Checkbox | Not Executed | - | - | - | - |
| TC-007 | Forgot Password Link Navigation | Not Executed | - | - | - | - |
| TC-008 | Social Media Links Navigation | Not Executed | - | - | - | - |
| TC-009 | Multiple Failed Login Attempts | Not Executed | - | - | - | - |
| TC-010 | ICARUS Logo Navigation | Not Executed | - | - | - | - |

**Total Test Cases:** 10  
**Passed:** 0  
**Failed:** 0  
**Blocked:** 0  
**Not Executed:** 10  
**Pass Rate:** 0%

---

## Notes & Recommendations

1. **Functional Coverage:** These 10 test cases cover the main functional areas of the ICARUS login interface and navigation.
2. **Positive vs Negative Tests:** 4 positive tests (TC-001, TC-006, TC-007, TC-008, TC-010) and 6 negative/edge-case tests (TC-002, TC-003, TC-004, TC-005, TC-009).
3. **Security Considerations:** Test cases include validation for sensitive areas such as brute-force attack prevention and password security.
4. **Test Data:** Actual credentials required for TC-001, TC-005, TC-006, and TC-009. Use test environment credentials only.
5. **Browser Compatibility:** Execute these tests across multiple browsers (Chrome, Firefox, Safari, Edge) for consistency.
6. **Automation Potential:** Tests TC-001 through TC-010 can be automated using Selenium, Playwright, or similar tools.

---

*Document Version: 1.0 | Last Updated: May 25, 2026*
