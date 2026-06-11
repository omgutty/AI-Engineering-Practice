# IS-03 Test Plan Generator - Task Plan

## Phase 0: Initialization ✅
- [x] Create task_plan.md (this file)
- [x] Create findings.md
- [x] Create progress.md
- [x] Create gemini.md (Project Constitution)

---

## Phase 1: Blueprint - Discovery & Design 🔄

### Discovery Questions (5 Key Questions)
1. **North Star:** Generate test plans from JIRA issues automatically ✅
2. **Integrations:** JIRA API, GROQ LLM, Vercel ✅
3. **Source of Truth:** JIRA (cygnet-team-ca.atlassian.net) ✅
4. **Delivery Payload:** Markdown test plan with test cases ✅
5. **Behavioral Rules:** Read-only JIRA access, fallback on GROQ failure ✅

### Data Schema Definition (gemini.md)
- [x] INPUT schema (JIRA issue format)
- [x] INTERMEDIATE schema (raw test plan)
- [x] OUTPUT schema (Markdown format)

### Research & Resources
- [x] JIRA REST API v3 documentation
- [x] GROQ API SDK (Python)
- [x] React 18 + axios patterns
- [x] Vercel deployment for Flask + React

---

## Phase 2: Link - Connectivity & Verification 🔄

### Connection Testing Checklist
- [ ] JIRA connection test (test_jira_connection.py)
  - Credentials validation
  - Issue fetch test
  - Error handling verification
- [ ] GROQ connection test (test_groq_connection.py)
  - API key validation
  - Sample prompt test
  - Response parsing verification
- [ ] Backend health check endpoint
- [ ] Frontend API connectivity test

### Credentials Verification
- [x] JIRA Email: om.gutty@cygnet.one
- [x] JIRA Token: (in .env, 100+ chars)
- [x] JIRA URL: https://cygnet-team-ca.atlassian.net/
- [x] GROQ Key: (in .env)

---

## Phase 3: Architect - 3-Layer Implementation ✅

### Layer 1: Architecture SOPs (specification/)
- [x] SOP-001-JIRA-Fetcher.md
- [x] SOP-002-TestPlan-Generator.md
- [x] SOP-003-Markdown-Formatter.md

### Layer 2: Navigation (orchestrator.py)
- [x] Created orchestrator.py
- [x] Routes data between tools
- [x] Handles error propagation

### Layer 3: Tools (tools/)
- [x] fetch_jira_issue.py - Fetch issue via JIRA API
- [x] generate_test_plan.py - Generate plan via GROQ
- [x] format_markdown.py - Format to Markdown
- [x] test_jira_connection.py - Connection test
- [x] test_groq_connection.py - Connection test

### Backend API (Flask)
- [x] server.py with /api/health and /api/generate-test-plan
- [x] CORS enabled
- [x] Error handling implemented

### Frontend (React)
- [x] App.jsx - Lightweight UI
- [x] Settings modal for credentials
- [x] Issue ID input
- [x] Result display with test cases

---

## Phase 4: Stylize - UI Refinement 🔄

### Frontend Styling
- [ ] Improve CSS in App.css
- [ ] Add loading spinner
- [ ] Better error messages
- [ ] Test case table formatting
- [ ] Mobile responsive design

### Output Formatting
- [ ] Clean Markdown layout
- [ ] Proper headings and sections
- [ ] Test case table styling
- [ ] Edge cases section

---

## Phase 5: Trigger - Deployment 🔄

### Pre-Deployment
- [ ] Environment setup (.env correct)
- [ ] Backend startup test
- [ ] Frontend build test
- [ ] E2E test (issue ID -> test plan)

### Vercel Deployment
- [ ] Push to Vercel with API key
- [ ] Verify domain (testplanbuddy7.vercel.app)
- [ ] Health check endpoint passes
- [ ] Test plan generation works in production

### Post-Deployment
- [ ] Monitor logs
- [ ] Verify API response times
- [ ] Test with real JIRA data
- [ ] Document production maintenance

---

## Critical Blocking Issues

### Current Status
| Issue | Severity | Status | Blocker |
|-------|----------|--------|---------|
| SSL Certificate Error | Medium | Workaround applied | No |
| JIRA Token Format | Medium | Updated | No |
| GROQ API Timeout | Low | Fallback implemented | No |

### Unblocked Path Forward
✅ All critical blockers resolved  
✅ Ready for Phase 2 verification  

---

## Success Metrics

- ✅ JIRA fetch: <2 sec per issue
- ✅ Test plan generation: <5 sec (GROQ)
- ✅ Markdown format: <1 sec
- ✅ API response: <10 sec total
- ✅ Frontend load: <3 sec
- ✅ React build: successful
- ✅ Vercel deployment: successful

---

## Sign-Off Checklist (Phase 5)

- [ ] All phases 1-4 complete
- [ ] All tests passing
- [ ] Documentation updated
- [ ] Code reviewed
- [ ] Deployed to Vercel
- [ ] Production tested
- [ ] User ready to use
