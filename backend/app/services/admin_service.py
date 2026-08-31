from sqlalchemy.orm import Session

from app.models.user import User

from app.core.security import hash_password

from app.schemas.admin import CreateStaff





ALLOWED_ROLES = [
    "ADMIN",
    "DOCTOR",
    "NURSE",
    "PATIENT"
]





def create_staff(
    db: Session,
    staff_data: CreateStaff
):

    if staff_data.role not in ALLOWED_ROLES:

        return None, "Invalid role"



    existing_username = (
        db.query(User)
        .filter(
            User.username == staff_data.username
        )
        .first()
    )


    if existing_username:

        return None, "Username already exists"



    existing_email = (
        db.query(User)
        .filter(
            User.email == staff_data.email
        )
        .first()
    )


    if existing_email:

        return None, "Email already exists"




    user = User(

        username=staff_data.username,

        email=staff_data.email,

        password_hash=hash_password(
            staff_data.password
        ),

        role=staff_data.role,

        status="ACTIVE"

    )


    db.add(user)

    db.commit()

    db.refresh(user)


    return user, None
