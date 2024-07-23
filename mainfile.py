#imports tkinter module and allows for window to be created
from tkinter import *
root = Tk()
#title of root window and creation of window
root.title("welcome to BankSimulator")
#set width and height
root.geometry('800x500')

#all widgets go down here

Bank_logo = PhotoImage(file="scotia_bank.png")
Bank_logo = Bank_logo.subsample(2)  # Adjust the subsample value as needed
bank_logo_display = Label(root, image=Bank_logo)
bank_logo_display.place(x=20, y=20)  # Adjust the x and y values as needed

#global variables initialization
account_balance = 0
account_number = 0
account_type = ""
account_name = ""
account_pin = 0
#amount user typed into deposit entry field
deposit_amount = StringVar()

def clicked():
    print("hello")

def deposit():
    global account_balance
    account_balance = account_balance + int(deposit_amount.get())
    account_value_label.config(text="Account Value: $" + str(account_balance))
    

# Entry widget
account_change = Entry(root, width=20, textvariable=deposit_amount)
account_change.place(x=500, y=200)
account_change.insert(0, "Enter amount")  # Add this line to provide a default text in the entry field


# Label widget
account_value_label = Label(root, text="Account Value: $" + str(account_balance))
account_value_label.place(x=500, y=170)
message_text = Label(root)
message_text.place(x=450, y=230)

# if statement to check if deposit_amount is a string and return an error message
if deposit_amount == str:
    message_text.config(text="please enter a valid number.")
elif deposit_amount == int:
    message_text.config(text="Deposit successful! Account Value: $" + str(account_balance))
else:
    message_text.config(text="please enter your deposit amount.")



# Button widget
Deposit_button = Button(root, text="Deposit", fg="red", command=deposit)
Deposit_button.place(x=450, y=200)

# Executes tkinter
root.mainloop()
