import time
from tkinter import DISABLED, NORMAL, END, Button, Frame, RIDGE, Label, PhotoImage, Tk, Text, messagebox
from tkinter import PhotoImage
from bank import Bank
from safe import SAFE

default_account_number = 12345678901234
Color = "#370053"
BG = "#fbf3ff"

STORAGE = {
    "pin": None,
    "balance": None,
    "operation": None
}

pins = [
    "1234",
    "0000",
    "1111",
]

class ATM:
    def __init__(self, tk_root):
        self.root = tk_root
        self.root.title("ATM")
        self.root.geometry("800x660")
        self.root.config(bg=BG)

        self.load_frames()
        self.load_assets()
        self.welcome()

# ========================================================================================================
    def welcome(self):
        self.display_image("icons/logo.png")
        self.root.after(2000, lambda: self.display_image("icons/welcome.png"))
        self.root.after(3000, self.card_input)

    def card_input(self):
        self.root.bind("<<ENTER_CLICKED>>", lambda event: self.login())
        self.display_image("icons/card.png")

    def main_menu(self):
        self.root.unbind("<<CANCEL_CLICKED>>")
        self.root.unbind("<<ENTER_CLICKED>>")
        self.root.bind("<<CANCEL_CLICKED>>", lambda event: self.card_input())
        self.show_button_labels()
        self.enable_buttons()


    def login(self):
        self.root.unbind("<<CANCEL_CLICKED>>")
        self.root.unbind("<<ENTER_CLICKED>>")
        self.root.bind("<<CANCEL_CLICKED>>", lambda event: self.card_input())
        self.clear_display()
        self.prompt("Please Enter Your PIN Number:", on_enter= lambda event: self.validate_pin(event))

# ========================================================================================================

    def display_image(self, image_path):
        self.clear_display()
        image = PhotoImage(file=image_path)
        self.screen_label = Label(self.SCREEN_FRAME_DISPLAY, image=image, width=317, height=262, relief=RIDGE, bd=0)
        self.screen_label.image = image
        self.screen_label.grid(row=0, column=0)

    def clear_display(self):
        for widget in self.SCREEN_FRAME_DISPLAY.winfo_children():
            widget.grid_forget()

    def display_text(self, text, height=13):
        self.clear_display()
        self.TEXT_AREA = Text(self.SCREEN_FRAME_DISPLAY, height=height, width=30, bd=0, font=('arial',12,'bold'), bg=BG)
        self.TEXT_AREA.grid(row=0, column=0, padx=10, pady=10)
        self.TEXT_AREA.insert(END, text)

    def prompt(self, text, on_enter, height=1):
        self.display_text(text, height)
        self.INPUT_AREA = Text(self.SCREEN_FRAME_DISPLAY, height=1, width=30, bd=0, font=('arial',12,'bold'), bg=BG)
        self.INPUT_AREA.grid(row=1, column=0)
        self.INPUT_AREA.focus_set()
        self.root.bind("<<ENTER_CLICKED>>", on_enter)

