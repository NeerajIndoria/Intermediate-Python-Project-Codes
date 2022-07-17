import datetime as dt
import pandas
import random
import smtplib

MY_EMAIL = "ineeraj98@yahoo.com"
PASSWORD = "fclviowmwsepggwf"

now = dt.datetime.now()
todays_tuple = (now.month, now.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if todays_tuple in birthdays_dict:
    birthdays_person = birthdays_dict[todays_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter:
        message = letter.read()
        message = message.replace("[NAME]", birthdays_person["name"])

    with smtplib.SMTP("smtp.mail.yahoo.com") as con:
        con.starttls()
        con.login(MY_EMAIL, PASSWORD)
        con.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthdays_person.email,
            msg=f"Subject:Happy Birthday\n\n{message}"
        )
