from pydantic import BaseModel, Field
from datetime import datetime

from app.core.enums import TransactionStatus


class TransactionCreate(BaseModel):
    customer_name: str = Field(..., example="Nicolas Castro")
    amount: float = Field(..., example=15000)
    transaction_type: str = Field(..., example="PIX")
    country: str = Field(..., example="Argentina")
    device: str = Field(..., example="unknown")
    ip_address: str = Field(..., example="192.168.0.10")


class TransactionResponse(TransactionCreate):
    id: int
    risk_score: int
    risk_reasons: str
    status: TransactionStatus
    reviewer_note: str | None
    reviewed_at: datetime | None
    created_at: datetime

    model_config = {
        "from_attributes": True
    }