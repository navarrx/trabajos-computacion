#Ejercicio 4 - Santiago Navarro

num = int(input("Ingrese un número entero"))
def diferencia21(a,b=21):
    if a > 21:
        resultado = (a - b) * 2
        return resultado
    else:
        resultado = b - a
        return resultado
print(diferencia21(num,))