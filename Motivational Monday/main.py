import smtplib
import datetime as dt
import random


MY_EMAIL = ""
MY_PASSWORD = ""

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    with open("./Motivational Monday/quotes.txt") as file:
        all_quotes = file.readlines()
        quote_of_the_day = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="",
            msg=f"Subject:Motivational Monday\n\n{quote_of_the_day}"
        )
