from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship

from app.database.connection import Base


class Radiology(Base):

    __tablename__ = "radiology_tests"


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


    test_type = Column(
        String(100),
        nullable=False
    )


    status = Column(
        String(30),
        default="PENDING"
    )


    result = Column(
        String(1000),
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
        "Doctor"
    )
