# 🌸 Iris Species Predictor - Quick Start Guide

Get your production-ready ML app running in minutes!

## ⚡ 30-Second Setup (Windows)

```bash
# 1. Run setup script
setup.bat

# 2. Activate virtual environment
venv\Scripts\activate

# 3. Run the app
python app/app.py

# 4. Open browser to: http://localhost:5000
```

## ⚡ 30-Second Setup (macOS/Linux)

```bash
# 1. Make setup script executable
chmod +x setup.sh

# 2. Run setup script
./setup.sh

# 3. Activate virtual environment
source venv/bin/activate

# 4. Run the app
python app/app.py

# 5. Open browser to: http://localhost:5000
```

## 📋 What You Need

- ✅ Python 3.11+ installed
- ✅ Your trained `model.pkl` file (or `logistic_regression_model.pkl`)

## 🚨 Important: Model File Location

Your model file should be in the project root. The app supports these names:
- `model.pkl` ← Recommended
- `logistic_regression_model.pkl`
- `iris_model.pkl`

**If you have an existing model file:**
```bash
# Windows
ren logistic_regression_model.pkl model.pkl

# macOS/Linux  
mv logistic_regression_model.pkl model.pkl
```

Or copy your model file to project root with one of the supported names.

## 🧪 Validate Everything

Run the test suite to verify setup:

```bash
# Make sure venv is activated, then:
python test.py
```

You should see:
```
✓ PASS: Imports
✓ PASS: Model
✓ PASS: Templates
✓ PASS: Static Files
✓ PASS: Flask App
```

## 🎯 Manual Setup (if scripts don't work)

```bash
# 1. Create virtual environment
python -m venv venv

# 2. Activate it (Windows)
venv\Scripts\activate
# OR (macOS/Linux)
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run app
python app/app.py
```

## 🌐 Access the App

Once running, open your browser:

- **Home:** http://localhost:5000
- **Predict:** http://localhost:5000/#predict
- **About:** http://localhost:5000/about
- **Health:** http://localhost:5000/health

## 🔧 Troubleshooting

### Problem: "Python not found"
**Solution:** Install Python 3.11+ from python.org

### Problem: "model.pkl not found"
**Solution:** Copy your trained model to project root as `model.pkl`

### Problem: "Address already in use"
**Solution:** Another app is using port 5000. Either:
- Close the other app, OR
- Change port in `app.py` line 102: `app.run(host='0.0.0.0', port=5001)`

### Problem: Module import errors
**Solution:** 
```bash
pip install -r requirements.txt --upgrade
```

## 📊 File Structure Created

```
iris_classifier_prediction/
├── app/
│   ├── app.py                 # Flask backend
│   ├── templates/
│   │   ├── index.html         # Home & predict page
│   │   └── about.html         # About page
│   └── static/
│       ├── css/style.css      # Modern styling
│       └── js/script.js       # Frontend logic
├── model.pkl                  # Your model (add this!)
├── requirements.txt           # Dependencies
├── Procfile                   # For Render
├── runtime.txt                # Python version
├── config.py                  # Configuration
├── test.py                    # Validation script
├── setup.bat/.sh              # Setup helpers
├── README.md                  # Full documentation
└── RENDER_DEPLOYMENT.md       # Deployment guide
```

## 🚀 Next Steps

### To Deploy on Render:
1. Follow [RENDER_DEPLOYMENT.md](RENDER_DEPLOYMENT.md)
2. Takes ~5 minutes with GitHub + Render setup

### To Modify/Customize:
- Edit `app/templates/index.html` for layout
- Edit `app/static/css/style.css` for styling
- Edit `app/static/js/script.js` for behavior
- Edit `app/app.py` for backend logic

### To Make Changes:
```bash
# Edit files...

# Test locally
python app/app.py

# Commit changes
git add .
git commit -m "Your change description"
git push

# If deployed on Render, it auto-deploys!
```

## 💡 API Testing

Quick test with curl:

```bash
# Test prediction
curl -X POST http://localhost:5000/api/predict \
  -H "Content-Type: application/json" \
  -d '{"sepal_length":5.1,"sepal_width":3.5,"petal_length":1.4,"petal_width":0.3}'

# Test health
curl http://localhost:5000/health
```

Expected output:
```json
{
  "success": true,
  "prediction": "Setosa",
  "confidence": 95.3,
  ...
}
```

## ✨ Features You Get

✓ Beautiful, responsive UI
✓ Dark/Light mode
✓ Form validation
✓ Loading states
✓ Error handling
✓ Mobile-friendly
✓ Production-ready
✓ Render-ready
✓ Fully documented

## 📚 Documentation

- `README.md` - Complete documentation
- `RENDER_DEPLOYMENT.md` - Step-by-step deployment
- `config.py` - Configuration options
- Code comments - Throughout codebase

## 🎓 Learning Resources

- Flask: https://flask.palletsprojects.com
- scikit-learn: https://scikit-learn.org
- Render: https://render.com/docs
- Iris Dataset: https://archive.ics.uci.edu/ml/datasets/iris

## 🤝 Support

If something doesn't work:

1. Check the error message carefully
2. Run `python test.py` to validate setup
3. Check `README.md` troubleshooting section
4. Review Flask error logs in terminal

## ✅ You're Ready!

```bash
# One more time:
python app/app.py

# Then visit: http://localhost:5000
```

**Happy predicting! 🌸**
