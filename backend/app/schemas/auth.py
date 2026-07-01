from pydantic import BaseModel, EmailStr, Field


class RegisterRequest(BaseModel):
    name: str = Field(..., example="Nicolas Castro")
    email: EmailStr = Field(..., example="nicolas@email.com")
    password: str = Field(..., min_length=6, example="123456")


class LoginRequest(BaseModel):
    email: EmailStr = Field(..., example="nicolas@email.com")
    password: str = Field(..., example="123456")


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    is_active: bool

    model_config = {
        "from_attributes": True
    }


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"