import datetime

class CODE:
    def __init__(self, code, message):
        self.code = code
        self.message = message

class Bank:

    SUCCESS = CODE('1-000', "Transaction successful.")
    VALID_ACCOUNT = CODE('1-001', "This account is valid.")
    ACCOUNT_EXISTS = CODE('1-002', "This account exists.")


    FAILED = CODE('0-000', "Transaction failed.")
    NO_ACCOUNT = CODE('0-001', "This account does not exist.")
    INSUFFICIENT_BALANCE = CODE('0-002', "Insufficient balance. Please try again.")
    INVALID_AMOUNT = CODE('0-003', "Invalid amount. Please try again.")
    WRONG_PIN = CODE('0-004', "Wrong PIN. Please try again.")
    INVALID_CARD = CODE('0-005', "Invalid card number. Please try again.")
    DIFFERENT_BANK = CODE('0-006', "This card is not issued by this bank.")
    DUPLICATE_ACCOUNT = CODE('0-007', "This account already exists.")



    def __init__(self, name, prefix, accounts):
        self.name = name
        self.prefix = prefix
        self.accounts = accounts

    def account_exists(self, account):
        for acc in self.accounts:
            if acc.card == account.card:
                return Bank.ACCOUNT_EXISTS
        return Bank.NO_ACCOUNT

    def validate_account_info(self, account):
        if not account.card.startswith(self.prefix):
            return Bank.DIFFERENT_BANK
        if len(account.card) != 16:
            return Bank.INVALID_CARD
        return Bank.VALID_ACCOUNT

    def validate_account(self, account):
        if not self.account_exists(account):
            return Bank.NO_ACCOUNT
        info = self.validate_account_info(account)
        if not info == Bank.VALID_ACCOUNT:
            return info
        return Bank.VALID_ACCOUNT

    def validate(self, account):
        code = self.validate_account(account)
        valid = code == Bank.VALID_ACCOUNT
        return valid, code.message

    def add_account(self, account):
        account_exists = self.account_exists(account)
        if account_exists == Bank.ACCOUNT_EXISTS:
            return False, account_exists.message

        info = self.validate_account_info(account)

        if code == Bank.VALID_ACCOUNT:
            self.accounts.append(account)
            return Bank.SUCCESS, code.message
        return False, code.message

    def remove_account(self, account):
        code = self.validate_account(account)
        if code == Bank.VALID_ACCOUNT:
            self.accounts.remove(account)
            return True, code.message
        return False, code.message

    def get_account(self, card, PIN):
        for account in self.accounts:
            if account.validate(card, PIN):
                return account, Bank.SUCCESS.message
        return False, Bank.NO_ACCOUNT.message

    def withdraw(self, account, amount):
        code = self.validate_account(account)
        if not code == Bank.VALID_ACCOUNT:
            return False, code.message
        if account.withdraw(amount):
            return True, Bank.SUCCESS.message
        return False, Bank.INSUFFICIENT_BALANCE.message

    def deposit(self, account, amount):
        code = self.validate_account(account)
        if not code == Bank.VALID_ACCOUNT:
            return False, code.message
        account.deposit(amount)
        return True, Bank.SUCCESS.message

    def change_PIN(self, account, new_PIN):
        account.change_PIN(new_PIN)
        return True

    def transfer(self, account, amount, target_account):
        if self.withdraw(account, amount):
            self.deposit(target_account, amount)
            return True
        return False

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

class Account:
    def __init__(self, name, balance, card, PIN):
        self.name = name
        self.balance = balance
        self.card = card
        self.PIN = PIN

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

    def change_PIN(self, new_PIN):
        self.PIN = new_PIN

    def validate(self, card, PIN):
        if self.card == card and self.PIN == PIN:
            return True
        return False


class Printer:
    @staticmethod
    def print_receipt(account, amount, transaction_type):
        print(f"Account Name: {account.name}")
        print(f"Account Balance: {account.balance}")
        print(f"Transaction Type: {transaction_type}")
        print(f"Transaction Amount: {amount}")
        print(f"New Balance: {account.balance}")
        print(f"Time: {datetime.now()}")


class Transaction:
    types = ["Withdraw", "Deposit"]
    statuses = ["Success", "Failed", "Cancelled", "Pending"]
    def __init__(self, account, amount, transaction_type, status = "Pending"):
        self.account = account
        self.amount = amount
        self.transaction_type = transaction_type
        self.transaction_time = datetime.now()
        self.status = status



class ATM:
    banks = {}