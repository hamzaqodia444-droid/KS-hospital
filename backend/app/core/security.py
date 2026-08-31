from passlib.context import CryptContext

from jose import jwt, JWTError

from datetime import datetime, timedelta



SECRET_KEY = "HHH_SECRET_KEY_CHANGE_LATER"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 60



password_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)




def hash_password(password):

    return password_context.hash(password)





def verify_password(
    plain_password,
    hashed_password
):

    return password_context.verify(
        plain_password,
        hashed_password
    )





def create_token(username: str):

    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )


    payload = {

        "sub": username,

        "exp": expire

    }


    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )





def verify_token(token: str):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload


    except JWTError:

        return None


def create_access_token(data: dict):

    to_encode = data.copy()


    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )


    to_encode.update({
        "exp": expire
    })


    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
