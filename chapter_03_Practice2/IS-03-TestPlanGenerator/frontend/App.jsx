import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [settings, setSettings] = useState({
    jiraEmail: 'automationrun7@gmail.com',
    jiraToken: '',
    jiraUrl: 'https://automationrun.atlassian.net/',
    groqKey: '',
    showSettings: false,
  });

  const [issueId, setIssueId] = useState('IS-3');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState('');

  const handleSettingsChange = (e) => {
    const { name, value } = e.target;
    setSettings(prev => ({ ...prev, [name]: value }));
  };

  const toggleSettings = () => {
    setSettings(prev => ({ ...prev, showSettings: !prev.showSettings }));
  };

  const saveSettings = () => {
    // In a real app, save to localStorage or backend
    localStorage.setItem('testPlanSettings', JSON.stringify(settings));
    setSettings(prev => ({ ...prev, showSettings: false }));
    setError('');
  };

  const handleGenerateTestPlan = async () => {
    if (!issueId.trim()) {
      setError('Please enter a JIRA issue ID');
      return;
    }

    setLoading(true);
    setError('');
    setResult(null);

    try {
      // Call backend API
      const response = await axios.post('/api/generate-test-plan', {
        issue_id: issueId,
        jira_email: settings.jiraEmail,
        jira_token: settings.jiraToken,
        jira_url: settings.jiraUrl,
        groq_key: settings.groqKey,
      });

      setResult(response.data);
    } catch (err) {
      setError(err.response?.data?.error || 'Failed to generate test plan');
    } finally {
      setLoading(false);
    }
  };

  const downloadMarkdown = () => {
    if (result?.markdown) {
      const element = document.createElement('a');
      const file = new Blob([result.markdown], { type: 'text/markdown' });
      element.href = URL.createObjectURL(file);
      element.download = `${issueId}_TestPlan.md`;
      document.body.appendChild(element);
      element.click();
      document.body.removeChild(element);
    }
  };

  return (
    <div className="app">
      {/* Header */}
      <header className="header">
        <div className="header-content">
          <h1>🧪 Test Plan Generator</h1>
          <p>Automatically generate comprehensive test plans from JIRA issues using AI</p>
        </div>
        <button className="settings-btn" onClick={toggleSettings}>
          ⚙️ Settings
        </button>
      </header>

      {/* Settings Panel */}
      {settings.showSettings && (
        <div className="settings-panel">
          <h2>Configuration</h2>
          
          <div className="setting-group">
            <label>JIRA Email</label>
            <input
              type="email"
              name="jiraEmail"
              value={settings.jiraEmail}
              onChange={handleSettingsChange}
              placeholder="your-email@company.com"
            />
          </div>

          <div className="setting-group">
            <label>JIRA API Token</label>
            <input
              type="password"
              name="jiraToken"
              value={settings.jiraToken}
              onChange={handleSettingsChange}
              placeholder="Enter your JIRA API token"
            />
          </div>

          <div className="setting-group">
            <label>JIRA Base URL</label>
            <input
              type="url"
              name="jiraUrl"
              value={settings.jiraUrl}
              onChange={handleSettingsChange}
              placeholder="https://your-domain.atlassian.net/"
            />
          </div>

          <div className="setting-group">
            <label>GROQ API Key</label>
            <input
              type="password"
              name="groqKey"
              value={settings.groqKey}
              onChange={handleSettingsChange}
              placeholder="Enter your GROQ API key (free from groq.com)"
            />
          </div>

          <div className="settings-actions">
            <button className="btn btn-primary" onClick={saveSettings}>
              Save Settings
            </button>
            <button className="btn btn-secondary" onClick={toggleSettings}>
              Cancel
            </button>
          </div>
        </div>
      )}

      {/* Main Content */}
      <main className="main-content">
        <div className="form-section">
          <h2>Generate Test Plan</h2>
          
          <div className="input-group">
            <label htmlFor="issueId">JIRA Issue ID</label>
            <div className="input-wrapper">
              <input
                id="issueId"
                type="text"
                value={issueId}
                onChange={(e) => setIssueId(e.target.value)}
                placeholder="e.g., IS-123"
                disabled={loading}
              />
              <button
                className="btn btn-primary"
                onClick={handleGenerateTestPlan}
                disabled={loading}
              >
                {loading ? '⏳ Generating...' : '🚀 Generate Test Plan'}
              </button>
            </div>
          </div>

          {error && <div className="error-message">❌ {error}</div>}
        </div>

        {/* Results Section */}
        {result && (
          <div className="results-section">
            <div className="result-header">
              <h2>📋 Test Plan: {result.issue_id}</h2>
              <button className="btn btn-success" onClick={downloadMarkdown}>
                ⬇️ Download Markdown
              </button>
            </div>

            {/* Summary Cards */}
            <div className="summary-cards">
              <div className="card">
                <h3>Total Test Cases</h3>
                <p className="large-number">{result.test_case_count || 0}</p>
              </div>
              <div className="card">
                <h3>Positive Tests</h3>
                <p className="positive-count">{result.positive_count || 0}</p>
              </div>
              <div className="card">
                <h3>Negative Tests</h3>
                <p className="negative-count">{result.negative_count || 0}</p>
              </div>
              <div className="card">
                <h3>Critical Tests (P0)</h3>
                <p className="critical-count">{result.critical_count || 0}</p>
              </div>
            </div>

            {/* Test Objectives */}
            <div className="test-objectives">
              <h3>🎯 Test Objectives</h3>
              <ul>
                {result.test_objectives?.map((obj, idx) => (
                  <li key={idx}>{obj}</li>
                ))}
              </ul>
            </div>

            {/* Test Cases Table */}
            <div className="test-cases-table">
              <h3>📝 Test Cases</h3>
              <div className="table-wrapper">
                <table>
                  <thead>
                    <tr>
                      <th>ID</th>
                      <th>Title</th>
                      <th>Type</th>
                      <th>Priority</th>
                      <th>RICE Score</th>
                    </tr>
                  </thead>
                  <tbody>
                    {result.test_cases?.map((tc, idx) => (
                      <tr key={idx}>
                        <td><strong>{tc.id}</strong></td>
                        <td>{tc.title}</td>
                        <td>
                          <span className={`badge ${tc.type}`}>
                            {tc.type === 'positive' ? '✅ Positive' : '❌ Negative'}
                          </span>
                        </td>
                        <td>
                          <span className={`priority ${tc.priority}`}>
                            {tc.priority}
                          </span>
                        </td>
                        <td><strong>{tc.rice_score}</strong></td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>

            {/* Acceptance Criteria */}
            <div className="acceptance-criteria">
              <h3>✓ Acceptance Criteria</h3>
              <ul>
                {result.acceptance_criteria?.map((criterion, idx) => (
                  <li key={idx}>{criterion}</li>
                ))}
              </ul>
            </div>
          </div>
        )}

        {/* Info Panel */}
        {!result && (
          <div className="info-panel">
            <h3>ℹ️ How It Works</h3>
            <ol>
              <li>Enter a JIRA issue ID (e.g., IS-123)</li>
              <li>The system fetches issue details from JIRA</li>
              <li>AI (GROQ) generates comprehensive test cases</li>
              <li>Test plan is formatted as professional markdown</li>
              <li>Download and use immediately</li>
            </ol>
          </div>
        )}
      </main>

      {/* Footer */}
      <footer className="footer">
        <p>🚀 Powered by JIRA API + GROQ LLM | Test Plan Generator v1.0</p>
      </footer>
    </div>
  );
}

export default App;
