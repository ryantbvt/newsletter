from fastapi import FastAPI, Request
from typing import Callable, Awaitable, Any

from app.schemas.config import Config
from app.middleware.cors import setup_cors

def setup_middleware(app: FastAPI, config: Config) -> None:
    """Setup all middleware for the application."""
    # Setup CORS middleware
    setup_cors(app, config) 

    # TODO: add the rate limit middleware