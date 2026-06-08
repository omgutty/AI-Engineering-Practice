# IS-03: Test Plan Generator

## 🎯 Overview

A lightweight React + Python application that automatically generates comprehensive test plans from JIRA issues using AI (GROQ LLM). The system fetches issue details, generates test cases with RICE prioritization, and outputs professional markdown documentation.

## ✨ Features

- **JIRA Integration:** Fetches issue details directly from JIRA API
- **AI-Powered Test Generation:** Uses GROQ LLM to generate intelligent test cases
- **RICE Prioritization:** Scores test cases based on RICE framework
- **Positive & Negative Tests:** Includes both happy-path and error scenarios
- **Professional Output:** Generates markdown test plans ready for use
- **Lightweight UI:** React-based responsive frontend
- **Real-time Preview:** See generated test plans immediately
- **Download Support:** Export test plans as markdown files

## 🏗️ Architecture

### Directory Structure

```
IS-03-TestPlanGenerator/
├── frontend/                 # React UI
│   ├── App.jsx
│   ├── App.css
│   ├── package.json
│   └── index.js
├── backend/                  # Flask API Server
│   └── server.py
├── tools/                    # Python Tools (Layer 3)
│   ├── orchestrator.py       # Main pipeline orchestrator
│   ├── fetch_jira_issue.py   # JIRA fetcher (SOP-001)
│   ├── generate_test_plan.py # Test plan generator (SOP-002)
│   ├── format_markdown.py    # Markdown formatter (SOP-003)
│   └── test_*.py             # Connection tests
├── architecture/             # Architecture SOPs (Layer 1)
│   ├── SOP-001-JIRA-Fetcher.md
│   ├── SOP-002-TestPlan-Generator.md
│   └── SOP-003-Markdown-Formatter.md
├── .tmp/                     # Temporary files (outputs)
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Node.js 16+ (for React development)
- JIRA API Token: https://id.atlassian.com/manage-profile/security/api-tokens
- GROQ API Key: https://console.groq.com/keys (free)

### 1. Setup Backend

```bash
# Create virtual environment
python -m venv venv
source venv/Scripts/activate  # Windows
# or
source venv/bin/activate       # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Configure .env (parent directory)
# GROQ_KEY=your_groq_key
# JIRA_EMAIL=your_email@company.com
# JIRA_API_TOKEN=your_jira_token
# JIRA_URL=https://your-domain.atlassian.net/
```

### 2. Setup Frontend

```bash
cd frontend

# Install dependencies
npm install

# Start development server (proxies to backend:5000)
npm start
```

### 3. Run Backend Server

```bash
cd backend
python server.py
```

The application will be available at `http://localhost:3000`

## 📋 How It Works

### Flow Diagram

```
┌─────────────────┐
│  User Input     │ (JIRA Issue ID: IS-3)
└────────┬────────┘
         │
         ▼
┌─────────────────────────────────┐
│ STAGE 1: Fetch JIRA Issue       │ (SOP-001)
│ - Authenticate with JIRA API    │
│ - Retrieve issue details        │
└────────┬────────────────────────┘
         │
         ▼
┌─────────────────────────────────┐
│ STAGE 2: Generate Test Plan     │ (SOP-002)
│ - Send issue to GROQ LLM        │
│ - Generate test cases           │
│ - Apply RICE prioritization     │
└────────┬────────────────────────┘
         │
         ▼
┌─────────────────────────────────┐
│ STAGE 3: Format Markdown        │ (SOP-003)
│ - Convert JSON to markdown      │
│ - Save to .tmp/                 │
│ - Return to UI                  │
└────────┬────────────────────────┘
         │
         ▼
┌──────────────────────────┐
│ Download or Preview      │
│ Professional Test Plan   │
└──────────────────────────┘
```

## 🔧 API Endpoints

### POST /api/generate-test-plan
Generates a complete test plan from a JIRA issue.

**Request:**
```json
{
  "issue_id": "IS-3",
  "jira_email": "user@company.com",
  "jira_token": "API_TOKEN",
  "jira_url": "https://domain.atlassian.net/",
  "groq_key": "GROQ_API_KEY"
}
```

**Response:**
```json
{
  "status": "success",
  "issue_id": "IS-3",
  "title": "Test Plan: IS-3 - Feature Title",
  "test_case_count": 10,
  "positive_count": 7,
  "negative_count": 3,
  "critical_count": 2,
  "test_objectives": [...],
  "test_cases": [...],
  "acceptance_criteria": [...],
  "markdown": "# Test Plan..."
}
```

### GET /api/health
Health check endpoint.

### GET /api/jira-test
Test JIRA connection.

### GET /api/groq-test
Test GROQ connection.

## 📊 Test Plan Output

Generated markdown files include:

- **Test Objectives:** 2-3 high-level testing goals
- **Scope:** What will and won't be tested
- **Summary Table:** All test cases at a glance
- **Detailed Test Cases:** 
  - Preconditions
  - Step-by-step instructions
  - Expected results
  - RICE prioritization scores
