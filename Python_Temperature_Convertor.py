# Import from tkinter
import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("480x360")

Cel = StringVar()
Fer = StringVar()
result = StringVar()


# Labels
label_c = Label(root, text="Temperature to covert C to F")
label_f = Label(root, text="Temperature to covert F to C")

label_c.place(x=20, y=20)
label_f.place(x=260, y=20)


# Entries
entry1 = Entry(root, textvariable=Cel)
entry2 = Entry(root, textvariable=Fer)
read_result = Entry(root)

entry1.place(x=20, y=50)
entry2.place(x=260, y=50)


# Calculations
def cel(fer):
    return (fer-32) * 5/9


def fer(cel):
    return cel * 9/5 + 32


# Programs
def clear():
    entry1.delete(0, END)
    entry2.delete(0, END)


def kill():
    return root.destroy()


# Buttons
button1 = Button(root, text="Show Cel to Fah")
button2 = Button(root, text="Show Fah to Cel")
button3 = Button(root, text="CLEAR", command=clear)
button4 = Button(root, text="EXIT", command=kill)

button1.place(x=20, y=200)
button2.place(x=300, y=200)
button3.place(x=50, y=300)
button4.place()

root.mainloop()
