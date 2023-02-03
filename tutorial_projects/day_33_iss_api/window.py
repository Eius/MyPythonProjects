from tkinter import Tk
from frames.coordinates_frame import CoordinatesFrame
from threading import Thread
from global_data import GlobalData


class Window(Tk):
    def __init__(self, global_data: GlobalData):
        super().__init__()
        # Save reference to global data class
        self.global_data: GlobalData = global_data

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
        print("\n\nStarting update thread")
        update_thread = self.global_data.async_update_data()
        self.monitor(update_thread)

    def monitor(self, thread: Thread, total_runtime=0.0):
        if thread.is_alive():
            total_runtime += 0.1
            self.after(100, lambda: self.monitor(thread, total_runtime))
        else:
            print("Update thread finished")
            print(f"Total runtime: {round(total_runtime, 2)}")
            self.coordinates_frame.update_data()
            self.update_loop()
            # self.after(5000, self.update_loop)