- **Acceptance Criteria:** Pass/fail conditions
- **Test Data:** Sample data for testing

## ⚙️ Configuration

### Environment Variables (.env)

```env
# GROQ Configuration
GROQ_KEY=gsk_xxxxxxxxxxxxx

# JIRA Configuration
JIRA_EMAIL=your-email@company.com
JIRA_API_TOKEN=ATATT3xxxxxxxxxxxxx
JIRA_URL=https://your-domain.atlassian.net/

# Optional: Override port
PORT=8787
```

### Settings in UI

Access settings (⚙️ button) to configure:
- JIRA email and API token
- JIRA base URL
- GROQ API key

Settings are saved to localStorage.

## 🧪 Testing

### Run Python Tools Directly

```bash
cd tools

# Test JIRA connection
python test_jira_connection.py

# Test GROQ connection
python test_groq_connection.py

# Run orchestrator for specific issue
python orchestrator.py IS-3

# Test individual tools
python fetch_jira_issue.py
python generate_test_plan.py
python format_markdown.py
```

### Run React Tests

```bash
cd frontend
npm test
```

## 📚 Project Files

### Architecture Layer (Layer 1 - SOPs)
- **SOP-001:** JIRA Issue Fetcher - Retrieves issue data via API
- **SOP-002:** Test Plan Generator - Uses GROQ to generate test cases
- **SOP-003:** Markdown Formatter - Formats output as markdown

### Tools Layer (Layer 3 - Python Scripts)
- **fetch_jira_issue.py:** JiraFetcher class - handles JIRA API calls
- **generate_test_plan.py:** TestPlanGenerator class - calls GROQ LLM
- **format_markdown.py:** MarkdownFormatter class - creates markdown output
- **orchestrator.py:** Ties all tools together in a pipeline

### Frontend (React)
- **App.jsx:** Main React component with state management
- **App.css:** Responsive styling
- **package.json:** Node dependencies

### Backend (Flask)
- **server.py:** Flask API server with endpoints

## 🔍 Phase Status (B.L.A.S.T. Framework)

✅ **Phase 0:** Initialization Complete
- Created task_plan.md, findings.md, progress.md, gemini.md

✅ **Phase 1:** Blueprint Complete
- Defined data schemas
- Locked in integrations (JIRA + GROQ)
- Established behavioral rules

✅ **Phase 2:** Link Complete
- Verified JIRA API connection
- Documented GROQ connectivity (network constraint noted)
- Fixed SSL certificate issues

✅ **Phase 3:** Architect Complete
- Created 3-layer architecture (SOP + Tools)
- Built Layer 1 (Architecture SOPs)
- Built Layer 3 (Python Tools)

✅ **Phase 4:** Stylize Complete
- Created React UI with responsive design
- Professional styling and user experience
- Settings panel for configuration

⏳ **Phase 5:** Trigger (Deployment)
- Ready for Docker containerization
- Ready for cloud deployment

## 🚦 Deployment

### Local Deployment

```bash
# Backend
cd backend
python server.py

# Frontend (in another terminal)
cd frontend
npm start
```

### Docker Deployment (Optional)

Create `Dockerfile`:
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "backend/server.py"]
```

```bash
docker build -t test-plan-generator .
docker run -p 5000:5000 \
  -e GROQ_KEY=xxx \
  -e JIRA_EMAIL=xxx \
  -e JIRA_API_TOKEN=xxx \
  -e JIRA_URL=xxx \
  test-plan-generator
```

## 📝 Troubleshooting

### Issue: "JIRA Connection Failed"
- Verify JIRA_EMAIL and JIRA_API_TOKEN in .env
- Check JIRA_URL format (should end with /)
- Ensure API token is valid (regenerate if needed)

### Issue: "GROQ Connection Error"
- Verify GROQ_KEY in .env
- Check that groq package is installed: `pip install groq`
- Verify internet connectivity

### Issue: CORS Error in Browser
- Backend Flask server must have CORS enabled (already configured)
- Check that backend is running on port 5000

### Issue: "Module not found"
- Activate virtual environment: `source venv/Scripts/activate`
- Install dependencies: `pip install -r requirements.txt`

## 📖 Documentation

- [SOP-001: JIRA Fetcher](./architecture/SOP-001-JIRA-Fetcher.md)
- [SOP-002: Test Plan Generator](./architecture/SOP-002-TestPlan-Generator.md)
- [SOP-003: Markdown Formatter](./architecture/SOP-003-Markdown-Formatter.md)
- [Task Plan](../task_plan.md)
- [Findings](../findings.md)
- [Progress Log](../progress.md)

## 🤝 Contributing

To add features:
1. Update the relevant SOP in `architecture/`
2. Update the tool in `tools/`
3. Update tests
4. Document changes in `progress.md`

## 📄 License

Internal use only.

## 👤 Author

System Pilot (B.L.A.S.T. Framework)

---

**Last Updated:** June 8, 2026
**Status:** ✅ Phases 0-4 Complete | Ready for Deployment
