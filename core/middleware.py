from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:5173",  
    "http://127.0.0.1:5173",
        "http://localhost:5174",  
    "http://127.0.0.1:5174",
    "https://hacknarok2025.github.io"

]


def add_cors_middleware(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
