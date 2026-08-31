from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database.connection import Base


class MedicalRecord(Base):

    __tablename__ = "medical_records"


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
        nullable=True
    )


    disease_name = Column(
        String(150),
        nullable=False
    )


    description = Column(
        Text,
        nullable=True
    )


    causes = Column(
        Text,
        nullable=True
    )


    severity = Column(
        String(50),
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
