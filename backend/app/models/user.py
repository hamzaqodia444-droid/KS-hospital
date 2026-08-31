from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.database.connection import Base


class User(Base):

    __tablename__ = "users"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    username = Column(
        String(50),
        unique=True,
        nullable=False,
        index=True
    )


    email = Column(
        String(120),
        unique=True,
        nullable=False,
        index=True
    )


    password_hash = Column(
        String(255),
        nullable=False
    )


    role = Column(
        String(20),
        nullable=False,
        default="PATIENT"
    )


    status = Column(
        String(20),
        default="ACTIVE"
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
