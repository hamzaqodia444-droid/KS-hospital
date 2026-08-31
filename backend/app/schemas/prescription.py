from pydantic import BaseModel

from datetime import datetime





class PrescriptionCreate(BaseModel):

    patient_id: int

    medicine_id: int

    instructions: str | None = None





class PrescriptionResponse(BaseModel):

    id: int

    patient_id: int

    doctor_id: int

    medicine_id: int

    instructions: str | None = None

    created_at: datetime


    class Config:

        from_attributes = True
