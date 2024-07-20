#imports tkinter module and allows for window to be created
from tkinter import *
root = Tk()
#title of root window and creation of window
root.title("welcome to BankSimulator")
#set width and height
root.geometry('800x500')

#all widgets go down here

#creates label to welcome user
label_1 = Label(root, text = "welcome to the bank")
label_1.grid()

#button widget
main_button = Button(root, text = "test", fg="red",)
main_button.grid(column=1, row=0)
#executes tkinter
root.mainloop()
