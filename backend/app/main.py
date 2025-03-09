from fastapi import FastAPI

from app.utils.logger import init_logger
from app.api.v1.router import api_router

# Initialize logger
logger = init_logger(__name__)
logger.info("Initializing backend...")

# Initialize app
app = FastAPI()

app.include_router(api_router, prefix="/v1")
