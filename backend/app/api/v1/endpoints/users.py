''' Users API - CRUD '''

from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.utils.logger import init_logger
from app.database.database import get_db
from app.database.database import Base, engine
from app.schemas.users import UserCreate, UserLogin, UserResponse
from app.models.users import User
from app.security.auth_handler import (
    create_access_token, 
    create_refresh_token, 
    verify_token,
    oauth2_scheme
)
from app.security.auth_schemas import TokenPayload, TokenResponse

# Initialize logger
logger = init_logger(__name__)

# Initialize PostgreSQL table
Base.metadata.create_all(bind=engine)

# Create API router
router = APIRouter()

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    '''
    Description: Get current user from token
    
    Args:
        token (str): JWT token
        db (Session): Database session dependency
        
    Returns:
        User: Current user object
        
    Raises:
        HTTPException: If token is invalid or user not found
    '''
    try:
        # Verify token
        payload = verify_token(token)
        
        # Get user from db
        user = db.query(User).filter(User.id == payload.user_id).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
            
        return user
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"}
        )

async def get_current_admin_user(current_user: User = Depends(get_current_user)) -> User:
    '''
    Description: Get current admin user
    
    Args:
        current_user (User): Current user object
        
    Returns:
        User: Current admin user object
        
    Raises:
        HTTPException: If user is not admin
    '''
    if not current_user.admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions"
        )
    return current_user

@router.get("/", response_model=List[UserResponse])
async def get_users_list(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin_user)
):
    '''
    Description: Allows admin to retrieve all users

    Args:
        db (Session): Database session dependency
        current_user (User): Current admin user

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

@router.post("/login", response_model=TokenResponse)
async def login_user(user: UserLogin, db: Session = Depends(get_db)):
    '''
    Description: Allows user login

    Args:
        user (UserLogin): json input for user login
        db (Session): Database session dependency

    Returns:
        token (TokenResponse): Access token and refresh token
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
    
    logger.info(f"User password verified. ID: {db_user.id}")

    # Create token payload
    token_payload = TokenPayload(
        user_id=str(db_user.id),
        admin=db_user.admin
    )

    # Create tokens
    access_token = create_access_token(token_payload)
    refresh_token = create_refresh_token(token_payload)
    
    logger.info(f"User logged in. ID: {db_user.id}")

    return TokenResponse(
        access_token=access_token,
        refresh_token=refresh_token,
        token_type="Bearer"
    )
    
@router.post("/logout")
async def logout_user(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    '''
    Description: Allows user logout
    
    Args:
        current_user (User): Current user object
        db (Session): Database session dependency

    Returns:
        message (str): Success message
    '''
    logger.info(f"Logging out user {current_user.id}.")
    
    # Update last login time
    current_user.last_login = None
    db.commit()
    
    return {"message": "User logged out successfully"}
    
