from fecha import *
import json

# TIPOS
BASICAS =   "[URL BASICAS]"
SISTEMAS =  "[URL SISTEMAS]"

# MATERIAS
materias = {"AM2" : "[URL]",
            "FISICA2" : "[URL]",
            "PDP" : "[URL]",
            "AdeS" : "[URL]",
            "SO" : "[URL]"
            }

ENVIAR =    "//*[@id='form-main-content1']/div/div/div[2]/div[2]/div/button"

nombres = []

# Abrimos JSON
with open("horario.json", "r") as f:
    horario = json.load(f)

# En base a la hora, establecemos la materia
for class_info in horario[day_name]:
    if class_info['startTime'] < current_hour_24 and class_info['endTime'] > current_hour_24:
        MATERIA = materias[class_info['course']]
        print(MATERIA)

# En base a la materia, establecemos el tipo
if MATERIA == "[]" or MATERIA == "[]":
    TIPO = BASICAS
else:
    TIPO = SISTEMAS
