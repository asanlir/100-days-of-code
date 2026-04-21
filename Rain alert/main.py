import os
from pathlib import Path

import requests
from twilio.rest import Client


def load_dotenv(dotenv_path: Path) -> None:
    if not dotenv_path.exists():
        return
    for line in dotenv_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip())


load_dotenv(Path(__file__).with_name(".env"))


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = os.environ.get("OWM_API_KEY")
acount_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")


weather_params = {
    "lat": 43.21,  # Your city latitude
    "lon": -8.24,  # Your city longitude
    "appid": API_KEY,
    # Number of timestamps to retrieve (3 hours interval, so 4 means 12 hours)
    "cnt": 4
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# weather_data["list"][0]["weather"][0]["id"] #Weather condition code for the first timestamp

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True
if will_rain:
    client = Client(acount_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☂️",
        from_="+1234567890",  # Your Twilio number
        to="+0987654321"  # Your phone number
    )
