#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Entry point for the Help Desk Ticket Management System.

This script runs the Flask application defined in the app package.
"""

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)