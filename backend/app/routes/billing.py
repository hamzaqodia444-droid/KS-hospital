from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.database.connection import get_database

from app.core.dependencies import require_role

from app.models.user import User

from app.schemas.billing import (
    BillingCreate,
    BillingResponse,
    PaymentUpdate
)

from app.services.billing_service import (
    create_bill,
    update_payment,
    get_patient_bills,
    get_all_bills
)



router = APIRouter(
    prefix="/billing",
    tags=["Billing"]
)





@router.post(
    "/create",
    response_model=BillingResponse
)
def add_bill(
    bill: BillingCreate,
    db: Session = Depends(get_database),
    current_user: User = Depends(
        require_role("ADMIN")
    )
):

    return create_bill(
        db,
        bill
    )





@router.put(
    "/{bill_id}/payment",
    response_model=BillingResponse
)
def pay_bill(
    bill_id: int,
    data: PaymentUpdate,
    db: Session = Depends(get_database),
    current_user: User = Depends(
        require_role("ADMIN")
    )
):

    bill = update_payment(
        db,
        bill_id,
        data
    )


    if not bill:

        raise HTTPException(
            status_code=404,
            detail="Bill not found"
        )


    return bill





@router.get(
    "/patient/{patient_id}",
    response_model=list[BillingResponse]
)
def patient_bills(
    patient_id: int,
    db: Session = Depends(get_database),
    current_user: User = Depends(
        require_role("PATIENT")
    )
):

    return get_patient_bills(
        db,
        patient_id
    )





@router.get(
    "/list",
    response_model=list[BillingResponse]
)
def bills_list(
    db: Session = Depends(get_database),
    current_user: User = Depends(
        require_role("ADMIN")
    )
):

    return get_all_bills(
        db
    )
