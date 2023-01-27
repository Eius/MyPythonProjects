from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

def validate_input(website: str, email_username: str, password: str):
    # Check if input is empty
    if len(website) == 0 or len(email_username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
        return False

    # Show message box with input and return true if it´s ok, if not return false
    is_ok = messagebox.askokcancel(title=website, message=f"There are the details you entered :"
                                                          f"\nEmail: {email_username}"
                                                          f"\nPassword: {password}"
                                                          "\nIs it ok to save?")

    return is_ok


def save_credentials(website: str, email_username: str, password: str):
    formatted_website = website.capitalize()
    with open("credentials.txt", "a") as file:
        file.write(f"{formatted_website} | {email_username} | {password}\n")


def generate_password():

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
    pyperclip.copy(password)
    return password
