from pydantic import BaseModel


class DoctorCreate(BaseModel):

    department_id: int

    full_name: str

    specialization: str

    license_number: str

    phone: str | None = None





class DoctorResponse(BaseModel):

    id: int

    user_id: int

    department_id: int

    full_name: str

    specialization: str

    license_number: str

    phone: str | None = None


    class Config:

        from_attributes = True
