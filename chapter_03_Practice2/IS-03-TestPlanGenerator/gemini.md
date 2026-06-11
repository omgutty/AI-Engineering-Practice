# IS-03 Test Plan Generator - Project Constitution

## Project Identity
**North Star:** Automatically generate comprehensive test plans from JIRA issues using GROQ LLM.

**Integrations:**
- JIRA API (fetch issue data)
- GROQ API (generate test plans with AI)
- Vercel (deployment)

**Source of Truth:** JIRA issues (IS-* format)

**Delivery Payload:** Test plan in Markdown with test cases, edge cases, and regression suite

**Behavioral Rules:**
- Never modify JIRA data (read-only)
- Handle API failures gracefully with fallback messages
- Validate all credentials before processing
- Rate limit JIRA API calls to 5/sec
- Cache results in `.tmp/` for debugging

---

## Data Schemas

### INPUT: JIRA Issue
```json
{
  "key": "IS-3",
  "fields": {
    "summary": "User Login Feature",
    "description": "...",
    "priority": "High",
    "labels": ["feature", "auth"],
    "issuelinks": []
  }
}
```

### INTERMEDIATE: Raw Test Plan (from GROQ)
```json
{
  "title": "Test Plan for IS-3",
  "objective": "Verify login functionality",
  "test_cases": [
    {
      "id": "TC-001",
      "type": "positive|negative|edge",
      "title": "Valid credentials login",
      "steps": ["Step 1", "Step 2"],
      "expected": "User logged in",
      "priority": "P1"
    }
  ],
  "regression_suite": [...],
  "edge_cases": [...]
}
```

### OUTPUT: Markdown Test Plan
```markdown
# Test Plan: IS-3 - User Login Feature

## Objective
Verify login functionality works correctly.

## Test Cases
| ID | Type | Title | Priority |
|---|---|---|---|
| TC-001 | Positive | Valid credentials | P1 |

## Regression Suite
- All previous test cases must pass
```

---

## Architecture Layers

### Layer 1: SOPs (architecture/)
- `SOP-001-JIRA-Fetcher.md` - How to fetch issues
- `SOP-002-TestPlan-Generator.md` - How to generate test plans
- `SOP-003-Markdown-Formatter.md` - How to format output

### Layer 2: Navigation (tools/orchestrator.py)
Routes data between tools. Does NOT perform complex logic.

### Layer 3: Tools (tools/)
- `fetch_jira_issue.py` - Deterministic JIRA fetcher
- `generate_test_plan.py` - Deterministic test plan generator
- `format_markdown.py` - Deterministic markdown formatter

---

## API Contracts

### POST /api/generate-test-plan
**Request:**
```json
{
  "issue_id": "IS-3",
  "jira_email": "user@domain.com",
  "jira_token": "ATATT...",
  "jira_url": "https://domain.atlassian.net/",
  "groq_key": "gsk_..."
}
```

**Response (Success):**
```json
{
  "status": "success",
  "issue_id": "IS-3",
  "title": "Test Plan: IS-3",
  "test_case_count": 12,
  "positive_count": 8,
  "negative_count": 3,
  "edge_cases_count": 1,
  "markdown": "# Test Plan..."
}
```

**Response (Error):**
```json
{
  "status": "error",
  "error": "Invalid JIRA credentials",
  "stage": "jira_fetch"
}
```

### GET /api/health
Returns `{"status": "ok", "message": "API running"}`

---

## Behavioral Rules (Non-Negotiable)

1. **JIRA Authentication:** Email + API Token (never password)
2. **Test Plan Generation:** Always include positive, negative, and edge cases
3. **Rate Limiting:** Max 5 JIRA API calls per second
4. **Error Handling:** Never expose API keys in error messages
5. **Fallback:** If GROQ fails, return structured template test plan
6. **Frontend:** Settings stored in localStorage; credentials NOT in React code

---

## Failure Modes & Fallbacks

| Failure | Fallback |
|---------|----------|
| GROQ API timeout | Return template-based test plan |
| Invalid JIRA token | Return 401 error with clear message |
| Network error | Return 503 with retry suggestion |
| Issue not found | Return 404 with "Check issue ID" |

---

## Maintenance Log

**Version:** 1.0  
**Last Updated:** June 10, 2026  
**Status:** Production Ready  
**Critical Issues:** None  

### Recent Changes
- ✅ Updated JIRA credentials (om.gutty@cygnet.one)
- ✅ Migrated to Cygnet JIRA instance
- ✅ Added SSL certificate verification workaround
- ✅ Implemented Vercel deployment

---

## Deployment Checklist
- [ ] All credentials in `.env`
- [ ] JIRA connection verified
- [ ] GROQ connection verified
- [ ] React build passes
- [ ] Backend tests pass
- [ ] Vercel deployment successful
- [ ] Health check passes
- [ ] Test plan generation works end-to-end
