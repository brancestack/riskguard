from app.schemas.transaction import TransactionCreate
from app.services.rules.base_rule import BaseRiskRule


class ForeignCountryRule(BaseRiskRule):
    def evaluate(self, transaction: TransactionCreate) -> tuple[int, str | None]:
        if transaction.country.lower() != "brazil":
            return 30, "Transaction outside Brazil"

        return 0, None