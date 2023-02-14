import tkinter as tk
from tkinter.constants import *


def convert_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    result_label.config(text=km)


window = tk.Tk()
window.title("Mile Converter")
window.config(padx=25, pady=25)
window.minsize(width=300, height=150)
window.anchor("center")

miles_input = tk.Entry(width=12)
miles_input.grid(column=2, row=1)

miles_label = tk.Label(text="Miles")
miles_label.grid(column=3, row=1)

equal_to_label = tk.Label(text="is equal to")
equal_to_label.grid(column=1, row=2)

result_label = tk.Label()
result_label.grid(column=2, row=2)

km_label = tk.Label(text="km")
km_label.grid(column=3, row=2)

calc_button = tk.Button(text="Calculate", command=convert_to_km, width=12)
calc_button.grid(column=2, row=3)

tk.mainloop()