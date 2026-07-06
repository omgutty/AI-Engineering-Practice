import { useState, useEffect, useRef } from "react";
import "./App.css";

const API = window.location.origin;

/* ── Chat Message ── */
function ChatMessage({ msg }) {
  const isUser = msg.role === "user";
  return (
    <div className={`chat-msg ${isUser ? "user" : "assistant"}`}>
      <div className="msg-avatar">{isUser ? "👤" : "🤖"}</div>
      <div className="msg-bubble">
        <div className="msg-role">{isUser ? "You" : "RAG Assistant"}</div>
        <div className="msg-content">{msg.content}</div>
      </div>
    </div>
  );
}

/* ── App ── */
function App() {
  const [status, setStatus] = useState(null);
  const [selectedPdf, setSelectedPdf] = useState("");
  const [ingesting, setIngesting] = useState(false);
  const [ingestResult, setIngestResult] = useState(null);
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const chatEnd = useRef(null);

  useEffect(() => {
    fetch(`${API}/api/status`)
      .then((r) => r.json())
      .then((s) => {
        setStatus(s);
        if (s.active_pdf) setSelectedPdf(s.active_pdf);
        return fetch(`${API}/api/chat/history`);
      })
      .then((r) => r.json())
      .then((h) => {
        if (h.history?.length) setMessages(h.history);
      })
      .catch(() => setStatus({ ingested: false, pdf_exists: false, pdfs: [] }));
  }, []);

  useEffect(() => {
    chatEnd.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const handleIngest = async () => {
    if (!selectedPdf) return;
    setIngesting(true);
    setError(null);
    try {
      const res = await fetch(`${API}/api/ingest/${encodeURIComponent(selectedPdf)}`, { method: "POST" });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error || "Ingestion failed");
      setIngestResult(data);
      setMessages([]);
      setStatus((s) => ({ ...s, ingested: true, active_pdf: selectedPdf }));
    } catch (e) {
      setError(e.message);
    }
    setIngesting(false);
  };

  const handleSend = async () => {
    const q = input.trim();
    if (!q) return;
    setInput("");
    setLoading(true);
    setError(null);

    const userMsg = { role: "user", content: q };
    setMessages((prev) => [...prev, userMsg]);

    try {
      const res = await fetch(`${API}/api/query`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question: q }),
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error || "Query failed");
      setMessages(data.history || [...messages, userMsg, { role: "assistant", content: data.answer }]);
    } catch (e) {
      setError(e.message);
      setMessages((prev) => prev.slice(0, -1));
    }
    setLoading(false);
  };

  const handleClear = async () => {
    await fetch(`${API}/api/chat/clear`, { method: "POST" });
    setMessages([]);
  };

  const pipelineActive = status?.ingested || !!ingestResult;

  return (
    <div className="app">
      {/* ── Sidebar ── */}
      <aside className="sidebar">
        <div className="sidebar-header">
          <h2>📚 RAG Explorer</h2>
          <p className="sidebar-sub">Retrieval-Augmented Generation</p>
        </div>

        {/* Pipeline Status */}
        <div className="pipeline-status">
          <h3>Pipeline</h3>
          <div className="pipeline-step">
            <span className={`dot ${status?.pdf_exists ? "done" : ""}`} />
            <span>PDF Loaded: {status?.active_pdf || "None"}</span>
          </div>
          <div className="pipeline-step">
            <span className={`dot ${pipelineActive ? "done" : ""}`} />
            <span>Text Chunking (500 tok)</span>
          </div>
          <div className="pipeline-step">
            <span className={`dot ${pipelineActive ? "done" : ""}`} />
            <span>Embedding (768-dim)</span>
          </div>
          <div className="pipeline-step">
            <span className={`dot ${pipelineActive ? "done" : ""}`} />
            <span>ChromaDB Indexed</span>
          </div>
          <div className="pipeline-step">
            <span className={`dot ${pipelineActive ? "done" : ""}`} />
            <span>Groq LLM Ready</span>
          </div>
        </div>

        {/* Document Selector */}
        <div className="doc-selector">
          <h3>Select Document</h3>
          {status?.pdfs?.length > 0 ? (
            <select
              value={selectedPdf}
              onChange={(e) => setSelectedPdf(e.target.value)}
              className="doc-select"
            >
              <option value="">— Choose a PDF —</option>
              {status.pdfs.map((name) => (
                <option key={name} value={name}>{name}</option>
              ))}
            </select>
          ) : (
            <p className="hint">Place PDFs in <code>data/</code></p>
          )}
          <button
            className="btn btn-ingest"
            onClick={handleIngest}
            disabled={ingesting || !selectedPdf}
          >
            {ingesting ? "⏳ Ingesting…" : "📥 Ingest & Index"}
          </button>
          {ingestResult && (
            <div className="ingest-info">
              <p>✅ {ingestResult.chunks} chunks</p>
              <p className="dim">{ingestResult.embedding_dim} dim vectors</p>
            </div>
          )}
        </div>

        {/* Controls */}
        <div className="sidebar-controls">
          {messages.length > 0 && (
            <button className="btn btn-clear" onClick={handleClear}>
              🗑️ Clear Chat
            </button>
          )}
        </div>

        <div className="sidebar-footer">
          <span>Nomic Embed</span>
          <span>·</span>
          <span>ChromaDB</span>
          <span>·</span>
          <span>Groq</span>
        </div>
      </aside>

      {/* ── Main Chat Area ── */}
      <main className="main">
        {/* Header */}
        <header className="chat-header">
          <h1>Chat with {status?.active_pdf || "your document"}</h1>
          {status?.active_pdf && (
            <span className="active-doc">📄 {status.active_pdf}</span>
          )}
        </header>

        {/* Messages */}
        <div className="chat-area">
          {messages.length === 0 && !pipelineActive && (
            <div className="welcome">
              <div className="welcome-icon">🔍</div>
              <h2>Welcome to RAG Explorer</h2>
              <p>Select a PDF document from the sidebar and click <strong>Ingest & Index</strong> to get started.</p>
              <p className="hint">The pipeline processes your document through chunking → embedding → vector storage → LLM-powered answers.</p>
            </div>
          )}
          {messages.length === 0 && pipelineActive && (
            <div className="welcome">
              <div className="welcome-icon">💬</div>
              <h2>Ready to chat!</h2>
              <p>Ask questions about <strong>{status?.active_pdf}</strong> below.</p>
            </div>
          )}
          {messages.map((msg, i) => (
            <ChatMessage key={i} msg={msg} />
          ))}

          {/* Loading indicator */}
          {loading && (
            <div className="chat-msg assistant">
              <div className="msg-avatar">🤖</div>
              <div className="msg-bubble thinking">
                <div className="typing-indicator">
                  <span></span><span></span><span></span>
                </div>
              </div>
            </div>
          )}

          <div ref={chatEnd} />
        </div>

        {/* Error banner */}
        {error && <div className="error-banner">{error}</div>}

        {/* Input */}
        <div className="chat-input-bar">
          <input
            type="text"
            className="chat-input"
            placeholder={pipelineActive ? "Ask a question about the document…" : "Ingest a document first…"}
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && handleSend()}
            disabled={!pipelineActive || loading}
          />
          <button
            className="btn btn-send"
            onClick={handleSend}
            disabled={!pipelineActive || loading || !input.trim()}
          >
            {loading ? "⏳" : "→"}
          </button>
        </div>
      </main>
    </div>
  );
}

export default App;
