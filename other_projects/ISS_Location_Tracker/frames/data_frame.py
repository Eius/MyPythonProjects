import tkinter as tk
from global_data import GlobalData
from styles import DataFrameStyle

FONT_BOLD = ("Arial", 10, "bold")
FONT_NORMAL = ("Arial", 9, "normal")


class DataFrame(tk.Frame):
    def __init__(self, master, global_data: GlobalData):
        super().__init__(master)
        self.style = DataFrameStyle()
        self.global_data = global_data

        # Latitude and longitude column labels
        self.latitude_column_label = tk.Label(self, text="Latitude", font=FONT_BOLD)
        self.longitude_column_label = tk.Label(self, text="Longitude", font=FONT_BOLD)

        # Current location labels and entries
        self.current_location_label = tk.Label(self, text="Current location:", anchor="e", font=FONT_BOLD)
        self.current_latitude_entry = tk.Entry(self, justify="center", bg="#c2ffc2", font=FONT_NORMAL)
        self.current_latitude_entry.insert(0, f"{global_data.current_location[0]}")
        self.current_longitude_entry = tk.Entry(self, justify="center", bg="#c2ffc2", font=FONT_NORMAL)
        self.current_longitude_entry.insert(0, f"{global_data.current_location[1]}")

        # ISS location labels and values
        self.iss_location_label = tk.Label(self, text="ISS location:", anchor="e", font=FONT_BOLD)
        self.iss_current_latitude_label = tk.Label(self, bd=2, relief="ridge", font=FONT_NORMAL)
        self.iss_current_longitude_label = tk.Label(self, bd=2, relief="ridge", font=FONT_NORMAL)

        # Distance and direction labels
        self.distance_label = tk.Label(self, text="Distance:", anchor="e", font=FONT_BOLD)
        self.distance_value_label = tk.Label(self, bd=2, relief="ridge", font=FONT_NORMAL)
        self.direction_label = tk.Label(self, text="Direction:", anchor="e", font=FONT_BOLD)
        self.direction_value_label = tk.Label(self, bd=2, relief="ridge", font=FONT_NORMAL)

        # Is night label
        self.is_night_label = tk.Label(self, text="Is night:", anchor="e", font=FONT_BOLD)
        self.is_night_value_label = tk.Label(self, bd=2, relief="ridge", font=FONT_NORMAL)

        # ARRANGE WIDGETS
        self.grid(column=0, row=0)
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
        self.distance_label.grid(column=0, row=3, sticky="ew", padx=(0, 5))
        self.distance_value_label.grid(column=1, row=3, columnspan=2, sticky="ew")
        # Row 4
        self.direction_label.grid(column=0, row=4, sticky="ew", padx=(0, 5))
        self.direction_value_label.grid(column=1, row=4, columnspan=2, sticky="ew")
        # Row 5
        self.is_night_label.grid(column=0, row=5, sticky="ew", padx=(0, 5))
        self.is_night_value_label.grid(column=1, row=5, columnspan=2, sticky="ew")

    def update_loop(self):
        print("Started updating")
        # Update current location
        self.global_data.current_location = (float(self.current_latitude_entry.get()),
                                             float(self.current_longitude_entry.get()))
        # Update ISS latitude and longitude value
        self.iss_current_latitude_label.config(text=f"{self.global_data.iss_location()[0]}°")
        self.iss_current_longitude_label.config(text=f"{self.global_data.iss_location()[1]}°")
        # Update distance and direction value
        self.distance_value_label.config(text=f"{self.global_data.distance()} KM")
        self.direction_value_label.config(text=f"{self.global_data.distance()}")
        # Update night state
        self.is_night_value_label.config(text=str(self.global_data.is_night()))
        print(f"Is night: {self.global_data.is_night()}")
        print("Update successful")


