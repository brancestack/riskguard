from app.repositories.dashboard_repository import DashboardRepository
from app.models.transaction import Transaction


class DashboardService:
    def __init__(self, repository: DashboardRepository):
        self.repository = repository

    def get_summary(self) -> dict:
        return {
            "total_transactions": self.repository.count_transactions(),
            "approved": self.repository.count_by_status("APPROVED"),
            "review": self.repository.count_by_status("REVIEW"),
            "blocked": self.repository.count_by_status("BLOCKED"),
            "confirmed_fraud": self.repository.count_by_status("CONFIRMED_FRAUD"),
            "false_positive": self.repository.count_by_status("FALSE_POSITIVE"),
            "average_risk_score": self.repository.get_average_risk_score()
        }

    def get_high_risk_transactions(self, limit: int = 10) -> list[Transaction]:
        return self.repository.find_high_risk_transactions(limit=limit)