from pydantic import BaseModel
from datetime import datetime



class RadiologyCreate(BaseModel):

    patient_id: int

    doctor_id: int

    test_type: str





class RadiologyUpdate(BaseModel):

    result: str





class RadiologyResponse(BaseModel):

    id: int

    patient_id: int

    doctor_id: int

    test_type: str

    status: str

    result: str | None = None

    created_at: datetime


    class Config:

        from_attributes = True
