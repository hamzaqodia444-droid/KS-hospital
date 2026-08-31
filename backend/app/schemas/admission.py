from pydantic import BaseModel
from datetime import datetime



class AdmissionCreate(BaseModel):

    patient_id: int

    doctor_id: int

    room_number: str | None = None

    admission_reason: str





class DischargeUpdate(BaseModel):

    discharge_notes: str | None = None





class AdmissionResponse(BaseModel):

    id: int

    patient_id: int

    doctor_id: int

    room_number: str | None = None

    admission_reason: str

    status: str

    discharge_notes: str | None = None

    admitted_at: datetime

    discharged_at: datetime | None = None


    class Config:

        from_attributes = True
