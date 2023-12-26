import datetime
from storage import JSONStorage
from models import Account, Transaction, TransactionType, TransactionStatus


class CODE:
    def __init__(self, code, message):
        self.code = code
        self.message = message

    def __str__(self):
        if self.code.startswith("1"):
            return f"INFO({self.code}): {self.message}"
        elif self.code.startswith("0"):
            return f"ERROR({self.code}): {self.message}"
        else:
            return f"UNKNOWN({self.code}): {self.message}"
    def __repr__(self):
        return self.__str__()


class Bank:
    SUCCESS = CODE("1-000", "Transaction successful.")
    VALID_ACCOUNT = CODE("1-001", "This account is valid.")
    VALID_ACCOUNT_INFO = CODE("1-001", "The info provided are vaild.")
    ACCOUNT_EXISTS = CODE("1-002", "This account exists.")

    FAILED = CODE("0-000", "Transaction failed.")
    NO_ACCOUNT = CODE("0-001", "This account does not exist.")
    INSUFFICIENT_BALANCE = CODE("0-002", "Insufficient balance. Please try again.")
    INVALID_AMOUNT = CODE("0-003", "Invalid amount. Please try again.")
    WRONG_PIN = CODE("0-004", "Wrong PIN. Please try again.")
    INVALID_CARD = CODE("0-005", "Invalid card number. Please try again.")
    DUPLICATE_ACCOUNT = CODE("0-007", "This account already exists.")

    @staticmethod
    def print_receipt(account_number):
        account = Bank._get_account(account_number)
        if isinstance(account, Account):
            transaction = account.transactions[-1]
            print(transaction.generate_receipt(account))
            return Bank.SUCCESS
        return Bank.NO_ACCOUNT

    @staticmethod
    def withdraw(account_number, amount):
        transaction_type = TransactionType.Withdraw
        amount = int(amount)

        account = Bank._get_account(account_number)

        if isinstance(account, Account):
            last_transaction_id = Bank._last_transaction_id(account)
            transaction = Transaction(
                id=last_transaction_id + 1, type=transaction_type, amount=amount
            )
            if account.balance >= amount:
                account.balance -= amount
                transaction.update_status(TransactionStatus.Successful)
                account.transactions.append(transaction)
                JSONStorage.save_account(account.model_dump())
                return Bank.SUCCESS
            transaction.update_status(Transaction.FAILED)
            account.transactions.append(transaction)
            JSONStorage.save_account(account.model_dump())
            return Bank.INSUFFICIENT_BALANCE
        else:
            return Bank.NO_ACCOUNT

    def deposit(account, amount):
        pass

    def balance_inquiry(account):
        pass

    def transfer(account, amount, target_account):
        pass

    def change_PIN(account, new_PIN):
        pass

    def history(account):
        pass

    @staticmethod
    def _save_transaction(transaction, account):
        account.transactions.append(transaction)
        JSONStorage.save_account(account.model_dump())

    @staticmethod
    def _last_transaction_id(account):
        try:
            return account.transactions[-1].id
        except IndexError:
            return 0

    @staticmethod
    def _account_exists(account: Account):
        account = JSONStorage.get_account(account.number)
        if account:
            return Bank.ACCOUNT_EXISTS
        return Bank.NO_ACCOUNT

    @staticmethod
    def _get_account(account_number):
        account = JSONStorage.get_account(account_number)
        if account:
            try:
                account = Account(**account)
                return account
            except ValueError as e:
                print(e)
                return Bank.INVALID_ACCOUNT
        else:
            return Bank.NO_ACCOUNT


class SAFE:
    DEFAULT_NOTES = {20: 100, 50: 100, 100: 100, 200: 100}
    NOTES = DEFAULT_NOTES.copy()

    @staticmethod
    def withdraw_note(note, amount):
        if note in SAFE.NOTES:
            if SAFE.NOTES[note] >= amount:
                SAFE.NOTES[note] -= amount
                return True
        return False

    @staticmethod
    def deposit_note(note, amount):
        if note in SAFE.NOTES:
            SAFE.NOTES[note] += amount
            return True
        return False

    @staticmethod
    @property
    def balance():
        for note, count in SAFE.NOTES.items():
            print(f"{note} EGP notes: {count}")


# class Account:
#     def __init__(self, name, balance, card, PIN):
#         self.name = name
#         self.balance = balance
#         self.card = card
#         self.PIN = PIN

#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#             return True
#         return False

#     def change_PIN(self, new_PIN):
#         self.PIN = new_PIN

#     def validate(self, card, PIN):
#         if self.card == card and self.PIN == PIN:
#             return True
#         return False


# class Printer:
#     @staticmethod
#     def print_receipt(account, amount, transaction_type):
#         print(f"Account Name: {account.name}")
#         print(f"Account Balance: {account.balance}")
#         print(f"Transaction Type: {transaction_type}")
#         print(f"Transaction Amount: {amount}")
#         print(f"New Balance: {account.balance}")
#         print(f"Time: {datetime.now()}")


# class Transaction:
#     types = ["Withdraw", "Deposit"]
#     statuses = ["Success", "Failed", "Cancelled", "Pending"]

#     def __init__(self, account, amount, transaction_type, status="Pending"):
#         self.account = account
#         self.amount = amount
#         self.transaction_type = transaction_type
#         self.transaction_time = datetime.now()
#         self.status = status


# class ATM:
#     banks = {}
