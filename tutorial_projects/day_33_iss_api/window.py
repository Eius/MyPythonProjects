from tkinter import Tk
from frames.coordinates_frame import CoordinatesFrame


class Window(Tk):
    def __init__(self, global_data):
        super().__init__()
        # Save reference to global data class
        self.global_data = global_data

        # Config window
        self.title("ISS Location Tracker")
        self.config(padx=18, pady=18)

        # Create frames
        self.coordinates_frame = CoordinatesFrame(self, self.global_data)

        # Start update loop
        self.update_loop()

        # Start tkinter mainloop
        self.mainloop()

    def update_loop(self):
        self.coordinates_frame.update_loop()
        self.after(100, self.update_loop)
