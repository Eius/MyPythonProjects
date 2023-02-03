import tkinter as tk
from global_data import GlobalData
from styles import CoordinateFrameStyle


class CoordinatesFrame(tk.Frame):
    def __init__(self, master, global_data: GlobalData):
        super().__init__(master,)
        self.style: CoordinateFrameStyle = CoordinateFrameStyle()
        self.global_data: GlobalData = global_data

        # Latitude and longitude column labels
        self.latitude_column_label = tk.Label(self, text="Latitude", **self.style.column_label)
        self.longitude_column_label = tk.Label(self, text="Longitude", **self.style.column_label)

        # Current location labels and entries
        self.current_location_label = tk.Label(self, text="Current location", **self.style.row_label)
        self.current_latitude_entry = tk.Entry(self, **self.style.current_location_entry)
        self.current_latitude_entry.insert(0, f"{global_data.current_location[0]}")
        self.current_longitude_entry = tk.Entry(self, **self.style.current_location_entry)
        self.current_longitude_entry.insert(0, f"{global_data.current_location[1]}")

        # ISS location labels and values
        self.iss_location_label = tk.Label(self, text="ISS location", **self.style.row_label)
        self.iss_current_latitude_label = tk.Label(self, **self.style.row_value)
        self.iss_current_longitude_label = tk.Label(self, **self.style.row_value)

        # Distance and direction labels
        self.distance_label = tk.Label(self, text="Distance:", **self.style.row_label)
        self.distance_value_label = tk.Label(self, **self.style.row_value)
        self.direction_label = tk.Label(self, text="Direction:", **self.style.row_label)
        self.direction_value_label = tk.Label(self, **self.style.row_value)

        # Is night label
        self.is_night_label = tk.Label(self, text="Is night:", **self.style.row_label)
        self.is_night_value_label = tk.Label(self, **self.style.row_value)

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

    def update_data(self):
        # Update current location in GlobalData class
        # If the current location entry is empty, set lat or long to 0.0
        current_lat = self.current_latitude_entry.get()
        current_long = self.current_longitude_entry.get()
        self.global_data.current_location = (float(current_lat) if current_lat else 0.0,
                                             float(current_long) if current_long else 0.0)

        # UPDATE DATA IN WIDGETS
        # Update ISS latitude and longitude value
        self.iss_current_latitude_label.config(text=f"{self.global_data.iss_location[0]}°")
        self.iss_current_longitude_label.config(text=f"{self.global_data.iss_location[1]}°")
        # Update distance and direction value
        self.distance_value_label.config(text=f"{self.global_data.distance} KM")
        self.direction_value_label.config(text=f"{self.global_data.direction}")
        # Update night state
        self.is_night_value_label.config(text=str(self.global_data.is_night))


