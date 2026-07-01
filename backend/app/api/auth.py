from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.dependencies import get_current_user
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.auth import (
    LoginRequest,
    RegisterRequest,
    TokenResponse,
    UserResponse,
)
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Authentication"])


def get_auth_service(db: Session = Depends(get_db)) -> AuthService:
    repository = UserRepository(db)
    return AuthService(repository)


@router.post("/register", response_model=UserResponse, status_code=201)
def register(
    data: RegisterRequest,
    service: AuthService = Depends(get_auth_service),
):
    return service.register(data)


@router.post("/login", response_model=TokenResponse)
def login(
    data: LoginRequest,
    service: AuthService = Depends(get_auth_service),
):
    token = service.login(data)

    return TokenResponse(
        access_token=token
    )


@router.get("/me", response_model=UserResponse)
def me(
    current_user: User = Depends(get_current_user)
):
    return current_user