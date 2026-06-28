"""
Flaky Test Analyzer — Flask frontend for Langflow
==================================================
Upload Playwright test results and analyze flaky tests
via the 003_PW_result_Flaky_analyzer Langflow workflow.
"""

import json
import os
import re
import zipfile
import io
from datetime import datetime
from pathlib import Path

import requests
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify, send_file

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
load_dotenv()

LANGFLOW_BASE_URL = os.getenv("LANGFLOW_BASE_URL", "http://localhost:7860").rstrip("/")
LANGFLOW_API_KEY = os.getenv("LANGFLOW_API_KEY", "")

FLOW_FILE = Path(__file__).parent / "flows" / "003_PW_result_Flaky_analyzer.json"
UPLOAD_DIR = Path(__file__).parent / "uploads"
REPORT_DIR = Path(__file__).parent / "reports"
UPLOAD_DIR.mkdir(exist_ok=True)
REPORT_DIR.mkdir(exist_ok=True)

MAX_FILE_SIZE = 50 * 1024 * 1024  # 50 MB
ALLOWED_EXT = {".json", ".xml", ".txt", ".log", ".zip"}

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = MAX_FILE_SIZE


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load_flow_id():
    if not FLOW_FILE.exists():
        return None
    with open(FLOW_FILE, encoding="utf-8") as f:
        data = json.load(f)
    return data.get("id")


FLOW_ID = load_flow_id()


def allowed_file(filename):
    return Path(filename).suffix.lower() in ALLOWED_EXT


def read_file_content(uploaded_file):
    """Read text content from an uploaded file (or zip archive)."""
    ext = Path(uploaded_file.filename).suffix.lower()
    raw = uploaded_file.read()

    if ext == ".zip":
        return _read_zip(raw)

    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError:
        return raw.decode("latin-1")


def _read_zip(raw):
    parts = []
    with zipfile.ZipFile(io.BytesIO(raw)) as zf:
        for name in zf.namelist():
            ext = Path(name).suffix.lower()
            if ext in {".json", ".xml", ".txt", ".log"}:
                try:
                    parts.append(f"--- {name} ---\n{zf.read(name).decode('utf-8')}")
                except UnicodeDecodeError:
                    parts.append(f"--- {name} ---\n{zf.read(name).decode('latin-1')}")
    return "\n\n".join(parts) if parts else "(empty archive)"


def run_langflow(file1_content, file2_content, context="", api_key=""):
    """Execute the Langflow flow via REST API."""
    if not FLOW_ID:
        raise RuntimeError("Flow ID not found. Check that the flow file exists.")

    key = api_key or LANGFLOW_API_KEY
    headers = {"Content-Type": "application/json"}
    if key:
        headers["x-api-key"] = key

    combined_file1 = f"{context.strip()}\n\n{file1_content}" if context.strip() else file1_content

    payload = {
        "input_value": "Analyze these Playwright test results for flaky tests.",
        "input_type": "chat",
        "output_type": "chat",
        "tweaks": {
            "Prompt Template-euQuy": {
                "file1": combined_file1,
                "file2": file2_content,
            }
        },
    }

    url = f"{LANGFLOW_BASE_URL}/api/v1/run/{FLOW_ID}"
    resp = requests.post(url, json=payload, headers=headers, timeout=300)
    resp.raise_for_status()
    return resp.json()


def parse_response(response):
    """Extract analysis text from Langflow API response."""
    try:
        outputs = response["outputs"][0]["outputs"]
        for out in outputs:
            results = out.get("results", {})
            msg = results.get("message", {})
            text = msg.get("text", "") or msg.get("data", {}).get("text", "")
            if text:
                return text

        # Fallback
        for out in outputs:
            for key in ("results", "artifacts"):
                val = out.get(key, {})
                if isinstance(val, dict):
                    for v in val.values():
                        if isinstance(v, dict) and v.get("text"):
                            return v["text"]
    except (KeyError, IndexError, TypeError) as e:
        raise RuntimeError(f"Could not parse Langflow response: {e}") from e

    raise RuntimeError("No analysis text found in response.")


