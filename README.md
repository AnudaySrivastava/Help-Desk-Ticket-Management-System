# Help Desk Ticket Management System

A Flask-based Help Desk Ticket Management System similar to HappyFox, designed for managing support tickets efficiently.

## Features

- Create, read, update, and delete support tickets
- Track ticket status (open, in_progress, closed)
- Assign priority levels (low, medium, high)
- RESTful API for easy integration
- SQLite database for local development

## Project Structure

```
HelpDesk Ticket Management System/
├── app/                      # Application package
│   ├── __init__.py           # Application factory
│   ├── config.py             # Configuration settings
│   ├── models/               # Database models
│   │   ├── __init__.py
│   │   └── ticket.py         # Ticket model
│   ├── routes/               # API routes
│   │   ├── __init__.py
│   │   └── tickets.py        # Ticket endpoints
│   └── schemas/              # Marshmallow schemas
│       ├── __init__.py
│       └── ticket_schema.py  # Ticket schema
├── static/                   # Static assets (CSS, JS, etc.)
├── templates/                # HTML templates
├── .env                      # Environment variables
├── .flaskenv                 # Flask environment variables
├── requirements.txt          # Project dependencies
└── run.py                    # Application entry point
```

## Installation

1. Clone the repository

2. Create a virtual environment and activate it:

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
flask run
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/tickets | Get all tickets |
| GET | /api/tickets/<ticket_id> | Get a specific ticket |
| POST | /api/tickets | Create a new ticket |
| PUT | /api/tickets/<ticket_id> | Update a ticket |
| DELETE | /api/tickets/<ticket_id> | Delete a ticket |

## API Usage Examples

### Get all tickets

```bash
curl -X GET http://localhost:5000/api/tickets
```

### Get a specific ticket

```bash
curl -X GET http://localhost:5000/api/tickets/1
```

### Create a new ticket

```bash
curl -X POST http://localhost:5000/api/tickets \
  -H "Content-Type: application/json" \
  -d '{"title":"Server Down","description":"The main server is not responding","status":"open","priority":"high"}'
```

### Update a ticket

```bash
curl -X PUT http://localhost:5000/api/tickets/1 \
  -H "Content-Type: application/json" \
  -d '{"status":"in_progress"}'
```

### Delete a ticket

```bash
curl -X DELETE http://localhost:5000/api/tickets/1
```

## Future Enhancements

- User authentication with JWT
- React frontend
- Docker containerization
- Email notifications
- Ticket assignment to support agents
- Reporting and analytics

## License

MIT