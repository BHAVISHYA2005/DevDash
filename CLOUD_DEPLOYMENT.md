# Portia Oncall Agent — Cloud Deployment Guide

This guide helps you deploy your backend API and dashboard to the cloud for a public demo link.

---

## 1. Deploy Flask Backend (API)

### Recommended: Render (Free, Easy)
- Go to https://render.com and sign up.
- Click "New Web Service" and connect your GitHub repo.
- Set the build command to:
  ```
  pip install -r requirements.txt
  ```
- Set the start command to:
  ```
  python approval_api.py
  ```
- Add environment variables as needed (e.g., Slack token, etc).
- After deploy, note your public API URL (e.g., `https://your-app.onrender.com`).

### Alternatives:
- [Railway](https://railway.app) — similar steps.
- [Heroku](https://heroku.com) — use a `Procfile` with `web: python approval_api.py`.

---

## 2. Host Dashboard (Frontend)

### Recommended: Vercel or Netlify
- Go to https://vercel.com or https://netlify.com and sign up.
- Drag and drop your `index.html`, `approval_dashboard_modern.html`, and any assets.
- Deploy the site and get your public dashboard URL.

### GitHub Pages (for static HTML)
- Push your HTML files to a `gh-pages` branch.
- Enable GitHub Pages in repo settings.

---

## 3. Update Dashboard API URLs
- In `approval_dashboard_modern.html`, change all `http://127.0.0.1:5000` URLs to your public backend API URL (e.g., `https://your-app.onrender.com`).
- Example:
  ```js
  fetch('https://your-app.onrender.com/approvals')
  ```

---

## 4. Share Your Demo
- Your dashboard is now public and connected to your backend API.
- Share the dashboard link with judges and users.

---

## 5. Troubleshooting
- Make sure CORS is enabled in your Flask API:
  ```python
  from flask_cors import CORS
  CORS(app)
  ```
- If you use environment variables, set them in your cloud platform dashboard.
- If you need help, check platform docs or ask for step-by-step help here.

---

## Example Demo Flow
1. Engineer triggers an error in the log.
2. Agent posts suggestion to backend API.
3. Dashboard shows pending approval.
4. Engineer approves/rejects via dashboard.
5. Agent proceeds or halts based on decision.
6. Slack notification sent with dashboard link.

---

**Good luck at the hackathon!**
