''' Consolidates all v1 endpoints to 1 api router '''

from fastapi import APIRouter
from app.api.v1.endpoints import posts, users

api_router = APIRouter()

# Load all endpoints
api_router.include_router(posts.router, prefix="/posts")
api_router.include_router(users.router, prefix="/auth")