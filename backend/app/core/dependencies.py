from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.database import get_db
from app.exceptions.custom_exceptions import InvalidCredentialsException
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.token import TokenPayload

bearer_scheme = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    db: Session = Depends(get_db)
) -> User:
    token = credentials.credentials

    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=["HS256"]
        )

        token_data = TokenPayload(sub=payload.get("sub"))

    except JWTError:
        raise InvalidCredentialsException()

    user_repository = UserRepository(db)
    user = user_repository.find_by_id(int(token_data.sub))

    if user is None:
        raise InvalidCredentialsException()

    return user