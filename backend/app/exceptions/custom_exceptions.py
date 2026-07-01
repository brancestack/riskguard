class TransactionNotFoundException(Exception):
    def __init__(self):
        super().__init__("Transaction not found")


class InvalidTransactionStatusException(Exception):
    def __init__(self):
        super().__init__("Invalid transaction status")


class UserAlreadyExistsException(Exception):
    def __init__(self):
        super().__init__("User already exists")


class InvalidCredentialsException(Exception):
    def __init__(self):
        super().__init__("Invalid email or password")