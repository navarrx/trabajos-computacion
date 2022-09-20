#Ejercicio 5 - Santiago Navarro

hora_actual = int(input("Ingrese la hora:"))
loro_hablando = str(input("El loro está hablando?"))
horas_prohibidas = [21,22,23,24,1,2,3,4,5,6]

def problema_loro(hablando, hora):
    if hablando == "si":
        hablando = True
    elif hablando == "no":
        hablando = False
    else:
        pass
    if hora in horas_prohibidas:
        hora = True
    else:
        hora = False
    if (hablando and hora) == True:
        return True
    else:
        return False

print(problema_loro(loro_hablando,hora_actual))