from pydantic import BaseModel

from datetime import datetime





class MedicalRecordCreate(BaseModel):

    patient_id: int

    disease_name: str

    description: str | None = None

    causes: str | None = None

    severity: str | None = None





class MedicalRecordResponse(BaseModel):

    id: int

    patient_id: int

    doctor_id: int | None = None

    disease_name: str

    description: str | None = None

    causes: str | None = None

    severity: str | None = None

    created_at: datetime


    class Config:

        from_attributes = True


class MedicalRecordUpdate(BaseModel):

    disease_name: str | None = None

    description: str | None = None

    causes: str | None = None

    severity: str | None = None
