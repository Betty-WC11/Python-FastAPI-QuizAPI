# The Director, entry point of your FastAPI.
# It creates the FastAPI() instance and tells it which routes to include.
# When you run uvicorn app.main:app, this is the file being executed.

from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Quiz API")

app.include_router(router)
