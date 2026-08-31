from pydantic import BaseModel





class CreateStaff(BaseModel):

    username: str

    email: str

    password: str

    role: str
