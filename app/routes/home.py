#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Home routes for the Help Desk Ticket Management System.

This module defines the routes for the web interface.
"""

from flask import Blueprint, render_template

# Create a Blueprint for home routes
home_bp = Blueprint('home', __name__)


@home_bp.route('/')
def index():
    """Render the index page.

    Returns:
        Response: The rendered index.html template.
    """
    return render_template('index.html')