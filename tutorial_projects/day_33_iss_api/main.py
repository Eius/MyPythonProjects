import requests
from datetime import datetime
import time
from geopy.distance import great_circle
import smtplib
import json
from email.mime.text import MIMEText
import math


def load_credentials():
    try:
        with open("data/credentials.json", "r") as file:
            credentials = json.load(file)

    except FileNotFoundError:
        error_message = "Credential Error: Required information is missing." \
                        "Please enter your email provider credentials.\n" \
                        "For Gmail users, it is necessary to create an app password." \
                        "For more information on this process, refer to the following link:\n" \
                        "https://support.google.com/accounts/answer/185833?visit_id=638107597085752106-702683512&" \
                        "p=InvalidSecondFactor&rd=1#zippy=%2Cwhy-you-may-need-an-app-password"
        print(error_message)
        try:
            username = input("Your email username: ")
            password = input("Your email password: ")
        except EOFError:
            print("Terminating program...")
            exit()
        credentials = {
            "username": f"{username}",
            "password": f"{password}"
        }
        with open("data/credentials.json", "w") as file:
            json.dump(credentials, file, indent=4)
    return credentials


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }
    req = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    req.raise_for_status()
    data = req.json()
    sunrise = int(data["results"]["nautical_twilight_begin"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["nautical_twilight_end"].split("T")[1].split(":")[0])
    time_now = int(datetime.now().hour)
    global IS_NIGHT
    if time_now < sunrise or time_now > sunset:
        return True
    else:
        return False


def is_iss_overhead():
    req = requests.get(url="http://api.open-notify.org/iss-now.json")
    req.raise_for_status()
    global ISS_LAT, ISS_LONG
    ISS_LAT = float(req.json()["iss_position"]["latitude"])
    ISS_LONG = float(req.json()["iss_position"]["longitude"])
    # Your position is within +5 or -5 degress of the ISS position
    if MY_LAT - 5.0 <= ISS_LAT <= MY_LAT + 5.0 and MY_LONG - 5.0 <= ISS_LONG <= MY_LONG + 5.0:
        return True
    else:
        return False


def print_info():

    print(f"Your coords: Lat: {MY_LAT} | Long: {MY_LONG}")
    print(f"ISS coords: Lat: {ISS_LAT} | Long: {ISS_LONG}")
    distance = f"{great_circle((MY_LAT, MY_LONG), (ISS_LAT, ISS_LONG)).km:.2f}"
    print(f"Distance to ISS: {distance} km")
    degrees = round(direction(MY_LAT, MY_LONG, ISS_LAT, ISS_LONG), 2)
    print(f"Direction to ISS: {degrees}° (N: 0°, E: 90°, S:180°, W: 270°)")
    today = datetime.today()
    print(f"Timestamp: {str(today.day).zfill(2)}.{str(today.month).zfill(2)}.{today.year} "
          f"{str(today.hour).zfill(2)}:{str(today.minute).zfill(2)}:{str(today.second).zfill(2)}")
    print(f"Is night: {IS_NIGHT}")


def direction(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    y = math.sin(lon2 - lon1) * math.cos(lat2)
    x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(lon2 - lon1)
    return math.degrees(math.atan2(y, x)) % 360


def send_email(subject: str, message: str):

    message = MIMEText(message, "plain", "utf-8")
    message["Subject"] = subject
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=CREDENTIALS["username"], password=CREDENTIALS["password"])
        connection.sendmail(from_addr=CREDENTIALS["username"],
                            to_addrs=CREDENTIALS["username"],
                            msg=message.as_bytes())


MY_LAT = 48.328870
MY_LONG = 17.870020
ISS_LAT = 0
ISS_LONG = 0
IS_NIGHT = True
CREDENTIALS = load_credentials()

while True:
    print("\nChecking...")
    IS_NIGHT = is_night()
    if is_iss_overhead() and IS_NIGHT:
        print("ISS can be seen from my location.")
    else:
        print("ISS can't be seen from my location.")
    print_info()
    time.sleep(30)
