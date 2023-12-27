# ATM Simulator

This project simulates an ATM (Automated Teller Machine) system. It includes a GUI (Graphical User Interface) and a backend system that handles transactions such as withdrawal, deposit, balance inquiry, and more.

## Project Structure

The project is structured as follows:

- `bank.py`: This file contains the `Bank` class which handles all the banking operations like withdrawal, deposit, balance inquiry, etc. It also contains the `CODE` class which is used for handling operation status codes.
- `GUI.py`: This file contains the `ATM` class which is responsible for the graphical user interface of the ATM. It includes methods for displaying images, text, and handling user input.
- `storage.py`: This file contains the `JSONStorage` class which is responsible for reading and writing account data to a JSON file.
- `safe.py`: This file contains the `SAFE` class which is responsible for dispensing cash in the ATM.
- `models/`: This directory contains the `Account` and `Transaction` classes which are used to represent bank accounts and transactions respectively.
- `utils/`: This directory contains utility functions and classes.
- `icons/`: This directory contains the images used in the GUI.

## How to Run

To run the project, execute the `GUI.py` file. This will start the ATM simulator.

## Features

The ATM simulator supports the following operations:

- Withdrawal: The user can withdraw money from their account.
- Deposit: The user can deposit money into their account.
- Balance Inquiry: The user can check their account balance.
- Transfer: The user can transfer money to another account.
- Change PIN: The user can change their account PIN.
- Print Receipt: The user can print a receipt of their last transaction.
- Eject Card: The user can eject their card and end the session.