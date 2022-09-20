#Ejercicio 6
file = open("C:/Users/santi/Desktop/Manejo de Archivos/Ejercicio 1/ejercicio1.txt", "r")
n = int(input("Ingrese hasta las lineas que desee: "))
while n > 0:
    print(file.readline())
    n = n - 1
file.close()