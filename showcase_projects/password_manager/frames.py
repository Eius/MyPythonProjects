import tkinter.ttk as ttk
import tkinter as tk
from tkinter.constants import *
from styles import VaultFrameStyle
from logic import validate_input, save_credentials, generate_password


class VaultFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__()
        # ------------- GET FRAME STYLE ------------- #
        self.style = VaultFrameStyle()

        # --------------- CONFIG FRAME --------------- #
        self.config(style="MainFrame.TFrame")

        # -------------- CREATE WIDGETS -------------- #
        self.bg_image = self.create_bg_image(self.style.bg_image)

        # LABELS #
        self.website_label = ttk.Label(self, text="Website: ", style="Bold.TLabel")
        self.email_username_label = ttk.Label(self, text="Email/Username: ", style="Bold.TLabel")
        self.password_label = ttk.Label(self, text="Password: ", style="Bold.TLabel")

        # ENTRIES #
        self.website_entry = ttk.Entry(self, style="Website.TEntry")
        self.website_entry.focus()
        self.email_username_entry = ttk.Entry(self, style="Email_Username.TEntry")
        self.password_entry = ttk.Entry(self, style="Password.TEntry")

        # BUTTONS #
        self.add_button = ttk.Button(self, text="Add", style="Add.TButton", command=self.on_add_button_click)
        self.generate_button = ttk.Button(self, text="Generate", style="Generate.TButton", command=self.on_generate_button_click)

        # -------------- ARRANGE WIDGETS -------------- #
        self.arrange_widgets()

    def on_add_button_click(self):
        website = self.website_entry.get()
        email_username = self.email_username_entry.get()
        password = self.password_entry.get()

        if validate_input(website, email_username, password):
            save_credentials(website,email_username,password)
            self.website_entry.delete(0, END)
            self.email_username_entry.delete(0, END)
            self.password_entry.delete(0, END)

    def on_generate_button_click(self):
        self.password_entry.delete(0, END)
        self.password_entry.insert(0, generate_password())

    def create_bg_image(self, style):
        canvas = tk.Canvas(self,
                           width=style["width"],
                           height=style["height"],
                           highlightthickness=style["highlightthickness"])

        img = tk.PhotoImage(file=style["image_path"])
        canvas.img = img
        canvas.create_image(style["image_x"], style["image_y"], image=img)
        return canvas

    def arrange_widgets(self):
        self.pack(fill="both", expand=True) # Frame grid placement
        self.bg_image.grid(column=0, row=0, columnspan=3, sticky="ew", pady=(0, 10))
        # LABELS #
        self.website_label.grid(column=0, row=1, sticky="ew")
        self.email_username_label.grid(column=0, row=2, sticky="ew")
        self.password_label.grid(column=0, row=3, sticky="ew")
        # ENTRIES #
        self.website_entry.grid(column=1, row=1, columnspan=2, sticky="ew")
        self.email_username_entry.grid(column=1, row=2, columnspan=2, sticky="ew")
        self.password_entry.grid(column=1, row=3, sticky="ew",)
        # BUTTONS #
        self.add_button.grid(column=1, row=4, columnspan=2, sticky="ew")
        self.generate_button.grid(column=2, row=3, sticky="ew", padx=(10, 0))
