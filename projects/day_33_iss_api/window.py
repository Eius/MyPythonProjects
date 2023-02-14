from tkinter import Tk
from frames.coordinates_frame import CoordinatesFrame
from threading import Thread
from global_data import GlobalData
from timeit import default_timer


class Window(Tk):
    def __init__(self, global_data: GlobalData):
        self.loop_handle = None
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

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Start tkinter mainloop
        self.mainloop()

    def update_loop(self):
        print("\n\nStarting update thread")
        update_thread = self.global_data.async_update_data()
        start_time = default_timer()
        self.monitor(update_thread, start_time)

    def monitor(self, thread: Thread, start_time):
        if thread.is_alive():
            self.after(100, lambda: self.monitor(thread, start_time))
        else:
            print("Update thread finished")
            end_time = default_timer()
            print(f"Total runtime: {round(end_time - start_time, 2)} second(s)")
            self.coordinates_frame.update_data()
            self.loop_handle = self.after(5000, self.update_loop)

    def on_closing(self):
        print("Terminating program...")
        self.destroy()

