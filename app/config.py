#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Configuration settings for the Help Desk Ticket Management System.

This module defines configuration classes for different environments.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """Base configuration class.

    This class defines configuration settings that are common across all environments.
    """
    # Flask configuration
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-key-for-development-only')
    DEBUG = False
    TESTING = False

    # SQLAlchemy configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///helpdesk.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """Development configuration class.

    This class extends the base configuration for development environments.
    """
    DEBUG = True


class TestingConfig(Config):
    """Testing configuration class.

    This class extends the base configuration for testing environments.
    """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class ProductionConfig(Config):
    """Production configuration class.

    This class extends the base configuration for production environments.
    """
    # Production-specific settings would go here
    pass


# Configuration dictionary for easy access to different configurations
config_dict = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}