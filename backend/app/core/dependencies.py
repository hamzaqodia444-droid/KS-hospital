from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.orm import Session

from app.database.connection import get_database
from app.core.security import verify_token

from app.models.user import User



oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)




def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_database)
):

    payload = verify_token(token)


    if not payload:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication token"
        )


    username = payload.get("sub")


    if not username:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token data"
        )


    user = (
        db.query(User)
        .filter(User.username == username)
        .first()
    )


    if not user:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )


    return user





def require_role(required_role: str):

    def role_checker(
        current_user: User = Depends(get_current_user)
    ):


        if current_user.role != required_role:

            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Access denied"
            )


        return current_user


    return role_checker
