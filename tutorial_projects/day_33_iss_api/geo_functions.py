import requests
import math
from geopy.distance import great_circle


def update_time_data(global_data):
    """Updates night state and TWILIGHT start and end"""
    # TWILIGHT BEGIN/END
    params = {"lat": global_data.current_location[0], "lng": global_data.current_location[1], "formatted": 0}
    response = requests.get("https://api.sunrise-sunset.org/json", params=params)
    response.raise_for_status()
    data = response.json()
    return data


def update_iss_location() -> (float, float):
    """Save the International Space Station's latitude and longitude to globals"""
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    latitude = float(data["iss_position"]["latitude"])
    longitude = float(data["iss_position"]["longitude"])
    return latitude, longitude


def calculate_distance(global_data) -> float:
    """Calculate the distance between the current location and ISS location"""
    current_location = (global_data.current_location[0], global_data.current_location[1])
    iss_location = (global_data.iss_location()[0], global_data.iss_location()[1])
    distance = round(great_circle(current_location, iss_location).km, 2)
    return distance


def calculate_direction(global_data) -> str:
    def get_directional_letter(brng):
        directional_letters = {
            (337.5, 360.0) + (0.0, 22.5): "N",
            (22.5, 67.5): "NE",
            (67.5, 112.5): "E",
            (112.5, 157.5): "SE",
            (157.5, 202.5): "S",
            (202.5, 247.5): "SW",
            (247.5, 292.5): "W",
            (292.5, 337.5): "NW"
        }
        for interval, letter in directional_letters.items():
            if interval[0] <= brng < interval[1]:
                return letter
    lat1, lon1 = math.radians(global_data.current_location[0]), math.radians(global_data.current_location[1])
    lat2, lon2 = math.radians(global_data.iss_location()[0]), math.radians(global_data.iss_location()[1])
    d_lon = lon2 - lon1
    y = math.sin(d_lon) * math.cos(lat2)
    x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(d_lon)
    bearing = math.atan2(y, x)
    bearing = math.degrees(bearing)
    bearing = round((bearing + 360) % 360, 2)
    bearing = f"{bearing}° {get_directional_letter(bearing)}"
    return bearing
