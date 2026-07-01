from app.schemas.transaction import TransactionCreate
from app.services.rules.high_amount_rule import HighAmountRule
from app.services.rules.foreign_country_rule import ForeignCountryRule
from app.services.rules.unknown_device_rule import UnknownDeviceRule
from app.services.rules.night_transaction_rule import NightTransactionRule


class RiskEngine:
    def __init__(self):
        self.rules = [
            HighAmountRule(),
            ForeignCountryRule(),
            UnknownDeviceRule(),
            NightTransactionRule(),
        ]

    def analyze(self, transaction: TransactionCreate) -> tuple[int, str, str]:
        score = 0
        reasons = []

        for rule in self.rules:
            points, reason = rule.evaluate(transaction)
            score += points

            if reason:
                reasons.append(reason)

        if score >= 70:
            status = "BLOCKED"
        elif score >= 40:
            status = "REVIEW"
        else:
            status = "APPROVED"

        return score, status, "; ".join(reasons)