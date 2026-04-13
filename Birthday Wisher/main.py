import datetime as dt
import pandas as pd
import random
import smtplib


MY_EMAIL = ""
MY_PASSWORD = ""


# Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:

    birthday_person = birthdays_dict[today_tuple]
    file_path = f"./Birthday Wisher/letter_templates/letter_{random.randint(1,3)}.txt"

    # Pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    # Send the letter to that person's email address.
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
