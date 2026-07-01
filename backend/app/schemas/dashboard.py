from pydantic import BaseModel


class DashboardSummaryResponse(BaseModel):
    total_transactions: int
    approved: int
    review: int
    blocked: int
    confirmed_fraud: int
    false_positive: int
    average_risk_score: float