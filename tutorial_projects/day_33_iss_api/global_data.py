from threading import Thread
import cachetools
from typing import Literal
import geo_functions
from datetime import datetime as dt


class GlobalData:
    def __init__(self):
        # Cached data
        self.time_data_cache = cachetools.TTLCache(maxsize=1, ttl=60)
        self.iss_location_cache = cachetools.TTLCache(maxsize=1, ttl=5)

        # (LATITUDE, LONGITUDE)
        self.current_location: (float, float) = (48.328869, 17.870020)
        self.iss_location: (float, float) = (0.0, 0.0)

        # Distance and direction to ISS
        self.distance: str = "0.0 km"
        self.direction: str = "0.0° S"

        # Twilight start and end
        self.night_begin: (int, int) = (0, 0)
        self.night_end: (int, int) = (0, 0)

        # Is night
        self.is_night: str = "False"

        # Current location twilight type (civil, nautical, astronomical)
        self.twilight_type: Literal["civil", "nautical", "astronomical"] = "nautical"

    def async_update_data(self):
        thread = AsyncUpdateData(self)
        thread.start()
        return thread


class AsyncUpdateData(Thread):
    def __init__(self, global_data: GlobalData):
        super().__init__()
        self.global_data: GlobalData = global_data

    def run(self):
        self._update_iss_location()
        self._update_night_begin()
        self._update_night_end()
        self._update_is_night()
        self._update_distance()
        self._update_direction()

    def _update_iss_location(self):
        if "iss_location" in self.global_data.iss_location_cache:
            data = self.global_data.iss_location_cache["iss_location"]
            print("ISS Location: Used cached ISS location data")
        else:
            data = geo_functions.fetch_iss_location()
            self.global_data.iss_location_cache["iss_location"] = data
            print("ISS Location: Fetched new ISS location data")
        self.global_data.iss_location = data

    def _update_night_begin(self):
        if "time_data" in self.global_data.time_data_cache:
            data = self.global_data.time_data_cache["time_data"]
            print("Night begin: Used cached time data")
        else:
            data = geo_functions.fetch_time_data(self.global_data)
            self.global_data.time_data_cache["time_data"] = data
            print("Night begin: Fetched new time data")
        twilight_begin_12h = dt.strptime(data["results"][f"{self.global_data.twilight_type}_twilight_end"], '%I:%M:%S %p')
        twilight_begin_24h = twilight_begin_12h.strftime('%H:%M:%S')
        twilight_begin_dt = dt.strptime(twilight_begin_24h, '%H:%M:%S')
        self.global_data.night_begin = (twilight_begin_dt.hour, twilight_begin_dt.minute)

    def _update_night_end(self):
        if "time_data" in self.global_data.time_data_cache:
            data = self.global_data.time_data_cache["time_data"]
            print("Night begin: Used cached time data")
        else:
            data = geo_functions.fetch_time_data(self.global_data)
            self.global_data.time_data_cache["time_data"] = data
            print("Night begin: Fetched new time data")
        twilight_end_12h = dt.strptime(data["results"][f"{self.global_data.twilight_type}_twilight_begin"], '%I:%M:%S %p')
        twilight_end_24h = twilight_end_12h.strftime('%H:%M:%S')
        twilight_end_dt = dt.strptime(twilight_end_24h, '%H:%M:%S')
        self.global_data.night_end = (twilight_end_dt.hour, twilight_end_dt.minute)

    def _update_is_night(self):
        current_time = (dt.now().hour, dt.now().minute)
        if current_time[0] > self.global_data.night_begin[0] and current_time[1] > self.global_data.night_begin[1] \
                or current_time[0] < self.global_data.night_end[0] and current_time[1] < self.global_data.night_end[1]:
            self.global_data.is_night = "True"
        else:
            self.global_data.is_night = "False"

    def _update_distance(self):
        self.global_data.distance = geo_functions.calculate_distance(self.global_data)

    def _update_direction(self):
        self.global_data.direction = geo_functions.calculate_direction(self.global_data)
