#Ejercicio 8 - Santiago Navarro

num1 = int(input("Ingrese un número entero: "))
num2 = int(input("Ingrese otro número entero: "))
negativo = str(input("Ingrese True or False: "))

def pos_negativa(a,b,negativa):
    print(a,b,negativa)
    if ((a < 0 and b > 0) or (b < 0 and a > 0)) and negativa == "False":
        return True
    elif (a < 0 and b < 0) and negativa == "True":
        return True
    else:
        return False

print(pos_negativa(num1,num2,negativo))