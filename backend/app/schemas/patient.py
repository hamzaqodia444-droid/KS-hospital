from pydantic import BaseModel

from datetime import date



class PatientCreate(BaseModel):

    full_name: str

    birth_date: date | None = None

    birth_place: str | None = None

    gender: str | None = None

    age: int | None = None

    height: float | None = None

    weight: float | None = None

    blood_type: str | None = None





class PatientResponse(BaseModel):

    id: int

    user_id: int

    full_name: str

    birth_date: date | None = None

    birth_place: str | None = None

    gender: str | None = None

    age: int | None = None

    height: float | None = None

    weight: float | None = None

    blood_type: str | None = None


    class Config:

        from_attributes = True
