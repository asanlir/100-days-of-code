import requests_cache
from pprint import pprint
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager


# Conserve requests and preserve free plan by caching the API responses
requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 3600,
    }
)


# Setup the data manager, flight search and notification manager instances
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
# pprint(sheet_data)
flight_search = FlightSearch()
# Create an instance of the NotificationManager
notification_manager = NotificationManager()


# Set the Dates and Origin Airport
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))
ORIGIN_CITY_IATA = "LHR"  # London Heathrow


# Find Cheap direct Flights
for destination in sheet_data:
    pprint(f"Getting direct flights for {destination['city']}...")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    cheapest_flight = find_cheapest_flight(flights, return_date=six_month_from_today.strftime("%Y-%m-%d"))
    pprint(f"{destination['city']}: GBP {cheapest_flight.price}")

    # Search for indirect flight if N/A
    if cheapest_flight.price == "N/A":
        print(f"No direct flight to {destination['city']}. Looking for indirect flights...")
        stopover_flights = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=six_month_from_today,
            is_direct=False
        )
        cheapest_flight = find_cheapest_flight(stopover_flights, return_date=six_month_from_today.strftime("%Y-%m-%d"))
        print(f"Cheapest indirect flight price is: GBP {cheapest_flight.price}")

    # Send Notifications
    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        pprint(f"Lower price flight found to {destination['city']}!")
        data_manager.update_lowest_price(destination["id"], cheapest_flight.price)
        # notification_manager.send_sms(
        #     message_body=f"Low price alert! Only GBP {cheapest_flight.price} to fly "
        #                 f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
        #                 f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        # )
        notification_manager.send_whatsapp(
            message_body=f"Low price alert! Only GBP {cheapest_flight.price} to fly "
                    f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                    f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        )
