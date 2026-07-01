from datetime import datetime

from app.schemas.transaction import TransactionCreate
from app.services.rules.base_rule import BaseRiskRule


class NightTransactionRule(BaseRiskRule):
    def evaluate(self, transaction: TransactionCreate) -> tuple[int, str | None]:
        current_hour = datetime.utcnow().hour

        if 0 <= current_hour <= 5:
            return 20, "Transaction performed during late night hours"

        return 0, None