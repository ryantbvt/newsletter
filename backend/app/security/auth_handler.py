''' Authentication handler'''

from datetime import datetime, timedelta
from typing import Dict, Optional, Any

from jose import jwt
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer

from app.security.jwt_dependencies import (
    JWT_SECRET_KEY,
    ALGORITHM,
    ACCESS_TOKEN_EXPIRE_MINUTES,
    REFRESH_TOKEN_EXPIRE_DAYS
)
from app.security.auth_schemas import TokenPayload

# OAuth2 configuration
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/users/login") # point to login endpoint

def create_token(data: TokenPayload, expires_delta: timedelta, token_type: str) -> str:
    '''
    Description: Helper function to create JWT tokens

    Args:
        data (TokenPayload): Data to encode in the token

    Returns:
        TokenResponse: Access token and refresh token
    '''
    # Create payload from data
    payload_dict = data.model_dump()

    # Add expiration time and token type to payload
    current_time = datetime.utcnow()
    payload_dict.update({
        "exp_time": int((current_time + expires_delta).timestamp()),  # Unix timestamp for expiration
        "iss_time": int(current_time.timestamp()),  # Unix timestamp for issued at
        "token_type": token_type
    })

    # Encode token
    encoded_token = jwt.encode(
        payload_dict,
        JWT_SECRET_KEY.encode('utf-8'),  # Convert secret key to bytes
        algorithm=ALGORITHM
    )

    return encoded_token

def create_access_token(data: TokenPayload) -> str:
    '''
    Description: Create short-lived access token

    Args:
        data (TokenPayload): Data to encode in the token

    Returns:
        str: Access token
    '''
    return create_token(data, timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES), "access"  )

def create_refresh_token(data: TokenPayload) -> str:
    '''
    Description: Create long-lived refresh token

    Args:
        data (TokenPayload): Data to encode in the token

    Returns:
        str: Refresh token
    '''
    return create_token(data, timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS), "refresh")
    
def verify_token(token: str) -> TokenPayload:
    '''
    Description: Verify and decode JWT token

    Args:
        token (str): JWT token to verify
    
    Returns:
        TokenPayload: Decoded token payload
    '''
    try:
        # Decode and verify token
        payload = jwt.decode(
            token, 
            JWT_SECRET_KEY.encode('utf-8'),  # Convert secret key to bytes
            algorithms=[ALGORITHM]
        )

        return TokenPayload(**payload)

    except jwt.JWTError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"}
        )
