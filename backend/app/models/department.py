from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database.connection import Base


class Department(Base):

    __tablename__ = "departments"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    name = Column(
        String(100),
        unique=True,
        nullable=False
    )


    description = Column(
        String(500),
        nullable=True
    )


    doctors = relationship(
        "Doctor",
        back_populates="department"
    )


    nurses = relationship(
        "Nurse",
        back_populates="department"
    )
