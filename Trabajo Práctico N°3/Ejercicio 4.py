#Ejercicio 4
file = open("archivo.txt","r")
lista = []
linea = file.readline()
while linea != '':
    linea = file.readline()
    lista.append(linea)
print(lista)
file.close()