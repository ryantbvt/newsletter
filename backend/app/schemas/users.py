''' Pydantic schemas for Users '''

from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    ''' Base user schema '''
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr

class UserCreate(UserBase):
    ''' Schema for creating a new user '''
    password: str = Field(..., min_length=8)
    role: Optional[str] = 'viewer'

class UserLogin(BaseModel):
    ''' Schema for user login '''
    email: EmailStr
    password: str

class UserResponse(UserBase):
    ''' Schema for user response (excluding sensitive data) '''
    id: int
    role: str
    created_at: datetime
    last_login: Optional[datetime]

    class Config:
        from_attributes = True 