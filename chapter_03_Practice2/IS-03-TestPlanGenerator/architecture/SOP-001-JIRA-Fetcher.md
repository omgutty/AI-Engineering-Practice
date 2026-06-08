# SOP-001: JIRA Issue Fetcher

**Phase 3, Layer 1: Architecture SOP**

## Goal
Fetch issue details from JIRA API for a given issue ID, ensuring data integrity and error handling.

## Input
- `issue_id` (string): JIRA issue ID, e.g., "IS-3"
- `jira_url` (string): Base JIRA URL from env
- `jira_email` (string): JIRA account email from env
- `jira_api_token` (string): JIRA API token from env

## Output (JSON)
```json
{
  "status": "success|error",
  "issue": {
    "key": "IS-3",
    "summary": "string",
    "description": "string",
    "issueType": "string",
    "priority": "string",
    "status": "string",
    "assignee": "string",
    "created": "ISO 8601 timestamp",
    "updated": "ISO 8601 timestamp",
    "project": {
      "key": "IS",
      "name": "string"
    },
    "components": ["string"],
    "labels": ["string"]
  },
  "error_message": "string (if error)"
}
```

## Tool Logic (Python)
1. **Validate Input:**
   - Check issue_id format (alphanumeric + dash)
   - Verify env variables are set

2. **Build API Request:**
   - Endpoint: `{JIRA_URL}/rest/api/3/issues/{issue_id}`
   - Auth: HTTP Basic (email, token)
   - Headers: Accept: application/json

3. **Handle Response:**
   - 200 OK: Parse and return issue data
   - 401: Auth failed → return error
   - 404: Issue not found → return error
   - 5XX: Server error → return error with retry flag

4. **Data Transformation:**
   - Extract only required fields
   - Normalize timestamps to ISO 8601
   - Clean HTML from description

## Edge Cases
- **Empty Description:** Use empty string
- **Missing Assignee:** Use "Unassigned"
- **Special Characters:** Escape JSON properly
- **Rate Limit (429):** Add exponential backoff retry

## Error Handling
- Graceful failure (never crash)
- Return structured error object
- Log all failures to .tmp/jira_errors.log

## Success Criteria
- Issue data is valid JSON
- All required fields present
- HTTP 200 response
