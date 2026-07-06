# RAG Explorer

An end-to-end **Retrieval-Augmented Generation** pipeline with a chat interface. Upload a PDF, ingest it through the RAG pipeline, and ask questions in natural language.

## Architecture

```
PDF ──► Text Chunking ──► Embedding (Nomic) ──► ChromaDB ──► Groq (LLaMA) ──► Answer
```

| Layer | Technology |
|-------|-----------|
| Backend | Flask (Python) |
| PDF Parsing | pypdf |
| Text Chunking | LangChain RecursiveCharacterTextSplitter (500 tokens, 50 overlap) |
| Embeddings | fastembed (Nomic Embed Text v1.5, 768-dim) |
| Vector DB | ChromaDB (PersistentClient, local storage) |
| LLM | Groq API (Llama 3.3 70B Versatile) |
| Frontend | React 19 + Vite 8 |

## Prerequisites

- **Python 3.10+**
- **Node.js 18+**
- A **Groq API key** ([get one free](https://console.groq.com))

## Setup

### 1. Clone and install backend dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Set your Groq API key

The `.env` file in `backend/` already has the key. If you want to use your own:

```bash
# Edit backend/.env
GROQ_API_KEY=gsk_your_key_here
```

### 3. Install frontend dependencies

```bash
cd frontend
npm install
```

### 4. Add PDFs to the data folder

Place PDF documents in the `data/` folder. The included demo file is:

- `data/Product Requirements Document_ VWO Login Dashboard.pdf`

## Running

Open **two terminals**.

**Terminal 1 — Backend (Flask on port 5000):**

```bash
cd backend
python app.py
```

You should see: `Running on http://127.0.0.1:5000`

**Terminal 2 — Frontend (Vite on port 5173):**

```bash
cd frontend
npm run dev
```

You should see: `Local: http://localhost:5173`

## Usage

1. Open **http://localhost:5173** in your browser
2. In the sidebar, select a PDF from the dropdown
3. Click **Ingest & Index** — this reads, chunks, embeds, and stores the document
4. Once indexed, type questions in the chat input and press Enter
5. The assistant answers using only the content from your document

### Features

- **Document selector** — pick any PDF from `data/` to ingest
- **Chat interface** — ask follow-up questions in a conversation
- **Pipeline visualization** — sidebar shows each RAG stage status
- **Session history** — chat persists across page refreshes

## Project Structure

```
Basic_RAG/
├── backend/
│   ├── app.py              # Flask RAG API
│   ├── requirements.txt    # Python dependencies
│   ├── .env                # Groq API key
│   └── chroma_db/          # Vector store (auto-created)
├── frontend/
│   ├── src/
│   │   ├── App.jsx         # Chat UI
│   │   ├── App.css         # Chat styles
│   │   ├── index.css       # Global styles
│   │   └── main.jsx        # React entry
│   ├── index.html
│   ├── vite.config.js      # Dev proxy to Flask
│   └── package.json
├── data/                   # Place PDFs here
└── README.md
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/status` | List PDFs and ingestion status |
| `POST` | `/api/ingest` | Ingest the first PDF found |
| `POST` | `/api/ingest/<filename>` | Ingest a specific PDF |
| `POST` | `/api/query` | Ask a question (returns answer + chunks) |
| `GET` | `/api/chat/history` | Get chat history |
| `POST` | `/api/chat/clear` | Clear chat history |
