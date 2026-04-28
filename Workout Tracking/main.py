import requests

GENDER = "YOUR_GENDER"
WEIGHT_KG = "YOUR_WEIGHT"
HEIGHT_CM = "YOUR_HEIGHT"
AGE = "YOUR_AGE"

APP_ID = "YOUR_APP_ID"
API_KEY = "YOUR_API_KEY"

exercise_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

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
print(result)
