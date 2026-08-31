from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.database.connection import get_database

from app.core.dependencies import require_role

from app.models.user import User

from app.schemas.nurse import (
    NurseCreate,
    NurseResponse,
    NursingNoteCreate
)

from app.services.nurse_service import (
    create_nurse,
    get_nurse_by_user,
    create_nursing_note,
    get_nurse_notes
)



router = APIRouter(
    prefix="/nurse",
    tags=["Nurse"]
)





@router.get("/dashboard")
def nurse_dashboard(
    current_user: User = Depends(
        require_role("NURSE")
    )
):

    return {

        "success": True,

        "message": "Welcome Nurse",

        "username": current_user.username,

        "role": current_user.role

    }





@router.post(
    "/profile/create",
    response_model=NurseResponse
)
def create_profile(
    nurse: NurseCreate,
    db: Session = Depends(get_database),
    current_user: User = Depends(
        require_role("NURSE")
    )
):

    new_nurse, error = create_nurse(
        db,
        current_user.id,
        nurse
    )


    if error:

        raise HTTPException(
            status_code=400,
            detail=error
        )


    return new_nurse





@router.get(
    "/profile",
    response_model=NurseResponse
)
def get_profile(
    db: Session = Depends(get_database),
    current_user: User = Depends(
        require_role("NURSE")
    )
):

    nurse = get_nurse_by_user(
        db,
        current_user.id
    )


    if not nurse:

        raise HTTPException(
            status_code=404,
            detail="Nurse profile not found"
        )


    return nurse


@router.post("/notes")
def create_note(
    note_data: NursingNoteCreate,
    db: Session = Depends(get_database),
    current_user: User = Depends(
        require_role("NURSE")
    )
):

    note = create_nursing_note(
        db,
        current_user.id,
        note_data
    )

    return {
        "success": True,
        "message": "Nursing note created",
        "note": note
    }




@router.get("/notes")
def get_notes(
    db: Session = Depends(get_database),
    current_user: User = Depends(
        require_role("NURSE")
    )
):

    notes = get_nurse_notes(
        db,
        current_user.id
    )

    return {
        "success": True,
        "notes": notes
    }
