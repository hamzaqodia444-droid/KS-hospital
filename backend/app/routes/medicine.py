from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.database.connection import get_database

from app.core.dependencies import require_role

from app.models.user import User

from app.schemas.medicine import (
    MedicineCreate,
    MedicineResponse
)

from app.services.medicine_service import (
    create_medicine,
    get_all_medicines
)



router = APIRouter(
    prefix="/medicine",
    tags=["Medicine"]
)





@router.post(
    "/create",
    response_model=MedicineResponse
)
def add_medicine(
    medicine: MedicineCreate,
    db: Session = Depends(get_database),
    current_user: User = Depends(
        require_role("ADMIN")
    )
):

    new_medicine, error = create_medicine(
        db,
        medicine
    )


    if error:

        raise HTTPException(
            status_code=400,
            detail=error
        )


    return new_medicine





@router.get(
    "/list",
    response_model=list[MedicineResponse]
)
def list_medicines(
    db: Session = Depends(get_database),
    current_user: User = Depends(
        require_role("DOCTOR")
    )
):

    return get_all_medicines(db)
