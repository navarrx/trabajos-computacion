#Ejercicio 1 - Santiago Navarro
dias_de_semana = ["lunes","martes","miercoles","jueves","viernes"]
#dia_semana es True si es dias_de_semana
#parametro vacaciones es True si esta en tiempo_vacaciones
dia = str(input("Que día es?"))
vacacion = str(input("¿Estas de Vacaciones?"))
def dormimos(dia_semana, vacaciones):
    if dia_semana in dias_de_semana:
        dia_semana = True
    else:
        dia_semana = False
    if vacaciones == "si":
        vacaciones = True
    else:
        vacaciones = False
    if dia_semana == False or vacaciones == True:
        return True
    else:
        return False
print(dormimos(dia,vacacion))
