from app.core.security import create_access_token, hash_password, verify_password
from app.exceptions.custom_exceptions import InvalidCredentialsException, UserAlreadyExistsException
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.auth import LoginRequest, RegisterRequest


class AuthService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def register(self, data: RegisterRequest) -> User:
        existing_user = self.repository.find_by_email(data.email)

        if existing_user:
            raise UserAlreadyExistsException()

        user = User(
            name=data.name,
            email=data.email,
            hashed_password=hash_password(data.password)
        )

        return self.repository.create(user)

    def login(self, data: LoginRequest) -> str:
        user = self.repository.find_by_email(data.email)

        if user is None:
            raise InvalidCredentialsException()

        if not verify_password(data.password, user.hashed_password):
            raise InvalidCredentialsException()

        return create_access_token(subject=str(user.id))