def structure_results(raw_text):
    sections = {}
    headers = [
        "REGRESSION_CANDIDATES", "CONSISTENT_FAILURES", "FLAKY_TESTS",
        "FIXED_TESTS", "PERFORMANCE_REGRESSIONS", "RERUN_RECOMMENDATION", "SUITE_HEALTH",
    ]
    for i, h in enumerate(headers):
        nxt = headers[i + 1] if i + 1 < len(headers) else None
        pattern = rf"^{re.escape(h)}\s*\n(.+?)(?=^{re.escape(nxt)}\s*\n|\Z)" if nxt else \
                 rf"^{re.escape(h)}\s*\n(.+)"
        m = re.search(pattern, raw_text, re.MULTILINE | re.DOTALL)
        sections[h.lower()] = m.group(1).strip() if m else "(No data)"
    sections["raw"] = raw_text
    return sections


def count_items(text):
    return sum(1 for line in text.split("\n") if line.strip() and not line.startswith("   "))


def generate_report(sections, files_info, fmt="json"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {
        "analysis_timestamp": timestamp,
        "build_1": files_info.get("build_1", ""),
        "build_2": files_info.get("build_2", ""),
        "summary": {
            "flaky_tests": count_items(sections.get("flaky_tests", "")),
            "regressions": count_items(sections.get("regression_candidates", "")),
            "consistent_failures": count_items(sections.get("consistent_failures", "")),
            "fixed_tests": count_items(sections.get("fixed_tests", "")),
        },
        **{k: v for k, v in sections.items() if k != "raw"},
    }

    if fmt == "json":
        return json.dumps(data, indent=2, ensure_ascii=False)

    md = f"""# Flaky Test Analysis Report

**Generated:** {timestamp}
**Build 1:** {files_info.get("build_1", "N/A")}
**Build 2:** {files_info.get("build_2", "N/A")}

---

## Suite Health

{data.get("suite_health", "N/A")}

---

## Regression Candidates

{data.get("regression_candidates", "N/A")}

---

## Consistent Failures

{data.get("consistent_failures", "N/A")}

---

## Flaky Tests

{data.get("flaky_tests", "N/A")}

---

## Fixed Tests

{data.get("fixed_tests", "N/A")}

---

## Performance Regressions

{data.get("performance_regressions", "N/A")}

---

## Rerun Recommendation

{data.get("rerun_recommendation", "N/A")}

---
*Generated by Flaky Test Analyzer*
"""
    return md


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.route("/")
def index():
    return render_template("index.html", flow_ok=FLOW_ID is not None)


@app.route("/api/status")
def api_status():
    """Check Langflow reachability and API key validity."""
    api_key = request.args.get("api_key", LANGFLOW_API_KEY)
    headers = {}
    if api_key:
        headers["x-api-key"] = api_key

    langflow_ok = False
    api_key_valid = False

    try:
        r = requests.get(f"{LANGFLOW_BASE_URL}/health", headers=headers, timeout=5)
        langflow_ok = r.status_code == 200
    except requests.ConnectionError:
        return jsonify({
            "langflow": "unreachable",
            "api_key": "unknown",
            "message": f"Cannot connect to {LANGFLOW_BASE_URL}",
        }), 200

    if langflow_ok and api_key:
        try:
            r2 = requests.get(
                f"{LANGFLOW_BASE_URL}/api/v1/store/api_key/validate",
                headers=headers, timeout=5,
            )
            api_key_valid = r2.status_code == 200
        except requests.RequestException:
            # Fallback: try a simple flow list endpoint
            try:
                r2 = requests.get(
                    f"{LANGFLOW_BASE_URL}/api/v1/flows/",
                    headers=headers, timeout=5,
                )
                api_key_valid = r2.status_code != 403
            except requests.RequestException:
                api_key_valid = False

    return jsonify({
        "langflow": "ok" if langflow_ok else "error",
        "api_key": "valid" if api_key_valid else ("invalid" if api_key else "not_provided"),
        "message": "",
    })


@app.route("/api/analyze", methods=["POST"])
def analyze():
    # Validate files
    if "file1" not in request.files or "file2" not in request.files:
        return jsonify({"error": "Both Build 1 and Build 2 files are required."}), 400

    file1 = request.files["file1"]
    file2 = request.files["file2"]

    if not file1.filename or not file2.filename:
        return jsonify({"error": "Both files must have a filename."}), 400

    for f, label in [(file1, "Build 1"), (file2, "Build 2")]:
        if not allowed_file(f.filename):
            return jsonify({"error": f"{label}: Unsupported file type '{Path(f.filename).suffix}'. Allowed: {', '.join(sorted(ALLOWED_EXT))}"}), 400
        if len(f.read()) > MAX_FILE_SIZE:
            return jsonify({"error": f"{label}: File exceeds 50 MB limit."}), 400
        f.seek(0)

    context = request.form.get("context", "")
    api_key = request.form.get("api_key", "") or LANGFLOW_API_KEY

    try:
        # Read content
        content1 = read_file_content(file1)
        content2 = read_file_content(file2)

        if not content1.strip():
            return jsonify({"error": "Build 1 file is empty."}), 400
        if not content2.strip():
            return jsonify({"error": "Build 2 file is empty."}), 400

        # Check Langflow connection
        hdrs = {}
        if api_key:
            hdrs["x-api-key"] = api_key
        try:
            hr = requests.get(f"{LANGFLOW_BASE_URL}/health", headers=hdrs, timeout=5)
            if hr.status_code != 200:
                return jsonify({"error": "Langflow health check failed."}), 503
        except requests.ConnectionError:
            return jsonify({"error": f"Cannot connect to Langflow at {LANGFLOW_BASE_URL}. Is it running?"}), 503

        # Run flow
        response = run_langflow(content1, content2, context, api_key)

        # Parse
        raw_text = parse_response(response)
        sections = structure_results(raw_text)

        # Build report
        files_info = {"build_1": file1.filename, "build_2": file2.filename}
        json_report = generate_report(sections, files_info, "json")
        md_report = generate_report(sections, files_info, "md")

        return jsonify({
            "success": True,
            "sections": {
                "regression_candidates": sections.get("regression_candidates", ""),
                "consistent_failures": sections.get("consistent_failures", ""),
                "flaky_tests": sections.get("flaky_tests", ""),
                "fixed_tests": sections.get("fixed_tests", ""),
                "performance_regressions": sections.get("performance_regressions", ""),
                "rerun_recommendation": sections.get("rerun_recommendation", ""),
                "suite_health": sections.get("suite_health", ""),
            },
            "summary": {
                "flaky_tests": count_items(sections.get("flaky_tests", "")),
                "regressions": count_items(sections.get("regression_candidates", "")),
                "consistent_failures": count_items(sections.get("consistent_failures", "")),
                "fixed_tests": count_items(sections.get("fixed_tests", "")),
            },
            "raw": sections.get("raw", ""),
            "reports": {
                "json": json_report,
                "markdown": md_report,
            },
        })

    except requests.Timeout:
        return jsonify({"error": "Langflow request timed out. Try smaller files."}), 504
    except requests.HTTPError as e:
        return jsonify({"error": f"Langflow API error: {e.response.status_code} — {e.response.text[:500]}"}), 502
    except RuntimeError as e:
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {e}"}), 500


@app.route("/api/download/<fmt>", methods=["POST"])
def download(fmt):
    if fmt not in ("json", "md", "markdown"):
        return jsonify({"error": "Invalid format. Use 'json' or 'md'."}), 400

    data = request.get_json()
    content = data.get("content", "")
    ext = "md" if fmt in ("md", "markdown") else "json"
    fname = f"flaky_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.{ext}"
    mime = "text/markdown" if ext == "md" else "application/json"

    buf = io.BytesIO(content.encode("utf-8"))
    return send_file(buf, mimetype=mime, as_attachment=True, download_name=fname)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print(f"🔬 Flaky Test Analyzer")
    print(f"   Flow ID: {FLOW_ID or 'NOT FOUND'}")
    print(f"   Langflow: {LANGFLOW_BASE_URL}")
    print(f"   Start:    http://localhost:8501")
    app.run(host="0.0.0.0", port=8501, debug=True)
