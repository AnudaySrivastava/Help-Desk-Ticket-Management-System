#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Application factory for the Help Desk Ticket Management System.

This module initializes the Flask application and its extensions.
"""

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import marshmallow as ma_base  # Import base marshmallow for compatibility
from flask_migrate import Migrate
from flask_cors import CORS

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()

# Create Marshmallow instance
ma = Marshmallow()


def create_app(config_class=None):
    """Create and configure the Flask application.

    Args:
        config_class: Configuration class to use. Defaults to None.

    Returns:
        Flask: The configured Flask application.
    """
    app = Flask(__name__, static_folder='../static', template_folder='../templates')

    # Load configuration
    if config_class is None:
        app.config.from_object('app.config.Config')
    else:
        app.config.from_object(config_class)

    # Initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)
    
    # Set up SQLAlchemy integration for Marshmallow
    # This is needed for compatibility with flask-marshmallow and marshmallow-sqlalchemy
    # The SQLAlchemy extension needs to be properly structured for Flask-Marshmallow
    class SQLAlchemyWrapper:
        def __init__(self, db):
            self.db = db
    
    app.extensions['sqlalchemy'] = SQLAlchemyWrapper(db)
    
    # Initialize Marshmallow after SQLAlchemy is properly set up
    ma.init_app(app)

    # Register blueprints
    from app.routes.tickets import tickets_bp
    from app.routes.home import home_bp
    app.register_blueprint(tickets_bp, url_prefix='/api')
    app.register_blueprint(home_bp)

    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()

    return app