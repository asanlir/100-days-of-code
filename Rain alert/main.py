import requests


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "6a42d2c18e29a6e84f2305781ad7323c"


weather_params = {
    "lat": 43.21, #Your city latitude
    "lon": -8.24, #Your city longitude
    "appid": API_KEY,
    "cnt": 4 #Number of timestamps to retrieve (3 hours interval, so 4 means 12 hours)
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"]) #Weather condition code for the first timestamp

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True
if will_rain:
    print("Bring an umbrella!")
