# Iris Species Predictor - Render Deployment Guide

## 📋 Prerequisites

Before deploying to Render, ensure you have:

1. ✅ GitHub account (github.com)
2. ✅ Render account (render.com) 
3. ✅ Your `model.pkl` file in the project root
4. ✅ All project files committed to GitHub

## 🚀 Step-by-Step Deployment

### Step 1: Prepare Your Repository

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: Production-ready Iris predictor"

# Create GitHub repository at github.com/new
# Then add remote and push
git remote add origin https://github.com/YOUR_USERNAME/iris-predictor.git
git branch -M main
git push -u origin main
```

### Step 2: Create Render Account & Connect GitHub

1. Go to [render.com](https://render.com)
2. Sign up with GitHub (recommended - one-click auth)
3. Click "Authorize render-oss" to connect GitHub

### Step 3: Deploy Web Service

1. In Render dashboard, click **"New +"** button
2. Select **"Web Service"**
3. Connect your `iris-predictor` repository
4. Fill in the deployment settings:

   **Basic Settings:**
   - Name: `iris-predictor` (or your preferred name)
   - Region: `Oregon (US West)`
   - Branch: `main`

   **Build Command:**
   ```
   pip install -r requirements.txt
   ```

   **Start Command:**
   ```
   gunicorn --bind 0.0.0.0:$PORT --workers 3 --timeout 60 app.app:app
   ```

   **Environment Variables:**
   ```
   FLASK_ENV=production
   ```

5. Select Plan: **Free** (or paid if preferred)
6. Click **"Create Web Service"**

### Step 4: Wait for Deployment

- Render will automatically build and deploy your app
- You'll see the deployment logs in real-time
- Once complete, your app will be available at:
  ```
  https://iris-predictor.onrender.com
  ```

### Step 5: Test Your Deployment

1. Visit your live URL: `https://iris-predictor.onrender.com`
2. Test the prediction form
3. Check the health endpoint: `https://iris-predictor.onrender.com/health`

## 🔄 Automatic Deployments

Render automatically redeploys when you:
- Push to the `main` branch
- Make changes to your GitHub repository

To manually trigger a redeploy:
1. Go to your service on Render dashboard
2. Click "Manual Deploy"
3. Select branch and wait

## ⚡ Performance Tips

### Reduce Cold Starts
Add to your `render.yaml` (create if doesn't exist):

```yaml
services:
  - type: web
    name: iris-predictor
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn --bind 0.0.0.0:$PORT --workers 3 --timeout 60 app.app:app
    autoDeploy: true
    plan: free
```

### Keep App Awake
- Free tier apps go to sleep after 15 minutes of inactivity
- Use a monitoring service to ping `/health` endpoint regularly
- Or upgrade to a paid plan (starting $7/month)

## 🛠️ Troubleshooting

### Deployment Fails - "Model not found"

**Error:** `Model file not found at /app/model.pkl`

**Solution:**
1. Check that `model.pkl` is in project root
2. Verify `.gitignore` doesn't exclude `*.pkl`
3. Commit and push again:
   ```bash
   git add model.pkl
   git commit -m "Add trained model"
   git push
   ```

### App Crashes - "ModuleNotFoundError"

**Error:** `ModuleNotFoundError: No module named 'flask'`

**Solution:**
1. Ensure all imports are in `requirements.txt`
2. Check Python version compatibility
3. Render logs should show the error:
   - Go to service → "Logs" tab
   - Scroll to find the actual error

### Predictions Fail - "500 Internal Server Error"

**Solution:**
1. Check Render logs for the actual error
2. Verify model.pkl is valid (not corrupted in upload)
3. Test locally first: `python app/app.py`

### Slow Performance

**Solution:**
1. Increase workers in start command (if on paid plan)
2. Optimize model prediction speed locally first
3. Consider caching predictions if applicable

## 📊 Monitoring

### View Logs

```bash
# Using Render CLI
render logs iris-predictor --tail 50

# Or through dashboard: Service → Logs tab
```

### Health Check

Render automatically monitors your health endpoint:
```
GET /health
```

If this returns non-200, Render may restart the service.

## 🔐 Security Considerations

1. **Environment Variables:** Store sensitive data in Render env vars
2. **HTTPS:** Render provides free HTTPS by default
3. **Model Security:** Don't expose model internals in error messages
4. **Input Validation:** All inputs are validated (already implemented)

## 📈 Scaling

### Free Tier Limitations
- 750 hours/month (auto-sleeping after 15 min inactivity)
- 0.5 CPU
- 512 MB RAM

### Paid Tier Benefits
- Continuous running
- More resources
- Priority support
- Starting at $7/month

To upgrade:
1. Service settings → Plan
2. Select desired tier
3. Update payment method

## 🔄 Continuous Deployment

Every time you push to GitHub:
```bash
git add .
git commit -m "Update: description"
git push origin main
```

Render automatically:
1. Pulls latest code
2. Installs dependencies
3. Rebuilds the app
4. Restarts the service

## 📞 Render Support

- Docs: https://render.com/docs
- Status: https://render-status.com
- Contact: support@render.com

## ✅ Final Checklist Before Going Live

- [ ] Model file uploaded and working locally
- [ ] All dependencies in requirements.txt
- [ ] Procfile and runtime.txt present
- [ ] App runs locally: `python app/app.py`
- [ ] Form validation works
- [ ] Error handling functional
- [ ] Dark mode toggle works
- [ ] Mobile responsive
- [ ] Health endpoint returns 200
- [ ] GitHub repo is up to date
- [ ] Render deployment successful
- [ ] Live URL accessible and working
- [ ] Predictions return correct results

---

**You're all set! 🚀 Your Iris Predictor is now live on Render!**
