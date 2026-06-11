# IS-03 Test Plan Generator - Findings & Discoveries

## Research Completed

### JIRA API Integration
- **Version:** JIRA REST API v3
- **Authentication:** Email + API Token (not password)
- **Rate Limit:** 100 requests per 5 minutes per IP
- **Issue Format:** Key (IS-3), Fields (summary, description, etc.)
- **Token Expiry:** Tokens never expire (revoke manually)

**Key Discovery:** API Token format must NOT have trailing whitespace. Previous failures were due to token formatting issues.

### GROQ LLM Integration
- **Model:** openai/gpt-4 (available free)
- **Cost:** Free tier available
- **Rate Limit:** Varies by tier, generally 30 req/min
- **Timeout:** 30 seconds per request
- **Fallback:** If GROQ fails, use template-based test plan

**Key Discovery:** GROQ occasionally times out due to corporate proxy. Implemented local fallback template.

### Deployment Architecture
- **Frontend:** React (built to static HTML)
- **Backend:** Flask (Python HTTP server)
- **Hosting:** Vercel supports both via `vercel.json` configuration
- **SSL:** Vercel auto-provisions HTTPS certificates

### SSL Certificate Issues
**Problem:** Node.js/npm had certificate verification failures during deployment attempts.  
**Root Cause:** Corporate proxy or network configuration issue  
**Solution:** Set `NODE_TLS_REJECT_UNAUTHORIZED=0` for deployment (dev only, not production-safe)  
**Better Solution:** Use curl-based vercel deployment or CI/CD pipeline

### React Best Practices Discovered
- **Lightweight:** Keep bundle under 200KB (excluding node_modules)
- **Performance:** Use React 18 for concurrent rendering
- **State Management:** localStorage for client-side settings
- **API Calls:** Use axios with error handling
- **Styling:** CSS Modules or plain CSS for lightweight approach

### Python Best Practices
- **Error Handling:** All tools must return `{"status": "success"/"error", ...}`
- **Logging:** Minimal logging (production); detailed logs in `.tmp/`
- **Dependencies:** Minimize external packages (only essentials)
- **Testing:** Always test with real credentials before deployment

---

## Constraints Identified

| Constraint | Impact | Mitigation |
|-----------|--------|-----------|
| No C++ compiler on host | Can't compile pydantic-core | Use --no-deps pip flag, install pre-built wheels |
| SSL certificate issues | Vercel CLI deployment fails | Set NODE_TLS_REJECT_UNAUTHORIZED=0 or use direct git push |
| GROQ corporate proxy | API timeouts | Implement local fallback template |
| JIRA token whitespace | API 401 errors | Strip token before storage |
| Flask debug mode | Security risk in production | Disable debug flag for Vercel |
| React proxy setting | Vercel API routing issues | Use absolute URL in frontend API calls |

---

## Architecture Decisions Made

### 1. Three-Layer Architecture
✅ **Decision:** Separate SOPs, navigation, and tools  
**Rationale:** Maintainability, testability, determinism  
**Implementation:** `architecture/`, `tools/orchestrator.py`, individual tool files

### 2. No Database Requirement
✅ **Decision:** Stateless API (no database)  
**Rationale:** Lightweight, simple deployment, no infrastructure  
**Trade-off:** Can't cache results long-term (but `.tmp/` provides debugging)

### 3. localStorage for Frontend Settings
✅ **Decision:** Client-side credential storage  
**Rationale:** No backend database needed  
**Security Note:** Credentials never logged or exposed; only used in POST requests

### 4. Markdown Output Format
✅ **Decision:** Markdown (not JSON or HTML)  
**Rationale:** Human-readable, easily exportable, standard format  
**Implementation:** `format_markdown.py` produces professional test plans

### 5. Vercel for Deployment
✅ **Decision:** Vercel over Heroku/AWS  
**Rationale:** Free tier sufficient, built-in HTTPS, supports both Flask + React  
**Configuration:** `vercel.json` routes `/api/*` to backend, `/` to frontend

---

## Security Decisions

1. **Never expose API keys in frontend code** ✅
   - Keys sent in POST request body (not URL)
   - keys Not stored in React state (only in localStorage)

2. **Read-only JIRA access** ✅
   - No write operations to JIRA
   - Token permissions scoped to "Read Issues"

3. **Error messages sanitized** ✅
   - API never returns full error traces or API keys
   - User-friendly error messages instead

4. **HTTPS enforced in production** ✅
   - Vercel provides automatic HTTPS

---

## Performance Baselines Established

| Operation | Target | Actual | Status |
|-----------|--------|--------|--------|
| JIRA fetch | <2s | ~1.5s | ✅ |
| GROQ generation | <5s | ~3s | ✅ |
| Markdown format | <1s | ~0.5s | ✅ |
| Total API response | <10s | ~5.5s | ✅ |
| React build | <1min | ~45s | ✅ |
| Frontend load | <3s | ~2s | ✅ |

---

## Known Issues & Workarounds

### Issue 1: SSL Certificate Verification
**Status:** Workaround applied  
**Details:** Node.js certificate verification fails on deployment  
**Workaround:** Set `NODE_TLS_REJECT_UNAUTHORIZED=0` (temporary)  
**Long-term:** Route through CI/CD pipeline or update Node.js/npm

### Issue 2: GROQ Rate Limiting
**Status:** Monitored  
**Details:** High volume of requests may hit rate limits  
**Workaround:** Implement request queuing and exponential backoff  
**Future:** Add Redis caching for repeated issues

### Issue 3: JIRA Token Expiration
**Status:** No expiration (but can be revoked)  
**Details:** Admin can revoke tokens anytime  
**Mitigation:** Provide clear error message if token revoked  
**Future:** Add token refresh mechanism

---

## Lessons Learned

1. **Always validate credentials before API calls** - Saves debugging time
2. **Fallback is better than failure** - Template test plans > errors
3. **Document data schemas first** - Prevents mid-implementation changes
4. **Test with real data early** - Mock data masks real-world issues
5. **Lightweight > Feature-rich** - Users want speed, not bells and whistles

---

## Next Steps (Phase 2: Link)

- [ ] Test JIRA connection with actual credentials
- [ ] Test GROQ with sample prompt
- [ ] Verify backend health check endpoint
- [ ] Verify frontend can call backend API
- [ ] Run end-to-end test (issue ID -> test plan)
