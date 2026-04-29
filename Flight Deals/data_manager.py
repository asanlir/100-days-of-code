import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

SHEETY_PRICES_ENDPOINT = "YOUR ENDPOINT HERE"


class DataManager:

    def __init__(self):
        self._user = os.environ["SHEETY_USERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_destination_data(self):
        # Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, auth=self._authorization)
        data = response.json()
        self.destination_data = data["prices"]
        # print(data)
        return self.destination_data

    def update_lowest_price(self, row_id, new_price):
        # Updated the price in the spreadsheet
        new_data = {
            "price": {
                "lowestPrice": new_price
            }
        }
        requests.put(
            url=f"{SHEETY_PRICES_ENDPOINT}/{row_id}",
            json=new_data,
            auth=self._authorization
        )
