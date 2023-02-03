from tkinter import Tk
from frames.data_frame import DataFrame
import threading


class Window(Tk):
    def __init__(self, global_data):
        super().__init__()
        # Save reference to global data class
        self.global_data = global_data

        # Config window
        self.title("ISS Location Tracker")
        self.config(padx=18, pady=18)

        # Create frames
        self.coordinates_frame = DataFrame(self, self.global_data)

        # Start update loop
        self.update_loop()

        # Start tkinter mainloop
        self.mainloop()

    def update_loop(self):
        self.coordinates_frame.update_loop()
        self.after(5000, self.update_loop)
