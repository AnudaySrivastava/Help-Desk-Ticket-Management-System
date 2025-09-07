#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Ticket schema for the Help Desk Ticket Management System.

This module defines the Marshmallow schema for ticket serialization and validation.
"""

from marshmallow import fields, validate
from app import ma, db
from app.models.ticket import Ticket


class TicketSchema(ma.SQLAlchemySchema):
    """Marshmallow schema for the Ticket model.

    This class defines the schema for serializing and deserializing Ticket instances.
    """
    class Meta:
        """Meta class for the TicketSchema.

        This class defines the model and fields to include in the schema.
        """
        model = Ticket
        load_instance = True
        include_fk = True

    id = ma.auto_field(dump_only=True)
    title = fields.String(required=True, validate=validate.Length(min=3, max=100))
    description = fields.String(required=True, validate=validate.Length(min=10))
    status = fields.String(
        validate=validate.OneOf(['open', 'in_progress', 'closed']),
        default='open'
    )
    priority = fields.String(
        validate=validate.OneOf(['low', 'medium', 'high']),
        default='medium'
    )
    created_at = ma.auto_field(dump_only=True)
    updated_at = ma.auto_field(dump_only=True)
    
    def jsonify(self, obj):
        """Serialize object to JSON response.
        
        This method is added for compatibility with newer Marshmallow versions.
        
        Args:
            obj: The object to serialize.
            
        Returns:
            Response: A Flask JSON response.
        """
        from flask import jsonify
        return jsonify(self.dump(obj))


# Initialize schema instances
ticket_schema = TicketSchema()
tickets_schema = TicketSchema(many=True)