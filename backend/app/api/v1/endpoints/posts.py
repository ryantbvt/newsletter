''' Posts API - CRUD '''

from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.utils.logger import init_logger
from app.database.database import get_db
from app.database.database import Base, engine
from app.schemas.posts import CreatePost
from app.models.posts import Post

# Initialize logger
logger = init_logger(__name__)

# Initailize PostgreSQL table
Base.metadata.create_all(bind=engine)

# Create API router
router = APIRouter()

@router.get("/", response_model=List[CreatePost])
async def test_posts(db: Session = Depends(get_db)):
    '''
    Description: Retrives all posts from the database

    Args:
        db (Session): Database session dependency

    Returns:
        posts (List[CreatePost]): List of all the posts in the database
    '''
    logger.info("Retrieving posts from database.")

    posts = db.query(Post).all()
    logger.info(f"Found {len(posts)} posts.")

    return posts

@router.post("/create")
async def create_post(post: CreatePost, db: Session = Depends(get_db)):
    '''
    Description: Allows post creation

    Args:
        post (CreatePost): json input for post creation
        db (Session): Database session dependency

    Return:
        new_post (CreatePost): The post that was created.
    '''
    logger.info("Creating new post.")

    new_post = Post(**post.model_dump())

    # Add new post to db
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    logger.info(f"New post created. ID: {new_post.id}")

    return new_post

@router.get("/{id}", response_model=CreatePost, status_code=200)
async def fetch_post(id: int, db: Session = Depends(get_db)):
    '''
    Description: Fetch post by id.

    Args:
        id (int): post id
        db (Session): Database session dependency

    Return:
        post (CreatePost): the post found in db

    Exceptions:
        404: when post is not found in db
    '''
    logger.info(f"Attempting to fetch post id: {id}")

    # Query db
    post = db.query(Post).filter(Post.id == id).first()

    if post is None:
        logger.warning(f"Post {id} not found.")
        raise HTTPException(status_code=404, detail=f"Post {id} not found.")
    
    logger.info(f"Found post {id}, returning...")

    return post
