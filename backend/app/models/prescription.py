from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database.connection import Base


class Prescription(Base):

    __tablename__ = "prescriptions"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    patient_id = Column(
        Integer,
        ForeignKey("patients.id"),
        nullable=False
    )


    doctor_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )


    medicine_id = Column(
        Integer,
        ForeignKey("medicines.id"),
        nullable=False
    )


    instructions = Column(
        Text,
        nullable=True
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


    patient = relationship(
        "Patient"
    )


    doctor = relationship(
        "User"
    )


    medicine = relationship(
        "Medicine"
    )
