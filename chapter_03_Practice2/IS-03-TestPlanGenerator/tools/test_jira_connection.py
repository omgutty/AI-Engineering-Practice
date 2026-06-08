#!/usr/bin/env python3
"""
Phase 2: Link - JIRA Connection Verification
Verifies that JIRA API is accessible and credentials are valid.
"""

import os
import json
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv(dotenv_path="../.env")

def test_jira_connection():
    """Test JIRA API connectivity and authentication."""
    
    JIRA_URL = os.getenv("JIRA_URL")
    JIRA_EMAIL = os.getenv("JIRA_EMAIL")
    JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")
    
    if not all([JIRA_URL, JIRA_EMAIL, JIRA_API_TOKEN]):
        return {
            "status": "error",
            "message": "Missing JIRA credentials in .env",
            "required": ["JIRA_URL", "JIRA_EMAIL", "JIRA_API_TOKEN"]
        }
    
    try:
        # Test endpoint: Get user profile
        url = f"{JIRA_URL.rstrip('/')}/rest/api/3/myself"
        
        response = requests.get(
            url,
            auth=(JIRA_EMAIL, JIRA_API_TOKEN),
            timeout=10,
            headers={"Accept": "application/json"}
        )
        
        if response.status_code == 200:
            user_data = response.json()
            return {
                "status": "success",
                "message": "JIRA connection successful",
                "user": user_data.get("displayName"),
                "email": user_data.get("emailAddress"),
                "account_id": user_data.get("accountId")
            }
        else:
            return {
                "status": "error",
                "message": f"JIRA authentication failed (HTTP {response.status_code})",
                "response": response.text[:200]
            }
            
    except Exception as e:
        return {
            "status": "error",
            "message": f"JIRA connection error: {str(e)}"
        }

if __name__ == "__main__":
    result = test_jira_connection()
    print(json.dumps(result, indent=2))
