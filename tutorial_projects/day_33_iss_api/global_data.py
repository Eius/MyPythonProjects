import cachetools
from typing import Literal
from geo_functions import update_iss_location, update_time_data, calculate_direction, calculate_distance
from datetime import datetime as dt


class GlobalData:
    def __init__(self):
        self._time_cache = cachetools.TTLCache(maxsize=1, ttl=3600)
        self._iss_cache = cachetools.TTLCache(maxsize=1, ttl=5)

        # (LATITUDE, LONGITUDE)
        self.current_location: (float, float) = (0, 0)

        # Current location twilight type (civil, nautical, astronomical)
        self.twilight_type: Literal["civil", "nautical", "astronomical"] = "nautical"

    def iss_location(self) -> (float, float):
        if "iss_data" in self._iss_cache:
            return self._iss_cache["iss_data"]
        else:
            return update_iss_location()

    def distance(self):
        return calculate_distance(self)

    def direction(self):
        return calculate_direction(self)

    def is_night(self):
        current_time = (dt.now().hour, dt.now().minute)
        if current_time[0] < self.twilight_begin()[0] and current_time[1] < self.twilight_begin()[1] \
                or current_time[0] > self.twilight_end()[0] and current_time[1] > self.twilight_end()[1]:
            return True
        else:
            return False

    def twilight_begin(self) -> (int, int):
        if "time_data" in self._time_cache:
            data = self._time_cache["time_data"]
        else:
            data = update_time_data(self)

        twilight_begin = dt.strptime(data["results"][f"{self.twilight_type}_twilight_end"], '%I:%M:%S %p')
        twilight_begin_24h = dt.strptime(twilight_begin.strftime("%H:%M"), "%H:%M")
        return twilight_begin_24h.hour, twilight_begin_24h.minute
# TODO convert 12h to 24h, got some error idk I am tired
    def twilight_end(self) -> (int, int):
        if "time_data" in self._time_cache:
            data = self._time_cache["time_data"]
        else:
            data = update_time_data(self)

        twilight_end = dt.strptime(data["results"][f"{self.twilight_type}_twilight_begin"], '%I:%M:%S %p')
        twilight_end_24h = dt.strptime(twilight_end.strftime("%H:%M"), "%H:%M")
        return twilight_end_24h.hour, twilight_end_24h.minute
