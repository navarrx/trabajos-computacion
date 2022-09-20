#Ejercicio 6 - Santiago Navarro

num1 = int(input("Ingrese el primer numero entero:"))
num2 = int(input("Ingrese el segundo numero entero:"))

def hacer10(a,b):
    if (num1 or num2) == 10:
        return True
    elif num1 + num2 == 10:
        return True
    else:
        return False

print(hacer10(num1,num2))