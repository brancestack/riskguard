from app.schemas.transaction import TransactionCreate
from app.services.rules.base_rule import BaseRiskRule


class UnknownDeviceRule(BaseRiskRule):
    def evaluate(self, transaction: TransactionCreate) -> tuple[int, str | None]:
        if transaction.device.lower() == "unknown":
            return 25, "Unknown device"

        return 0, None