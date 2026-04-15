import requests
from datetime import datetime, timezone
import smtplib
import time

from config import (
    CHECK_INTERVAL_SECONDS,
    MY_EMAIL,
    MY_LAT,
    MY_LONG,
    MY_PASSWORD,
    SMTP_HOST,
)


def is_iss_overhead():
    response = requests.get(
        url="http://api.open-notify.org/iss-now.json", timeout=10)
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Tu posición esta dentro de +/- 5 grados de la ISS.
    return (
        MY_LAT - 5 <= iss_latitude <= MY_LAT + 5
        and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5
    )


def is_night():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(
        "https://api.sunrise-sunset.org/json", params=parameters, timeout=10)
    response.raise_for_status()
    data = response.json()
    sunrise = datetime.fromisoformat(
        data["results"]["sunrise"].replace("Z", "+00:00")
        ).hour
    sunset = datetime.fromisoformat(
        data["results"]["sunset"].replace("Z", "+00:00")
        ).hour

    # La API devuelve horas en UTC; comparamos contra hora actual UTC.
    time_now = datetime.now(timezone.utc).hour

    return time_now >= sunset or time_now <= sunrise


# Si la ISS esta cerca y es de noche, envía un aviso por correo.
while True:
    time.sleep(CHECK_INTERVAL_SECONDS)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP(SMTP_HOST) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject:Look Up\n\nThe ISS is above you in the sky.",
            )
