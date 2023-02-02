import globals
import requests
from geopy.distance import great_circle
import math


def update_sunset_sunrise_data():
    """Updates SUNRISE, SUNSET, CIVIL_TWILIGHT, NAUTICAL_TWILIGHT, ASTRONOMICAL_TWILIGHT starts and ends"""
    def update_night_state():
        from datetime import datetime as dt
        current_time = (dt.now().hour, dt.now().minute)
        if current_time[0] < globals.TWILIGHT_BEGIN[0] and current_time[1] < globals.TWILIGHT_BEGIN[1] \
                or current_time[0] > globals.TWILIGHT_END[0] and current_time[1] > globals.TWILIGHT_END[1]:
            globals.IS_NIGHT = True
        else:
            globals.IS_NIGHT = False
    params = {"lat": globals.CURRENT_LOCATION[0], "lng": globals.CURRENT_LOCATION[1], "formatted": 0}
    response = requests.get("https://api.sunrise-sunset.org/json", params=params)
    response.raise_for_status()
    data = response.json()
    begin_hour = data["results"]["nautical_twilight_end"].split("T")[1].split(":")[0]
    begin_minute = data["results"]["nautical_twilight_end"].split("T")[1].split(":")[1]
    end_hour = data["results"]["nautical_twilight_begin"].split("T")[1].split(":")[0]
    end_minute = data["results"]["nautical_twilight_begin"].split("T")[1].split(":")[1]
    globals.TWILIGHT_BEGIN = (int(begin_hour), int(begin_minute))
    globals.TWILIGHT_END = (int(end_hour), int(end_minute))
    update_night_state()




def update_iss_location():
    """Save the International Space Station's latitude and longitude to globals"""
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    latitude = float(data["iss_position"]["latitude"])
    longitude = float(data["iss_position"]["longitude"])
    globals.ISS_LOCATION = (latitude, longitude)


def calculate_distance():
    """Calculate the distance between the current location and ISS location"""
    from geopy.distance import great_circle
    current_location = (globals.CURRENT_LOCATION[0], globals.CURRENT_LOCATION[1])
    iss_location = (globals.ISS_LOCATION[0], globals.ISS_LOCATION[1])
    distance = round(great_circle(current_location, iss_location).km, 2)
    return distance


def calculate_direction():
    def get_directional_letter(brng):
        if brng >= 337.5 or brng < 22.5:
            return "N"
        elif 22.5 <= brng < 67.5:
            return "NE"
        elif 67.5 <= brng < 112.5:
            return "E"
        elif 112.5 <= brng < 157.5:
            return "SE"
        elif 157.5 <= brng < 202.5:
            return "S"
        elif 202.5 <= brng < 247.5:
            return "SW"
        elif 247.5 <= brng < 292.5:
            return "W"
        elif 292.5 <= brng < 337.5:
            return "NW"
    lat1, lon1 = math.radians(globals.CURRENT_LOCATION[0]), math.radians(globals.CURRENT_LOCATION[1])
    lat2, lon2 = math.radians(globals.ISS_LOCATION[0]), math.radians(globals.ISS_LOCATION[1])
    d_lon = lon2 - lon1
    y = math.sin(d_lon) * math.cos(lat2)
    x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(d_lon)
    bearing = math.atan2(y, x)
    bearing = math.degrees(bearing)
    bearing = round((bearing + 360) % 360, 2)
    bearing = str(bearing) + "° " + get_directional_letter(bearing)
    return bearing


