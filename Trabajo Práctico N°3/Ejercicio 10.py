#Ejercicio 10
file = open("C:/Users/santi/Desktop/Manejo de Archivos/Ejercicio 1/ejercicio1.txt","r")
expresion = input("Ingrese una expresión a buscar:")
indice = 0
for linea in file:
    indice = indice + 1
    if expresion in linea:
        print("\nLinea en la que se encuentra:",linea)
        print("Se encuentra en la número",indice)
file.close()