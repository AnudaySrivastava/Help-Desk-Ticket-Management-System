#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Ticket routes for the Help Desk Ticket Management System.

This module defines the API endpoints for ticket management.
"""

from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app import db
from app.models.ticket import Ticket
from app.schemas.ticket_schema import ticket_schema, tickets_schema

# Create a Blueprint for ticket routes
tickets_bp = Blueprint('tickets', __name__)


@tickets_bp.route('/tickets', methods=['GET'])
def get_tickets():
    """Get all tickets.

    Returns:
        Response: JSON response with all tickets.
    """
    tickets = Ticket.query.all()
    result = tickets_schema.dump(tickets)
    return jsonify(result)


@tickets_bp.route('/tickets/<int:ticket_id>', methods=['GET'])
def get_ticket(ticket_id):
    """Get a specific ticket by ID.

    Args:
        ticket_id (int): The ID of the ticket to retrieve.

    Returns:
        Response: JSON response with the ticket data or an error message.
    """
    ticket = Ticket.query.get_or_404(ticket_id)
    return ticket_schema.jsonify(ticket)


@tickets_bp.route('/tickets', methods=['POST'])
def create_ticket():
    """Create a new ticket.

    Returns:
        Response: JSON response with the created ticket data or validation errors.
    """
    try:
        ticket = ticket_schema.load(request.json)
        db.session.add(ticket)
        db.session.commit()
        return ticket_schema.jsonify(ticket), 201
    except ValidationError as err:
        return jsonify(err.messages), 400


@tickets_bp.route('/tickets/<int:ticket_id>', methods=['PUT'])
def update_ticket(ticket_id):
    """Update a specific ticket by ID.

    Args:
        ticket_id (int): The ID of the ticket to update.

    Returns:
        Response: JSON response with the updated ticket data or an error message.
    """
    ticket = Ticket.query.get_or_404(ticket_id)

    try:
        # Partial update - only update fields that are provided
        data = request.json
        if 'title' in data:
            ticket.title = data['title']
        if 'description' in data:
            ticket.description = data['description']
        if 'status' in data:
            ticket.status = data['status']
        if 'priority' in data:
            ticket.priority = data['priority']

        db.session.commit()
        return ticket_schema.jsonify(ticket)
    except ValidationError as err:
        return jsonify(err.messages), 400


@tickets_bp.route('/tickets/<int:ticket_id>', methods=['DELETE'])
def delete_ticket(ticket_id):
    """Delete a specific ticket by ID.

    Args:
        ticket_id (int): The ID of the ticket to delete.

    Returns:
        Response: JSON response with a success message or an error message.
    """
    ticket = Ticket.query.get_or_404(ticket_id)
    db.session.delete(ticket)
    db.session.commit()
    return jsonify({'message': f'Ticket {ticket_id} deleted successfully'})