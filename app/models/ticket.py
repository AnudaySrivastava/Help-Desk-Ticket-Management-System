#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Ticket model for the Help Desk Ticket Management System.

This module defines the SQLAlchemy ORM model for tickets.
"""

from datetime import datetime
from app import db


class Ticket(db.Model):
    """SQLAlchemy model for tickets.

    This class defines the database schema for tickets in the help desk system.
    """
    __tablename__ = 'tickets'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), nullable=False, default='open')
    priority = db.Column(db.String(20), nullable=False, default='medium')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, title, description, status='open', priority='medium'):
        """Initialize a new Ticket instance.

        Args:
            title (str): The ticket title.
            description (str): The ticket description.
            status (str, optional): The ticket status. Defaults to 'open'.
            priority (str, optional): The ticket priority. Defaults to 'medium'.
        """
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority

    def __repr__(self):
        """Return a string representation of the Ticket instance.

        Returns:
            str: A string representation of the Ticket instance.
        """
        return f'<Ticket {self.id}: {self.title}>'

    @property
    def serialize(self):
        """Return a dictionary representation of the Ticket instance.

        Returns:
            dict: A dictionary representation of the Ticket instance.
        """
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'priority': self.priority,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }