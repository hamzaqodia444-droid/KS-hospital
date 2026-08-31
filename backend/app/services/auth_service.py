from sqlalchemy.orm import Session

from app.models.user import User
from app.core.security import hash_password, verify_password


def validate_password(password: str):

    if len(password) < 8:
        return False, "Password must contain at least 8 characters"

    if not any(c.isupper() for c in password):
        return False, "Password must contain an uppercase letter"

    if not any(c.isdigit() for c in password):
        return False, "Password must contain a number"

    return True, None



def create_user(
    db: Session,
    username: str,
    email: str,
    password: str
):

    existing_username = (
        db.query(User)
        .filter(User.username == username)
        .first()
    )

    if existing_username:
        return None, "Username already exists"


    existing_email = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    if existing_email:
        return None, "Email already exists"



    valid, error = validate_password(password)

    if not valid:
        return None, error



    user = User(
        username=username,
        email=email,
        password_hash=hash_password(password),
        role="PATIENT",
        status="ACTIVE"
    )


    db.add(user)
    db.commit()
    db.refresh(user)


    return user, None




def authenticate_user(
    db: Session,
    username: str,
    password: str
):

    user = (
        db.query(User)
        .filter(User.username == username)
        .first()
    )


    if not user:
        return None, "Account not found"



    if not verify_password(
        password,
        user.password_hash
    ):
        return None, "Incorrect password"



    return user, None
