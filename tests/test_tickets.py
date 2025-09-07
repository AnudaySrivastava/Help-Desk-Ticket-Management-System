#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test cases for the ticket API endpoints.

This module contains unit tests for the ticket API endpoints.
"""

import json
import unittest
from app import create_app, db
from app.models.ticket import Ticket


class TicketTestCase(unittest.TestCase):
    """Test case for the ticket API endpoints.

    This class contains unit tests for the ticket API endpoints.
    """

    def setUp(self):
        """Set up the test environment.

        This method is called before each test.
        """
        self.app = create_app('app.config.TestingConfig')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        # Create a test ticket
        self.ticket = Ticket(
            title='Test Ticket',
            description='This is a test ticket',
            status='open',
            priority='medium'
        )
        db.session.add(self.ticket)
        db.session.commit()

    def tearDown(self):
        """Tear down the test environment.

        This method is called after each test.
        """
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_get_all_tickets(self):
        """Test getting all tickets.

        This test verifies that the GET /api/tickets endpoint returns all tickets.
        """
        response = self.client.get('/api/tickets')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['title'], 'Test Ticket')

    def test_get_ticket(self):
        """Test getting a specific ticket.

        This test verifies that the GET /api/tickets/<id> endpoint returns the correct ticket.
        """
        response = self.client.get(f'/api/tickets/{self.ticket.id}')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['title'], 'Test Ticket')
        self.assertEqual(data['description'], 'This is a test ticket')

    def test_create_ticket(self):
        """Test creating a new ticket.

        This test verifies that the POST /api/tickets endpoint creates a new ticket.
        """
        ticket_data = {
            'title': 'New Ticket',
            'description': 'This is a new ticket',
            'status': 'open',
            'priority': 'high'
        }

        response = self.client.post(
            '/api/tickets',
            data=json.dumps(ticket_data),
            content_type='application/json'
        )
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['title'], 'New Ticket')
        self.assertEqual(data['priority'], 'high')

        # Verify the ticket was added to the database
        tickets = Ticket.query.all()
        self.assertEqual(len(tickets), 2)

    def test_update_ticket(self):
        """Test updating a ticket.

        This test verifies that the PUT /api/tickets/<id> endpoint updates a ticket.
        """
        update_data = {
            'status': 'in_progress',
            'priority': 'high'
        }

        response = self.client.put(
            f'/api/tickets/{self.ticket.id}',
            data=json.dumps(update_data),
            content_type='application/json'
        )
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], 'in_progress')
        self.assertEqual(data['priority'], 'high')
        self.assertEqual(data['title'], 'Test Ticket')  # Unchanged field

    def test_delete_ticket(self):
        """Test deleting a ticket.

        This test verifies that the DELETE /api/tickets/<id> endpoint deletes a ticket.
        """
        response = self.client.delete(f'/api/tickets/{self.ticket.id}')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertIn('deleted successfully', data['message'])

        # Verify the ticket was removed from the database
        ticket = Ticket.query.get(self.ticket.id)
        self.assertIsNone(ticket)

    def test_invalid_ticket_id(self):
        """Test accessing a non-existent ticket.

        This test verifies that the API returns a 404 error when accessing a non-existent ticket.
        """
        response = self.client.get('/api/tickets/999')
        self.assertEqual(response.status_code, 404)

    def test_validation_error(self):
        """Test validation error when creating a ticket.

        This test verifies that the API returns a 400 error when validation fails.
        """
        # Missing required field 'description'
        ticket_data = {
            'title': 'Invalid Ticket',
            'status': 'open',
            'priority': 'low'
        }

        response = self.client.post(
            '/api/tickets',
            data=json.dumps(ticket_data),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()