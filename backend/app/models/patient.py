from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.database.connection import Base


class Patient(Base):

    __tablename__ = "patients"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        unique=True,
        nullable=False
    )


    full_name = Column(
        String(100),
        nullable=False
    )


    birth_date = Column(
        Date,
        nullable=True
    )


    birth_place = Column(
        String(100),
        nullable=True
    )


    gender = Column(
        String(20),
        nullable=True
    )


    age = Column(
        Integer,
        nullable=True
    )


    height = Column(
        Float,
        nullable=True
    )


    weight = Column(
        Float,
        nullable=True
    )


    blood_type = Column(
        String(10),
        nullable=True
    )


    user = relationship(
        "User"
    )
