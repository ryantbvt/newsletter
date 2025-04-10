''' SQLAlchemy models for Users '''

from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text
from sqlalchemy.sql import func
from sqlalchemy.ext.hybrid import hybrid_property
import bcrypt

from app.database.database import Base

class User(Base):
    ''' SQL model for a User object '''
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    _password = Column("password", String, nullable=False)
    admin = Column(Boolean, nullable=False, server_default=text("false"))
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    last_login = Column(TIMESTAMP(timezone=True), nullable=True)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, plain_password: str):
        hashed = bcrypt.hashpw(
            bytes(plain_password, encoding="utf-8"),
            bcrypt.gensalt()
        )
        self._password = hashed.decode("utf-8")

    def verify_password(self, plain_password: str) -> bool:
        return bcrypt.checkpw(
            bytes(plain_password, encoding="utf-8"),
            bytes(self._password, encoding="utf-8")
        )