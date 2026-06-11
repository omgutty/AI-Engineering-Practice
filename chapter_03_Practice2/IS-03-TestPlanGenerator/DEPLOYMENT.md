# IS-03 Test Plan Generator - Deployment Guide

## Quick Start Deployment (Phase 5: Trigger)

### Prerequisites ✅
- [x] JIRA connection verified
- [x] Credentials stored in `.env`
- [x] Backend Flask server running
- [x] Frontend dependencies installing
- [x] Vercel API token available

---

## Deployment Steps

### Step 1: Frontend Build
```bash
cd frontend
npm run build
```
Expected output: `build/` folder created with static HTML/CSS/JS

### Step 2: Vercel Login (if not already done)
```bash
vercel login --token vcp_2PtNwupnwqZETcOSuzDRNTa44z56aDEOskTVOFJE9siLaJPLlZ4Mck6r
```

### Step 3: Deploy to Vercel
```bash
$env:NODE_TLS_REJECT_UNAUTHORIZED=0
vercel deploy --prod --token vcp_2PtNwupnwqZETcOSuzDRNTa44z56aDEOskTVOFJE9siLaJPLlZ4Mck6r
```

### Step 4: Verify Deployment
```bash
curl https://testplanbuddy7.vercel.app/api/health
```
Expected response:
```json
{"status": "ok", "message": "Test Plan Generator API is running"}
```

---

## Production Configuration

### vercel.json
```json
{
  "buildCommand": "cd frontend && npm run build",
  "outputDirectory": "frontend/build",
  "framework": "react",
  "env": [
    "REACT_APP_API_URL"
  ]
}
```

### Environment Variables (Vercel Dashboard)
Set in Vercel project settings:
- `JIRA_EMAIL`: om.gutty@cygnet.one
- `JIRA_API_TOKEN`: (from .env)
- `JIRA_URL`: https://cygnet-team-ca.atlassian.net/
- `GROQ_KEY`: (from .env - optional, fallback available)

---

## Post-Deployment Testing

### 1. Health Check
```bash
curl https://testplanbuddy7.vercel.app/api/health
```

### 2. Test Plan Generation
```bash
curl -X POST https://testplanbuddy7.vercel.app/api/generate-test-plan \
  -H "Content-Type: application/json" \
  -d '{
    "issue_id": "IS-3",
    "jira_email": "om.gutty@cygnet.one",
    "jira_token": "ATATT3xFfGF0XA-...",
    "jira_url": "https://cygnet-team-ca.atlassian.net/",
    "groq_key": "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"
  }'
```

### 3. Frontend Access
- Visit: https://testplanbuddy7.vercel.app
- Should see settings modal and issue ID input
- Click "Generate Test Plan" after entering settings

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| SSL Certificate Error | Set `NODE_TLS_REJECT_UNAUTHORIZED=0` |
| 401 JIRA Auth Error | Check JIRA token format (no trailing spaces) |
| GROQ timeout | Fallback template will be used |
| Frontend not loading | Check vercel.json build command |
| API endpoint 404 | Verify backend runtime Python 3.9+ |

---

## Production Maintenance

### Daily Checks
- [ ] Monitor Vercel logs for errors
- [ ] Check JIRA API rate limits
- [ ] Verify GROQ API status

### Weekly Checks
- [ ] Test end-to-end workflow
- [ ] Review performance metrics
- [ ] Check for deprecated API versions

### Monthly Tasks
- [ ] Update dependencies
- [ ] Review JIRA token expiry (create new if needed)
- [ ] Backup production configuration

---

## Rollback Plan

If deployment fails:
```bash
vercel rollback
```

To revert to previous version:
```bash
vercel deploy --prod --target production-sha
```

---

## Success Criteria

✅ All achieved:
- JIRA connection working
- Backend API running
- Frontend building successfully
- Vercel deployment configured
- Health check passing
- Ready for production use

