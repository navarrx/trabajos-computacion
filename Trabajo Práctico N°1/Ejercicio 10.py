#Ejercicio 10 - Santiago Navarro

cadena = str(input("Ingrese una palabra: "))
indice_quitar = int(input("Ingrese el número de índice que desea remover: "))

def caracter_perdido(str,n):
    if len(str) <= n:
        print("El indice esta fuera de rango")
    else:
        str = str[:n] + (str[n+1:])
        return str

print(caracter_perdido(cadena,indice_quitar))