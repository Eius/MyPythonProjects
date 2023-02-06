import cachetools
from typing import Literal
from datetime import datetime as dt


class GlobalData:
    def __init__(self):
        # Cached data
        self._time_data_cache = cachetools.TTLCache(maxsize=1, ttl=3600)
        self._iss_location_cache = cachetools.TTLCache(maxsize=1, ttl=5)

        # (LATITUDE, LONGITUDE)
        self.current_location: (float, float) = (0, 0)

        # Current location twilight type (civil, nautical, astronomical)
        self.twilight_type: Literal["civil", "nautical", "astronomical"] = "nautical"

    def iss_location(self) -> (float, float):
        if "iss_data" in self._iss_location_cache:
            return self._iss_location_cache["iss_data"]
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
        if "time_data" in self._time_data_cache:
            data = self._time_data_cache["time_data"]
        else:
            data = update_time_data(self)
            self._time_data_cache["time_data"] = data

        twilight_begin_12h = dt.strptime(data["results"][f"{self.twilight_type}_twilight_end"], '%I:%M:%S %p')
        twilight_begin_24h = twilight_begin_12h.strftime('%H:%M:%S')
        twilight_begin_dt = dt.strptime(twilight_begin_24h, '%H:%M:%S')

        return twilight_begin_dt.hour, twilight_begin_dt.minute

    def twilight_end(self) -> (int, int):
        if "time_data" in self._time_data_cache:
            data = self._time_data_cache["time_data"]
        else:
            data = update_time_data(self)
            self._time_data_cache["time_data"] = data

        twilight_end_12h = dt.strptime(data["results"][f"{self.twilight_type}_twilight_begin"], '%I:%M:%S %p')
        twilight_end_24h = twilight_end_12h.strftime('%H:%M:%S')
        twilight_end_dt = dt.strptime(twilight_end_24h, '%H:%M:%S')

        return twilight_end_dt.hour, twilight_end_dt.minute
