import tkinter as tk
from tkinter import Toplevel
import pyperclip
from utilities import get_style


class CredentialsWindow(Toplevel):
    def __init__(self, website: str, username: str, password: str):
        super().__init__()
        self.style = get_style("credentials_messagebox")
        self.focus()
        self.title = website
        self.config(pady=12, padx=12)
        self.username = tk.Label(self, text=f"{username}", font=self.style["font_normal"])
        self.password = tk.Label(self, text=f"{password}", font=self.style["font_normal"])
        self.username_label = tk.Label(self, text=f"Username:", font=self.style["font_normal"])
        self.password_label = tk.Label(self, text=f"Password:", font=self.style["font_normal"])

        self.copy_username_button = tk.Button(self, text="Copy Username",
                                              font=self.style["font_bold"],
                                              command=self.copy_username,
                                              width= 20)
        self.copy_password_button = tk.Button(self, text="Copy Password",
                                              font=self.style["font_bold"],
                                              command=self.copy_password,
                                              width= 20)

        self.arrange_widgets()
        self.mainloop()

    def arrange_widgets(self):
        self.username_label.grid(column=0, row=0, columnspan=2)
        self.password_label.grid(column=0, row=1, columnspan=2)
        self.username.grid(column=2, row=0)
        self.password.grid(column=2, row=1)
        self.copy_username_button.grid(column=0, row=2, sticky="ew", padx=(0, 3), pady=(7, 0))
        self.copy_password_button.grid(column=2, row=2, sticky="ew", padx=(3, 0), pady=(7, 0))

    def copy_username(self):
        pyperclip.copy(self.username.cget("text"))

    def copy_password(self):
        pyperclip.copy(self.password.cget("text"))

    def close_window(self):
        self.destroy()

