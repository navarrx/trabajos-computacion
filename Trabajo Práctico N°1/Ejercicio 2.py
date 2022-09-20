#Ejercicio 2 - Santiago Navarro
a = str(input("El mono A sonríe?"))
b = str(input("El mono B sonríe?"))

def problemas_monos(a_sonriendo,b_sonriendo):
    if a_sonriendo == "si":
        a_sonriendo = True
    elif a_sonriendo == "no":
        a_sonriendo = False
    print(a_sonriendo)
    if b_sonriendo == "si":
        b_sonriendo = True
    elif b_sonriendo == "no":
        b_sonriendo = False
    print(b_sonriendo)
    if a_sonriendo == b_sonriendo:
        return True
    if a_sonriendo == b_sonriendo:
        return False
    else:
        return False
    #if a_sonriendo == True and b_sonriendo == True:
        #return True
   # if a_sonriendo == False and b_sonriendo == False:
       # return False
   # else:
       # return False
print(problemas_monos(a,b))