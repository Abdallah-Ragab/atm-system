from models import Account
from storage import JSONStorage

default_account_number = 11111111111111
account = Account(
    name="Abdallah Sameh",
    account_number=default_account_number,
    bank="Banque Misr",
    balance=1000,
    card=1111111111111111,
    PIN="0000",
)

JSONStorage.save_account(account.model_dump())

account = Account(
    name="Abdallah Ragab",
    account_number=11111111111112,
    bank="QNB",
    balance=1000,
    card=1111111111111112,
    PIN="0000",
)

JSONStorage.save_account(account.model_dump())





