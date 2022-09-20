#Ejercicio 3 - Santiago Navarro
num1 = int(input("Ingrese un valor entero: "))
num2 = int(input("Ingrese otro valor entero: "))

def suma_doble(a,b):
    if num1 == num2:
        num3 = (num1 + num2) * 2
        return num3
    elif num1 != num2:
        num3 = num1 + num2
        return num3
print(suma_doble(num1,num2))
