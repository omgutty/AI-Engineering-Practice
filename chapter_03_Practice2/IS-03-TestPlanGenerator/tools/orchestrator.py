#!/usr/bin/env python3
"""
Orchestrator: Pipeline that ties all tools together
Fetches JIRA → Generates Test Plan → Formats Markdown
"""

import json
import sys
from fetch_jira_issue import JiraFetcher
from generate_test_plan import TestPlanGenerator
from format_markdown import MarkdownFormatter

class TestPlanOrchestrator:
    def __init__(self):
        self.jira_fetcher = JiraFetcher()
        self.test_plan_generator = TestPlanGenerator()
        self.markdown_formatter = MarkdownFormatter()
    
    def execute(self, issue_id):
        """Execute the full pipeline: JIRA → TestPlan → Markdown."""
        
        result = {
            "status": "in_progress",
            "issue_id": issue_id,
            "stages": {}
        }
        
        # Stage 1: Fetch JIRA Issue
        print(f"[1/3] Fetching JIRA issue: {issue_id}")
        jira_result = self.jira_fetcher.fetch_issue(issue_id)
        result["stages"]["jira_fetch"] = jira_result
        
        if jira_result.get("status") != "success":
            result["status"] = "error"
            result["error_message"] = jira_result.get("error_message")
            return result
        
        issue = jira_result.get("issue")
        print(f"✅ Fetched issue: {issue.get('summary')}")
        
        # Stage 2: Generate Test Plan
        print("[2/3] Generating test plan with GROQ...")
        test_plan_result = self.test_plan_generator.generate_test_plan(issue)
        result["stages"]["test_plan_generation"] = {
            "status": test_plan_result.get("status"),
            "warning": test_plan_result.get("warning")
        }
        
        if test_plan_result.get("status") != "success":
            result["status"] = "error"
            result["error_message"] = "Failed to generate test plan"
            return result
        
        test_plan = test_plan_result.get("test_plan")
        print(f"✅ Generated {len(test_plan.get('test_cases', []))} test cases")
        
        # Stage 3: Format Markdown
        print("[3/3] Formatting markdown output...")
        markdown_result = self.markdown_formatter.format_to_markdown(test_plan)
        result["stages"]["markdown_formatting"] = markdown_result
        
        if markdown_result.get("status") != "success":
            result["status"] = "error"
            result["error_message"] = markdown_result.get("error_message")
            return result
        
        print(f"✅ Saved to file: {markdown_result.get('file_name')}")
        
        # Success
        result["status"] = "success"
        result["output_file"] = markdown_result.get("file_path")
        result["output_filename"] = markdown_result.get("file_name")
        result["test_plan_summary"] = {
            "total_test_cases": len(test_plan.get("test_cases", [])),
            "positive_cases": len([tc for tc in test_plan.get("test_cases", []) if tc.get("type") == "positive"]),
            "negative_cases": len([tc for tc in test_plan.get("test_cases", []) if tc.get("type") == "negative"]),
            "critical_tests": len([tc for tc in test_plan.get("test_cases", []) if tc.get("priority") == "P0"])
        }
        
        return result

def main():
    if len(sys.argv) > 1:
        issue_id = sys.argv[1]
    else:
        issue_id = "IS-3"
    
    orchestrator = TestPlanOrchestrator()
    result = orchestrator.execute(issue_id)
    
    print("\n" + "="*60)
    print(json.dumps(result, indent=2, default=str))

if __name__ == "__main__":
    main()
