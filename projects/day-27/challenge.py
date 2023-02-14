import tkinter as tk
from tkinter.constants import *

window = tk.Tk()
window.title("Why are you reading this title, focus on the program!")
window.minsize(width=500, height=400)
window.config(padx=20, pady=20)

my_label = tk.Label(text="This is a label.")
my_label.grid(column=0, row=0)

my_button1 = tk.Button(text="Click me!")
my_button1.grid(column=2, row=0)

my_button2 = tk.Button(text="Click me too!")
my_button2.grid(column=1, row=1)

my_entry = tk.Entry(width=12)
my_entry.grid(column=3, row=2)

tk.mainloop()
