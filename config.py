"""
Configuration file for Iris Species Predictor
Separates settings for different environments
"""

import os
from pathlib import Path

class Config:
    """Base configuration"""
    # Flask settings
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    
    # Application settings
    JSON_SORT_KEYS = False
    PROPAGATE_EXCEPTIONS = True
    
    # Model settings
    MODEL_PATH = Path(__file__).parent / 'model.pkl'
    
    # CORS settings (if needed)
    CORS_ORIGINS = os.environ.get('CORS_ORIGINS', '*').split(',')


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    ENV = 'development'


class ProductionConfig(Config):
    """Production configuration for Render/Cloud"""
    DEBUG = False
    ENV = 'production'
    
    # Stricter settings for production
    CORS_ORIGINS = os.environ.get('CORS_ORIGINS', 'https://iris-predictor.onrender.com').split(',')


class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    DEBUG = True
    ENV = 'testing'


# Select configuration based on environment
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}

def get_config():
    """Get appropriate configuration based on FLASK_ENV"""
    env = os.environ.get('FLASK_ENV', 'development')
    return config.get(env, config['default'])
