from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.database.connection import get_database

from app.core.dependencies import require_role

from app.models.user import User

from app.schemas.department import (
    DepartmentCreate,
    DepartmentResponse
)

from app.services.department_service import (
    create_department,
    get_all_departments
)



router = APIRouter(
    prefix="/department",
    tags=["Department"]
)





@router.post(
    "/create",
    response_model=DepartmentResponse
)
def add_department(
    department: DepartmentCreate,
    db: Session = Depends(get_database),
    current_user: User = Depends(
        require_role("ADMIN")
    )
):

    new_department, error = create_department(
        db,
        department
    )


    if error:

        raise HTTPException(
            status_code=400,
            detail=error
        )


    return new_department





@router.get(
    "/list",
    response_model=list[DepartmentResponse]
)
def list_departments(
    db: Session = Depends(get_database),
    current_user: User = Depends(
        require_role("ADMIN")
    )
):

    return get_all_departments(db)
