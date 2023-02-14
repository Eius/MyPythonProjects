import os
import requests
from datetime import datetime

query = input("Write out your exercises: ")

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
workout_sheet_endpoint = "https://api.sheety.co/ed067959202a14e3d77b1d11d5b33973/myWorkouts/workouts"

headers = {
    "x-app-key": os.environ.get("APP_KEY"),
    "x-app-id": os.environ.get("APP_ID"),
    "x-remote-user-id": "0"
}

params = {
    "query": query,
    "gender": "male",
    "weight_kg": 65,
    "height_cm": 181,
    "age": 23
}

response = requests.post(url=nutritionix_endpoint, json=params, headers=headers)
print(response.json())

exercises = []
for item in response.json()["exercises"]:
    exercise = {
        "name": item["name"],
        "duration": item["duration_min"],
        "calories": item["nf_calories"]
    }
    exercises.append(exercise)

for exercise in exercises:
    headers = {
        "Authorization": f"Basic {os.environ.get('TOKEN')}"
    }

    params = {
        "workout": {
            "date": datetime.today().strftime("%d/%m/%Y"),
            "time": datetime.today().strftime("%H:%M:00"),
            "exercise": exercise["name"].capitalize(),
            "duration": f"{exercise['duration']}m",
            "calories": exercise["calories"]
        }
    }
    response = requests.post(url=workout_sheet_endpoint, json=params, headers=headers)
