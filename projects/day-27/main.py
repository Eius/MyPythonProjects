import tkinter as tk
from tkinter.constants import *
from playground import add, calculate


def button_clicked():
    my_label1.config(text=f"{entry_input.get()}")
    entry_input.delete(0, END)


window = tk.Tk()
window.title("Just some window")
window.minsize(width=500, height=400)

# Label
my_label1 = tk.Label(text="This Is a Prompt", font=("Arial", 24, "italic"))
my_label1.grid(column=1, row=0)

# Button
my_button = tk.Button(text="Click me!", command=button_clicked)
my_button.grid(column=1, row=1)

# Entry
entry_input = tk.Entry(width=12)
entry_input.grid(column=1, row=2)

# Multiline text
text_entry_box = tk.Text(width=20, height=7)
text_entry_box.insert(END, "Example of multi-line text entry.")
print(f"Content of multiline text box: {text_entry_box.get(1.0, END)}")
text_entry_box.grid(column=1, row=3)


# Spinbox
def spinbox_used():
    print(spinbox.get())

spinbox = tk.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.grid(column=1, row=4)


# Scale
# Called with current scale value.
def scale_used(value):
    print(value)

scale = tk.Scale(from_=0, to=100, command=scale_used)
scale.grid(column=1, row=5)


# Checkbutton
def check_button_used():
    # Prints 1 if On, otherwise 0
    print(checked_state.get())

checked_state = tk.BooleanVar()
check_button = tk.Checkbutton(text="Is On?", command=check_button_used, variable=checked_state)
check_button.grid(column=1, row=6)


# Radiobutton
choices = {
    1: "Jablko",
    2: "Hruška",
    3: "Jahoda",
    4: "Ananás",
    5: "Banán"
}

def radio_used():
    index = radio_state.get()
    print(choices[index])

radio_state = tk.IntVar()
radio_buttons = []

for (key, value) in choices.items():
    radio_button = tk.Radiobutton(text=value, value=key, variable=radio_state, command=radio_used)
    radio_button.grid(column=1, row=7)
    radio_buttons.append(radio_button)

# Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))
    print(event)


fruits = ["Jablko", "Hruška", "Pomaranč", "Banán"]
listbox = tk.Listbox(height=len(fruits))
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.grid(column=2, row=8)

window.mainloop()
