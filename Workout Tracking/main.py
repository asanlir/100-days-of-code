import requests
from datetime import datetime


GENDER = "YOUR_GENDER"
WEIGHT_KG = "YOUR_WEIGHT"
HEIGHT_CM = "YOUR_HEIGHT"
AGE = "YOUR_AGE"

APP_ID = "YOUR_APP_ID"
API_KEY = "YOUR_API_KEY"


exercise_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
sheet_endpoint = "YOUR_SHEETY_ENDPOINT"


exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    print(sheet_response.text)
