import smtplib


my_email = "example@example.com"
password = "pass1234()"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="recipient@mail.com",
                        msg="Subject: Hello\n\nThis is a test email from Python.")
