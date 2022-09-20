'''Archivos
Para abrir un archivo se usa:
file = open("nombre_archivo.txt", "w")
Si no está lo crea, sino lo abre
w = para escritura, sobreescribe el archivo
a = agrega al final del archivo, guarda lo anterior
r = sirve para leer la información de dentro de un archivo. se usa file.readline() o file.readlines() pero nos devuelve en una lista
Para escribir dentro del archivo file.write("Hola Clase")
Para cerrar el archivo se usa file.close()'''

file = open("nombre.txt","w")
file.write("Hola clase")
file.close()

file = open("nombre.txt","a")
file.write("\nComputación")
file.close()

file = open("nombre.txt","r")
lista = file.readlines()
caracteres_removidos = []
print(lista)
for i in lista:
    i = i.strip("\n")
    caracteres_removidos.append(i)
print(caracteres_removidos)
file.close()
