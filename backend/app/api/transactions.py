from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.dependencies import get_current_user
from app.core.enums import TransactionStatus
from app.models.user import User
from app.repositories.transaction_repository import TransactionRepository
from app.schemas.pagination import PaginatedResponse
from app.schemas.transaction import TransactionCreate, TransactionResponse
from app.schemas.transaction_review import TransactionReviewRequest
from app.services.transaction_service import TransactionService

router = APIRouter(prefix="/transactions", tags=["Transactions"])


def get_transaction_service(db: Session = Depends(get_db)) -> TransactionService:
    repository = TransactionRepository(db)
    return TransactionService(repository)


@router.post("/", response_model=TransactionResponse)
def create_transaction(
    data: TransactionCreate,
    current_user: User = Depends(get_current_user),
    service: TransactionService = Depends(get_transaction_service)
):
    return service.create_transaction(data)


@router.get("/", response_model=PaginatedResponse[TransactionResponse])
def list_transactions(
    status: TransactionStatus | None = Query(default=None),
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=10, ge=1, le=50),
    current_user: User = Depends(get_current_user),
    service: TransactionService = Depends(get_transaction_service)
):
    return service.list_transactions(
        status=status.value if status else None,
        skip=skip,
        limit=limit
    )


@router.get("/{transaction_id}", response_model=TransactionResponse)
def get_transaction_by_id(
    transaction_id: int,
    current_user: User = Depends(get_current_user),
    service: TransactionService = Depends(get_transaction_service)
):
    return service.get_transaction_by_id(transaction_id)


@router.patch("/{transaction_id}/review", response_model=TransactionResponse)
def review_transaction(
    transaction_id: int,
    data: TransactionReviewRequest,
    current_user: User = Depends(get_current_user),
    service: TransactionService = Depends(get_transaction_service)
):
    return service.review_transaction(transaction_id, data)