# ========================================================================================================

    def show_button_labels(self):
        self.clear_display()

        self.labelL1.grid(row=0, column=0, pady=20, padx=30, sticky="w")  # Add sticky="w" to align the text to the left
        self.labelL2.grid(row=1, column=0, pady=20, padx=30, sticky="w")
        self.labelL3.grid(row=2, column=0, pady=20, padx=30, sticky="w")
        self.labelL4.grid(row=3, column=0, pady=20, padx=30, sticky="w")
        self.labelR1.grid(row=0, column=1, pady=20, padx=30, sticky="e")
        self.labelR2.grid(row=1, column=1, pady=20, padx=30, sticky="e")
        self.labelR3.grid(row=2, column=1, pady=20, padx=30, sticky="e")
        self.labelR4.grid(row=3, column=1, pady=20, padx=30, sticky="e")

    def enable_buttons(self):
        if self.btnArrowR1:
            self.btnArrowR1.config(state=NORMAL)
        if self.btnArrowR2:
            self.btnArrowR2.config(state=NORMAL)
        if self.btnArrowR3:
            self.btnArrowR3.config(state=NORMAL)
        if self.btnArrowR4:
            self.btnArrowR4.config(state=NORMAL)
        if self.btnArrowL1:
            self.btnArrowL1.config(state=NORMAL)
        if self.btnArrowL2:
            self.btnArrowL2.config(state=NORMAL)
        if self.btnArrowL3:
            self.btnArrowL3.config(state=NORMAL)
        if self.btnArrowL4:
            self.btnArrowL4.config(state=NORMAL)

    def disable_buttons(self):
        self.btnArrowR1.config(state=DISABLED)
        self.btnArrowR2.config(state=DISABLED)
        self.btnArrowR3.config(state=DISABLED)
        self.btnArrowR4.config(state=DISABLED)
        self.btnArrowL1.config(state=DISABLED)
        self.btnArrowL2.config(state=DISABLED)
        self.btnArrowL3.config(state=DISABLED)
        self.btnArrowL4.config(state=DISABLED)

    def load_frames(self):
        self.MainFrame = Frame(self.root, bd=20, width=784, height=700, relief=RIDGE)
        self.MainFrame.grid()

        self.NUMBER_PAD_FRAME = Frame(self.MainFrame, bd=7, width=734, height=300, relief=RIDGE, bg=BG)
        self.NUMBER_PAD_FRAME.grid(row=1, column=0, padx=12)

        self.SCREEN_FRAME = Frame(self.MainFrame, bd=7, width=734, height=300, relief=RIDGE)
        self.SCREEN_FRAME.grid(row=0, column=0, padx=8)

        self.SCREEN_FRAME_LEFT = Frame(self.SCREEN_FRAME, bd=5, width=190, height=300, relief=RIDGE, bg=BG)
        self.SCREEN_FRAME_LEFT.grid(row=0, column=0, padx=3)

        self.SCREEN_FRAME_DISPLAY = Frame(self.SCREEN_FRAME, bd=12, width=340, height=280, relief=RIDGE, bg=BG)
        self.SCREEN_FRAME_DISPLAY.grid_propagate(False)
        self.SCREEN_FRAME_DISPLAY.grid(row=0, column=1, padx=3)

        self.SCREEN_FRAME_RIGHT = Frame(self.SCREEN_FRAME, bd=5, width=190, height=300, relief=RIDGE, bg=BG)
        self.SCREEN_FRAME_RIGHT.grid(row=0, column=2, padx=3)

    def load_assets(self):
        self.INPUT_AREA = Text(self.SCREEN_FRAME_DISPLAY, height=1, width=30, bd=0, font=('arial',12,'bold'), bg=BG)

        self.img_arrow_Left = PhotoImage(file = "icons/arrow_right.png")

        self.btnArrowL1 = Button(self.SCREEN_FRAME_LEFT, width=160, height=50, state=DISABLED, command=self.withdraw, image=self.img_arrow_Left)
        self.btnArrowL1.grid(row=0, column=0, padx=2, pady=2)
        self.btnArrowL2 = Button(self.SCREEN_FRAME_LEFT, width=160, height=50, state=DISABLED, command=self.balance, image=self.img_arrow_Left)
        self.btnArrowL2.grid(row=1, column=0, padx=2, pady=2)
        self.btnArrowL3= Button(self.SCREEN_FRAME_LEFT, width=160, height=50, state=DISABLED, command=self.receipt, image=self.img_arrow_Left)
        self.btnArrowL3.grid(row=2, column=0, padx=2, pady=2)
        self.btnArrowL4 = Button(self.SCREEN_FRAME_LEFT, width=160, height=50, state=DISABLED, command=self.history, image=self.img_arrow_Left)
        self.btnArrowL4.grid(row=3, column=0, padx=2, pady=2)

        self.labelL1 = Label(self.SCREEN_FRAME_DISPLAY, text="Withdraw", font=('arial',12,'bold'), bg=BG)
        self.labelL2 = Label(self.SCREEN_FRAME_DISPLAY, text="Balance", font=('arial',12,'bold'), bg=BG)
        self.labelL3 = Label(self.SCREEN_FRAME_DISPLAY, text="Print Receipt", font=('arial',12,'bold'), bg=BG)
        self.labelL4 = Label(self.SCREEN_FRAME_DISPLAY, text="History", font=('arial',12,'bold'), bg=BG)

        self.img_arrow_Right = PhotoImage(file = "icons/arrow_left.png")

        self.btnArrowR1 = Button(self.SCREEN_FRAME_RIGHT, width=160, height=50, state=DISABLED, command=self.deposit, image=self.img_arrow_Right)
        self.btnArrowR1.grid(row=0, column=0, padx=2, pady=2)
        self.btnArrowR2 = Button(self.SCREEN_FRAME_RIGHT, width=160, height=50, state=DISABLED, command=self.transfer, image=self.img_arrow_Right)
        self.btnArrowR2.grid(row=1, column=0, padx=2, pady=2)
        self.btnArrowR3 = Button(self.SCREEN_FRAME_RIGHT, width=160, height=50, state=DISABLED, command=self.change_pin, image=self.img_arrow_Right)
        self.btnArrowR3.grid(row=2, column=0, padx=2, pady=2)
        self.btnArrowR4 = Button(self.SCREEN_FRAME_RIGHT, width=160, height=50, state=DISABLED, command=self.eject, image=self.img_arrow_Right)
        self.btnArrowR4.grid(row=3, column=0, padx=2, pady=2)

        self.labelR1 = Label(self.SCREEN_FRAME_DISPLAY, text="Deposit", font=('arial',12,'bold'), bg=BG, anchor="e")
        self.labelR2 = Label(self.SCREEN_FRAME_DISPLAY, text="Transfer", font=('arial',12,'bold'), bg=BG, anchor="e")
        self.labelR3 = Label(self.SCREEN_FRAME_DISPLAY, text="Change PIN", font=('arial',12,'bold'), bg=BG, anchor="e")
        self.labelR4 = Label(self.SCREEN_FRAME_DISPLAY, text="Eject Card", font=('arial',12,'bold'), bg=BG, anchor="e")


        self.img1 = PhotoImage(file = "icons/one.png")
        self.btn1 = Button(self.NUMBER_PAD_FRAME, width=160, height=60, command=lambda: self.pad_insert(1), image=self.img1).grid(row=2, column=0, padx=6, pady=4)

        self.img2 = PhotoImage(file = "icons/two.png")
        self.btn2 = Button(self.NUMBER_PAD_FRAME, width=160, height=60,command=lambda: self.pad_insert(2), image=self.img2).grid(row=2, column=1, padx=6, pady=4)

        self.img3 = PhotoImage(file = "icons/three.png")
        self.btn3 = Button(self.NUMBER_PAD_FRAME, width=160, height=60,command=lambda: self.pad_insert(3), image=self.img3).grid(row=2, column=2, padx=6, pady=4)

        self.imgCE = PhotoImage(file = "icons/cancel.png")
        self.btnCancel = Button(self.NUMBER_PAD_FRAME, width=160, height=60, command=self.cancel, image=self.imgCE).grid(row=2, column=3, padx=6, pady=4)
        #=========================================
        self.img4 = PhotoImage(file = "icons/four.png")
        self.btn4 = Button(self.NUMBER_PAD_FRAME, width=160, height=60,command=lambda: self.pad_insert(4), image=self.img4).grid(row=3, column=0, padx=4, pady=4)

        self.img5 = PhotoImage(file = "icons/five.png")
        self.btn5 = Button(self.NUMBER_PAD_FRAME, width=160, height=60,command=lambda: self.pad_insert(5), image=self.img5).grid(row=3, column=1, padx=6, pady=4)

        self.img6 = PhotoImage(file = "icons/six.png")
        self.btn6 = Button(self.NUMBER_PAD_FRAME, width=160, height=60, command=lambda: self.pad_insert(6), image=self.img6).grid(row=3, column=2, padx=6, pady=4)

        self.imgCl = PhotoImage(file = "icons/clear.png")
        self.btnClear = Button(self.NUMBER_PAD_FRAME, width=160, height=60, command=self.clear, image=self.imgCl).grid(row=3, column=3, padx=6, pady=4)
        #==========================================
        self.img7 = PhotoImage(file = "icons/seven.png")
        self.btn7 = Button(self.NUMBER_PAD_FRAME, width=160, height=60, command=lambda: self.pad_insert(7), image=self.img7).grid(row=4, column=0, padx=4, pady=4)

        self.img8 = PhotoImage(file = "icons/eight.png")
        self.btn8 = Button(self.NUMBER_PAD_FRAME, width=160, height=60, command=lambda: self.pad_insert(8), image=self.img8).grid(row=4, column=1, padx=6, pady=4)

        self.img9 = PhotoImage(file = "icons/nine.png")
        self.btn9 = Button(self.NUMBER_PAD_FRAME, width=160, height=60,command=lambda: self.pad_insert(9), image=self.img9).grid(row=4, column=2, padx=6, pady=4)

        self.imgEnter = PhotoImage(file = "icons/enter.png")
        self.btnEnter = Button(self.NUMBER_PAD_FRAME, width=160, height=60, command=self.enter, image=self.imgEnter).grid(row=4, column=3, padx=6, pady=4)
        #===========================================
        self.imgSp1 = PhotoImage(file = "icons/empty.png")
        self.btnSp1 = Button(self.NUMBER_PAD_FRAME, width=160, height=60, image=self.imgSp1).grid(row=5, column=0, padx=4, pady=4)

        self.img0 = PhotoImage(file = "icons/zero.png")
        self.btn0 = Button(self.NUMBER_PAD_FRAME, width=160, height=60, command=lambda: self.pad_insert(0), image=self.img0).grid(row=5, column=1, padx=6, pady=4)

        self.imgSp2 = PhotoImage(file = "icons/empty.png")
        self.btnSp2 = Button(self.NUMBER_PAD_FRAME, width=160, height=60, image=self.imgSp2).grid(row=5, column=2, padx=6, pady=4)

        self.imgSp3 = PhotoImage(file = "icons/empty.png")
        self.btnSp3 = Button(self.NUMBER_PAD_FRAME, width=160, height=60, image=self.imgSp3).grid(row=5, column=3, padx=6, pady=4)

