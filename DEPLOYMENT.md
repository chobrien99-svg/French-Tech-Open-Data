# Deploying the i-Lab Dashboard

## Option 1: Streamlit Cloud (Recommended - Free & Easy)

### Prerequisites
- ✅ GitHub account (you already have this)
- ✅ Streamlit account (free - sign in with GitHub)

### Step-by-Step Deployment:

#### 1. Create Streamlit Account
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click "Sign in with GitHub"
3. Authorize Streamlit to access your GitHub repos
4. Done! No credit card needed.

#### 2. Create requirements.txt
```bash
# Run this in your repo root
pip freeze > requirements.txt
```

Or manually create `requirements.txt` with:
```
streamlit>=1.28.0
pandas>=2.0.0
plotly>=5.17.0
```

#### 3. Deploy to Streamlit Cloud
1. Visit [share.streamlit.io](https://share.streamlit.io)
2. Click "New app"
3. Select your repository: `chobrien99-svg/French-Tech-Open-Data`
4. Select branch: `main` (or `claude/import-gov-data-P3BKE`)
5. Main file path: `streamlit_app.py`
6. Click "Deploy!"

#### 4. Wait ~2 minutes
Streamlit Cloud will:
- Clone your repo
- Install dependencies
- Launch your app
- Give you a public URL like: `https://your-app.streamlit.app`

### URL Structure:
Your app will be at: `https://[username]-[reponame]-[identifier].streamlit.app`

Example: `https://chobrien99-svg-french-tech-open-data-p3bke.streamlit.app`

### Features:
- ✅ Free hosting forever
- ✅ Auto-deploys on git push
- ✅ Public URL to share
- ✅ SSL/HTTPS included
- ✅ No server management
- ✅ Analytics dashboard

### Limitations (Free Tier):
- 1GB RAM per app
- 1 concurrent user gets full speed (others slightly slower)
- Public apps only (private requires Team plan)

---

## Option 2: GitHub Pages (Static HTML - Already Works!)

You already have `data/ilab/ilab_dashboard.html` which works standalone!

### To deploy:
1. Go to your repo settings
2. Pages → Source → Deploy from branch
3. Select branch and `/` (root) folder
4. Save
5. Access at: `https://chobrien99-svg.github.io/French-Tech-Open-Data/data/ilab/ilab_dashboard.html`

**Pros**:
- No account needed (besides GitHub)
- Instant deployment
- Works offline

**Cons**:
- No interactive filters
- Static data (need to regenerate HTML for updates)

---

## Option 3: Render.com (Alternative to Streamlit)

Similar to Streamlit Cloud but more configuration needed:

1. Sign up at [render.com](https://render.com)
2. Connect GitHub
3. Create "Web Service"
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `streamlit run streamlit_app.py --server.port=$PORT`
6. Deploy

**Pros**:
- More customization options
- Better for production apps

**Cons**:
- More complex setup
- Free tier spins down after inactivity (takes 30s to wake up)

---

## Option 4: Vercel (For Next.js version)

If you want to use Vercel, you'd need to rebuild in JavaScript:

### Tech stack would be:
- Next.js (React framework)
- Recharts or Plotly.js
- Leaflet for maps
- TailwindCSS for styling

**This would require**:
1. Converting Python scripts to JavaScript
2. Setting up Next.js project
3. Creating React components
4. Loading CSV as static JSON

**Time investment**: ~4-8 hours to rebuild

**When to use**: If you want to add features like:
- Authentication
- User accounts
- Database integration
- Complex API interactions

---

## Comparison Table

| Platform | Cost | Setup Time | Best For | Limitations |
|----------|------|------------|----------|-------------|
| **Streamlit Cloud** | Free | 5 min | Python apps, data dashboards | 1GB RAM, public only |
| **GitHub Pages** | Free | 2 min | Static sites | No backend, no interactivity |
| **Render.com** | Free | 15 min | Production apps | Sleeps after inactivity |
| **Vercel** | Free | 4-8 hrs | React/Next.js apps | Need to rebuild in JS |

---

## My Recommendation: Streamlit Cloud

**Why?**
1. ✅ You already have the Python code
2. ✅ Takes 5 minutes to deploy
3. ✅ Free forever
4. ✅ Auto-updates when you push to GitHub
5. ✅ Perfect for data dashboards
6. ✅ No coding changes needed

**Steps**:
1. Create `requirements.txt` (I'll do this for you)
2. Commit and push to GitHub
3. Sign in to Streamlit Cloud with GitHub
4. Click deploy
5. Share your URL!

---

## Testing Locally First

Before deploying, test the Streamlit app locally:

```bash
# Install Streamlit
pip install streamlit pandas plotly

# Run the app
streamlit run streamlit_app.py

# Opens automatically in browser at http://localhost:8501
```

If it works locally, it'll work on Streamlit Cloud!

---

## Next Steps

1. I'll create the `requirements.txt` file
2. We'll test the app locally
3. You commit and push to GitHub
4. You deploy to Streamlit Cloud (literally 3 clicks)
5. You have a live, shareable dashboard!

Ready to proceed?
