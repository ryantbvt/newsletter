''' CORS Middleware '''

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.schemas.config import Config

def setup_cors(app: FastAPI, config: Config):
    """Setup CORS middleware with configuration."""
    app.add_middleware(
        CORSMiddleware,
        allow_origins=config.cors.allow_origins,
        allow_credentials=config.cors.allow_credentials,
        allow_methods=config.cors.allow_methods,
        allow_headers=config.cors.allow_headers,
    ) 