#Ejercicio 2
file = open("C:/Users/santi/Desktop/Manejo de Archivos/Ejercicio 1/ejercicio1.txt","r")
indice = int(input("Ingrese las lineas que desea leer: "))
while indice > 0:
    indice = indice - 1
    print(file.readline())
file.close()