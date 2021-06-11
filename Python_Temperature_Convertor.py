# Import from tkinter
import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("500x360")


# Labels
label_c = LabelFrame(root, text="Covert Celsius to Fahrenheit")
label_f = LabelFrame(root, text="Covert Fahrenheit to Celsius")

label_c.place(x=20, y=20, height = 100, width = 200)
label_f.place(x=260, y=20, height = 100, width = 200)


# Entries
entry1 = Entry(label_c, width = 10, state = "readonly")
entry2 = Entry(label_f, width = 10, state = "readonly")
result_entry3 = Entry(root)

entry1.place(x=55, y=30)
entry2.place(x=50, y=30)
result_entry3.place(x=230, y=220, height = 29, width = 170)


# Programs
def show_Cel():
    if entry1['state'] == "normal":
        entry1.config(state = "disabled")
    else:
        entry1.config(state = "normal")
        entry2.config(state = "disabled")

def show_Fah():
    if entry2['state'] == "normal":
        entry2.config(state = "disabled")
    else:
        entry2.config(state = "normal")
        entry1.config(state = "disabled")


def temp_Cal():
    if entry1['state'] == "normal" and entry1.get() != "":
        covert_to_F = float(entry1.get()) * 9/5 + 32
        result_entry3.delete(0,END)
        result_entry3.insert(0, covert_to_F)
    elif entry2['state'] == "normal" and entry2.get() != "":
        covert_to_C = (float(entry2.get()) - 32) * 5/9
        result_entry3.delete(0,END)
        result_entry3.insert(0, covert_to_C)
    else:
        return None


def clear():
    entry1.delete(0, END)
    entry1.config(state="disable")
    entry2.delete(0, END)
    entry2.config(state="disabled")
    result_entry3.delete(0, END)


def kill():
    return root.destroy()


# Buttons
button1 = Button(root, text = "Activate Cel to Fah", command = show_Cel)
button2 = Button(root, text = "Activate Fah to Cel", command = show_Fah)
button3 = Button(root, text = "Covert", command = temp_Cal)
button4 = Button(root, text="CLEAR", command=clear)
button5 = Button(root, text="EXIT", command=kill)

button1.place(x=50, y=150)
button2.place(x=290, y=150)
button3.place(x=150, y=220)
button4.place(x=50, y=300)
button5.place(x=400, y=300)

root.mainloop()
