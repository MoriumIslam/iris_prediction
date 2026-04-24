@echo off
REM Iris Species Predictor - Setup Script for Windows

echo.
echo ====================================
echo 🌸 Iris Species Predictor Setup
echo ====================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python 3.11+ from python.org
    pause
    exit /b 1
)

echo ✓ Python found

REM Create virtual environment
echo.
echo Creating virtual environment...
python -m venv venv

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo.
echo Installing dependencies...
pip install -r requirements.txt

REM Check for model file
if not exist model.pkl (
    echo.
    echo ⚠️  model.pkl not found!
    echo Please add your trained model file (model.pkl) to the project root
    echo.
)

echo.
echo ====================================
echo ✅ Setup Complete!
echo ====================================
echo.
echo To run the app:
echo.
echo 1. Activate virtual environment:
echo    venv\Scripts\activate
echo.
echo 2. Run the application:
echo    python app/app.py
echo.
echo 3. Open browser to: http://localhost:5000
echo.
pause
