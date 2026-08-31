from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database.connection import Base


class Billing(Base):

    __tablename__ = "billings"


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


    service_name = Column(
        String(100),
        nullable=False
    )


    amount = Column(
        Float,
        nullable=False
    )


    payment_status = Column(
        String(30),
        default="UNPAID"
    )


    payment_method = Column(
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
