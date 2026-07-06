import os
import json
from pathlib import Path
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# ── Config ──
DATA_DIR = Path(__file__).parent.parent / "data"
CHROMA_DIR = Path(__file__).parent / "chroma_db"
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
COLLECTION_NAME = "rag_docs"
GROQ_MODEL = "llama-3.3-70b-versatile"

# Lazy-init globals
embedder = None
splitter = None
chroma_client = None
collection = None
groq_client = None
ingested = False
active_pdf = None
chat_history = []


def _ensure_vector_deps():
    global embedder, splitter, chroma_client, collection
    if embedder is None:
        from fastembed import TextEmbedding
        embedder = TextEmbedding(model_name="nomic-ai/nomic-embed-text-v1.5")
    if splitter is None:
        from langchain_text_splitters import RecursiveCharacterTextSplitter
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP,
            length_function=len, separators=["\n\n", "\n", ". ", " ", ""],
        )
    if chroma_client is None:
        import chromadb
        chroma_client = chromadb.PersistentClient(path=str(CHROMA_DIR))
    if collection is None:
        existing = [c.name for c in chroma_client.list_collections()]
        if COLLECTION_NAME in existing:
            collection = chroma_client.get_collection(COLLECTION_NAME)
        else:
            collection = chroma_client.create_collection(COLLECTION_NAME)


def _ensure_groq():
    global groq_client
    if groq_client is None:
        from groq import Groq
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise RuntimeError("GROQ_API_KEY not set in .env")
        groq_client = Groq(api_key=api_key)


def _read_pdf(path: Path) -> str:
    from pypdf import PdfReader
    reader = PdfReader(path)
    return "\n".join(page.extract_text() or "" for page in reader.pages)


def _get_pdfs() -> list:
    return sorted(DATA_DIR.glob("*.pdf"))


# ── Routes ──

@app.route("/api/status", methods=["GET"])
def status():
    pdfs = _get_pdfs()
    return jsonify({
        "ingested": ingested,
        "active_pdf": active_pdf,
        "pdfs": [p.name for p in pdfs],
        "pdf_exists": len(pdfs) > 0,
    })


@app.route("/api/ingest/<filename>", methods=["POST"])
def ingest_file(filename):
    global ingested, active_pdf
    _ensure_vector_deps()

    pdf_path = DATA_DIR / filename
    if not pdf_path.exists() or pdf_path.suffix.lower() != ".pdf":
        return jsonify({"error": f"PDF '{filename}' not found in data/"}), 404

    text = _read_pdf(pdf_path)
    if not text.strip():
        return jsonify({"error": "PDF content is empty"}), 400

    chunks = splitter.split_text(text)
    if not chunks:
        return jsonify({"error": "No chunks generated"}), 400

    embeddings = list(embedder.embed(chunks))
    embeddings = [e.tolist() for e in embeddings]

    ids = [f"chunk_{i}" for i in range(len(chunks))]
    metadatas = [{"source": filename, "chunk_index": i} for i in range(len(chunks))]

    # Clear old data for this source
    try:
        collection.delete(where={"source": filename})
    except Exception:
        pass

    collection.add(ids=ids, embeddings=embeddings, metadatas=metadatas, documents=chunks)

    ingested = True
    active_pdf = filename
    chat_history.clear()

    return jsonify({
        "message": "PDF ingested successfully",
        "pdf_name": filename,
        "chunks": len(chunks),
        "embedding_dim": len(embeddings[0]) if embeddings else 0,
    })


@app.route("/api/ingest", methods=["POST"])
def ingest():
    pdfs = _get_pdfs()
    if not pdfs:
        return jsonify({"error": "No PDF found in data/"}), 400
    return ingest_file(pdfs[0].name)


@app.route("/api/query", methods=["POST"])
def query():
    _ensure_vector_deps()
    _ensure_groq()

    if not collection:
        return jsonify({"error": "No data ingested. Ingest a document first."}), 400

    data = request.get_json()
    question = (data or {}).get("question", "").strip()
    if not question:
        return jsonify({"error": "Question is required"}), 400

    q_embeddings = list(embedder.embed([question]))
    q_vector = q_embeddings[0].tolist()

    results = collection.query(
        query_embeddings=[q_vector],
        n_results=4,
        include=["documents", "metadatas", "distances"],
    )

    documents = results["documents"][0] if results.get("documents") else []
    distances = results["distances"][0] if results.get("distances") else []
    metadatas = results["metadatas"][0] if results.get("metadatas") else []

    context = "\n\n---\n\n".join(documents)

    system_prompt = (
        "You are a helpful assistant. Answer the user's question based solely on the "
        "provided context. If the context does not contain enough information, say so."
    )
    user_prompt = f"Context:\n{context}\n\nQuestion: {question}\n\nAnswer:"

    response = groq_client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.2,
        max_tokens=1024,
    )

    answer = response.choices[0].message.content.strip()

    retrieved_chunks = [
        {
            "chunk_index": m.get("chunk_index"),
            "content": doc,
            "score": round(1 - d, 4),
        }
        for doc, d, m in zip(documents, distances, metadatas)
    ]

    # Store in chat history
    chat_history.append({"role": "user", "content": question})
    chat_history.append({"role": "assistant", "content": answer})

    return jsonify({
        "question": question,
        "answer": answer,
        "chunks": retrieved_chunks,
        "model": GROQ_MODEL,
        "history": chat_history[-20:],  # last 20 messages
    })


@app.route("/api/chat/history", methods=["GET"])
def get_chat_history():
    return jsonify({"history": chat_history, "active_pdf": active_pdf})


@app.route("/api/chat/clear", methods=["POST"])
def clear_chat():
    chat_history.clear()
    return jsonify({"message": "Chat history cleared"})


if __name__ == "__main__":
    app.run(port=5000, debug=True)
