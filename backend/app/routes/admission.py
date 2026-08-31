from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.database.connection import get_database

from app.core.dependencies import require_role

from app.models.user import User

from app.schemas.admission import (
    AdmissionCreate,
    AdmissionResponse,
    DischargeUpdate
)

from app.services.admission_service import (
    create_admission,
    discharge_patient,
    get_patient_admissions,
    get_doctor_admissions
)



router = APIRouter(
    prefix="/admission",
    tags=["Admission"]
)





@router.post(
    "/create",
    response_model=AdmissionResponse
)
def add_admission(
    admission: AdmissionCreate,
    db: Session = Depends(get_database),
    current_user: User = Depends(
        require_role("DOCTOR")
    )
):

    return create_admission(
        db,
        admission
    )





@router.put(
    "/{admission_id}/discharge",
    response_model=AdmissionResponse
)
def discharge(
    admission_id: int,
    data: DischargeUpdate,
    db: Session = Depends(get_database),
    current_user: User = Depends(
        require_role("DOCTOR")
    )
):

    admission = discharge_patient(
        db,
        admission_id,
        data
    )


    if not admission:

        raise HTTPException(
            status_code=404,
            detail="Admission not found"
        )


    return admission





@router.get(
    "/patient/{patient_id}",
    response_model=list[AdmissionResponse]
)
def patient_admissions(
    patient_id: int,
    db: Session = Depends(get_database),
    current_user: User = Depends(
        require_role("PATIENT")
    )
):

    return get_patient_admissions(
        db,
        patient_id
    )





@router.get(
    "/doctor/{doctor_id}",
    response_model=list[AdmissionResponse]
)
def doctor_admissions(
    doctor_id: int,
    db: Session = Depends(get_database),
    current_user: User = Depends(
        require_role("DOCTOR")
    )
):

    return get_doctor_admissions(
        db,
        doctor_id
    )
