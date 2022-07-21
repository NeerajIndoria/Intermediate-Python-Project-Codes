import time
import requests
from datetime import datetime
import smtplib

MY_LAT = 28.895515  # Your latitude
MY_LON = 76.606613   # Your longitude
MY_EMAIL = "ineeraj98@yahoo.com"
MY_PASSWORD = "fclviowmwsepggwf"


def is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LON-5 <= iss_longitude <= MY_LON+5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LON,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_overhead() and is_night():
        with smtplib.SMTP("smtp.mail.yahoo.com") as con:
            con.starttls()
            con.login(MY_EMAIL, MY_PASSWORD)
            con.sendmail(
                to_addrs="neeraj.indoria@yahoo.com",
                from_addr=MY_EMAIL,
                msg="Subject:Look UP☝🏻\n\nThe ISS is above you in the sky."
            )
            con.close()
# If the ISS is close to my current position,
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
