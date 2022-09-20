from Library import Library
from Book import Book
from Client import Client
import time

library = Library()

def menu():
    print("====== ( ) ======" + "\nWelcome to our Library System" + "\nPlease type a number to choose an option" + "\n1. Add a new book" + "\n2. Add a new Client" + "\n3. Show Book list" + "\n4. Show Clients List" + "\n5. Assign a book to a client" + "\n6. Show assigned books list" + "\n7. Exit" + "\n====== ( ) ======")
    option = int(input("Insert the number of option you want to execute: "))
    decider(option)
def decider(number):
    if number == 1:
        print("====== ( ) ======")
        title = str(input("Insert book name: "))
        author = str(input("Insert author name: "))
        price = str(input("Insert book price: "))
        book = Book(title, author, price)
        library.set_books_list(book)
        print("BOOK SAVED!"+"\n====== ( ) ======")
        time.sleep(2)
        menu()
    elif number == 2:
        print("====== ( ) ======")
        name = str(input("Insert client name: "))
        age = str(input("Insert client age: "))
        address = str(input("Insert client address: "))
        client = Client(name,age,address)
        library.set_clients_list(client)
        print("CLIENT SAVED!" + "\n====== ( ) ======")
        time.sleep(2)
        menu()
    elif number == 3:
        print("====== ( ) ======" + "\nBooks List")
        showBooks = library.showBooks()
        print(showBooks)
        print("====== ( ) ======")
        time.sleep(5)
        menu()
    elif number == 4:
        print("====== ( ) ======" + "\nClients List")
        showClients = library.showClients()
        print(showClients)
        print("====== ( ) ======")
        time.sleep(5)
        menu()
    elif number == 5:
        print("====== ( ) ======")
        client = str(input("Insert the name of the client:"))
        book = str(input("Insert the name of the book:"))
        print("Book assigned correctly!","\n====== ( ) ======")
        time.sleep(3)
        library.assign(client, book)
        menu()
    elif number == 6:
        print("====== ( ) ======")
        library.showAssigned()
        print("====== ( ) ======")
        time.sleep(5)
        menu()
    elif number == 7:
        print("Thanks for using our system! See you soon")
        exit()
menu()