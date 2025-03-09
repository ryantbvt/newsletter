''' Consolidates all v1 endpoints to 1 api router '''

from fastapi import APIRouter
from app.api.v1.endpoints import posts

api_router = APIRouter()

# Load all endpoints
api_router.include_router(posts.router, prefix="/posts")
