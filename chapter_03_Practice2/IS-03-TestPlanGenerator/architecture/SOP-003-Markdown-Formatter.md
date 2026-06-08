# SOP-003: Markdown Test Plan Formatter

**Phase 3, Layer 1: Architecture SOP**

## Goal
Transform test plan JSON into a professional, readable markdown file.

## Input
```json
{
  "issue_id": "IS-3",
  "title": "string",
  "test_objectives": ["string"],
  "scope": "string",
  "test_cases": [
    {
      "id": "TC-001",
      "title": "string",
      "type": "positive|negative",
      "priority": "P0|P1|P2|P3",
      "preconditions": ["string"],
      "steps": ["string"],
      "expected_result": "string",
      "rice_score": 0-100
    }
  ],
  "acceptance_criteria": ["string"],
  "test_data": {},
  "timeline_estimate": "string"
}
```

## Output
- **File:** `.tmp/TestPlan_{issue_id}_{timestamp}.md`
- **Format:** Professional markdown with tables, sections, and styling

## Markdown Template

```markdown
# Test Plan: {Issue_ID} - {Title}

**Generated:** {ISO 8601 timestamp}  
**Status:** Ready for Review

---

## 1. Test Objectives

- Objective 1
- Objective 2
- ...

---

## 2. Scope

### In Scope
- {scope details}

### Out of Scope
- {non-testable items}

---

## 3. Test Cases ({total_count})

| TC ID | Title | Type | Priority | Steps | Expected | RICE |
|-------|-------|------|----------|-------|----------|------|
| TC-001 | ... | Positive | P0 | 5 | ... | 95 |
| TC-002 | ... | Negative | P1 | 4 | ... | 72 |

### Detailed Test Cases

#### TC-001: {Title}
- **Type:** Positive
- **Priority:** P0 (Critical)
- **RICE Score:** 95

**Preconditions:**
1. Precondition 1
2. Precondition 2

**Test Steps:**
1. Step 1
2. Step 2
3. Step 3

**Expected Result:**
- Result 1
- Result 2

---

## 4. Acceptance Criteria

- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

---

## 5. Test Data Requirements

| Variable | Type | Example | Notes |
|----------|------|---------|-------|
| username | string | test_user | Valid user account |
| password | string | Pass@123 | Must meet security policy |

---

## 6. Timeline Estimate

**Total Test Execution Time:** {estimate}  
**Parallel Test Execution:** Yes (Independent tests)

---

## Notes

- Critical tests (P0) should be executed first
- Tests are sorted by RICE score (highest priority first)
- Use the test data table to prepare environment
```

## Tool Logic (Python)
1. **Validate Input:** Check all required fields present

2. **Build Markdown:**
   - Add header section with metadata
   - Build objectives section
   - Build scope section
   - Create summary table of all test cases
   - Create detailed sections for each test case
   - Add acceptance criteria
   - Add test data table
   - Add timeline section

3. **Format Details:**
   - Sort test cases by RICE score (descending)
   - Color-code priorities (P0=🔴, P1=🟠, P2=🟡, P3=🟢)
   - Use readable spacing and tables
   - Add emoji for visual clarity

4. **Save File:**
   - Write to `.tmp/TestPlan_{issue_id}_{timestamp}.md`
   - Return file path

## Edge Cases
- **Empty test cases:** Still generate framework
- **Missing RICE scores:** Use default 50
- **Special characters in title:** Escape properly
- **Very long descriptions:** Truncate with ellipsis

## Error Handling
- Validate JSON input before processing
- Handle missing optional fields gracefully
- Return error if output file can't be written

## Success Criteria
- Markdown file created successfully
- All test cases included
- Valid markdown syntax
- File is readable in all markdown viewers
