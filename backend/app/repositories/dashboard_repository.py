from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.transaction import Transaction


class DashboardRepository:
    def __init__(self, db: Session):
        self.db = db

    def count_transactions(self) -> int:
        return self.db.query(Transaction).count()

    def count_by_status(self, status: str) -> int:
        return (
            self.db
            .query(Transaction)
            .filter(Transaction.status == status)
            .count()
        )

    def get_average_risk_score(self) -> float:
        average = self.db.query(func.avg(Transaction.risk_score)).scalar()
        return round(average or 0, 2)

    def find_high_risk_transactions(self, limit: int = 10) -> list[Transaction]:
        return (
            self.db
            .query(Transaction)
            .filter(Transaction.risk_score >= 70)
            .order_by(Transaction.risk_score.desc())
            .limit(limit)
            .all()
        )