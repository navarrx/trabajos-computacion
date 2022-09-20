#Ejercicio 9 - Santiago Navarro

palabra = str(input("Ingrese una palabra: "))

def no_cadena(str):
    if str[0:2] == "no":
        return str
    else:
        str = "no"+ " " + str
        return str

print(no_cadena(palabra))