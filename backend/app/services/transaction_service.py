from datetime import datetime

from app.core.logging import logger
from app.exceptions.custom_exceptions import TransactionNotFoundException
from app.models.transaction import Transaction
from app.repositories.transaction_repository import TransactionRepository
from app.schemas.pagination import PaginatedResponse
from app.schemas.transaction import TransactionCreate, TransactionResponse
from app.schemas.transaction_review import TransactionReviewRequest
from app.services.risk_engine import RiskEngine


class TransactionService:
    def __init__(self, repository: TransactionRepository):
        self.repository = repository
        self.risk_engine = RiskEngine()

    def create_transaction(self, data: TransactionCreate) -> Transaction:
        risk_score, status, risk_reasons = self.risk_engine.analyze(data)

        transaction = Transaction(
            **data.model_dump(),
            risk_score=risk_score,
            risk_reasons=risk_reasons,
            status=status
        )

        created_transaction = self.repository.create(transaction)

        logger.info(
            f"Transaction created | id={created_transaction.id} | "
            f"score={created_transaction.risk_score} | status={created_transaction.status}"
        )

        if created_transaction.risk_score >= 70:
            logger.warning(
                f"High risk transaction detected | id={created_transaction.id} | "
                f"score={created_transaction.risk_score}"
            )

        return created_transaction

    def list_transactions(
        self,
        status: str | None = None,
        skip: int = 0,
        limit: int = 10
    ) -> PaginatedResponse[TransactionResponse]:

        transactions = self.repository.find_all(
            status=status,
            skip=skip,
            limit=limit
        )

        total = self.repository.count_all(status=status)

        return PaginatedResponse(
            items=transactions,
            total=total,
            skip=skip,
            limit=limit
        )

    def get_transaction_by_id(self, transaction_id: int) -> Transaction:
        transaction = self.repository.find_by_id(transaction_id)

        if transaction is None:
            logger.warning(f"Transaction not found | id={transaction_id}")
            raise TransactionNotFoundException()

        return transaction

    def review_transaction(
        self,
        transaction_id: int,
        data: TransactionReviewRequest
    ) -> Transaction:

        transaction = self.repository.find_by_id(transaction_id)

        if transaction is None:
            logger.warning(f"Transaction not found for review | id={transaction_id}")
            raise TransactionNotFoundException()

        transaction.status = data.status.value
        transaction.reviewer_note = data.reviewer_note
        transaction.reviewed_at = datetime.utcnow()

        reviewed_transaction = self.repository.update(transaction)

        logger.info(
            f"Transaction reviewed | id={reviewed_transaction.id} | "
            f"status={reviewed_transaction.status}"
        )

        return reviewed_transaction