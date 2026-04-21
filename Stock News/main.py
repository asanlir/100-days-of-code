import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "your_alpha_vantage_api_key"
NEWS_API_KEY = "your_news_api_key"
TWILIO_SID = "your_twilio_sid"
TWILIO_AUTH_TOKEN = "your_twilio_auth_token"


# Get yesterday's closing stock price.
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in stock_data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]


# Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]


# Find the positive difference between 1 and 2.
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"


# Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage_diff = round((difference / float(day_before_yesterday_closing_price)) * 100)


# Use the News API to get articles related to the COMPANY_NAME.
if abs(percentage_diff) > 5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]


# Create a list that contains the first 3 articles properly formatted.
three_articles = articles[:3]
formatted_articles = [f"{STOCK_NAME}: {up_down}{percentage_diff}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]


# Send each article as a separate message via Twilio.
client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
for article in formatted_articles:
    message = client.messages.create(
        body=article,
        from_="+1234567890",  # Your Twilio number
        to="+0987654321"  # Your phone number
    )
