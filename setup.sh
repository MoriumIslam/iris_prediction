#!/bin/bash

# Iris Species Predictor - Setup Script for macOS/Linux

echo ""
echo "===================================="
echo "🌸 Iris Species Predictor Setup"
echo "===================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed"
    echo "Please install Python 3.11+ from python.org"
    exit 1
fi

echo "✓ Python found: $(python3 --version)"

# Create virtual environment
echo ""
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo ""
echo "Installing dependencies..."
pip install -r requirements.txt

# Check for model file
echo ""
if [ ! -f model.pkl ]; then
    echo "⚠️  model.pkl not found!"
    echo "Please add your trained model file (model.pkl) to the project root"
    echo ""
fi

echo "===================================="
echo "✅ Setup Complete!"
echo "===================================="
echo ""
echo "To run the app:"
echo ""
echo "1. Activate virtual environment:"
echo "   source venv/bin/activate"
echo ""
echo "2. Run the application:"
echo "   python app/app.py"
echo ""
echo "3. Open browser to: http://localhost:5000"
echo ""
