from sqlalchemy import Column, Integer, String, Date, Time, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship

from app.database.connection import Base


class Appointment(Base):

    __tablename__ = "appointments"


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


    appointment_date = Column(
        Date,
        nullable=False
    )


    appointment_time = Column(
        Time,
        nullable=False
    )


    status = Column(
        String(30),
        default="PENDING"
    )


    notes = Column(
        String(500),
        nullable=True
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


    patient = relationship("Patient")

    doctor = relationship("Doctor")
