from fecha import *
import json

# TIPOS
BASICAS =   "https://t.qrjp.net/fo72"
SISTEMAS =  "https://t.qrjp.net/5dwz"

# MATERIAS
materias = {"AM2" : "https://forms.office.com/r/1N6zdx5r0g",
            "FISICA2" : "https://forms.office.com/r/4qJ7pBqejr",
            "PDP" : "https://forms.office.com/r/4sTEQkwTp9",
            "AdeS" : "https://forms.office.com/r/wjENULr1Uk",
            "SO" : "https://forms.office.com/r/4kk5B3imHf"
            }

ENVIAR =    "//*[@id='form-main-content1']/div/div/div[2]/div[2]/div/button"

nombres = ['"Zanin"', '"Brizio"', '"Waniewski"', '"Lanselotto"']

# Abrimos JSON
with open("horario.json", "r") as f:
    horario = json.load(f)

# En base a la hora, establecemos la materia
for class_info in horario[day_name]:
    if class_info['startTime'] < current_hour_24 and class_info['endTime'] > current_hour_24:
        MATERIA = materias[class_info['course']]
        print(MATERIA)

# En base a la materia, establecemos el tipo
if MATERIA == "FISICA2" or MATERIA == "AM2":
    TIPO = BASICAS
else:
    TIPO = SISTEMAS
