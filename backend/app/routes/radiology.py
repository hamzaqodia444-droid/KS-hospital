from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.database.connection import get_database

from app.core.dependencies import require_role

from app.models.user import User

from app.schemas.radiology import (
    RadiologyCreate,
    RadiologyResponse,
    RadiologyUpdate
)

from app.services.radiology_service import (
    create_radiology_test,
    update_radiology_result,
    get_patient_radiology_tests,
    get_doctor_radiology_tests
)



router = APIRouter(
    prefix="/radiology",
    tags=["Radiology"]
)





@router.post(
    "/create",
    response_model=RadiologyResponse
)
def add_radiology_test(
    radiology: RadiologyCreate,
    db: Session = Depends(get_database),
    current_user: User = Depends(
        require_role("DOCTOR")
    )
):

    return create_radiology_test(
        db,
        radiology
    )





@router.put(
    "/{radiology_id}/result",
    response_model=RadiologyResponse
)
def complete_radiology_test(
    radiology_id: int,
    data: RadiologyUpdate,
    db: Session = Depends(get_database),
    current_user: User = Depends(
        require_role("DOCTOR")
    )
):

    radiology = update_radiology_result(
        db,
        radiology_id,
        data
    )


    if not radiology:

        raise HTTPException(
            status_code=404,
            detail="Radiology test not found"
        )


    return radiology





@router.get(
    "/patient/{patient_id}",
    response_model=list[RadiologyResponse]
)
def patient_radiology_tests(
    patient_id: int,
    db: Session = Depends(get_database),
    current_user: User = Depends(
        require_role("PATIENT")
    )
):

    return get_patient_radiology_tests(
        db,
        patient_id
    )





@router.get(
    "/doctor/{doctor_id}",
    response_model=list[RadiologyResponse]
)
def doctor_radiology_tests(
    doctor_id: int,
    db: Session = Depends(get_database),
    current_user: User = Depends(
        require_role("DOCTOR")
    )
):

    return get_doctor_radiology_tests(
        db,
        doctor_id
    )
