# SOP-002: Test Plan Generator (GROQ LLM)

**Phase 3, Layer 1: Architecture SOP**

## Goal
Generate a comprehensive test plan from JIRA issue data using GROQ LLM, following RICE prioritization and including positive/negative test cases.

## Input
```json
{
  "issue": {
    "key": "IS-3",
    "summary": "string",
    "description": "string",
    "issueType": "string",
    "priority": "string"
  },
  "groq_api_key": "string",
  "model": "mixtral-8x7b-32768"
}
```

## Output (JSON)
```json
{
  "status": "success|error",
  "test_plan": {
    "issue_id": "IS-3",
    "title": "Test Plan for [Issue Summary]",
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
    "test_data": {
      "key1": "value1"
    },
    "timeline_estimate": "string"
  },
  "error_message": "string (if error)"
}
```

## Prompt Template (for GROQ)
```
You are a QA expert. Generate a detailed test plan for the following JIRA issue.

ISSUE DETAILS:
- ID: {issue_key}
- Title: {summary}
- Description: {description}
- Type: {issueType}
- Priority: {priority}

REQUIREMENTS:
1. Create test objectives (2-3 high-level goals)
2. Define scope (what will/won't be tested)
3. Generate 8-12 test cases (mix of positive and negative)
4. For each test case, include:
   - ID (TC-001, TC-002, etc.)
   - Title
   - Type (positive or negative)
   - Priority (P0=Critical, P1=High, P2=Medium, P3=Low)
   - Preconditions
   - Steps (numbered)
   - Expected result
   - RICE score (0-100, where 100 = highest priority)
5. Define acceptance criteria (3-5 criteria)
6. Suggest test data requirements

FORMAT OUTPUT AS VALID JSON ONLY. No markdown, no explanations.
```

## Tool Logic (Python)
1. **Validate Input:**
   - Check GROQ API key
   - Validate issue data structure

2. **Build Prompt:**
   - Substitute issue details into template
   - Ensure JSON format requirement

3. **Call GROQ API:**
   - Model: mixtral-8x7b-32768
   - Temperature: 0.7 (deterministic but creative)
   - Max tokens: 2000
   - Timeout: 30 seconds

4. **Parse Response:**
   - Extract JSON from response
   - Validate structure against schema
   - Fallback to default test cases if parsing fails

5. **Enhance Data:**
   - Sort test cases by RICE score (descending)
   - Ensure all required fields present
   - Add defaults for missing data

## Edge Cases
- **Invalid JSON from LLM:** Log error, return default test cases
- **API Rate Limit (429):** Add exponential backoff
- **Timeout:** Return partial test plan with available data
- **Empty Issue:** Use generic test objectives

## Error Handling
- Never hallucinate data (all test cases must relate to issue)
- Validate RICE scores are numeric
- Log all API calls and responses
- Return error object if LLM fails

## Success Criteria
- Test plan is valid JSON
- Minimum 5 test cases (positive + negative mix)
- RICE scores present for all test cases
- No missing required fields
