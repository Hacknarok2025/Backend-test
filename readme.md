# Calendar FastAPI Backend

A simple backend API for managing calendar events built with FastAPI and SQLModel.

## Features

- Create, read, and delete calendar events
- Persistent storage using SQLite database
- CORS middleware for cross-origin requests

## Tech Stack

- FastAPI: Modern, fast web framework for building APIs
- SQLModel: SQL databases in Python, designed for simplicity and type safety
- Uvicorn: ASGI server implementation for Python

## Setup and Installation

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

Start the server with:

```bash
./start.sh
```

Or run it directly with:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## API Endpoints

- `GET /events/`: List all events
- `POST /events/`: Create a new event
- `GET /events/{event_id}`: Get a specific event
- `DELETE /events/{event_id}`: Delete an event

## Deployment

The application is configured for deployment on Render.com using the provided `render.yaml` file.