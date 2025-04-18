''' JWT dependencies'''

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS"))

if JWT_SECRET_KEY is None:
    raise ValueError("JWT_SECRET_KEY is not set")

if ALGORITHM is None:
    raise ValueError("ALGORITHM is not set")
    