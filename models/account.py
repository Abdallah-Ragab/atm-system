import datetime
from typing import Optional
from typing_extensions import Annotated
from pydantic import BaseModel, Field, field_validator, model_validator
from enum import Enum


class TransactionType(str, Enum):
    Deposit = "Deposit"
    Withdraw = "Withdraw"
    Transfer = "Transfer"
    Inquiry = "Inquiry"

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value


class TransactionStatus(str, Enum):
    Successful = "Successful"
    Failed = "Failed"
    Cancelled = "Cancelled"
    Pending = "Pending"

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value


class Transaction(BaseModel):
    id: int
    type: TransactionType
    amount: Optional[int] = Field(default=None, validate_default=True)
    account_number: Optional[int] = Field(default=None, validate_default=True)
    timestamp: datetime.datetime = datetime.datetime.now()
    status: TransactionStatus = TransactionStatus.Pending

    @field_validator("amount")
    @classmethod
    def validate_amount(cls, v, values, **kwargs):
        if values.data["type"] == TransactionType.Inquiry:
            return v
        if v is None or v <= 0:
            raise ValueError("amount must be provided and greater than 0")
        return v

    @field_validator("account_number")
    @classmethod
    def validate_account_number(cls, v, values, **kwargs):
        if values.data["type"] != TransactionType.Transfer:
            return v
        if v is None:
            raise ValueError("account number must be provided for transfer")
        return v

    def generate_receipt(self, account):
        _str = f"{account.bank}Bank\n"
        _str = f"******{self.type.title()} Transaction****** \n\n"
        _str += f"Customer Name: {account.name}\n"
        _str += f"Customer Account Number: {account.account_number}\n"
        _str += f"Time: {self.timestamp}\n"
        if self.type != TransactionType.Inquiry:
            _str += f"Transaction Amount: {self.amount}\n"
        else:
            _str += f"Account Balance: {account.balance}\n"
        if self.type == TransactionType.Transfer:
            _str += f"Receiving Account Number: {self.account_number}\n"
        _str += f"Transaction Status: {self.status}\n"
        return _str

    def update_status(self, status):
        self.status = status
        self.timestamp = datetime.datetime.now()

    def __str__(self):
        return f"{self.type.title()} Transaction of {self.amount} EGP at {self.timestamp} with status {self.status}"


class Account(BaseModel):
    name: str
    balance: Optional[int] = 0
    account_number: int
    bank: str
    card: Optional[int] = None
    PIN: Optional[str] = None
    transactions: Optional[list[Transaction]] = []

    @field_validator("balance")
    @classmethod
    def validate_balance(cls, v, values, **kwargs):
        if v < 0:
            raise ValueError("balance must be greater or equal to 0")
        return v

    @field_validator("card")
    @classmethod
    def validate_card(cls, v, values, **kwargs):
        if v is None:
            return v
        if len(str(v)) != 16:
            raise ValueError("card number must be 16 digits")
        return v

    @model_validator(mode="after")
    @classmethod
    def validate_card_and_PIN(cls, values, **kwargs):
        if values.card is not None and values.PIN is None:
            raise ValueError("PIN must be provided with card")
        return values

    @field_validator("account_number")
    @classmethod
    def validate_account_number(cls, v, values, **kwargs):
        if len(str(v)) != 14:
            raise ValueError("account number must be 14 digits")
        return v
