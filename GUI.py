import time
from tkinter import DISABLED, NORMAL, END, Button, Frame, RIDGE, Label, PhotoImage, Tk, Text, messagebox
from tkinter import PhotoImage


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

        self.display_frames()
        self.display_assets()
        self.welcome()

    def welcome(self):
        # Display Large ATM Logo and Welcome Message
        self.display_image("icons/logo.png")
        self.root.after(500, lambda: self.display_image("icons/welcome.png"))
        self.root.after(1000, self.get_pin)

    def get_pin(self):
        self.prompt("Please Enter Your PIN Number:", on_enter = self.validate_pin)

    def validate_pin(self, event):
        pin = self.MEMORY.strip()
        print("x", pin, "x", sep='')
        if pin in pins:
            STORAGE.update({"pin": pin})
        else :
            self.display_text("Invalid PIN Number. Please Try Again.")
            self.root.after(1200, self.get_pin)
            return



    def display_image(self, image_path):
        self.clear_screen()
        image = PhotoImage(file=image_path)
        self.screen_label = Label(self.SCREEN_FRAME_DISPLAY, image=image, width=317, height=262, relief=RIDGE, bd=0)
        self.screen_label.image = image
        self.screen_label.grid(row=0, column=0)

    def clear_screen(self):
        for widget in self.SCREEN_FRAME_DISPLAY.winfo_children():
            widget.grid_forget()

    def display_text(self, text, height=16):
        self.clear_screen()
        self.TEXT_AREA = Text(self.SCREEN_FRAME_DISPLAY, height=height, width=45, bd=0, font=('arial',9,'bold'), bg=BG)
        self.TEXT_AREA.grid(row=0, column=0)
        self.TEXT_AREA.insert(END, text)

    def prompt(self, text, on_enter):

        self.display_text(text, height=1)
        self.INPUT_AREA = Text(self.SCREEN_FRAME_DISPLAY, height=1, width=45, bd=0, font=('arial',9,'bold'), bg=BG)
        self.INPUT_AREA.grid(row=1, column=0)
        self.INPUT_AREA.focus_set()
        self.root.bind("<<ENTER_CLICKED>>", on_enter)


    def display_frames(self):
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

    def display_assets(self):

        self.img_arrow_Left = PhotoImage(file = "icons/arrow.png")

        self.btnArrowL1 = Button(self.SCREEN_FRAME_LEFT, width=160, height=50, state=DISABLED, command=self.WithdrawCash, image=self.img_arrow_Left).grid(row=0, column=0, padx=2, pady=2)

        self.btnArrowL2 = Button(self.SCREEN_FRAME_LEFT, width=160, height=50, state=DISABLED, command=self.WithdrawCash, image=self.img_arrow_Left).grid(row=1, column=0, padx=2, pady=2)

        self.btnArrowL3= Button(self.SCREEN_FRAME_LEFT, width=160, height=50, state=DISABLED, command=self.balance, image=self.img_arrow_Left).grid(row=2, column=0, padx=2, pady=2)

        self.btnArrowL4 = Button(self.SCREEN_FRAME_LEFT, width=160, height=50, state=DISABLED, command=self.statement, image=self.img_arrow_Left).grid(row=3, column=0, padx=2, pady=2)


        self.img_arrow_Right = PhotoImage(file = "icons/images.png")

        self.btnArrowR1 = Button(self.SCREEN_FRAME_RIGHT, width=160, height=50, state=DISABLED, command=self.Laon, image=self.img_arrow_Right).grid(row=0, column=0, padx=2, pady=2)

        self.btnArrowR2 = Button(self.SCREEN_FRAME_RIGHT, width=160, height=50, state=DISABLED, command=self.Deposit, image=self.img_arrow_Right).grid(row=1, column=0, padx=2, pady=2)

        self.btnArrowR3 = Button(self.SCREEN_FRAME_RIGHT, width=160, height=50, state=DISABLED, command=self.Request_new_pin, image=self.img_arrow_Right).grid(row=2, column=0, padx=2, pady=2)

        self.btnArrowR4 = Button(self.SCREEN_FRAME_RIGHT, width=160, height=50, state=DISABLED, command=self.statement, image=self.img_arrow_Right).grid(row=3, column=0, padx=2, pady=2)


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


    def prompt_pin(self):
        self.TEXT_AREA.insert(END, "Please Enter Your Pin Number")
        self.TEXT_AREA.insert(END, "\n")

    def clear(self):
        self.INPUT_AREA.delete("1.0",END)

    def enter(self):
        self.MEMORY = self.INPUT_AREA.get("1.0",END)
        self.INPUT_AREA.delete("1.0",END)
        self.root.event_generate("<<ENTER_CLICKED>>")

    def disable_buttons(self):

        self.btnArrowR1 = Button(self.SCREEN_FRAME_RIGHT, width=160, height=50, state=DISABLED, image=self.img_arrow_Right).grid(row=0, column=0, padx=2, pady=2)

        self.btnArrowR2 = Button(self.SCREEN_FRAME_RIGHT, width=160, height=50, state=DISABLED, image=self.img_arrow_Right).grid(row=1, column=0, padx=2, pady=2)

        self.btnArrowR3 = Button(self.SCREEN_FRAME_RIGHT, width=160, height=50, state=DISABLED, image=self.img_arrow_Right).grid(row=2, column=0, padx=2, pady=2)

        self.btnArrowR4 = Button(self.SCREEN_FRAME_RIGHT, width=160, height=50, state=DISABLED, image=self.img_arrow_Right).grid(row=3, column=0, padx=2, pady=2)


        self.btnArrowL1 = Button(self.SCREEN_FRAME_LEFT, width=160, height=50, state=DISABLED, image=self.img_arrow_Left).grid(row=0, column=0, padx=2, pady=2)

        self.btnArrowL2 = Button(self.SCREEN_FRAME_LEFT, width=160, height=50, state=DISABLED, image=self.img_arrow_Left).grid(row=1, column=0, padx=2, pady=2)

        self.btnArrowL3= Button(self.SCREEN_FRAME_LEFT, width=160, height=50, state=DISABLED, image=self.img_arrow_Left).grid(row=2, column=0, padx=2, pady=2)

        self.btnArrowL4 = Button(self.SCREEN_FRAME_LEFT, width=160, height=50, state=DISABLED, image=self.img_arrow_Left).grid(row=3, column=0, padx=2, pady=2)

    def enable_buttons(self):

        self.btnArrowR1 = Button(self.SCREEN_FRAME_RIGHT, width=160, height=50, state=NORMAL, command=self.Laon, image=self.img_arrow_Right).grid(row=0, column=0, padx=2, pady=2)

        self.btnArrowR2 = Button(self.SCREEN_FRAME_RIGHT, width=160, height=50, state=NORMAL, command=self.Deposit, image=self.img_arrow_Right).grid(row=1, column=0, padx=2, pady=2)

        self.btnArrowR3 = Button(self.SCREEN_FRAME_RIGHT, width=160, height=50, state=NORMAL, command=self.Request_new_pin, image=self.img_arrow_Right).grid(row=2, column=0, padx=2, pady=2)

        self.btnArrowR4 = Button(self.SCREEN_FRAME_RIGHT, width=160, height=50, state=NORMAL, command=self.statement, image=self.img_arrow_Right).grid(row=3, column=0, padx=2, pady=2)


        self.btnArrowL1 = Button(self.SCREEN_FRAME_LEFT, width=160, height=50, state=NORMAL, command=self.WithdrawCash, image=self.img_arrow_Left).grid(row=0, column=0, padx=2, pady=2)

        self.btnArrowL2 = Button(self.SCREEN_FRAME_LEFT, width=160, height=50, state=NORMAL, command=self.WithdrawCash, image=self.img_arrow_Left).grid(row=1, column=0, padx=2, pady=2)

        self.btnArrowL3= Button(self.SCREEN_FRAME_LEFT, width=160, height=50, state=NORMAL, command=self.balance, image=self.img_arrow_Left).grid(row=2, column=0, padx=2, pady=2)

        self.btnArrowL4 = Button(self.SCREEN_FRAME_LEFT, width=160, height=50, state=NORMAL, command=self.statement, image=self.img_arrow_Left).grid(row=3, column=0, padx=2, pady=2)

    def pad_insert(self, value):
        self.INPUT_AREA.insert(END, value)

    def cancel(self):
        cancel = messagebox.askyesno("ATM","Are you sure you want to cancel the operation and exit?")
        if cancel > 0:
            self.root.destroy()
            return

    def WithdrawCash (self):
        self.enter_Pin()
        self.TEXT_AREA.delete("1.0",END)
        self.TEXT_AREA.focus_set()

    def Laon (self):
        self.enter_Pin()
        self.TEXT_AREA.delete("1.0",END)
        self.TEXT_AREA.insert(END, 'Laon $ ')
        self.TEXT_AREA.focus_set()

    def Deposit (self):
        self.enter_Pin()
        self.TEXT_AREA.delete("1.0",END)
        self.TEXT_AREA.focus_set()

    def Request_new_pin(self):
        self.enter_Pin()
        self.TEXT_AREA.delete("1.0",END)
        self.TEXT_AREA.insert(END, '\t\tWelcome to iBank\n')
        self.TEXT_AREA.insert(END, 'New Pin will be send to your home address\n')
        self.TEXT_AREA.insert(END, 'Withdraw Cash\t\t\t Loan' + "\n\n\n\n")
        self.TEXT_AREA.insert(END, 'Cash With Receipt\t\t\t Deposit' + "\n\n\n\n")
        self.TEXT_AREA.insert(END, 'Balance\t\t\t Request New Pin' + "\n\n\n\n")
        self.TEXT_AREA.insert(END, 'Mini Statement\t\t\t Print Statement' + "\n\n\n\n")
        self.TEXT_AREA.insert(END, '\t\tThanks for using iBank\n')

    def balance(self):
        self.TEXT_AREA.delete("1.0",END)
        self.TEXT_AREA.insert(END, '\t\tWelcome to iBank\n')
        self.TEXT_AREA.insert(END, '$1296' + "\n")
        self.TEXT_AREA.insert(END, 'Withdraw Cash\t\t\t Loan' + "\n\n\n\n")
        self.TEXT_AREA.insert(END, 'Cash With Receipt\t\t\t Deposit' + "\n\n\n\n")
        self.TEXT_AREA.insert(END, 'Balance\t\t\t Request New Pin' + "\n\n\n\n")
        self.TEXT_AREA.insert(END, 'Mini Statement\t\t\t Print Statement' + "\n\n\n\n")
        self.TEXT_AREA.insert(END, '\t\tThanks for using iBank\n')

    def statement(self):
        pinNo1 = str(self.TEXT_AREA.get("1.0","end-1c"))
        pinNo2 = str(pinNo1)
        pinNo3 = float(pinNo2)
        pinNo4 = float(1296 - (pinNo3))
        self.TEXT_AREA.delete("1.0",END)
        self.TEXT_AREA.insert(END, '\n\t' + str(pinNo4) + "\t\t")
        self.TEXT_AREA.insert(END, '\t\t\t\n\n    Account Balance $' + str(pinNo4) + "\t\t\n\n")
        self.TEXT_AREA.insert(END, 'Rent \t\t\t\t $1200' + "\n\n")
        self.TEXT_AREA.insert(END, 'Tesco \t\t\t\t $79.36' + "\n\n")
        self.TEXT_AREA.insert(END, 'Rent \t\t\t\t $1200' + "\n\n")
        self.TEXT_AREA.insert(END, 'Sainsbury'+'s \t\t\t\t $53.87'+ "\n\n")
        self.TEXT_AREA.insert(END, 'Poundland \t\t\t\t $19.00'+ "\n\n")

    def enter_Pin(self):
        pinNo1 = str(self.TEXT_AREA.get("1.0","end-1c"))
        pinNo2 = str(pinNo1)
        pinNo3 = float(pinNo2)
        pinNo4 = float(1296 - (pinNo3))
        self.TEXT_AREA.delete("1.0",END)
        self.TEXT_AREA.insert(END, '\n\t' + str(pinNo4) + "\t\t")
        self.TEXT_AREA.insert(END, '\t\t\t\n\n    Account Balance $' + str(pinNo4) + "\t\t\n\n")
        self.TEXT_AREA.insert(END, 'Withdraw Cash\t\t\t Loan' + "\n\n\n\n")
        self.TEXT_AREA.insert(END, 'Cash With Receipt\t\t\t Deposit' + "\n\n\n\n")
        self.TEXT_AREA.insert(END, 'Balance\t\t\t Request New Pin' + "\n\n\n\n")
        self.TEXT_AREA.insert(END, 'Mini Statement\t\t\t Print Statement' + "\n\n\n\n")
        self.TEXT_AREA.insert(END, '\t\tThanks for using iBank\n')


if __name__ == "__main__":
    root = Tk()
    atm = ATM(root)
    root.mainloop()
