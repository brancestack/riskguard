from abc import ABC, abstractmethod
from app.schemas.transaction import TransactionCreate


class BaseRiskRule(ABC):
    @abstractmethod
    def evaluate(self, transaction: TransactionCreate) -> tuple[int, str | None]:
        pass