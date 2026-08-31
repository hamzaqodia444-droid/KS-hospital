from sqlalchemy.orm import Session

from app.models.billing import Billing

from app.schemas.billing import (
    BillingCreate,
    PaymentUpdate
)





def create_bill(
    db: Session,
    billing_data: BillingCreate
):

    bill = Billing(

        patient_id=billing_data.patient_id,

        service_name=billing_data.service_name,

        amount=billing_data.amount

    )


    db.add(bill)

    db.commit()

    db.refresh(bill)


    return bill





def update_payment(
    db: Session,
    bill_id: int,
    payment_data: PaymentUpdate
):

    bill = (
        db.query(Billing)
        .filter(
            Billing.id == bill_id
        )
        .first()
    )


    if not bill:

        return None


    bill.payment_status = (
        payment_data.payment_status
    )

    bill.payment_method = (
        payment_data.payment_method
    )


    db.commit()

    db.refresh(bill)


    return bill





def get_patient_bills(
    db: Session,
    patient_id: int
):

    return (
        db.query(Billing)
        .filter(
            Billing.patient_id == patient_id
        )
        .all()
    )





def get_all_bills(
    db: Session
):

    return (
        db.query(Billing)
        .all()
    )
