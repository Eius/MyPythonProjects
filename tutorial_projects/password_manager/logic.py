import tkinter
import pyperclip
from tkinter import messagebox
from tkinter.constants import *
from credentials_window import CredentialsWindow
from random import choice, shuffle, randint
from utilities import get_config
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password(password_entry):
    # Password Generator Project
    config = get_config()["password_generator"]
    lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                         't', 'u', 'v', 'w', 'x', 'y', 'z']
    uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                         'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_lowercase_letters = [choice(lowercase_letters) for _ in range(randint(8, 10))]
    password_uppercase_letters = [choice(uppercase_letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = []
    if config["include_lowercase"] == "True":
        password_list += password_lowercase_letters
    if config["include_uppercase"] == "True":
        password_list += password_uppercase_letters
    if config["include_numbers"] == "True":
        password_list += password_numbers
    if config["include_symbols"] == "True":
        password_list += password_symbols

    shuffle(password_list)
    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def validate_and_save_credentials(website_entry, username_entry, password_entry):
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
            with open("data/credentials.json", "r") as file:
                # Reading old data
                data = json.load(file)

        except FileNotFoundError:
            with open("data/credentials.json", "w") as file:
                # If file does not exist, create it and write new data into it
                json.dump(new_data, file, indent=4)

        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data/credentials.json", "w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- SEARCH PASSWORD ------------------------------- #

def search_credentials(website_entry: tkinter.Entry):
    website = website_entry.get().capitalize()
    if len(website) == 0:
        messagebox.showwarning(title="Oops", message="Website entry is empty!")
        return

    try:
        with open("data/credentials.json", "r") as file:
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
