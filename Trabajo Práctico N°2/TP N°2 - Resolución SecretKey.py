#Ejercicio Clave Secreta - Santiago Navarro

import os
import re
contenido = os.listdir("C:/Users/santi/Desktop/SecretKey")
for i in contenido:
    j = re.sub(r"[0-9]+","",i)
    os.chdir("C:/Users/santi/Desktop/SecretKey")
    os.rename(i,j)