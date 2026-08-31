from pydantic import BaseModel
from datetime import datetime



class BillingCreate(BaseModel):

    patient_id: int

    service_name: str

    amount: float





class PaymentUpdate(BaseModel):

    payment_status: str

    payment_method: str | None = None





class BillingResponse(BaseModel):

    id: int

    patient_id: int

    service_name: str

    amount: float

    payment_status: str

    payment_method: str | None = None

    created_at: datetime


    class Config:

        from_attributes = True
