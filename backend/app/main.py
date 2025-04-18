from fastapi import FastAPI

from app.utils.logger import init_logger
from app.api.v1.router import api_router
from app.schemas.config import Config
from app.middleware import setup_middleware

# Initialize logger
logger = init_logger(__name__)
logger.info("Initializing backend...")

# Load configuration
logger.info("Loading configuration...")
config = Config.from_yaml()
logger.info("Configurations loaded successfully")

# Initialize app
app = FastAPI()

# Setup middleware
setup_middleware(app, config)

# Include routers
app.include_router(api_router, prefix="/v1")

logger.info("Backend initialized successfully")

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "ok"}

# Readiness check endpoint
@app.get("/ready")
async def readiness_check():
    return {"status": "ok"}
