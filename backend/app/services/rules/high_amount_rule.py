from app.schemas.transaction import TransactionCreate
from app.services.rules.base_rule import BaseRiskRule


class HighAmountRule(BaseRiskRule):
    def evaluate(self, transaction: TransactionCreate) -> tuple[int, str | None]:
        if transaction.amount >= 10000:
            return 35, "High amount transaction"

        return 0, None