#Ejercicio 7 - Santiago Navarro

num = int(input("Ingrese un valor entero:"))

def cerca_cien(n):
    if(n >= 90 and n <= 110) or (n >= 190 and n <= 210):
        return True
    else:
        return False

print(cerca_cien(num))