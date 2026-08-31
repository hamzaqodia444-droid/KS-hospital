from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database.connection import get_database

from app.core.dependencies import require_role

from app.models.user import User

from app.schemas.appointment import (
    AppointmentCreate,
    AppointmentResponse
)

from app.services.appointment_service import (
    create_appointment,
    get_patient_appointments,
    get_doctor_appointments
)



router = APIRouter(
    prefix="/appointment",
    tags=["Appointment"]
)





@router.post(
    "/create",
    response_model=AppointmentResponse
)
def add_appointment(
    appointment: AppointmentCreate,
    db: Session = Depends(get_database),
    current_user: User = Depends(
        require_role("DOCTOR")
    )
):

    return create_appointment(
        db,
        appointment
    )





@router.get(
    "/doctor/{doctor_id}",
    response_model=list[AppointmentResponse]
)
def doctor_appointments(
    doctor_id: int,
    db: Session = Depends(get_database),
    current_user: User = Depends(
        require_role("DOCTOR")
    )
):

    return get_doctor_appointments(
        db,
        doctor_id
    )





@router.get(
    "/patient/{patient_id}",
    response_model=list[AppointmentResponse]
)
def patient_appointments(
    patient_id: int,
    db: Session = Depends(get_database),
    current_user: User = Depends(
        require_role("PATIENT")
    )
):

    return get_patient_appointments(
        db,
        patient_id
    )
