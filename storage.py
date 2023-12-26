import json
import os
from utils.encoders import DateTimeEncoder

class JSONStorage:
    file_path = "accounts.json"
    _data = None

    @staticmethod
    def create_if_not_exists():
        if not os.path.exists(JSONStorage.file_path):
            with open(JSONStorage.file_path, "w") as f:
                json.dump({"accounts":[]}, f)

    @staticmethod
    def read_file():
        JSONStorage.create_if_not_exists()
        with open(JSONStorage.file_path, "r") as f:
            JSONStorage._data = json.load(f)

    @staticmethod
    def write_file():
        JSONStorage.create_if_not_exists()
        print("Writing to file...")
        print(JSONStorage._data)
        with open(JSONStorage.file_path, "w") as f:
            json.dump(JSONStorage._data, f, cls=DateTimeEncoder)

    @staticmethod
    def save_account(account_dict):
        JSONStorage.read_file()
        accounts = JSONStorage._data["accounts"]
        account = JSONStorage.get_account(account_dict['account_number'])
        if account:
            accounts.remove(account)
        accounts.append(account_dict)
        JSONStorage._data = {"accounts": accounts}
        JSONStorage.write_file()

    @staticmethod
    def get_account(account_number):
        JSONStorage.read_file()
        accounts = JSONStorage._data["accounts"]
        for account in accounts:
            if account["account_number"] == account_number:
                return account
        return None