from sqlalchemy import Column, Integer, ForeignKey, DateTime
from datetime import datetime

from app.database.connection import Base


class DoctorPatient(Base):

    __tablename__ = "doctor_patients"

    id = Column(
        Integer,
        primary_key=True
    )

    doctor_id = Column(
        Integer,
        ForeignKey("doctors.id"),
        nullable=False
    )

    patient_id = Column(
        Integer,
        ForeignKey("patients.id"),
        nullable=False
    )

    assigned_at = Column(
        DateTime,
        default=datetime.utcnow
    )
