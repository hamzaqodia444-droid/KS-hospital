from pydantic import BaseModel


class NurseCreate(BaseModel):

    department_id: int

    full_name: str

    license_number: str | None = None

    phone: str | None = None





class NurseResponse(BaseModel):

    id: int

    user_id: int

    department_id: int

    full_name: str

    license_number: str | None = None

    phone: str | None = None


    class Config:

        from_attributes = True


class NursingNoteCreate(BaseModel):

    patient_id: int

    note: str | None = None

    patient_status: str | None = None




class NursingNoteResponse(BaseModel):

    id: int

    patient_id: int

    nurse_id: int

    note: str | None = None

    patient_status: str | None = None


    class Config:

        from_attributes = True
