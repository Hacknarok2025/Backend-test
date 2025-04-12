# Hacknarok 2025 Game API

A FastAPI backend for a Norse mythology-themed game built for Hacknarok 2025, connecting the nine worlds of Norse mythology.

## Project Theme

"Connect 9 worlds into one code" - A game based on the nine worlds of Norse mythology:
- Asgard - world of the Aesir (gods)
- Alfheim - world of the Light Elves
- Nidavellir/Svartalfheim - world of the Dwarves/Dark Elves
- Midgard - world of humans
- Jotunheim - world of Giants
- Vanaheim - world of the Vanir (second family of gods)
- Niflheim - world of ice and mist
- Muspelheim - world of fire
- Helheim - world of the dead

## Features

- Progress through the nine Norse worlds
- Score tracking and leaderboard functionality
- Game state persistence
- No login required - player identification via unique tokens

## Tech Stack

- FastAPI: Modern, fast web framework for building APIs
- SQLModel: SQL databases in Python, designed for simplicity and type safety
- PostgreSQL: Database backend for storing game data and progress
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
4. Create a `.env` file with your database connection string:
   ```
   DATABASE_URL=postgresql://username:password@localhost:5432/dbname
   ```

## Running the Application

Start the server with:

```bash
uvicorn core.main:app --host 127.0.0.1 --port 8000
```

## API Endpoints

### Game Management
- `POST /players/new`: Create a new player and receive unique player token
- `GET /worlds/`: Get information about all nine worlds
- `GET /worlds/{world_id}`: Get details about a specific world

### Game Progression
- `GET /players/{player_token}/current`: Get current player state and available worlds
- `POST /players/{player_token}/complete/{world_id}`: Mark a world as completed and update progress

### Leaderboard
- `GET /leaderboard`: Get the top 10 players by score

## Deployment

The application is configured for deployment on Render.com using the provided `render.yaml` file.