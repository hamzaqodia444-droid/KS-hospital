from pydantic import BaseModel
from datetime import datetime


class LabTestCreate(BaseModel):

    patient_id: int

    doctor_id: int

    test_name: str

    result: str | None = None





class LabTestResponse(BaseModel):

    id: int

    patient_id: int

    doctor_id: int

    test_name: str

    result: str | None = None

    status: str

    created_at: datetime


    class Config:

        from_attributes = True


class LabTestUpdate(BaseModel):

    result: str
