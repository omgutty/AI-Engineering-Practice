#!/usr/bin/env python3
"""
Backend Flask Server for Test Plan Generator
Handles API requests and orchestrates the tools
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
import sys
from pathlib import Path

# Add tools directory to path
tools_dir = Path(__file__).parent.parent / "tools"
sys.path.insert(0, str(tools_dir))

from fetch_jira_issue import JiraFetcher
from generate_test_plan import TestPlanGenerator
from format_markdown import MarkdownFormatter

app = Flask(__name__)
CORS(app)

# Initialize tools
jira_fetcher = JiraFetcher()
test_plan_generator = TestPlanGenerator()
markdown_formatter = MarkdownFormatter()

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint."""
    return jsonify({
        "status": "ok",
        "message": "Test Plan Generator API is running"
    })

@app.route('/api/generate-test-plan', methods=['POST'])
def generate_test_plan():
    """
    Main endpoint: Generate test plan from JIRA issue
    
    POST body:
    {
      "issue_id": "IS-3",
      "jira_email": "user@company.com",
      "jira_token": "API_TOKEN",
      "jira_url": "https://domain.atlassian.net/",
      "groq_key": "GROQ_API_KEY"
    }
    """
    
    try:
        data = request.get_json()
        issue_id = data.get('issue_id')
        
        if not issue_id:
            return jsonify({"error": "issue_id is required"}), 400
        
        # Stage 1: Fetch JIRA Issue
        jira_result = jira_fetcher.fetch_issue(issue_id)
        
        if jira_result.get("status") != "success":
            return jsonify({
                "error": jira_result.get("error_message"),
                "stage": "jira_fetch"
            }), 400
        
        issue = jira_result.get("issue")
        
        # Stage 2: Generate Test Plan
        test_plan_result = test_plan_generator.generate_test_plan(issue)
        
        if test_plan_result.get("status") != "success":
            return jsonify({
                "error": "Failed to generate test plan",
                "stage": "test_plan_generation"
            }), 500
        
        test_plan = test_plan_result.get("test_plan")
        
        # Stage 3: Format Markdown
        markdown_result = markdown_formatter.format_to_markdown(test_plan)
        
        if markdown_result.get("status") != "success":
            return jsonify({
                "error": markdown_result.get("error_message"),
                "stage": "markdown_formatting"
            }), 500
        
        # Prepare response
        test_cases = test_plan.get("test_cases", [])
        
        response = {
            "status": "success",
            "issue_id": issue_id,
            "title": test_plan.get("title"),
            "test_case_count": len(test_cases),
            "positive_count": len([tc for tc in test_cases if tc.get("type") == "positive"]),
            "negative_count": len([tc for tc in test_cases if tc.get("type") == "negative"]),
            "critical_count": len([tc for tc in test_cases if tc.get("priority") == "P0"]),
            "test_objectives": test_plan.get("test_objectives", []),
            "test_cases": test_cases,
            "acceptance_criteria": test_plan.get("acceptance_criteria", []),
            "markdown": markdown_result.get("markdown"),
            "warning": test_plan_result.get("warning")
        }
        
        return jsonify(response)
    
    except Exception as e:
        return jsonify({
            "error": f"Internal server error: {str(e)}"
        }), 500

@app.route('/api/jira-test', methods=['GET'])
def jira_test():
    """Test JIRA connection."""
    
    try:
        # Try to fetch the logged-in user
        result = jira_fetcher.session.get(
            f"{jira_fetcher.jira_url.rstrip('/')}/rest/api/3/myself",
            auth=(jira_fetcher.jira_email, jira_fetcher.jira_api_token),
            timeout=10,
            headers={"Accept": "application/json"},
            verify=False
        )
        
        if result.status_code == 200:
            user_data = result.json()
            return jsonify({
                "status": "success",
                "message": "JIRA connection successful",
                "user": user_data.get("displayName"),
                "email": user_data.get("emailAddress")
            })
        else:
            return jsonify({
                "status": "error",
                "message": f"JIRA connection failed (HTTP {result.status_code})"
            }), 400
    
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"JIRA connection error: {str(e)}"
        }), 500

@app.route('/api/groq-test', methods=['GET'])
def groq_test():
    """Test GROQ connection."""
    
    try:
        import requests
        import urllib3
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        
        groq_key = os.getenv("GROQ_KEY")
        
        if not groq_key:
            return jsonify({
                "status": "error",
                "message": "GROQ_KEY not found in environment"
            }), 400
        
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {groq_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "mixtral-8x7b-32768",
            "messages": [
                {"role": "user", "content": "Say 'Working' in one word."}
            ],
            "temperature": 0.7,
            "max_tokens": 10
        }
        
        response = requests.post(
            url,
            json=payload,
            headers=headers,
            timeout=10,
            verify=False
        )
        
        if response.status_code == 200:
            data = response.json()
            message = data["choices"][0]["message"]["content"]
            return jsonify({
                "status": "success",
                "message": "GROQ connection successful",
                "response": message.strip()
            })
        else:
            return jsonify({
                "status": "error",
                "message": f"GROQ connection failed (HTTP {response.status_code})"
            }), 400
    
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"GROQ connection error: {str(e)}"
        }), 500

@app.route('/api/config', methods=['GET'])
def get_config():
    """Get current configuration (safe, no secrets)."""
    
    return jsonify({
        "jira_url": jira_fetcher.jira_url,
        "jira_email": jira_fetcher.jira_email,
        "groq_model": test_plan_generator.model
    })

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Load environment variables
    from dotenv import load_dotenv
    env_path = Path(__file__).parent.parent / ".env"
    load_dotenv(dotenv_path=env_path)
    
    # Run development server
    app.run(debug=True, host='0.0.0.0', port=5000)
