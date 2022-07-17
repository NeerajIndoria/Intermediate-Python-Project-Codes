# import smtplib
# import datetime as dt
#
# now = dt.datetime.now()
# weekday = now.weekday()
#
# my_email = "ineeraj98@yahoo.com"
# password = "fclviowmwsepggwf"
# with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="neeraj.indoria@yahoo.com",
#         msg="Subject:Hello\n\nThis is body of my email"
#     )
#
# connection.close()
#
#
#
import smtplib
import datetime as dt
import random

MY_EMAIL = "ineeraj98@yahoo.com"
PASSWORD = "fclviowmwsepggwf"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 5:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="neeraj.indoria@yahoo.com",
            msg=f"Subject:Today's Motivation\n\n{quote}"
        )
