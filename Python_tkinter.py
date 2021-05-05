# import Tkinter
import tkinter as tk
from tkinter import *


# Parent window Of Tkinter
root = tk.Tk()
root.title('CALCULATE')
root.geometry("480x360")

# Variable Name
n1 = StringVar()
n2 = StringVar()
res = StringVar()


# Labeling
label_n1 = Label(root, text="Enter First Number:")
label_n2 = Label(root, text="Enter Second Number:")
label_result = Label(root, text="Your answer:")

label_n1.place(x=20, y=10)
label_n2.place(x=20, y=50)
label_result.place(x=20, y=90)

# Entries
entry1 = Entry(root, textvariable=n1)
entry2 = Entry(root, textvariable=n2)
read_result = Entry(root, textvariable=res)

entry1.place(x=180, y=10)
entry2.place(x=180, y=50)
read_result.place(x=180, y=90)


# Definitions
def add_number():
    n1 = int(entry1.get())
    n2 = int(entry2.get())
    your_answer = n1 + n2
    res.set(your_answer)


def clear():
    entry1.delete(0, END)
    entry2.delete(0, END)
    read_result.delete(0, END)


def exit():
    return root.destroy()


# Button Functions For Tkinter
button1 = Button(root, text="Add", command=add_number)
button2 = Button(root, text="Clear", command=clear)
button3 = Button(root, text="Exit", command=exit)

button1.place(x=40, y=120)
button2.place(x=100, y=120)
button3.place(x=170, y=120)

root.mainloop()
