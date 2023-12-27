import datetime
from storage import JSONStorage
from models import Account, Transaction, TransactionType, TransactionStatus


class CODE:
    positive = False
    def __init__(self, code, message):
        self.code = code
        self.message = message
        self.positive = self.code.startswith("1")

    def __str__(self):
        if self.positive:
            return f"INFO(code:{self.code}): {self.message}"
        else:
            return f"ERROR(code:{self.code}): {self.message}"
    def __repr__(self):
        return self.__str__()

    def __bool__(self):
        return self.positive


class Bank:
    SUCCESS = CODE("1-000", "Operation successful.")
    VALID_ACCOUNT = CODE("1-001", "This account is valid.")
    VALID_ACCOUNT_INFO = CODE("1-001", "The info provided are vaild.")
    ACCOUNT_EXISTS = CODE("1-002", "This account exists.")

    FAILED = CODE("0-000", "Operation failed.")
    NO_ACCOUNT = CODE("0-001", "This account does not exist.")
    NO_TARGET_ACCOUNT = CODE("0-004", "The target account does not exist.")
    INSUFFICIENT_BALANCE = CODE("0-003", "Insufficient balance. Please try again.")
    WRONG_PIN = CODE("0-004", "Wrong PIN. Please try again.")
    INVALID_CARD = CODE("0-005", "Invalid card number. Please try again.")
    DUPLICATE_ACCOUNT = CODE("0-007", "This account already exists.")
    INVALID_AMOUNT = CODE("0-008", "Invalid amount. Please try again.")
    INVALID_PIN = CODE("0-009", "Invalid PIN. the PIN must be 4 digits.")

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

            account, code = Bank._withdraw(account, amount)
            if code == Bank.SUCCESS:
                transaction.update_status(TransactionStatus.Successful)
            else:
                transaction.update_status(TransactionStatus.Failed)
            account.transactions.append(transaction)
            JSONStorage.save_account(account.model_dump())
            return code
        else:
            return Bank.NO_ACCOUNT

    def _withdraw(account, amount):
        if account.balance >= amount:
            account.balance -= amount
            return account, Bank.SUCCESS
        else:
            return account, Bank.INSUFFICIENT_BALANCE

    def deposit(account_number, amount):
        transaction_type = TransactionType.Deposit
        amount = int(amount)
        account = Bank._get_account(account_number)
        if isinstance(account, Account):
            last_transaction_id = Bank._last_transaction_id(account)
            transaction = Transaction(
                id=last_transaction_id + 1, type=transaction_type, amount=amount
            )
            account, code = Bank._deposit(account, amount)
            if code == Bank.SUCCESS:
                transaction.update_status(TransactionStatus.Successful)
            else:
                transaction.update_status(TransactionStatus.Failed)
            account.transactions.append(transaction)
            JSONStorage.save_account(account.model_dump())
            return code
        else:
            return Bank.NO_ACCOUNT

    def _deposit(account, amount):
        account.balance += amount
        return account, Bank.SUCCESS

    def balance_inquiry(account_number):
        transaction_type = TransactionType.Inquiry
        account = Bank._get_account(account_number)
        if isinstance(account, Account):
            last_transaction_id = Bank._last_transaction_id(account)
            transaction = Transaction(
                id=last_transaction_id + 1, type=transaction_type
            )
            balance = account.balance
            transaction.update_status(TransactionStatus.Successful)
            account.transactions.append(transaction)
            JSONStorage.save_account(account.model_dump())
            return balance, Bank.SUCCESS
        else:
            return Bank.NO_ACCOUNT

    def transfer(account_number, target_account_number, amount):
        transaction_type = TransactionType.Transfer
        amount = int(amount)

        account = Bank._get_account(account_number)

        if isinstance(account, Account):
            last_transaction_id = Bank._last_transaction_id(account)
            transaction = Transaction(
                id=last_transaction_id + 1, type=transaction_type, amount=amount, account_number=target_account_number
            )
            print(transaction)

            account, code = Bank._transfer(account, amount, target_account_number)
            if code == Bank.SUCCESS:
                transaction.update_status(TransactionStatus.Successful)
            else:
                transaction.update_status(TransactionStatus.Failed)
            account.transactions.append(transaction)
            JSONStorage.save_account(account.model_dump())
            return code
        else:
            return Bank.NO_ACCOUNT

    def _transfer(account, amount, target_account_number):
        target_account = Bank._get_account(target_account_number)
        if isinstance(target_account, Account):
            if account.balance >= amount:
                account.balance -= amount
                target_account.balance += amount
                JSONStorage.save_account(target_account.model_dump())
                return account, Bank.SUCCESS
            else:
                return account, Bank.INSUFFICIENT_BALANCE
        else:
            return account, Bank.NO_TARGET_ACCOUNT

    def change_PIN(account_number, old_PIN, new_PIN):
        account = Bank._get_account(account_number)
        if isinstance(account, Account):
            if account.PIN != old_PIN:
                return Bank.WRONG_PIN
            try:
                account.PIN = new_PIN
                Account.model_validate(account)
                JSONStorage.save_account(account.model_dump())
                return Bank.SUCCESS
            except ValueError as e:
                return Bank.INVALID_PIN
        else:
            return Bank.NO_ACCOUNT

    def history(account_number):
        account = Bank._get_account(account_number)
        if isinstance(account, Account):
            history_str = ""
            for transaction in account.transactions:
                history_str += str(transaction) + "\n"
            return history_str, Bank.SUCCESS
        else:
            return Bank.NO_ACCOUNT

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
