''' SQLAlchemy models for Posts '''

from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text

from app.database.database import Base

class Post(Base):
    ''' SQL model for a Post object '''
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default=text("true"))
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"))
