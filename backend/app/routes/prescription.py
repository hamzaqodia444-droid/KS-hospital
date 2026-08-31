from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database.connection import get_database

from app.core.dependencies import require_role

from app.models.user import User

from app.schemas.prescription import (
    PrescriptionCreate,
    PrescriptionResponse
)

from app.services.prescription_service import (
    create_prescription,
    get_patient_prescriptions,
    get_doctor_prescriptions
)



router = APIRouter(
    prefix="/prescription",
    tags=["Prescription"]
)





@router.post(
    "/create",
    response_model=PrescriptionResponse
)
def add_prescription(
    prescription: PrescriptionCreate,
    db: Session = Depends(get_database),
    current_user: User = Depends(
        require_role("DOCTOR")
    )
):

    return create_prescription(
        db,
        current_user.id,
        prescription
    )





@router.get(
    "/doctor",
    response_model=list[PrescriptionResponse]
)
def doctor_prescriptions(
    db: Session = Depends(get_database),
    current_user: User = Depends(
        require_role("DOCTOR")
    )
):

    return get_doctor_prescriptions(
        db,
        current_user.id
    )





@router.get(
    "/patient/{patient_id}",
    response_model=list[PrescriptionResponse]
)
def patient_prescriptions(
    patient_id: int,
    db: Session = Depends(get_database),
    current_user: User = Depends(
        require_role("PATIENT")
    )
):

    return get_patient_prescriptions(
        db,
        patient_id
    )
