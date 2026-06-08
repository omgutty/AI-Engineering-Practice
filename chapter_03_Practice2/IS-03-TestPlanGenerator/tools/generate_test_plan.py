#!/usr/bin/env python3
"""
Tool 2: Test Plan Generator (SOP-002)
Generates test cases using GROQ LLM based on JIRA issue data.
"""

import os
import json
import requests
import re
from dotenv import load_dotenv

# Load environment variables
load_dotenv(dotenv_path="../../.env")

class TestPlanGenerator:
    def __init__(self):
        self.groq_key = os.getenv("GROQ_KEY")
        self.groq_url = "https://api.groq.com/openai/v1/chat/completions"
        self.model = "mixtral-8x7b-32768"
        
    def generate_test_plan(self, issue):
        """Generate test plan from JIRA issue data using GROQ."""
        
        if not self.groq_key:
            return self._get_default_test_plan(issue)
        
        # Build prompt
        prompt = self._build_prompt(issue)
        
        try:
            headers = {
                "Authorization": f"Bearer {self.groq_key}",
                "Content-Type": "application/json"
            }
            
            payload = {
                "model": self.model,
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.7,
                "max_tokens": 3000
            }
            
            response = requests.post(
                self.groq_url,
                json=payload,
                headers=headers,
                timeout=30,
                verify=False
            )
            
            if response.status_code == 200:
                data = response.json()
                message_content = data["choices"][0]["message"]["content"]
                
                # Parse JSON from response
                test_plan = self._parse_test_plan_json(message_content, issue)
                
                return {
                    "status": "success",
                    "test_plan": test_plan
                }
            
            else:
                # Fallback to default
                return {
                    "status": "success",
                    "test_plan": self._get_default_test_plan(issue),
                    "warning": f"GROQ API error (HTTP {response.status_code}), using default test cases"
                }
        
        except Exception as e:
            # Graceful fallback
            return {
                "status": "success",
                "test_plan": self._get_default_test_plan(issue),
                "warning": f"GROQ connection error: {str(e)}, using default test cases"
            }
    
    def _build_prompt(self, issue):
        """Build the prompt for GROQ LLM."""
        
        return f"""You are a QA expert. Generate a detailed test plan for the following JIRA issue.

ISSUE DETAILS:
- ID: {issue.get('key', 'N/A')}
- Title: {issue.get('summary', 'N/A')}
- Description: {issue.get('description', 'N/A')}
- Type: {issue.get('issueType', 'N/A')}
- Priority: {issue.get('priority', 'N/A')}

REQUIREMENTS:
1. Create test objectives (2-3 high-level goals)
2. Define scope (what will/won't be tested)
3. Generate 8-12 test cases (mix of positive and negative)
4. For each test case, include:
   - id: TC-001, TC-002, etc.
   - title: string
   - type: "positive" or "negative"
   - priority: "P0", "P1", "P2", or "P3"
   - preconditions: ["string"]
   - steps: ["string"]
   - expected_result: "string"
   - rice_score: 0-100
5. Define acceptance criteria (3-5 criteria)
6. Suggest test data requirements

OUTPUT ONLY VALID JSON. Do not include markdown or explanations. JSON structure:
{{
  "test_objectives": ["obj1", "obj2"],
  "scope": "what will be tested",
  "test_cases": [
    {{
      "id": "TC-001",
      "title": "string",
      "type": "positive",
      "priority": "P0",
      "preconditions": ["prep1"],
      "steps": ["step1", "step2"],
      "expected_result": "string",
      "rice_score": 90
    }}
  ],
  "acceptance_criteria": ["criterion1"],
  "test_data": {{"key": "value"}}
}}"""
    
    def _parse_test_plan_json(self, response_text, issue):
        """Parse JSON from LLM response."""
        
        try:
            # Try to extract JSON from response
            json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
            
            if json_match:
                json_str = json_match.group(0)
                parsed = json.loads(json_str)
                
                return {
                    "issue_id": issue.get('key'),
                    "title": f"Test Plan for {issue.get('summary', 'Issue')}",
                    "test_objectives": parsed.get("test_objectives", []),
                    "scope": parsed.get("scope", ""),
                    "test_cases": parsed.get("test_cases", []),
                    "acceptance_criteria": parsed.get("acceptance_criteria", []),
                    "test_data": parsed.get("test_data", {}),
                    "timeline_estimate": "2-3 hours"
                }
        
        except json.JSONDecodeError:
            pass
        
        # Fallback
        return self._get_default_test_plan(issue)
    
    def _get_default_test_plan(self, issue):
        """Return a default test plan when LLM is unavailable."""
        
        return {
            "issue_id": issue.get('key'),
            "title": f"Test Plan for {issue.get('summary', 'Issue')}",
            "test_objectives": [
                f"Verify {issue.get('summary', 'feature')} functions correctly",
                "Validate input validation and error handling",
                "Ensure user experience meets acceptance criteria"
            ],
            "scope": f"Testing {issue.get('summary', 'the feature')} as specified in {issue.get('key')}",
            "test_cases": [
                {
                    "id": "TC-001",
                    "title": "Positive: Verify core functionality",
                    "type": "positive",
                    "priority": "P0",
                    "preconditions": ["System is ready", "User has valid credentials"],
                    "steps": ["Step 1", "Step 2", "Step 3"],
                    "expected_result": "Feature works as designed",
                    "rice_score": 95
                },
                {
                    "id": "TC-002",
                    "title": "Negative: Invalid input handling",
                    "type": "negative",
                    "priority": "P1",
                    "preconditions": ["System is ready"],
                    "steps": ["Enter invalid input", "Observe system response"],
                    "expected_result": "System shows appropriate error message",
                    "rice_score": 85
                },
                {
                    "id": "TC-003",
                    "title": "Edge case: Boundary values",
                    "type": "positive",
                    "priority": "P2",
                    "preconditions": ["System is ready"],
                    "steps": ["Enter boundary value", "Verify processing"],
                    "expected_result": "Boundary value is handled correctly",
                    "rice_score": 70
                }
            ],
            "acceptance_criteria": [
                "All test cases pass",
                "No critical bugs found",
                "Performance meets requirements"
            ],
            "test_data": {
                "valid_input": "example_data",
                "invalid_input": "bad_data"
            },
            "timeline_estimate": "2-3 hours"
        }

def main():
    generator = TestPlanGenerator()
    
    # Test with a sample issue
    sample_issue = {
        "key": "IS-3",
        "summary": "User login functionality",
        "description": "Implement user login with email and password",
        "issueType": "Story",
        "priority": "High"
    }
    
    result = generator.generate_test_plan(sample_issue)
    print(json.dumps(result, indent=2, default=str))

if __name__ == "__main__":
    main()
