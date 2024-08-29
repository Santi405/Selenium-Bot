import datetime

# Obtiene el nombre del día (en ingles)
today = datetime.date.today()
day_name = today.strftime("%A")


# Obtiene la hora en formato (HH:MM)
now = datetime.datetime.now()
current_hour_24 = now.strftime("%H:%M")


