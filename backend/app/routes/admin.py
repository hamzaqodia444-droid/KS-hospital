from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.database.connection import get_database

from app.core.dependencies import require_role

from app.models.user import User

from app.schemas.admin import CreateStaff

from app.services.admin_service import create_staff



router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)





@router.get("/dashboard")
def admin_dashboard(
    current_user: User = Depends(
        require_role("ADMIN")
    )
):

    return {

        "success": True,

        "message": "Welcome Administrator",

        "username": current_user.username,

        "role": current_user.role

    }





@router.post("/create-staff")
def create_staff_account(
    staff: CreateStaff,
    db: Session = Depends(get_database),
    current_user: User = Depends(
        require_role("ADMIN")
    )
):

    user, error = create_staff(
        db,
        staff
    )


    if error:

        raise HTTPException(
            status_code=400,
            detail=error
        )


    return {

        "success": True,

        "message": "Staff account created",

        "username": user.username,

        "role": user.role

    }


@router.get("/statistics")
def admin_statistics(
    db: Session = Depends(get_database),
    current_user: User = Depends(
        require_role("ADMIN")
    )
):

    from app.models.patient import Patient
    from app.models.doctor import Doctor
    from app.models.nurse import Nurse

    return {

        "success": True,

        "statistics": {

            "users": db.query(User).count(),

            "patients": db.query(Patient).count(),

            "doctors": db.query(Doctor).count(),

            "nurses": db.query(Nurse).count()

        }

    }


@router.post("/assign-doctor/{doctor_id}/{patient_id}")
def assign_doctor_patient(
    doctor_id: int,
    patient_id: int,
    db: Session = Depends(get_database),
    current_user: User = Depends(
        require_role("ADMIN")
    )
):

    from app.services.doctor_patient_service import assign_patient

    result, error = assign_patient(
        db,
        doctor_id,
        patient_id
    )

    if error:
        raise HTTPException(
            status_code=400,
            detail=error
        )

    return {
        "success": True,
        "message": "Doctor assigned to patient"
    }
