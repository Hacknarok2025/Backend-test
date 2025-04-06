from fastapi import FastAPI
from .middleware import add_cors_middleware
from .event_router import router
from .database import create_db_and_tables


app = FastAPI()

add_cors_middleware(app)
app.include_router(router)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
async def root():
    return "Welcome to the Calendar API"
