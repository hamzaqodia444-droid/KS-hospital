from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database.connection import Base


class Doctor(Base):

    __tablename__ = "doctors"


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


    department_id = Column(
        Integer,
        ForeignKey("departments.id"),
        nullable=False
    )


    full_name = Column(
        String(100),
        nullable=False
    )


    specialization = Column(
        String(100),
        nullable=False
    )


    license_number = Column(
        String(100),
        unique=True,
        nullable=False
    )


    phone = Column(
        String(30),
        nullable=True
    )


    user = relationship(
        "User"
    )


    department = relationship(
        "Department",
        back_populates="doctors"
    )
