#!/usr/bin/env python3
"""
Tool 1: JIRA Issue Fetcher (SOP-001)
Fetches issue details from JIRA API.
"""

import os
import json
import requests
import urllib3
from dotenv import load_dotenv
from datetime import datetime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Load environment variables
load_dotenv(dotenv_path="../../.env")

class JiraFetcher:
    def __init__(self):
        self.jira_url = os.getenv("JIRA_URL")
        self.jira_email = os.getenv("JIRA_EMAIL")
        self.jira_api_token = os.getenv("JIRA_API_TOKEN")
        self.session = requests.Session()
        
    def fetch_issue(self, issue_id):
        """Fetch a single issue from JIRA."""
        
        if not all([self.jira_url, self.jira_email, self.jira_api_token]):
            return {
                "status": "error",
                "error_message": "Missing JIRA credentials in .env"
            }
        
        try:
            url = f"{self.jira_url.rstrip('/')}/rest/api/3/issues/{issue_id}"
            
            response = self.session.get(
                url,
                auth=(self.jira_email, self.jira_api_token),
                timeout=10,
                headers={"Accept": "application/json"},
                verify=False
            )
            
            if response.status_code == 200:
                issue_data = response.json()
                fields = issue_data.get("fields", {})
                
                return {
                    "status": "success",
                    "issue": {
                        "key": issue_data.get("key"),
                        "summary": fields.get("summary", ""),
                        "description": fields.get("description", "") or "",
                        "issueType": fields.get("issuetype", {}).get("name", ""),
                        "priority": fields.get("priority", {}).get("name", "Medium"),
                        "status": fields.get("status", {}).get("name", ""),
                        "assignee": fields.get("assignee", {}).get("displayName") or "Unassigned",
                        "created": fields.get("created", ""),
                        "updated": fields.get("updated", ""),
                        "project": {
                            "key": fields.get("project", {}).get("key", ""),
                            "name": fields.get("project", {}).get("name", "")
                        },
                        "components": [c.get("name") for c in fields.get("components", [])],
                        "labels": fields.get("labels", [])
                    }
                }
            
            elif response.status_code == 404:
                return {
                    "status": "error",
                    "error_message": f"Issue '{issue_id}' not found in JIRA"
                }
            
            elif response.status_code == 401:
                return {
                    "status": "error",
                    "error_message": "JIRA authentication failed - check credentials"
                }
            
            else:
                return {
                    "status": "error",
                    "error_message": f"JIRA API error (HTTP {response.status_code}): {response.text[:100]}"
                }
        
        except requests.exceptions.Timeout:
            return {
                "status": "error",
                "error_message": "JIRA request timed out (30s)"
            }
        
        except Exception as e:
            return {
                "status": "error",
                "error_message": f"JIRA connection error: {str(e)}"
            }

def main():
    fetcher = JiraFetcher()
    
    # Test with IS-3
    result = fetcher.fetch_issue("IS-3")
    print(json.dumps(result, indent=2, default=str))

if __name__ == "__main__":
    main()
