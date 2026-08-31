from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.database.connection import get_database

from app.core.dependencies import require_role

from app.models.user import User

from app.schemas.patient import (
    PatientCreate,
    PatientResponse
)

from app.services.patient_service import (
    create_patient,
    get_patient_by_user
)



router = APIRouter(
    prefix="/patient",
    tags=["Patient"]
)





@router.get("/dashboard")
def patient_dashboard(
    current_user: User = Depends(
        require_role("PATIENT")
    )
):

    return {

        "success": True,

        "message": "Welcome Patient",

        "username": current_user.username,

        "role": current_user.role

    }





@router.post(
    "/profile/create",
    response_model=PatientResponse
)
def create_profile(
    patient: PatientCreate,
    db: Session = Depends(get_database),
    current_user: User = Depends(
        require_role("PATIENT")
    )
):

    new_patient, error = create_patient(
        db,
        current_user.id,
        patient
    )


    if error:

        raise HTTPException(
            status_code=400,
            detail=error
        )


    return new_patient





@router.get(
    "/profile",
    response_model=PatientResponse
)
def get_profile(
    db: Session = Depends(get_database),
    current_user: User = Depends(
        require_role("PATIENT")
    )
):

    patient = get_patient_by_user(
        db,
        current_user.id
    )


    if not patient:

        raise HTTPException(
            status_code=404,
            detail="Patient profile not found"
        )


    return patient
