from pydantic import BaseModel





class MedicineCreate(BaseModel):

    name: str

    description: str | None = None

    usage: str | None = None

    side_effects: str | None = None

    warnings: str | None = None





class MedicineResponse(BaseModel):

    id: int

    name: str

    description: str | None = None

    usage: str | None = None

    side_effects: str | None = None

    warnings: str | None = None


    class Config:

        from_attributes = True
