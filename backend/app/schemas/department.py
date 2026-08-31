from pydantic import BaseModel


class DepartmentCreate(BaseModel):

    name: str

    description: str | None = None




class DepartmentResponse(BaseModel):

    id: int

    name: str

    description: str | None = None


    class Config:

        from_attributes = True
