from sqlalchemy.orm import Session

from app.models.transaction import Transaction


class TransactionRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, transaction: Transaction) -> Transaction:
        self.db.add(transaction)
        self.db.commit()
        self.db.refresh(transaction)
        return transaction

    def update(self, transaction: Transaction) -> Transaction:
        self.db.commit()
        self.db.refresh(transaction)
        return transaction

    def count_all(self, status: str | None = None) -> int:
        query = self.db.query(Transaction)

        if status:
            query = query.filter(Transaction.status == status)

        return query.count()

    def find_all(
        self,
        status: str | None = None,
        skip: int = 0,
        limit: int = 10
    ) -> list[Transaction]:
        query = self.db.query(Transaction)

        if status:
            query = query.filter(Transaction.status == status)

        return (
            query
            .order_by(Transaction.created_at.desc())
            .offset(skip)
            .limit(limit)
            .all()
        )

    def find_by_id(self, transaction_id: int) -> Transaction | None:
        return (
            self.db
            .query(Transaction)
            .filter(Transaction.id == transaction_id)
            .first()
        )