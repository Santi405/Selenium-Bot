import datetime

# Get today's date
today = datetime.date.today()
day_name = today.strftime("%A")


# Get the current time
now = datetime.datetime.now()
current_hour_24 = now.strftime("%H:%M")


