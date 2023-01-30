from tkinter import Tk
import tkinter as tk
from generate_config_window import GenerateConfigWindow
from logic import search_credentials, validate_and_save_credentials, generate_password


class Window(Tk):
    def __init__(self):
        super().__init__()

        # Window
        self.title("Password Manager")
        self.config(padx=50, pady=20)
        self.minsize(width=600, height=400)

        # Canvas
        self.canvas = tk.Canvas(height=350, width=350)
        self.logo_img = tk.PhotoImage(file="resources/logo.png")
        self.canvas.create_image(175, 175, image=self.logo_img)

        # Labels
        self.website_label = tk.Label(text="Website:")
        self.username_label = tk.Label(text="Email/Username:")
        self.password_label = tk.Label(text="Password:")

        # Entries
        self.website_entry = tk.Entry()
        self.website_entry.focus()
        self.username_entry = tk.Entry()
        self.username_entry.insert(0, "@gmail.com")
        self.password_entry = tk.Entry()

        # Buttons
        self.search_button = tk.Button(text="Search", command=self.on_search_button_click)
        self.generate_button = tk.Button(text="Generate Password", command=self.on_generate_button_click)
        self.generate_config_button = tk.Button(text="⚙", command=self.on_generate_config_button_click)
        self.add_button = tk.Button(text="Add", width=36, command=self.on_add_button_click)

        self.arrange_widgets()
        self.mainloop()

    def arrange_widgets(self):
        # Window
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        # Canvas
        self.canvas.grid(column=0, row=0, columnspan=4)
        # Labels
        self.website_label.grid(column=0, row=1)
        self.username_label.grid(column=0, row=2)
        self.password_label.grid(column=0, row=3)
        # Entries
        self.website_entry.grid(column=1, row=1, sticky="ew", padx=(3, 3))
        self.username_entry.grid(column=1, row=2, columnspan=3, sticky="ew", padx=(3, 0))
        self.password_entry.grid(column=1, row=3, sticky="ew", padx=3)
        # Buttons
        self.search_button.grid(column=2, row=1, sticky="ew", columnspan=2)
        self.generate_button.grid(column=2, row=3, sticky="ew")
        self.generate_config_button.grid(column=3, row=3)
        self.add_button.grid(column=1, row=4, columnspan=3, sticky="ew")

    def on_search_button_click(self):
        search_credentials(self.website_entry)

    def on_generate_button_click(self):
        generate_password(self.password_entry)

    def on_generate_config_button_click(self):
        cfg_window = GenerateConfigWindow()

    def on_add_button_click(self):
        validate_and_save_credentials(self.website_entry, self.username_entry, self.password_entry)
