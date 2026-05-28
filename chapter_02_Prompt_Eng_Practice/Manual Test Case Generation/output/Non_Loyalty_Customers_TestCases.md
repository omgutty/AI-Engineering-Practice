# TEST CASES: Non-Loyalty Customers Feature - Store Traffic Dashboard

**Project Name:** Store Traffic Analytics & Customer Management System  
**Feature:** Add a clickable "Non-Loyalty Customers" view in Store Traffic  
**Test Plan ID:** TP-ST-2026-NLC-001  
**Release Version:** 1.2.0  
**Date:** May 27, 2026  

---

## Test Case Summary

| Sr. No. | Scenario ID | Test Case ID | Priority | Test Case Description | Pre-Conditions | Step No. | Action Steps | Test Data | Expected Result | Actual Result (Cycle 1) | Execution Status (Cycle 1) | Bug ID | Actual Result (Cycle 2) | Execution Status (Cycle 2) | Overall Status for Test Case | Remarks |
|---------|-------------|--------------|----------|----------------------|----------------|----------|--------------|-----------|-----------------|------------------------|--------------------------|--------|------------------------|--------------------------|------------------------------|---------|
| 1 | NLC-UI-001 | TC-NLC-UI-001 | HIGH | Verify "Non-Loyalty Customers" clickable element is visible in Store Traffic dashboard | 1. User is logged in with valid Store Owner/Store Admin credentials<br/>2. User has navigated to Store Traffic dashboard<br/>3. Store has transaction data available | 1 | Navigate to Store Traffic Dashboard | N/A | The Store Traffic dashboard loads successfully with navigation menu visible | | | | | | | |
| | | | | | | 2 | Look for "Non-Loyalty Customers" metric/element in the dashboard | N/A | "Non-Loyalty Customers" clickable element is displayed prominently in the dashboard | | | | | | | |
| | | | | | | 3 | Verify the element has clickable appearance (styling, cursor change on hover) | Move mouse over "Non-Loyalty Customers" element | Element has visual indication of being clickable (color change, cursor becomes pointer) | | | | | | | |
| 2 | NLC-UI-002 | TC-NLC-UI-002 | HIGH | Verify clicking "Non-Loyalty Customers" opens filtered transaction table | 1. User is logged in successfully<br/>2. User is on Store Traffic dashboard<br/>3. "Non-Loyalty Customers" element is visible and clickable | 1 | Navigate to Store Traffic Dashboard | N/A | Dashboard loads with "Non-Loyalty Customers" element visible | | | | | | | |
| | | | | | | 2 | Click on "Non-Loyalty Customers" metric/element | Single click on the element | A new page/modal/table view opens displaying filtered transactions | | | | | | | |
| | | | | | | 3 | Wait for page to load completely | Wait for 3-5 seconds | Filtered transaction table displays with only non-loyalty customer data | | | | | | | |
| 3 | NLC-DATA-001 | TC-NLC-DATA-001 | HIGH | Verify transaction table displays correct columns for non-loyalty customers | 1. User is logged in with appropriate permissions<br/>2. Non-Loyalty Customers transaction table is open<br/>3. Data is loaded in the table | 1 | Open Non-Loyalty Customers transaction table | N/A | Table loads successfully | | | | | | | |
| | | | | | | 2 | Verify all required columns are displayed | Check table header | The following columns are present: System Capture Data, Transaction Date, Location ID, Location Name, Cashier, Quantity, Amount, Status, Tags, Payment Types, Last Updated At, Last Updated By | | | | | | | |
| | | | | | | 3 | Verify column headers are properly labeled and visible | Inspect header row | All columns have clear, readable headers with proper alignment | | | | | | | |
| 4 | NLC-DATA-002 | TC-NLC-DATA-002 | HIGH | Verify only non-loyalty customer transactions are displayed in the table | 1. User is logged in<br/>2. Transaction table for non-loyalty customers is open<br/>3. Database has mixed loyalty and non-loyalty customer records | 1 | Open Non-Loyalty Customers filtered table | N/A | Table loads with transaction data | | | | | | | |
| | | | | | | 2 | Inspect transaction records in the table | Review 5-10 random records | All displayed transactions belong to non-loyalty customers (verified by loyalty status indicator or similar) | | | | | | | |
| | | | | | | 3 | Verify no loyalty customer transactions are present | Cross-check against loyalty customer records if available | No transactions from loyalty customers are displayed | | | | | | | |
| | | | | | | 4 | Verify data accuracy and consistency | Compare with backend data | Transaction details match source system data (amount, date, location, cashier) | | | | | | | |
| 5 | NLC-FILTER-001 | TC-NLC-FILTER-001 | MEDIUM | Verify Search by Location filter is functional | 1. User is logged in<br/>2. Non-Loyalty Customers transaction table is open<br/>3. Multiple locations have non-loyalty customer data | 1 | Navigate to the Filters section | N/A | Filters section is visible at the top of the table | | | | | | | |
| | | | | | | 2 | Locate "Search by Location" filter field | N/A | Search field is displayed and accessible | | | | | | | |
| | | | | | | 3 | Click on the location search field and enter a valid location | Enter location name: "Downtown Store" or Location ID: "LOC-001" | Search field accepts input and displays matching locations in dropdown | | | | | | | |
| | | | | | | 4 | Select a location from the dropdown | Click on a location option | Table data filters to show only transactions from the selected location | | | | | | | |
| 6 | NLC-FILTER-002 | TC-NLC-FILTER-002 | MEDIUM | Verify Select Date Range filter is functional | 1. User is logged in<br/>2. Non-Loyalty Customers table is open<br/>3. System clock is set to a valid date | 1 | Locate "Select Date Range" filter option | N/A | Date range filter is visible and accessible | | | | | | | |
| | | | | | | 2 | Click on the date range picker | Click on date field | Date picker calendar opens | | | | | | | |
| | | | | | | 3 | Select start date | Select date: "May 01, 2026" | Start date is populated in the filter | | | | | | | |
| | | | | | | 4 | Select end date | Select date: "May 27, 2026" | End date is populated in the filter and table updates to show only transactions within the date range | | | | | | | |
| 7 | NLC-FILTER-003 | TC-NLC-FILTER-003 | MEDIUM | Verify Search Button applies multiple filters | 1. User is logged in<br/>2. Non-Loyalty Customers table is open<br/>3. Multiple filter options are available | 1 | Set location filter | Enter "Downtown Store" | Location filter is populated | | | | | | | |
| | | | | | | 2 | Set date range filter | Select date range "May 01-27, 2026" | Date range filter is populated | | | | | | | |
| | | | | | | 3 | Click the "Search" button | Click Search button | Table refreshes and displays only non-loyalty customer transactions from "Downtown Store" within "May 01-27, 2026" | | | | | | | |
| 8 | NLC-ACTION-001 | TC-NLC-ACTION-001 | HIGH | Verify "Assign Loyalty ID" action button is visible and functional | 1. User is logged in with Store Admin/Owner role<br/>2. Non-Loyalty Customers transaction table is open<br/>3. At least one transaction record is present | 1 | View transaction table rows | N/A | Transaction rows are displayed with action buttons | | | | | | | |
| | | | | | | 2 | Locate "Assign Loyalty ID" button in a transaction row | Inspect row actions | "Assign Loyalty ID" button is visible in the row-level actions section | | | | | | | |
| | | | | | | 3 | Click "Assign Loyalty ID" button on a specific transaction | Select transaction ID: "TRX-2026-05-001" and click button | System navigates to Assign Loyalty ID module/screen with the transaction context pre-populated (customer details, transaction data) | | | | | | | |
| | | | | | | 4 | Verify relevant transaction and customer information is passed to the Assign Loyalty ID screen | Inspect the opened screen | Transaction ID, Customer details, Location, Amount, and other relevant data are visible in the Assign Loyalty ID module | | | | | | | |
| 9 | NLC-ACTION-002 | TC-NLC-ACTION-002 | HIGH | Verify "Capture Demographics" action button is visible and functional | 1. User is logged in with Store Admin/Owner role<br/>2. Non-Loyalty Customers transaction table is open<br/>3. Transaction records are available | 1 | View transaction table rows | N/A | Transaction rows are displayed | | | | | | | |
| | | | | | | 2 | Locate "Capture Demographics" button in a transaction row | Inspect row actions | "Capture Demographics" button is visible in row-level actions | | | | | | | |
| | | | | | | 3 | Click "Capture Demographics" button on a transaction | Select transaction ID: "TRX-2026-05-001" and click button | System opens the Demographics Capture screen with transaction and customer context pre-populated | | | | | | | |
| | | | | | | 4 | Verify customer transaction context is available in Demographics module | Inspect the opened Demographics capture screen | Customer ID, Transaction ID, Location, Transaction details are visible and linked to the demographics form | | | | | | | |
| 10 | NLC-ACTION-003 | TC-NLC-ACTION-003 | HIGH | Verify "Customer Communication / Comments" action button is visible and functional | 1. User is logged in with Store Admin/Owner role<br/>2. Non-Loyalty Customers transaction table is open<br/>3. Transaction data is loaded | 1 | View transaction table rows | N/A | Transaction rows are displayed with action columns | | | | | | | |
| | | | | | | 2 | Locate "Customer Communication / Comments" button in a transaction row | Inspect row actions | "Customer Communication / Comments" button is visible in row-level actions | | | | | | | |
| | | | | | | 3 | Click "Customer Communication / Comments" button | Select transaction ID: "TRX-2026-05-001" and click button | System opens Customer Communication module with transaction and customer context pre-populated | | | | | | | |
| | | | | | | 4 | Verify communication context includes customer and transaction information | Inspect the opened Communication screen | Customer details, Transaction context, and communication history (if any) are visible for reference | | | | | | | |
| 11 | NLC-REDIRECT-001 | TC-NLC-REDIRECT-001 | HIGH | Verify redirection behavior for "Assign Loyalty ID" action | 1. User is logged in<br/>2. Non-Loyalty Customers table is open<br/>3. User has permissions to assign loyalty IDs | 1 | Click "Assign Loyalty ID" action on a transaction | Select a transaction row and click action button | System opens Assign Loyalty ID module | | | | | | | |
| | | | | | | 2 | Verify the module opens with correct transaction context | Check URL and page title | URL contains transaction ID and customer context; module loads relevant data | | | | | | | |
| | | | | | | 3 | Complete the loyalty ID assignment action | Assign a loyalty ID and save | Action completes successfully and returns to the Non-Loyalty Customers table or confirmation screen | | | | | | | |
| 12 | NLC-REDIRECT-002 | TC-NLC-REDIRECT-002 | HIGH | Verify redirection behavior for "Capture Demographics" action | 1. User is logged in<br/>2. Non-Loyalty Customers table is open<br/>3. User has permissions to capture demographics | 1 | Click "Capture Demographics" action on a transaction | Select a transaction row and click action button | System opens Demographics Capture module with customer context | | | | | | | |
| | | | | | | 2 | Verify correct module and context are loaded | Inspect demographics form | Form displays customer transaction details and is ready for demographic data input | | | | | | | |
| | | | | | | 3 | Complete demographic capture | Enter required demographic data and save | Demographics are captured and stored; user is returned to the Non-Loyalty Customers table | | | | | | | |
| 13 | NLC-REDIRECT-003 | TC-NLC-REDIRECT-003 | HIGH | Verify redirection behavior for "Customer Communication / Comments" action | 1. User is logged in<br/>2. Non-Loyalty Customers table is open<br/>3. User has permissions to manage communications | 1 | Click "Customer Communication / Comments" action | Select a transaction row and click action button | System opens Customer Communication screen with customer context | | | | | | | |
| | | | | | | 2 | Verify communication context is loaded correctly | Inspect communication module | Customer ID, transaction reference, and communication history are pre-populated | | | | | | | |
| | | | | | | 3 | Complete communication action (e.g., send message) | Create and send communication | Communication is recorded and associated with the customer and transaction | | | | | | | |
| 14 | NLC-UI-CHANGES-001 | TC-NLC-UI-CHANGES-001 | MEDIUM | Verify Status filter is removed from top filters section | 1. User is logged in<br/>2. Non-Loyalty Customers table is open<br/>3. Previous version of the UI had Status filter | 1 | Inspect the top filters section | N/A | Top filters section displays Search by Location and Select Date Range filters | | | | | | | |
| | | | | | | 2 | Verify "Status" filter is NOT present | Check all filter options | Status filter is not displayed in the top filters area | | | | | | | |
| | | | | | | 3 | Verify "Type" filter is NOT present | Check all filter options | Type filter is not displayed in the top filters area | | | | | | | |
| 15 | NLC-UI-CHANGES-002 | TC-NLC-UI-CHANGES-002 | MEDIUM | Verify row-level actions display three buttons (Assign Loyalty ID, Capture Demographics, Customer Communication) | 1. User is logged in<br/>2. Non-Loyalty Customers transaction table is open<br/>3. Transaction rows are displayed | 1 | Inspect a transaction row | N/A | Transaction row is visible with action buttons | | | | | | | |
| | | | | | | 2 | Verify three action buttons are present in each row | Count and identify buttons | Exactly three buttons are displayed: "Assign Loyalty ID", "Capture Demographics", "Customer Communication / Comments" | | | | | | | |
| | | | | | | 3 | Verify "View Transaction" action is replaced by the three buttons | Check for old "View Transaction" button | Old "View Transaction" button is not present; only the three new buttons are shown | | | | | | | |
| 16 | NLC-SECURITY-001 | TC-NLC-SECURITY-001 | HIGH | Verify role-based access control for Non-Loyalty Customers view | 1. Test environment is set up<br/>2. Multiple user roles exist (Store Owner, Store Admin, Security Operator, Compliance Officer)<br/>3. Users have different permission levels | 1 | Log in as Store Owner | Use Store Owner credentials | User logs in successfully | | | | | | | |
| | | | | | | 2 | Verify Store Owner can access Non-Loyalty Customers view | Navigate to Store Traffic dashboard | Store Owner can see "Non-Loyalty Customers" element and open the filtered table | | | | | | | |
| | | | | | | 3 | Perform action (e.g., "Assign Loyalty ID") | Click action button | Action is executed successfully | | | | | | | |
| | | | | | | 4 | Log out and log in as Security Operator with limited permissions | Use Security Operator credentials | User logs in successfully | | | | | | | |
| | | | | | | 5 | Verify Security Operator permissions for Non-Loyalty Customers access | Navigate to Store Traffic dashboard | Based on role configuration, access is either granted, denied, or partially restricted (view-only) | | | | | | | |
| 17 | NLC-SECURITY-002 | TC-NLC-SECURITY-002 | HIGH | Verify audit logs track all access to Non-Loyalty Customers data and actions | 1. User is logged in with admin credentials<br/>2. Audit Logs feature is accessible<br/>3. Actions have been performed on Non-Loyalty Customers | 1 | Log in with admin credentials | Use admin credentials | Admin user logs in successfully | | | | | | | |
| | | | | | | 2 | Navigate to Audit Logs section | N/A | Audit Logs page/module is accessible | | | | | | | |
| | | | | | | 3 | Search for Non-Loyalty Customers access logs | Search for: "Non-Loyalty Customers", User, Date range | Audit logs display all access events to Non-Loyalty Customers view | | | | | | | |
| | | | | | | 4 | Verify action logs are recorded | Search for action: "Assign Loyalty ID", "Capture Demographics" | Each action performed is logged with: User ID, Timestamp, Action Type, Transaction ID, and Result | | | | | | | |
| 18 | NLC-PERF-001 | TC-NLC-PERF-001 | MEDIUM | Verify table loads within acceptable time for large data sets | 1. User is logged in<br/>2. Database contains large volume of non-loyalty customer transactions (10,000+ records)<br/>3. Test environment is configured | 1 | Open Non-Loyalty Customers transaction table | N/A | Table starts loading | | | | | | | |
| | | | | | | 2 | Measure time to display first set of records | Use browser developer tools or monitoring tool | Table displays initial records within 3-5 seconds (acceptable performance threshold) | | | | | | | |
| | | | | | | 3 | Verify pagination or lazy loading works | Scroll or navigate to next page | Additional records load without significant delay | | | | | | | |
| 19 | NLC-DATA-ACCURACY-001 | TC-NLC-DATA-ACCURACY-001 | HIGH | Verify transaction data accuracy in filtered table | 1. User is logged in<br/>2. Reference data is available (backend database, transaction system)<br/>3. Non-Loyalty Customers table is open | 1 | Identify a specific transaction in the table | Transaction ID: "TRX-2026-05-001" | Transaction is displayed in the table | | | | | | | |
| | | | | | | 2 | Cross-check table data with backend/source system | Compare: Amount, Date, Location, Customer ID, Payment Type | All displayed data matches source system data exactly (no discrepancies) | | | | | | | |
| | | | | | | 3 | Verify calculated fields (if any) are correct | Verify totals, sums, or other calculations | All calculations are accurate and match manual verification | | | | | | | |
| 20 | NLC-EDGE-CASE-001 | TC-NLC-EDGE-CASE-001 | MEDIUM | Verify system behavior when no non-loyalty customers exist | 1. User is logged in<br/>2. Test database is configured with only loyalty customers<br/>3. No non-loyalty transactions are available | 1 | Navigate to Store Traffic dashboard | N/A | Dashboard loads successfully | | | | | | | |
| | | | | | | 2 | Click on "Non-Loyalty Customers" element | Click the element | Table or view opens | | | | | | | |
| | | | | | | 3 | Verify empty state handling | Inspect the opened view | System displays a meaningful message (e.g., "No non-loyalty customers found") or an empty table with appropriate notification | | | | | | | |
| 21 | NLC-EDGE-CASE-002 | TC-NLC-EDGE-CASE-002 | MEDIUM | Verify system behavior with complex filter combinations | 1. User is logged in<br/>2. Multiple filters are available<br/>3. Large dataset exists | 1 | Apply Location filter | Select "Downtown Store" | Filter is applied | | | | | | | |
| | | | | | | 2 | Apply Date Range filter | Select "May 01-15, 2026" | Second filter is applied | | | | | | | |
| | | | | | | 3 | Apply additional custom filters (if supported) | Apply any additional filters | All filters work together and table displays correctly filtered results | | | | | | | |
| | | | | | | 4 | Click Reset or Clear Filters button (if available) | Click reset button | All filters are cleared and full dataset is displayed again | | | | | | | |
| 22 | NLC-MOBILE-001 | TC-NLC-MOBILE-001 | LOW | Verify Non-Loyalty Customers view is responsive on mobile devices | 1. Mobile or responsive testing environment is set up<br/>2. User is logged in on a mobile device<br/>3. Store Traffic dashboard is accessible | 1 | Navigate to Store Traffic on mobile browser | Access on iOS/Android device | Dashboard loads on mobile screen | | | | | | | |
| | | | | | | 2 | Locate and click "Non-Loyalty Customers" element | Click element on mobile | Mobile-optimized table view opens (or adaptive layout) | | | | | | | |
| | | | | | | 3 | Verify table columns are readable on mobile | Inspect table layout | Columns are either scrollable, stacked, or shown in card format for mobile readability | | | | | | | |
| | | | | | | 4 | Verify action buttons are accessible and clickable on mobile | Attempt to click action buttons | Buttons are properly sized and responsive for touch interaction | | | | | | | |

---

## Additional Test Coverage Notes

### Out of Scope (Not Tested in This Set)
- Browser-specific compatibility testing (covered separately)
- Performance testing with extreme load (>100,000 records)
- Accessibility testing (WCAG compliance)

### Risk Areas to Monitor
1. Data consistency after demographic capture and loyalty ID assignment
2. Concurrent user actions on the same transaction
3. Session timeout while performing actions
4. Error handling for failed API calls

### Test Environment Requirements
- Valid user accounts with appropriate roles (Store Owner, Store Admin, Compliance Officer)
- Non-loyalty customer transaction data loaded in test database
- Integration with Assign Loyalty ID, Demographics Capture, and Communication modules
- Audit logging system functional
- Multiple store locations configured for location-based filtering

---

**Document Version:** 1.0  
**Last Updated:** May 27, 2026  
**Status:** Ready for Execution
