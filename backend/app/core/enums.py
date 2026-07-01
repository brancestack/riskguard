from enum import Enum


class TransactionStatus(str, Enum):
    APPROVED = "APPROVED"
    REVIEW = "REVIEW"
    BLOCKED = "BLOCKED"
    CONFIRMED_FRAUD = "CONFIRMED_FRAUD"
    FALSE_POSITIVE = "FALSE_POSITIVE"