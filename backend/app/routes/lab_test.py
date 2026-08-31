from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.database.connection import get_database

from app.core.dependencies import require_role

from app.models.user import User

from app.schemas.lab_test import (
    LabTestCreate,
    LabTestResponse,
    LabTestUpdate
)

from app.services.lab_test_service import (
    create_lab_test,
    update_lab_result,
    get_patient_lab_tests,
    get_doctor_lab_tests
)



router = APIRouter(
    prefix="/lab-test",
    tags=["Lab Test"]
)





@router.post(
    "/create",
    response_model=LabTestResponse
)
def add_lab_test(
    lab_test: LabTestCreate,
    db: Session = Depends(get_database),
    current_user: User = Depends(
        require_role("DOCTOR")
    )
):

    return create_lab_test(
        db,
        lab_test
    )





@router.put(
    "/{lab_id}/result",
    response_model=LabTestResponse
)
def complete_lab_test(
    lab_id: int,
    data: LabTestUpdate,
    db: Session = Depends(get_database),
    current_user: User = Depends(
        require_role("DOCTOR")
    )
):

    lab_test = update_lab_result(
        db,
        lab_id,
        data
    )


    if not lab_test:

        raise HTTPException(
            status_code=404,
            detail="Lab test not found"
        )


    return lab_test





@router.get(
    "/patient/{patient_id}",
    response_model=list[LabTestResponse]
)
def patient_lab_tests(
    patient_id: int,
    db: Session = Depends(get_database),
    current_user: User = Depends(
        require_role("PATIENT")
    )
):

    return get_patient_lab_tests(
        db,
        patient_id
    )





@router.get(
    "/doctor/{doctor_id}",
    response_model=list[LabTestResponse]
)
def doctor_lab_tests(
    doctor_id: int,
    db: Session = Depends(get_database),
    current_user: User = Depends(
        require_role("DOCTOR")
    )
):

    return get_doctor_lab_tests(
        db,
        doctor_id
    )
