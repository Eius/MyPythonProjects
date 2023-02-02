from tkinter import Tk
import tkinter as tk
import globals
from geo_functions import *

FONT_BOLD = ("Arial", 10, "bold")
FONT_NORMAL = ("Arial", 9, "normal")

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("ISS Location Tracker")
        self.config(padx=18, pady=18)

        # Latitude and longitude column labels
        self.latitude_column_label = tk.Label(self, text="Latitude", font=FONT_BOLD)
        self.longitude_column_label = tk.Label(self, text="Longitude", font=FONT_BOLD)

        # Current location labels and entries
        self.current_location_label = tk.Label(self, text="Current location:", anchor="e", font=FONT_BOLD)
        self.current_latitude_entry = tk.Entry(self, justify="center", bg="#c2ffc2", font=FONT_NORMAL)
        self.current_latitude_entry.insert(0, f"{globals.CURRENT_LOCATION[0]}")
        self.current_longitude_entry = tk.Entry(self, justify="center", bg="#c2ffc2", font=FONT_NORMAL)
        self.current_longitude_entry.insert(0, f"{globals.CURRENT_LOCATION[1]}")

        # ISS location labels and values
        self.iss_location_label = tk.Label(self, text="ISS location:", anchor="e", font=FONT_BOLD)
        self.iss_current_latitude_label = tk.Label(self, bd=2, relief="ridge", font=FONT_NORMAL)
        self.iss_current_longitude_label = tk.Label(self, bd=2, relief="ridge", font=FONT_NORMAL)

        # Dividing line
        self.dividing_line = tk.Canvas(self, height=2, highlightthickness=0)
        self.dividing_line.config(background="#555755")

        # Distance and direction labels
        self.distance_label = tk.Label(self, text="Distance:", anchor="e", font=FONT_BOLD)
        self.distance_value_label = tk.Label(self, bd=2, relief="ridge", font=FONT_NORMAL)
        self.direction_label = tk.Label(self, text="Direction:", anchor="e", font=FONT_BOLD)
        self.direction_value_label = tk.Label(self, bd=2, relief="ridge", font=FONT_NORMAL)

        # Is night label
        self.is_night_label = tk.Label(self, text="Is night:", anchor="e", font=FONT_BOLD)
        self.is_night_value_label = tk.Label(self, bd=2, relief="ridge", font=FONT_NORMAL)

        # Arrange widgets and start update loop
        self.arrange_widgets()
        self.loop_handle = self.update_loop()

        # Start tkinter mainloop
        self.mainloop()

    def arrange_widgets(self):
        # Row 0
        self.latitude_column_label.grid(column=1, row=0, sticky="ew")
        self.longitude_column_label.grid(column=2, row=0, sticky="ew")

        # Row 1
        self.current_location_label.grid(column=0, row=1, sticky="ew", padx=(0, 5))
        self.current_latitude_entry.grid(column=1, row=1, sticky="ew")
        self.current_longitude_entry.grid(column=2, row=1, sticky="ew")

        # Row 2
        self.iss_location_label.grid(column=0, row=2, sticky="ew", padx=(0, 5))
        self.iss_current_latitude_label.grid(column=1, row=2, sticky="ew")
        self.iss_current_longitude_label.grid(column=2, row=2, sticky="ew")

        # Row 3
        self.dividing_line.grid(column=0, row=3, columnspan=3, sticky="ew")

        # Row 4
        self.distance_label.grid(column=0, row=4, sticky="ew", padx=(0, 5))
        self.distance_value_label.grid(column=1, row=4, columnspan=2, sticky="ew")

        # Row 5
        self.direction_label.grid(column=0, row=5, sticky="ew", padx=(0, 5))
        self.direction_value_label.grid(column=1, row=5, columnspan=2, sticky="ew")

        # Row 6
        self.is_night_label.grid(column=0, row=6, sticky="ew", padx=(0, 5))
        self.is_night_value_label.grid(column=1, row=6, columnspan=2, sticky="ew")

    def update_loop(self):
        print("Started updating")
        # Update realtime data from APIs
        update_sunset_sunrise_data()
        update_iss_location()
        # Update current location
        globals.CURRENT_LOCATION = (float(self.current_latitude_entry.get()), float(self.current_longitude_entry.get()))
        # Update ISS latitude and longitude value
        self.iss_current_latitude_label.config(text=f"{globals.ISS_LOCATION[0]}°")
        self.iss_current_longitude_label.config(text=f"{globals.ISS_LOCATION[1]}°")
        # Update distance and direction value
        self.distance_value_label.config(text=f"{calculate_distance()} KM")
        self.direction_value_label.config(text=f"{calculate_direction()}")
        # Update night state
        self.is_night_value_label.config(text=str(globals.IS_NIGHT))
        print(globals.IS_NIGHT)
        print("Update successful")
        return self.after(5000, self.update_loop)
