import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "EZ3OJXEB6IK1SLD1"
NEWS_API_KEY = "27bc3351c654402186d9bd3f864c9548"


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
print(yesterday_closing_price)


# Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)


# Find the positive difference between 1 and 2.
difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
print(difference)


# Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage_diff = (difference / float(day_before_yesterday_closing_price)) * 100
print(percentage_diff)


# Use the News API to get articles related to the COMPANY_NAME.
if percentage_diff > 1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]


# Create a list that contains the first 3 articles
three_articles = articles[:3]
print(three_articles)

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number.

# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.


#TODO 9. - Send each article as a separate message via Twilio.



#Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors
are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions
as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors
are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions
as of March 31st, near the height of the coronavirus market crash.
"""
