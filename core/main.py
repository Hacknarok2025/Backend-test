from fastapi import FastAPI
from middleware import add_cors_middleware
from event_router import router

app = FastAPI()

add_cors_middleware(app)
app.include_router(router)