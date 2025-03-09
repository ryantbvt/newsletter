''' Initialize db '''

import os
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.utils.logger import init_logger

logger = init_logger(__name__)

# load .env
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL is None:
    logger.critical("Database URL not provided.")
    raise ValueError("Database URL not provided.")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autoflush=False, bind=engine)
Base = declarative_base()

logger.info("Database initialized")

def get_db():
    '''
    Creates a new database session and ensures it's properly closed after use.
    
    This function serves as a dependency that can be injected into API routes
    to provide a database session. It uses a context manager pattern to ensure
    proper cleanup of database resources.
    
    Args:
        None
        
    Returns:
        SQLAlchemy Session: A database session that will be automatically closed
                           when the request is complete.
    '''
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
