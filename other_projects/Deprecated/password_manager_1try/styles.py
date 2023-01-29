from tkinter import ttk
from tkinter.ttk import Style


class WindowStyle(Style):
    def __init__(self):
        super().__init__()
        self.window = {
            "min_width": 500,
            "min_height": 320,
            "max_width": 500,
            "max_height": 320,
            "pad_x": 5,
            "pad_y": 5
        }


class VaultFrameStyle(Style):
    def __init__(self):
        super().__init__()
        self.configure("MainFrame.TFrame"
                       )

        self.bg_image = {
            "width": 500,
            "height": 200,
            "image_x": 400,
            "image_y": 200,
            "highlightthickness": 0,
            "image_path": "resources/vault_img.png"
        }

        self.configure("Normal.TLabel",
                       font=("Arial", 11, "bold"),
                       )

        self.configure("Bold.TLabel",
                       font=("Arial", 11, "bold"),
                       anchor="center"
                       )

        self.configure("Website.TEntry",
                       width=35
                       )

        self.configure("Email_Username.TEntry",
                       width=35
                       )

        self.configure("Password.TEntry",
                       width=21
                       )

        self.configure("Add.TButton",
                       width=36,
                       font=("Arial", 10, "normal")
                       )

        self.configure("Generate.TButton",
                       width=15,
                       margin=(50, 50, 50, 50),
                       font=("Arial", 10, "normal")
                       )
