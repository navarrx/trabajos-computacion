#Ejercicio 5
import shutil   
file = open("C:/Users/santi/Desktop/Manejo de Archivos/Ejercicio 1/ejercicio5.txt","w")
shutil.copy("C:/Users/santi/Desktop/Manejo de Archivos/Ejercicio 1/ejercicio1.txt","C:/Users/santi/Desktop/Manejo de Archivos/Ejercicio 1/ejercicio5.txt")
print("Copiado Exitosamente!")
file.close()
