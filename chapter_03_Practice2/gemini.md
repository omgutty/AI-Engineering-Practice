# gemini.md - Project Constitution (IS-3: Test Plan Generator)

## Project Identity
- **Project Name:** IS-3 Test Plan Generator
- **North Star:** Generate a comprehensive test plan from a JIRA issue (with RICE prioritization, positive & negative test cases, functional focus)
- **Status:** Phase 1 ✓ (Blueprint Complete) → Phase 2 Ready

---

## 1. Data Schema (INPUT/OUTPUT)

### Input Schema
```json
{
  "jira_id": "string (required, e.g., 'IS-123')",
  "jira_instance": "string (https://automationrun.atlassian.net/)",
  "project_key": "string (IS)"
}
```

### Output Schema (Markdown File)
```json
{
  "test_plan": {
    "issue_id": "string",
    "issue_title": "string",
    "test_objectives": ["string"],
    "scope": "string",
    "test_cases": [
      {
        "id": "TC-001",
        "title": "string",
        "preconditions": ["string"],
        "steps": ["string"],
        "expected_result": "string",
        "priority": "P0|P1|P2|P3",
        "test_type": "positive|negative",
        "rice_score": "number"
      }
    ],
    "acceptance_criteria": ["string"],
    "test_data": "object",
    "timeline_estimate": "string"
  },
  "status": "success|error",
  "error_message": "string (if error)"
}
```

---

## 2. Behavioral Rules
- **Rule 1:** Must include BOTH positive and negative test cases
- **Rule 2:** Focus on functional testing only (no performance/load testing)
- **Rule 3:** Apply RICE prioritization scoring to each test case
- **Rule 4:** Must fetch live data from JIRA (https://automationrun.atlassian.net/)
- **Rule 5:** Validate JIRA ID format (e.g., IS-123) before fetching
- **Rule 6:** Never make up data; if JIRA data is incomplete, flag it in output

---

## 3. Architectural Invariants
- Invariant: JIRA API must be called to fetch issue details (Source of Truth)
- Invariant: GroQ LLM generates test cases based on issue description
- Invariant: Output is always a valid markdown file
- Invariant: Every test case has a unique ID and priority
- Invariant: System halts gracefully if JIRA connection fails (no LLM hallucination)

---

## 4. External Integrations
- **JIRA API:** https://automationrun.atlassian.net/ (Project: IS)
  - Authentication: API Token (Credential: JIRA_API_TOKEN)
  - Rate Limit: TBD (to verify in Phase 2)
  - Timeout: 30 seconds
  
- **GroQ LLM API:** For generating test cases
  - Authentication: API Key (Credential: GROQ_API_KEY)
  - Model: mixtral-8x7b or similar
  - Temperature: 0.7 (deterministic but creative)

---

## 5. Maintenance Log
- Last Updated: June 8, 2026
- Blueprint Finalized: YES
- Next: Phase 2 (Link - API Verification)
- Critical Changes: Schema defined, integrations locked in
