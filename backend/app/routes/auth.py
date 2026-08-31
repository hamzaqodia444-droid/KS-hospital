from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_database
from app.schemas.user import UserCreate, UserLogin

from app.services.auth_service import (
    create_user,
    authenticate_user
)

from app.core.security import create_access_token



router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)



@router.post("/register")
def register(
    user: UserCreate,
    db: Session = Depends(get_database)
):

    new_user, error = create_user(
        db,
        user.username,
        user.email,
        user.password
    )


    if error:
        raise HTTPException(
            status_code=400,
            detail=error
        )


    return {
        "success": True,
        "message": "Account created successfully",
        "username": new_user.username
    }




@router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_database)
):

    authenticated_user, error = authenticate_user(
        db,
        user.username,
        user.password
    )


    if error:
        raise HTTPException(
            status_code=401,
            detail=error
        )


    token = create_access_token(
        {
            "sub": authenticated_user.username,
            "role": authenticated_user.role,
            "user_id": authenticated_user.id
        }
    )


    return {
        "success": True,
        "message": "Login successful",
        "access_token": token,
        "token_type": "bearer",
        "username": authenticated_user.username,
        "role": authenticated_user.role
    }
