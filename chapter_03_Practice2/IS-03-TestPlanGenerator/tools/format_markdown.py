#!/usr/bin/env python3
"""
Tool 3: Markdown Test Plan Formatter (SOP-003)
Converts test plan JSON to professional markdown format.
"""

import os
import json
from datetime import datetime

class MarkdownFormatter:
    def __init__(self):
        self.output_dir = ".tmp"
        os.makedirs(self.output_dir, exist_ok=True)
    
    def format_to_markdown(self, test_plan):
        """Convert test plan JSON to markdown format."""
        
        try:
            markdown = self._build_markdown(test_plan)
            
            # Save to file
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            issue_id = test_plan.get("issue_id", "TEST_PLAN")
            filename = f"{issue_id}_TestPlan_{timestamp}.md"
            filepath = os.path.join(self.output_dir, filename)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(markdown)
            
            return {
                "status": "success",
                "file_path": filepath,
                "file_name": filename,
                "markdown": markdown
            }
        
        except Exception as e:
            return {
                "status": "error",
                "error_message": f"Failed to format markdown: {str(e)}"
            }
    
    def _build_markdown(self, test_plan):
        """Build markdown content from test plan."""
        
        lines = []
        
        # Header
        lines.append(f"# Test Plan: {test_plan.get('issue_id')} - {test_plan.get('title')}")
        lines.append("")
        lines.append(f"**Generated:** {datetime.now().isoformat()}")
        lines.append("**Status:** Ready for Review")
        lines.append("")
        lines.append("---")
        lines.append("")
        
        # Test Objectives
        lines.append("## 1. Test Objectives")
        lines.append("")
        for obj in test_plan.get("test_objectives", []):
            lines.append(f"- {obj}")
        lines.append("")
        lines.append("---")
        lines.append("")
        
        # Scope
        lines.append("## 2. Scope")
        lines.append("")
        lines.append("### In Scope")
        lines.append(f"- {test_plan.get('scope', 'Testing specified features')}")
        lines.append("")
        lines.append("### Out of Scope")
        lines.append("- Non-functional testing")
        lines.append("- Performance testing")
        lines.append("")
        lines.append("---")
        lines.append("")
        
        # Test Cases Summary Table
        test_cases = test_plan.get("test_cases", [])
        lines.append(f"## 3. Test Cases ({len(test_cases)} Total)")
        lines.append("")
        
        # Build summary table
        lines.append("| ID | Title | Type | Priority | RICE Score |")
        lines.append("|----|----|------|----------|------------|")
        for tc in sorted(test_cases, key=lambda x: x.get("rice_score", 0), reverse=True):
            priority_emoji = self._get_priority_emoji(tc.get("priority", "P2"))
            type_icon = "✅" if tc.get("type") == "positive" else "❌"
            lines.append(
                f"| {tc.get('id')} | {tc.get('title')} | {type_icon} {tc.get('type')} | "
                f"{priority_emoji} {tc.get('priority')} | {tc.get('rice_score', 0)} |"
            )
        lines.append("")
        lines.append("---")
        lines.append("")
        
        # Detailed Test Cases
        lines.append("## 4. Detailed Test Cases")
        lines.append("")
        
        for idx, tc in enumerate(sorted(test_cases, key=lambda x: x.get("rice_score", 0), reverse=True), 1):
            lines.append(f"### {tc.get('id')}: {tc.get('title')}")
            lines.append("")
            lines.append(f"**Type:** {tc.get('type').capitalize()}")
            lines.append(f"**Priority:** {tc.get('priority')} ({self._priority_description(tc.get('priority'))})")
            lines.append(f"**RICE Score:** {tc.get('rice_score', 0)}")
            lines.append("")
            
            # Preconditions
            lines.append("**Preconditions:**")
            preconditions = tc.get("preconditions", [])
            if preconditions:
                for i, precond in enumerate(preconditions, 1):
                    lines.append(f"{i}. {precond}")
            else:
                lines.append("- System is ready")
            lines.append("")
            
            # Test Steps
            lines.append("**Test Steps:**")
            steps = tc.get("steps", [])
            if steps:
                for i, step in enumerate(steps, 1):
                    lines.append(f"{i}. {step}")
            else:
                lines.append("1. Execute test")
            lines.append("")
            
            # Expected Result
            lines.append("**Expected Result:**")
            expected = tc.get("expected_result", "Test passes")
            lines.append(f"- {expected}")
            lines.append("")
            lines.append("---")
            lines.append("")
        
        # Acceptance Criteria
        lines.append("## 5. Acceptance Criteria")
        lines.append("")
        for criterion in test_plan.get("acceptance_criteria", []):
            lines.append(f"- [ ] {criterion}")
        lines.append("")
        lines.append("---")
        lines.append("")
        
        # Test Data
        test_data = test_plan.get("test_data", {})
        if test_data:
            lines.append("## 6. Test Data Requirements")
            lines.append("")
            lines.append("| Variable | Type | Example | Notes |")
            lines.append("|----------|------|---------|-------|")
            for key, value in test_data.items():
                lines.append(f"| {key} | string | {value} | Test data |")
            lines.append("")
            lines.append("---")
            lines.append("")
        
        # Timeline
        lines.append("## 7. Timeline Estimate")
        lines.append("")
        lines.append(f"**Total Estimated Time:** {test_plan.get('timeline_estimate', '2-3 hours')}")
        lines.append("")
        lines.append("---")
        lines.append("")
        
        # Footer
        lines.append("## Notes")
        lines.append("")
        lines.append("- Critical tests (P0) should be executed first")
        lines.append("- Tests are sorted by RICE score (highest priority first)")
        lines.append("- Prepare test environment using the test data table above")
        lines.append("- Report any issues found during execution")
        
        return "\n".join(lines)
    
    def _get_priority_emoji(self, priority):
        """Get emoji for priority level."""
        emojis = {
            "P0": "🔴",
            "P1": "🟠",
            "P2": "🟡",
            "P3": "🟢"
        }
        return emojis.get(priority, "⚪")
    
    def _priority_description(self, priority):
        """Get description for priority level."""
        descriptions = {
            "P0": "Critical",
            "P1": "High",
            "P2": "Medium",
            "P3": "Low"
        }
        return descriptions.get(priority, "Unknown")

def main():
    formatter = MarkdownFormatter()
    
    # Test with a sample test plan
    sample_test_plan = {
        "issue_id": "IS-3",
        "title": "Test Plan for User Login",
        "test_objectives": [
            "Verify login functionality works correctly",
            "Validate error handling for invalid credentials"
        ],
        "scope": "Testing user authentication and login workflow",
        "test_cases": [
            {
                "id": "TC-001",
                "title": "Login with valid credentials",
                "type": "positive",
                "priority": "P0",
                "preconditions": ["User account exists", "System is accessible"],
                "steps": ["Navigate to login page", "Enter valid credentials", "Click Login"],
                "expected_result": "User logged in successfully",
                "rice_score": 95
            }
        ],
        "acceptance_criteria": [
            "All tests pass",
            "No bugs found"
        ],
        "test_data": {
            "username": "test_user@example.com",
            "password": "SecurePass123"
        },
        "timeline_estimate": "2-3 hours"
    }
    
    result = formatter.format_to_markdown(sample_test_plan)
    print(json.dumps(result, indent=2, default=str))

if __name__ == "__main__":
    main()
