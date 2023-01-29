import tkinter as tk
import tkinter.ttk as ttk
from styles import WindowStyle
from frames import VaultFrame


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.style = WindowStyle()
        # -------------- CONFIG WINDOW -------------- #
        self.title("The Vault")

        self.grid_columnconfigure(0, weight=1)

        self.minsize(width=int(self.style.window["min_width"] + self.style.window["pad_x"]/2),
                     height=int(self.style.window["min_height"] + self.style.window["pad_y"]/2))

        self.maxsize(width=int(self.style.window["max_width"] + self.style.window["pad_x"]/2),
                     height=int(self.style.window["max_height"] + self.style.window["pad_y"]/2))

        self.config(pady=self.style.window["pad_y"],
                    padx=self.style.window["pad_x"])

        # -------------- CREATE WIDGETS -------------- #
        self.vault_frame = self.create_vault_frame()

        self.mainloop()

    def create_vault_frame(self):
        return VaultFrame(self)



