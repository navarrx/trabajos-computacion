from Controltower import Controltower
import time

control_tower = Controltower()

def menu():
    print("====== ( ) ======" + "\nWelcome to our Control Tower" + "\nPlease type a number to choose an option" + "\n1. Recognise landing/taking off airplanes" + "\n2. Take off/Land an airplane" + "\n3. Show queue status" + "\n4. Exit" + "\n====== ( ) ======")
    option = int(input("Insert the number of option you want to execute: "))
    decider(option)

def decider(number):
    if number == 1:
        name = str(input("Insert the airplane name: "))
        test = int(input("Insert the status of the airplane" + "\n1 = Landing" + "\n2 = Taking off"))
        control_tower.reconocimiento(name,test)
        time.sleep(2)
        menu()
    elif number == 2:
        print("Control Tower sending a signal to the correct airplane...")
        control_tower.action()
        time.sleep(2)
        menu()
    elif number == 3:
        control_tower.__str__()
        time.sleep(2)
        menu()
    elif number == 4:
        exit()
    else:
        menu()

menu()