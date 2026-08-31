from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime

from sqlalchemy.orm import relationship

from app.database.connection import Base





class LabTest(Base):

    __tablename__ = "lab_tests"


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


    test_name = Column(
        String(100),
        nullable=False
    )


    result = Column(
        String(500),
        nullable=True
    )


    status = Column(
        String(30),
        default="PENDING"
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


    patient = relationship(
        "Patient"
    )


    doctor = relationship(
        "Doctor"
    )
