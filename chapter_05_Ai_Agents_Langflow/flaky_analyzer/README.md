# 🔬 Flaky Test Analyzer

Streamlit-free Flask UI for the **003_PW result Flaky analyzer** Langflow workflow.
Upload two Playwright result files (Build 1 vs Build 2) and get AI-powered flaky test classification via Groq.

---

## 📋 Prerequisites

- Python 3.10+
- Langflow installed (`pip install langflow`)
- A Groq API key (for the LLM inside the flow)

---

## 🚀 How to Run Langflow

Open a **separate terminal** and run:

```bash
langflow run --port 7860
```

Then open: **http://localhost:7860**

1. Go to **Settings → API Keys → Add New** and generate an API key
2. Copy that key — you'll paste it into the Flaky Analyzer UI
3. Import the flow file: `flows/003_PW_result_Flaky_analyzer.json`
   - Click **Import** and select the file
4. Verify the **Groq API key** is set inside the flow's Groq component
5. The flow should now be ready to run

---

## 🚀 How to Run the Flaky Analyzer UI

Open a **second terminal** and run:

```bash
cd chapter_05_Ai_Agents_Langflow/flaky_analyzer
python app.py
```

Then open: **http://localhost:8501**

### First-time setup

1. Paste your **Langflow API key** (from Langflow Settings → API Keys) into the UI field
2. The badge should turn green: **API Key: valid**
3. Upload two Playwright result files (Build 1 = baseline, Build 2 = current)
4. Click **Run Analysis**

---

## 📁 Project Structure

```
flaky_analyzer/
├── app.py                   # Flask backend (port 8501)
├── .env                     # Langflow URL + API key (fallback)
├── README.md
├── flows/
│   └── 003_PW_result_Flaky_analyzer.json   # Langflow workflow
├── templates/
│   └── index.html           # Dark-themed Bootstrap UI
├── uploads/                 # Runtime uploads
└── reports/                 # Runtime downloads
```

---

## 🌐 URLs at a Glance

| Service | URL | Port |
|---------|-----|------|
| Langflow UI | http://localhost:7860 | 7860 |
| Flaky Analyzer UI | http://localhost:8501 | 8501 |
| Langflow API | http://localhost:7860/api/v1/run/{flow_id} | 7860 |

---

## 📄 Supported File Types

`.json`, `.xml`, `.txt`, `.log`, `.zip` (max 50 MB each)

---

## 🔑 Environment Variables (`.env`)

| Variable | Default | Description |
|----------|---------|-------------|
| `LANGFLOW_BASE_URL` | `http://localhost:7860` | Langflow server URL |
| `LANGFLOW_API_KEY` | *(empty)* | Fallback API key (optional — set in UI instead) |
