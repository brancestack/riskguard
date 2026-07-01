from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.api.dashboard import router as dashboard_router
from app.api.transactions import router as transactions_router
from app.core.config import settings
from app.core.database import Base, engine
from app.models.transaction import Transaction
from app.models.user import User
from app.exceptions.custom_exceptions import (
    InvalidCredentialsException,
    TransactionNotFoundException,
    UserAlreadyExistsException,
)
from app.exceptions.handlers import (
    bad_request_exception_handler,
    conflict_exception_handler,
    not_found_exception_handler,
    unauthorized_exception_handler,
)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    description="Fraud Risk Monitoring Platform",
    version=settings.APP_VERSION,
)

app.add_exception_handler(
    TransactionNotFoundException,
    not_found_exception_handler
)

app.add_exception_handler(
    UserAlreadyExistsException,
    conflict_exception_handler
)

app.add_exception_handler(
    InvalidCredentialsException,
    unauthorized_exception_handler
)

app.add_exception_handler(
    ValueError,
    bad_request_exception_handler
)

app.include_router(auth_router)
app.include_router(transactions_router)
app.include_router(dashboard_router)


@app.get("/")
def root():
    return {
        "message": f"{settings.APP_NAME} is running!",
        "version": settings.APP_VERSION
    }