# ========================================================================================================

    def clear(self):
        self.INPUT_AREA.delete("1.0",END)
        self.root.event_generate("<<CLEAR_CLICKED>>")

    def enter(self):
        self.MEMORY = self.INPUT_AREA.get("1.0",END)
        self.INPUT_AREA.delete("1.0",END)
        self.root.event_generate("<<ENTER_CLICKED>>")

    def pad_insert(self, value):
        self.INPUT_AREA.insert(END, value)

    def cancel(self):
        self.root.event_generate("<<CANCEL_CLICKED>>")

# ========================================================================================================


    def validate_pin(self, event):
        pin = self.MEMORY.strip()
        print(pin)
        if Bank.validate_pin(int(default_account_number), pin) == Bank.SUCCESS:
            STORAGE["pin"] = pin
            self.main_menu()
        else :
            print(Bank.validate_pin(int(default_account_number), pin))
            self.display_text("Invalid PIN Number. Please Try Again.")
            self.root.after(1200, self.login)
        self.root.unbind("<<ENTER_CLICKED>>")

    def withdraw (self):
        self.root.bind("<<CANCEL_CLICKED>>", lambda event: self.main_menu())
        self.prompt("Please Enter Amount:", on_enter= lambda event: self.withdraw_amount(event))

    def withdraw_amount(self, event):
        amount = self.MEMORY.strip()
        notes = SAFE.withdraw(int(amount))

        if notes == False:
            self.display_text("Sorry, we can't dispense this amount. Please try again.")
            self.root.after(1200, self.main_menu)

        text = "Please Take Your Cash\n "

        for note, count in notes.items():
            text += f"{count} x ${note} = {count * note} EGP\n"
        text += f"Total: {amount} EGP"

        bank_code = Bank.withdraw(int(default_account_number), amount)
        if bank_code == Bank.SUCCESS:
            self.display_text(text)
            self.root.after(1200, self.main_menu)
        else:
            self.display_text(bank_code.message)
            self.root.after(1200, self.main_menu)

    def balance(self):
        self.root.bind("<<CANCEL_CLICKED>>", lambda event: self.main_menu())
        balance, code = Bank.balance_inquiry(int(default_account_number))
        if code == Bank.SUCCESS:
            self.ask_for_receipt(f"Your Balance is {balance} EGP")
        else:
            self.ask_for_receipt(code.message)


    def history(self):
        self.root.bind("<<CANCEL_CLICKED>>", lambda event: self.main_menu())
        history, code = Bank.history(int(default_account_number))
        if code == Bank.SUCCESS:
            self.display_text(history, height=13)
        else:
            self.main_menu()

    def deposit(self):
        self.root.bind("<<CANCEL_CLICKED>>", lambda event: self.main_menu())
        self.prompt("Please Enter Amount:", on_enter= lambda event: self.deposit_amount(event))

    def deposit_amount(self, event):
        amount = self.MEMORY.strip()
        bank_code = Bank.deposit(int(default_account_number), amount)
        if bank_code == Bank.SUCCESS:
            self.ask_for_receipt("Deposit Successful")
        else:
            self.ask_for_receipt(bank_code.message)

    def transfer(self):
        self.root.bind("<<CANCEL_CLICKED>>", lambda event: self.main_menu())
        self.prompt("Please Enter Account Number:", on_enter= lambda event: self.transfer_account(event))

    def transfer_account(self, event):
        account_number = self.MEMORY.strip()
        self.prompt("Please Enter Amount:", on_enter= lambda event: self.transfer_amount(event, account_number))

    def transfer_amount(self, event, account_number):
        amount = self.MEMORY.strip()
        bank_code = Bank.transfer(int(default_account_number), int(account_number), amount)
        if bank_code == Bank.SUCCESS:
            self.ask_for_receipt("Transfer Successful")
        else:
            self.display_text(bank_code.message)

    def receipt(self):
        self.root.bind("<<CANCEL_CLICKED>>", lambda event: self.main_menu())
        receipt, code = Bank.print_receipt(int(default_account_number))
        if code == Bank.SUCCESS:
            self.display_text(receipt, height=13)
        else:
            self.main_menu()

    def ask_for_receipt(self, message):
        text = f"{message}\n\nWould you like to print a receipt?\n\nPress Enter for Yes\nPress Cancel for No"
        self.prompt(text, on_enter= lambda event: self.receipt_event(event), height=10)
        self.root.bind("<<CANCEL_CLICKED>>", lambda event: self.receipt_no())
        self.root.bind("<<ENTER_CLICKED>>", lambda event: self.receipt_yes())

    def receipt_yes(self):

        # self.root.unbind("<<CANCEL_CLICKED>>")
        self.root.unbind("<<ENTER_CLICKED>>")
        self.receipt()

    def receipt_no(self):
        self.root.unbind("<<CANCEL_CLICKED>>")
        self.root.unbind("<<ENTER_CLICKED>>")
        self.main_menu()


    def change_pin(self):
        self.root.bind("<<CANCEL_CLICKED>>", lambda event: self.main_menu())
        self.prompt("Please Enter New PIN Number:", on_enter= lambda event: self.change_pin_number(event))

    def change_pin_number(self, event):
        pin = self.MEMORY.strip()
        bank_code = Bank.change_pin(int(default_account_number), pin)
        if bank_code == Bank.SUCCESS:
            self.display_text("PIN Changed Successfully")
            self.root.after(1200, self.main_menu)
        else:
            self.display_text(bank_code.message)
            self.root.after(1200, self.main_menu)

    def eject(self):
        self.display_text("Please Take Your Card")
        self.root.after(1200, self.card_input)



if __name__ == "__main__":
    root = Tk()
    atm = ATM(root)
    root.mainloop()
