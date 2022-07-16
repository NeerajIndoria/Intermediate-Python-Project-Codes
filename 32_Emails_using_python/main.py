import smtplib
import datetime as dt

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 5:

my_email = "ineeraj98@yahoo.com"
password = "fclviowmwsepggwf"
with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="neeraj.indoria@yahoo.com",
        msg="Subject:Hello\n\nThis is body of my email"
    )

connection.close()
