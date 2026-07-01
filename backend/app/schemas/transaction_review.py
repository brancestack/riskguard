from pydantic import BaseModel, Field

from app.core.enums import TransactionStatus


class TransactionReviewRequest(BaseModel):
    status: TransactionStatus = Field(..., example=TransactionStatus.CONFIRMED_FRAUD)
    reviewer_note: str = Field(..., example="Customer confirmed this transaction was fraudulent.")