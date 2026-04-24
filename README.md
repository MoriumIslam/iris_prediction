# 🌸 Iris Species Predictor - Production-Ready ML Web App

A modern, responsive machine learning web application that predicts iris flower species based on physical measurements. Built with Flask + JavaScript, production-ready for Render deployment.

## 🎯 Features

✨ **Beautiful UI**
- Modern gradient design with smooth animations
- Responsive layout (desktop, tablet, mobile)
- Dark/Light mode toggle
- Polished UX with loading states and smooth transitions

🤖 **ML Prediction**
- Load pre-trained pickle/joblib models
- Real-time predictions with confidence scores
- Input validation with helpful error messages
- Safe error handling and graceful fallbacks

🚀 **Production Ready**
- Deployment-ready for Render
- Environment variable support
- Gunicorn WSGI server configured
- Health check endpoint for monitoring
- Proper PORT handling for cloud deployment

🔒 **Robust Backend**
- Input validation and sanitization
- Error handling on all routes
- Model loading verification
- JSON API responses

## 📁 Project Structure

```
iris_classifier_prediction/
├── app/
│   ├── app.py                    # Flask application
│   ├── templates/
│   │   ├── index.html            # Home page
│   │   └── about.html            # About page
│   └── static/
│       ├── css/
│       │   └── style.css         # Responsive styling
│       ├── js/
│       │   └── script.js         # Frontend logic
│       └── images/
├── model.pkl                     # Your trained model (add this)
├── requirements.txt              # Python dependencies
├── Procfile                      # Render deployment config
├── runtime.txt                   # Python version
├── .gitignore
└── README.md
```

## 🚀 Quick Start (Local Development)

### 1. Prerequisites
- Python 3.11+
- Your trained `model.pkl` file

### 2. Setup

```bash
# Navigate to project directory
cd iris_classifier_prediction

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Add Your Model
Place your trained pickle model in the project root:
```bash
cp /path/to/your/model.pkl iris_classifier_prediction/
```

Or if using a different name:
```bash
cp /path/to/your/logistic_regression_model.pkl iris_classifier_prediction/model.pkl
```

Supported model file names:
- `model.pkl` (recommended)
- `logistic_regression_model.pkl`
- `iris_model.pkl`

### 4. Run Locally
```bash
# Set development environment
set FLASK_ENV=development  # Windows
export FLASK_ENV=development  # macOS/Linux

# Run the app
python app/app.py
```

The app will be available at: **http://localhost:5000**

## 📋 API Reference

### Prediction Endpoint
**POST** `/api/predict`

Request (JSON):
```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.3
}
```

Response (Success):
```json
{
  "success": true,
  "prediction": "Setosa",
  "species_id": 0,
  "description": "The smallest iris species with short, wide petals...",
  "characteristics": "Compact flower, native to Mediterranean regions",
  "color": "#FF6B6B",
  "confidence": 95.3,
  "input_data": {
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.3
  }
}
```

Response (Error):
```json
{
  "success": false,
  "error": "Validation failed",
  "details": ["Sepal Length: Enter a value between 4.0 and 8.0cm"]
}
```

### Health Check
**GET** `/health`

Response:
```json
{
  "status": "healthy",
  "model_loaded": true
}
```

## 🎨 UI Features

### Home Page (`/`)
- Hero section with animated flowers
- Beautiful gradient typography
- Call-to-action button
- Navigation to prediction and about pages

### Prediction Page
- Clean form with 4 input fields
- Real-time input validation
- Loading spinner during prediction
- Result card with species info
- Dark/light mode toggle
- Mobile responsive

### About Page (`/about`)
- Information about Iris dataset
- ML concepts explanation
- Technology stack details
- Dataset source and credits

## 📦 Deployment on Render

### 1. Prepare Git Repository
```bash
git init
git add .
git commit -m "Initial commit: Iris predictor app"
```

### 2. Push to GitHub
```bash
git remote add origin https://github.com/yourusername/iris-predictor.git
git branch -M main
git push -u origin main
```

### 3. Deploy on Render

1. Go to [render.com](https://render.com)
2. Sign up/Login with GitHub
3. Click "New +" → "Web Service"
4. Connect your GitHub repository
5. Fill in deployment settings:
   - **Name:** `iris-predictor`
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn --bind 0.0.0.0:$PORT --workers 3 --timeout 60 app.app:app`

6. Click "Create Web Service"
7. Render will automatically deploy from your main branch
8. Your app will be live at: `https://iris-predictor.onrender.com`

### 4. Set Environment Variables (if needed)
In Render dashboard → Environment:
```
FLASK_ENV=production
```

## ✅ Pre-Deployment Checklist

- [ ] Model file (`model.pkl`) is in the project root
- [ ] All dependencies are in `requirements.txt`
- [ ] `Procfile` and `runtime.txt` are present
- [ ] Local testing works: `python app/app.py` runs without errors
- [ ] Health check endpoint works: `http://localhost:5000/health`
- [ ] Form validation works and shows proper errors
- [ ] Dark mode toggle works
- [ ] Mobile responsive layout tested
- [ ] No console errors in browser developer tools
- [ ] Git repository is clean (run `git status`)

## 🔧 Troubleshooting

### Model not loading
```
Error: Model file not found at ...
```
**Solution:** Ensure `model.pkl` is in the project root directory

### Port already in use
```
Error: Address already in use
```
**Solution:** 
```bash
# Windows: Kill process on port 5000
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# macOS/Linux:
lsof -i :5000
kill -9 <PID>
```

### ImportError: No module named 'flask'
**Solution:** 
```bash
pip install -r requirements.txt
```

### Prediction returns 500 error
**Solution:** Check Render logs for model loading errors

## 🎓 Input Ranges (Iris Dataset)

| Feature | Min | Max | Unit |
|---------|-----|-----|------|
| Sepal Length | 4.0 | 8.0 | cm |
| Sepal Width | 2.0 | 4.5 | cm |
| Petal Length | 1.0 | 7.0 | cm |
| Petal Width | 0.1 | 2.5 | cm |

## 🔐 Security Features

✅ Input validation on all numeric fields
✅ Error messages don't expose system details
✅ CORS-safe API responses
✅ Proper HTTP status codes
✅ No sensitive data in responses
✅ Environment-based configuration

## 📝 Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `PORT` | 5000 | Server port |
| `FLASK_ENV` | production | Flask environment |

## 🤝 Contributing

Feel free to fork, modify, and improve this project!

## 📄 License

This project is open source and available for educational and commercial use.

## 🙏 Credits

- Built with **Flask** - Python web framework
- Styled with custom **CSS3** - Responsive design
- Model trained on **Fisher's Iris Dataset**
- Deployed on **Render** - Cloud platform

---

**Happy predicting! 🌸**

For questions or issues, check the Render logs:
```bash
render logs --tail 100
```
# iris_prediction
