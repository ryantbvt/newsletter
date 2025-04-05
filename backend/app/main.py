from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.utils.logger import init_logger
from app.api.v1.router import api_router

# Initialize logger
logger = init_logger(__name__)
logger.info("Initializing backend...")

# Initialize app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # currently only frontend
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Include routers
app.include_router(api_router, prefix="/v1")
