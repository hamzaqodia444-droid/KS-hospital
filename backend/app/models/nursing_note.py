from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.database.connection import Base


class NursingNote(Base):

    __tablename__ = "nursing_notes"


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


    nurse_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )


    note = Column(
        Text,
        nullable=True
    )


    patient_status = Column(
        String(50),
        nullable=True
    )


    created_at = Column(
        DateTime,
        nullable=True
    )


    patient = relationship(
        "Patient"
    )


    nurse = relationship(
        "User"
    )
