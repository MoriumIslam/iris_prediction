"""
Iris Flower Species Prediction Web App
A production-ready Flask application for predicting iris species
using a pre-trained machine learning model.
"""

import os
import joblib
import numpy as np
from flask import Flask, render_template, request, jsonify
from pathlib import Path

# Initialize Flask app
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# Load model on startup
MODEL_PATH = None
MODEL = None

def find_model():
    """Find the model file in the project root"""
    # Check for both common names
    root = Path(__file__).parent.parent
    for model_name in ['model.pkl', 'logistic_regression_model.pkl', 'iris_model.pkl']:
        path = root / model_name
        if path.exists():
            return path
    return None

def load_model():
    """Load the pickled model on application startup"""
    global MODEL, MODEL_PATH
    try:
        MODEL_PATH = find_model()
        if MODEL_PATH and MODEL_PATH.exists():
            MODEL = joblib.load(MODEL_PATH)
            print(f"✓ Model loaded successfully from {MODEL_PATH}")
        else:
            print(f"✗ Model file not found in project root")
            print("  Supported names: model.pkl, logistic_regression_model.pkl, iris_model.pkl")
    except Exception as e:
        print(f"✗ Error loading model: {str(e)}")


# Iris species information
SPECIES_INFO = {
    0: {
        "name": "Setosa",
        "description": "The smallest iris species with short, wide petals and a delicate appearance.",
        "characteristics": "Compact flower, native to Mediterranean regions",
        "color": "#FF6B6B"
    },
    1: {
        "name": "Versicolor",
        "description": "A medium-sized iris with intermediate petal lengths.",
        "characteristics": "Versatile species, medium height with varied colors",
        "color": "#4ECDC4"
    },
    2: {
        "name": "Virginica",
        "description": "The largest iris species with long, broad petals.",
        "characteristics": "Tall flowering plant, deep purple or blue hues",
        "color": "#95E1D3"
    }
}

# Validation ranges for iris measurements (in cm)
VALID_RANGES = {
    "sepal_length": (4.0, 8.0),
    "sepal_width": (2.0, 4.5),
    "petal_length": (1.0, 7.0),
    "petal_width": (0.1, 2.5)
}

# CRITICAL: Load model at module level (runs when Gunicorn imports the app)
load_model()


def validate_input(data):
    """Validate input data before prediction"""
    errors = []
    
    required_fields = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
    
    for field in required_fields:
        if field not in data:
            errors.append(f"Missing field: {field}")
            continue
        
        try:
            value = float(data[field])
            min_val, max_val = VALID_RANGES[field]
            
            if value < min_val or value > max_val:
                errors.append(
                    f"{field.replace('_', ' ').title()}: "
                    f"Enter a value between {min_val} and {max_val}cm"
                )
        except ValueError:
            errors.append(f"{field.replace('_', ' ').title()}: Must be a valid number")
    
    return errors


@app.route('/')
def home():
    """Render home page"""
    return render_template('index.html')


@app.route('/about')
def about():
    """Render about page"""
    return render_template('about.html')


@app.route('/api/predict', methods=['POST'])
def predict():
    """
    API endpoint for iris species prediction
    Accepts JSON or form data with flower measurements
    """
    try:
        # Parse input data
        if request.is_json:
            data = request.get_json()
        else:
            data = request.form.to_dict()
        
        # Validate input
        errors = validate_input(data)
        if errors:
            return jsonify({
                "success": False,
                "error": "Validation failed",
                "details": errors
            }), 400
        
        # Prepare features for prediction
        features = [
            float(data["sepal_length"]),
            float(data["sepal_width"]),
            float(data["petal_length"]),
            float(data["petal_width"])
        ]
        
        # Make prediction
        if MODEL is None:
            return jsonify({
                "success": False,
                "error": "Model not loaded",
                "details": ["The prediction model failed to load. Please contact support."]
            }), 500
        
        prediction = MODEL.predict([features])[0]
        
        # Get prediction probability if available
        try:
            probabilities = MODEL.predict_proba([features])[0]
            confidence = float(np.max(probabilities)) * 100
        except (AttributeError, IndexError):
            confidence = None
        
        # Prepare response
        species_info = SPECIES_INFO.get(int(prediction), {})
        
        response = {
            "success": True,
            "prediction": species_info.get("name", f"Species {prediction}"),
            "species_id": int(prediction),
            "description": species_info.get("description", ""),
            "characteristics": species_info.get("characteristics", ""),
            "color": species_info.get("color", "#000000"),
            "confidence": round(confidence, 1) if confidence else None,
            "input_data": {
                "sepal_length": float(data["sepal_length"]),
                "sepal_width": float(data["sepal_width"]),
                "petal_length": float(data["petal_length"]),
                "petal_width": float(data["petal_width"])
            }
        }
        
        return jsonify(response), 200
    
    except Exception as e:
        return jsonify({
            "success": False,
            "error": "Prediction error",
            "details": [str(e)]
        }), 500


@app.route('/health')
def health():
    """Health check endpoint for deployment monitoring"""
    return jsonify({
        "status": "healthy",
        "model_loaded": MODEL is not None
    }), 200


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({"error": "Endpoint not found"}), 404


@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors"""
    return jsonify({"error": "Internal server error"}), 500


if __name__ == '__main__':
    # Load model before starting server
    load_model()
    
    # Get port from environment or default to 5000
    port = int(os.environ.get('PORT', 5000))
    
    # Run app (debug=False for production)
    app.run(
        host='0.0.0.0',
        port=port,
        debug=os.environ.get('FLASK_ENV') == 'development'
    )
