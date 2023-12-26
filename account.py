import datetime
from typing import Optional
from typing_extensions import Annotated
from pydantic import BaseModel, Field, field_validator
from enum import Enum


class TransactionType(str, Enum):
    Deposit = "Deposit"
    Withdraw = "Withdraw"
    Transfer = "Transfer"
    Inquiry = "Inquiry"

class Transaction(BaseModel):
    type: TransactionType
    amount: Annotated[Optional[int], Field(default=None, validate_default=True)]
    account_number: Optional[int] = Field(default=None, validate_default=True)
    timestamp: datetime.datetime = datetime.datetime.now()

    @field_validator("amount")
    @classmethod
    def validate_amount(cls, v, values, **kwargs):
        if values.data['type'] == TransactionType.Inquiry:
            return v
        if v is None or v <= 0:
            raise ValueError("amount must be provided and greater than 0")
        return v

    @field_validator("account_number")
    @classmethod
    def validate_account_number(cls, v, values, **kwargs):
        if values.data['type'] != TransactionType.Transfer:
            return v
        if v is None:
            raise ValueError("account number must be provided for transfer")
        return v

    def generate_receipt(self):
        _str = f"******{self.type.title()} Transaction****** \n\n"
        _str += f"Time: {self.timestamp}\n"
        if self.type != TransactionType.Inquiry:
            _str += f"Transaction Amount: {self.amount}\n"
        if self.type == TransactionType.Transfer:
            _str += f"Account Number: {self.account_number}\n"
        return _str

class Account(BaseModel):
    name: str
    balance: int
    card: int = None
    PIN: str = None
    account_number: int = 0
    transactions: list[Transaction] = []
