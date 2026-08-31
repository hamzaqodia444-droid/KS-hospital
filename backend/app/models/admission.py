from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship

from app.database.connection import Base


class Admission(Base):

    __tablename__ = "admissions"


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
        ForeignKey("doctors.id"),
        nullable=False
    )


    room_number = Column(
        String(50),
        nullable=True
    )


    admission_reason = Column(
        String(500),
        nullable=False
    )


    status = Column(
        String(30),
        default="ADMITTED"
    )


    discharge_notes = Column(
        String(1000),
        nullable=True
    )


    admitted_at = Column(
        DateTime,
        default=datetime.utcnow
    )


    discharged_at = Column(
        DateTime,
        nullable=True
    )


    patient = relationship(
        "Patient"
    )


    doctor = relationship(
        "Doctor"
    )
