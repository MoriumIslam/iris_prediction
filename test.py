#!/usr/bin/env python3
"""
Iris Species Predictor - Local Test Script
Quick testing and validation for development
"""

import os
import sys
from pathlib import Path

def test_imports():
    """Test if all required modules are importable"""
    print("\n📦 Testing imports...")
    
    modules = {
        'flask': 'Flask',
        'joblib': 'joblib',
        'sklearn': 'scikit-learn',
        'numpy': 'NumPy'
    }
    
    failed = []
    for module, name in modules.items():
        try:
            __import__(module)
            print(f"  ✓ {name}")
        except ImportError:
            print(f"  ✗ {name} - NOT INSTALLED")
            failed.append(name)
    
    if failed:
        print(f"\n❌ Missing: {', '.join(failed)}")
        print("   Run: pip install -r requirements.txt")
        return False
    return True

def test_model():
    """Test if model file exists and can be loaded"""
    print("\n🤖 Testing model...")
    
    model_path = Path('model.pkl')
    
    if not model_path.exists():
        print(f"  ✗ model.pkl not found in {model_path.absolute()}")
        return False
    
    print(f"  ✓ model.pkl found ({model_path.stat().st_size / 1024:.1f} KB)")
    
    try:
        import joblib
        model = joblib.load(model_path)
        print(f"  ✓ Model loaded successfully")
        
        # Try a test prediction
        test_data = [[5.1, 3.5, 1.4, 0.3]]
        pred = model.predict(test_data)
        print(f"  ✓ Test prediction works: {pred[0]}")
        
        return True
    except Exception as e:
        print(f"  ✗ Error loading model: {e}")
        return False

def test_app():
    """Test if Flask app can be imported"""
    print("\n🚀 Testing Flask app...")
    
    try:
        sys.path.insert(0, str(Path.cwd()))
        from app.app import app
        print(f"  ✓ Flask app imported successfully")
        
        # Test if routes exist
        routes = [route.rule for route in app.url_map.iter_rules()]
        required_routes = ['/', '/api/predict', '/health', '/about']
        
        for route in required_routes:
            if route in routes:
                print(f"  ✓ Route {route} exists")
            else:
                print(f"  ✗ Route {route} missing")
                return False
        
        return True
    except Exception as e:
        print(f"  ✗ Error loading app: {e}")
        return False

def test_templates():
    """Test if all template files exist"""
    print("\n🎨 Testing templates...")
    
    templates = {
        'app/templates/index.html': 'Home page',
        'app/templates/about.html': 'About page'
    }
    
    for template, desc in templates.items():
        if Path(template).exists():
            print(f"  ✓ {desc} ({template})")
        else:
            print(f"  ✗ {desc} missing ({template})")
            return False
    
    return True

def test_static():
    """Test if all static files exist"""
    print("\n📁 Testing static files...")
    
    files = {
        'app/static/css/style.css': 'Stylesheet',
        'app/static/js/script.js': 'JavaScript'
    }
    
    for file, desc in files.items():
        if Path(file).exists():
            size = Path(file).stat().st_size
            print(f"  ✓ {desc} ({size} bytes)")
        else:
            print(f"  ✗ {desc} missing ({file})")
            return False
    
    return True

def main():
    print("=" * 50)
    print("🌸 Iris Species Predictor - Test Suite")
    print("=" * 50)
    
    tests = [
        ("Imports", test_imports),
        ("Model", test_model),
        ("Templates", test_templates),
        ("Static Files", test_static),
        ("Flask App", test_app),
    ]
    
    results = {}
    for test_name, test_func in tests:
        try:
            results[test_name] = test_func()
        except Exception as e:
            print(f"\n❌ {test_name} test failed with error: {e}")
            results[test_name] = False
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 Summary")
    print("=" * 50)
    
    for test_name, result in results.items():
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{status}: {test_name}")
    
    all_pass = all(results.values())
    
    print("\n" + "=" * 50)
    if all_pass:
        print("✅ All tests passed! Ready to run:")
        print("   python app/app.py")
        print("\nThen open: http://localhost:5000")
    else:
        print("❌ Some tests failed. See above for details.")
        print("\nCommon fixes:")
        print("  1. Run: pip install -r requirements.txt")
        print("  2. Add model.pkl to project root")
        print("  3. Check file structure matches documentation")
    print("=" * 50 + "\n")
    
    return 0 if all_pass else 1

if __name__ == '__main__':
    sys.exit(main())
