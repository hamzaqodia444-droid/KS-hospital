from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.database.connection import get_database

from app.core.dependencies import require_role

from app.models.user import User

from app.schemas.medical_record import (
    MedicalRecordCreate,
    MedicalRecordResponse,
    MedicalRecordUpdate
)

from app.services.medical_record_service import (
    create_medical_record,
    get_patient_records,
    get_doctor_records,
    update_medical_record
)



router = APIRouter(
    prefix="/medical-record",
    tags=["Medical Record"]
)





@router.post(
    "/create",
    response_model=MedicalRecordResponse
)
def create_record(
    record: MedicalRecordCreate,
    db: Session = Depends(get_database),
    current_user: User = Depends(
        require_role("DOCTOR")
    )
):

    new_record = create_medical_record(
        db,
        current_user.id,
        record
    )


    return new_record





@router.get(
    "/doctor",
    response_model=list[MedicalRecordResponse]
)
def doctor_records(
    db: Session = Depends(get_database),
    current_user: User = Depends(
        require_role("DOCTOR")
    )
):

    return get_doctor_records(
        db,
        current_user.id
    )





@router.get(
    "/patient/{patient_id}",
    response_model=list[MedicalRecordResponse]
)
def patient_records(
    patient_id: int,
    db: Session = Depends(get_database),
    current_user: User = Depends(
        require_role("PATIENT")
    )
):

    return get_patient_records(
        db,
        patient_id
    )


@router.put(
    "/{record_id}",
    response_model=MedicalRecordResponse
)
def update_record(
    record_id: int,
    update_data: MedicalRecordUpdate,
    db: Session = Depends(get_database),
    current_user: User = Depends(
        require_role("DOCTOR")
    )
):

    updated_record, error = update_medical_record(
        db,
        record_id,
        current_user.id,
        update_data
    )


    if error:
        raise HTTPException(
            status_code=404,
            detail=error
        )


    return updated_record


from app.schemas.medical_record import MedicalRecordUpdate

from app.services.medical_record_service import update_medical_record



@router.put(
    "/{record_id}",
    response_model=MedicalRecordResponse
)
def edit_record(
    record_id: int,
    update_data: MedicalRecordUpdate,
    db: Session = Depends(get_database),
    current_user: User = Depends(
        require_role("DOCTOR")
    )
):

    updated_record, error = update_medical_record(
        db,
        record_id,
        current_user.id,
        update_data
    )


    if error:

        from fastapi import HTTPException

        raise HTTPException(
            status_code=403,
            detail=error
        )


    return updated_record

