from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.database.connection import get_database

from app.core.dependencies import require_role

from app.models.user import User
from app.models.patient import Patient
from app.models.medical_record import MedicalRecord

from app.schemas.doctor import DoctorCreate, DoctorResponse

from app.services.doctor_service import (
    get_doctor_patients,
    create_doctor,
    get_doctor_by_user,
    get_full_patient_profile,
)



router = APIRouter(
    prefix="/doctor",
    tags=["Doctor"]
)





@router.get("/dashboard")
def doctor_dashboard(
    current_user: User = Depends(
        require_role("DOCTOR")
    )
):

    return {

        "success": True,

        "message": "Welcome Doctor",

        "username": current_user.username,

        "role": current_user.role

    }





@router.post(
    "/profile/create",
    response_model=DoctorResponse
)
def create_profile(
    doctor: DoctorCreate,
    db: Session = Depends(get_database),
    current_user: User = Depends(
        require_role("DOCTOR")
    )
):

    new_doctor, error = create_doctor(
        db,
        current_user.id,
        doctor
    )


    if error:

        raise HTTPException(
            status_code=400,
            detail=error
        )


    return new_doctor





@router.get(
    "/profile",
    response_model=DoctorResponse
)
def get_profile(
    db: Session = Depends(get_database),
    current_user: User = Depends(
        require_role("DOCTOR")
    )
):

    doctor = get_doctor_by_user(
        db,
        current_user.id
    )


    if not doctor:

        raise HTTPException(
            status_code=404,
            detail="Doctor profile not found"
        )


    return doctor


@router.get("/patients")
def get_my_patients(
    db: Session = Depends(get_database),
    current_user: User = Depends(
        require_role("DOCTOR")
    )
):

    patients = (
        db.query(Patient)
        .join(
            MedicalRecord,
            MedicalRecord.patient_id == Patient.id
        )
        .filter(
            MedicalRecord.doctor_id == current_user.id
        )
        .distinct()
        .all()
    )


    return {

        "success": True,

        "patients": patients

    }



@router.get("/patients")
def my_patients(
    db: Session = Depends(get_database),
    current_user: User = Depends(
        require_role("DOCTOR")
    )
):

    patients = get_doctor_patients(
        db,
        current_user.id
    )


    return {

        "success": True,

        "patients": patients

    }



@router.get("/patient/{patient_id}/full-profile")
def full_patient_profile(
    patient_id: int,
    db: Session = Depends(get_database),
    current_user: User = Depends(
        require_role("DOCTOR")
    )
):

    profile = get_full_patient_profile(
        db,
        patient_id,
        current_user.id
    )


    if not profile:

        raise HTTPException(
            status_code=404,
            detail="Patient profile not found"
        )


    return {

        "success": True,

        "profile": profile

    }

