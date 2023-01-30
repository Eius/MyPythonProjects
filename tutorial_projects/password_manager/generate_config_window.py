import tkinter as tk
from tkinter import BooleanVar
from tkinter import Toplevel
from utilities import get_style, get_config, save_config


class GenerateConfigWindow(Toplevel):
    def __init__(self):
        super().__init__()
        self.style = get_style("generate_config_window")
        self.cfg = get_config()
        self.focus()
        self.title = "Password generator config"
        self.config(pady=12, padx=12)

        # Labels
        self.lowercase_label = tk.Label(self, text="Include lowercase characters:", font=self.style["font_normal"], anchor="e")
        self.uppercase_label = tk.Label(self, text="Include uppercase characters:", font=self.style["font_normal"], anchor="e")
        self.numbers_label = tk.Label(self, text="Include numbers:", font=self.style["font_normal"], anchor="e")
        self.symbols_label = tk.Label(self, text="Include symbols:", font=self.style["font_normal"], anchor="e")

        # Checkbuttons
        self.lower_bool = BooleanVar()
        self.lowercase_checkbutton = tk.Checkbutton(self, anchor="w", variable=self.lower_bool)
        self.upper_bool = BooleanVar()
        self.uppercase_checkbutton = tk.Checkbutton(self, anchor="w", variable=self.upper_bool)
        self.numbers_bool = BooleanVar()
        self.numbers_checkbutton = tk.Checkbutton(self, anchor="w", variable=self.numbers_bool)
        self.symbols_bool = BooleanVar()
        self.symbols_checkbutton = tk.Checkbutton(self, anchor="w", variable=self.symbols_bool)

        # Checkbutton labels
        self.lowercase_check_label = tk.Label(self, text="( e.g. abcdefgh )", font=self.style["font_normal"], anchor="w")
        self.uppercase_check_label = tk.Label(self, text="( e.g. ABCDEFGH )", font=self.style["font_normal"], anchor="w")
        self.numbers_check_label = tk.Label(self, text="( e.g. 123456 )", font=self.style["font_normal"], anchor="w")
        self.symbols_check_label = tk.Label(self, text="( e.g. @#$% )", font=self.style["font_normal"], anchor="w")

        # Buttons
        self.cancel_button = tk.Button(self, text="Cancel", font=self.style["font_bold"], command=self.on_cancel_click, width=20)
        self.save_button = tk.Button(self, text="Save", font=self.style["font_bold"], command=self.on_save_click, width=20)

        self.arrange_widgets()
        self.mainloop()

    def arrange_widgets(self):
        # Labels
        self.lowercase_label.grid(column=0, row=0, columnspan=2, sticky="ew")
        self.uppercase_label.grid(column=0, row=1, columnspan=2, sticky="ew")
        self.numbers_label.grid(column=0, row=2, columnspan=2, sticky="ew")
        self.symbols_label.grid(column=0, row=3, columnspan=2, sticky="ew")
        # Checkbuttons
        self.lowercase_checkbutton.grid(column=2, row=0, sticky="ew")
        self.uppercase_checkbutton.grid(column=2, row=1, sticky="ew")
        self.numbers_checkbutton.grid(column=2, row=2, sticky="ew")
        self.symbols_checkbutton.grid(column=2, row=3, sticky="ew")
        # Checkbuttons labels
        self.lowercase_check_label.grid(column=2, row=0, sticky="ew", padx=20)
        self.uppercase_check_label.grid(column=2, row=1, sticky="ew", padx=20)
        self.numbers_check_label.grid(column=2, row=2, sticky="ew", padx=20)
        self.symbols_check_label.grid(column=2, row=3, sticky="ew", padx=20)
        # Buttons
        self.cancel_button.grid(column=0, row=4, sticky="ew", padx=(0, 3), pady=(7, 0))
        self.save_button.grid(column=2, row=4, sticky="ew", padx=(3, 0), pady=(7, 0))

    def on_cancel_click(self):
        self.destroy()

    def on_save_click(self):
        new_config = {"password_generator": {
                "include_lowercase": str(self.lower_bool.get()),
                "include_uppercase": str(self.upper_bool.get()),
                "include_numbers": str(self.numbers_bool.get()),
                "include_symbols": str(self.symbols_bool.get())
            }}
        save_config(new_config)
        self.destroy()
