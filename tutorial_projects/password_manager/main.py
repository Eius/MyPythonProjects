import json
import tkinter as tk
from tkinter import messagebox
from tkinter.constants import *
from random import choice, randint, shuffle
from credentials_messagebox import CredentialsWindow
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def validate_and_save_credentials():
    website = website_entry.get().capitalize()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please make sure you haven't left any fields empty!")
        return

    is_ok = messagebox.askokcancel(title=f"{website}", message=f"There are the details you entered: "
                                                               f"\nEmail/Username: {username}"
                                                               f"\nPassword: {password}"
                                                               f"\nIs it ok to save?")

    if is_ok:
        new_data = {website: {
            "username": username,
            "password": password
        }}
        try:
            with open("credentials.json", "r") as file:
                # Reading old data
                data = json.load(file)

        except FileNotFoundError:
            with open("credentials.json", "w") as file:
                # If file does not exist, create it and write new data into it
                json.dump(new_data, file, indent=4)

        else:
            # Updating old data with new data
            data.update(new_data)

            with open("credentials.json", "w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- SEARCH PASSWORD ------------------------------- #

def search_credentials():
    website = website_entry.get().capitalize()
    if len(website) == 0:
        messagebox.showwarning(title="Oops", message="Website entry is empty!")
        return

    try:
        with open("credentials.json", "r") as file:
            data: dict = json.load(file)
            credentials: dict = data[website]

    except (FileNotFoundError, KeyError) as e:
        error_message = ""
        if isinstance(e, FileNotFoundError):
            error_message = "Credentials file does not exist!"

        elif isinstance(e, KeyError):
            error_message = f"No credentials found for {e}!"

        messagebox.showwarning(title="Error",
                               message=f"{error_message}")

    else:
        username = credentials.get("username")
        password = credentials.get("password")
        cred_win = CredentialsWindow(website, username, password)

# ---------------------------- UI SETUP ------------------------------- #


# Window
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=20)
window.minsize(width=500, height=400)

# Canvas
canvas = tk.Canvas(height=200, width=200)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)

# Labels
website_label = tk.Label(text="Website:")
username_label = tk.Label(text="Email/Username:")
password_label = tk.Label(text="Password:")

# Entries
website_entry = tk.Entry()
website_entry.focus()
username_entry = tk.Entry()
username_entry.insert(0, "@gmail.com")
password_entry = tk.Entry()

# Buttons
search_button = tk.Button(text="Search", command=search_credentials)
generate_button = tk.Button(text="Generate Password", command=generate_password)
add_button = tk.Button(text="Add", width=36, command=validate_and_save_credentials)

# ---------- GRID ARRANGEMENT ---------- #
# Window
window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(0, weight=1)
# Canvas
canvas.grid(column=0, row=0, columnspan=3)
# Labels
website_label.grid(column=0, row=1)
username_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)
# Entries
website_entry.grid(column=1, row=1, sticky="ew", padx=(3, 3))
username_entry.grid(column=1, row=2, columnspan=2, sticky="ew", padx=(3, 0))
password_entry.grid(column=1, row=3, sticky="ew", padx=3)
# Buttons
search_button.grid(column=2, row=1, sticky="ew")
generate_button.grid(column=2, row=3, sticky="ew")
add_button.grid(column=1, row=4, columnspan=2, sticky="ew")

window.mainloop()
