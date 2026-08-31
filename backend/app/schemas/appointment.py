from pydantic import BaseModel
from datetime import date, time, datetime


class AppointmentCreate(BaseModel):

    patient_id: int

    doctor_id: int

    appointment_date: date

    appointment_time: time

    notes: str | None = None




class AppointmentResponse(BaseModel):

    id: int

    patient_id: int

    doctor_id: int

    appointment_date: date

    appointment_time: time

    status: str

    notes: str | None = None

    created_at: datetime


    class Config:

        from_attributes = True
