''' Authentication schemas'''

from pydantic import BaseModel, Field
from typing import Optional

class TokenPayload(BaseModel):
    user_id: str
    admin: bool
    exp_time: Optional[int] = None
    iss_time: Optional[int] = None
    token_type: Optional[str] = None

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: Optional[str] = None
    token_type: str = "Bearer"
