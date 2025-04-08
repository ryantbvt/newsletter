''' Users API - CRUD '''

from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.utils.logger import init_logger
from app.database.database import get_db
from app.database.database import Base, engine
from app.schemas.users import UserCreate, UserLogin, UserResponse
from app.models.users import User

# Initialize logger
logger = init_logger(__name__)

# Initialize PostgreSQL table
Base.metadata.create_all(bind=engine)

# Create API router
router = APIRouter()

@router.get("/", response_model=List[UserResponse])
async def get_users_list(db: Session = Depends(get_db)):
    '''
    Description: Allows admin to retrieve all users

    Args:
        db (Session): Database session dependency

    Returns:
        users (List[UserResponse]): List of all users in the database
    '''
    logger.info("Retrieving all users.")

    user_list = db.query(User).all()
    logger.info(f"Found {len(user_list)} users.")

    return user_list

@router.post("/register", response_model=UserResponse)
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    '''
    Description: Allows user registration

    Args:
        user (UserCreate): json input for user creation
        db (Session): Database session dependency

    Returns:
        user (UserResponse): The user that was created.
    '''
    logger.info("Registering new user.")

    # Check if user already exists
    existing_user = db.query(User).filter(User.email == user.email).first()
    
    if existing_user:
        logger.error(f"User with email {user.email} already exists.")
        raise HTTPException(status_code=400, detail="User already exists")
    
    # Create new user
    new_user = User(**user.model_dump())
    
    # Add new user to db
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    logger.info(f"New user created. ID: {new_user.id}")

    return new_user

@router.post("/login", response_model=UserResponse)
async def login_user(user: UserLogin, db: Session = Depends(get_db)):
    '''
    Description: Allows user login

    Args:
        user (UserLogin): json input for user login
        db (Session): Database session dependency

    Returns:
        user (UserResponse): The user that was logged in.
    '''
    logger.info("Logging in user.")
    
    # Check if user exists
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user:
        logger.error(f"User with email {user.email} not found.")
        raise HTTPException(status_code=400, detail="Invalid credentials")

    logger.info(f"User found. ID: {db_user.id}")
    
    # Check password
    if not db_user.verify_password(user.password):
        logger.error(f"Invalid password for user {user.email}.")
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    logger.info(f"User logged in. ID: {db_user.id}")
    
    return db_user
    
@router.post("/logout")
async def logout_user(db: Session = Depends(get_db)):
    '''
    Description: Allows user logout
    
    Args:
        db (Session): Database session dependency

    Returns:
        message (str): Success message
    '''
    logger.info("Logging out user.")
    
    # TODO: Implement logout logic

    return {"message": "User logged out successfully"}
    
