class Library:
    def __init__(self):
        self.__client_list = []
        self.__book_list = []
        self.__assigned_books = []

    def set_clients_list(self,client):
        self.__client_list.append(client)

    def set_books_list(self,book):
        self.__book_list.append(book)

    def showBooks(self):
        return self.__book_list

    def showClients(self):
        return self.__client_list
 
    def assign(self,client,book):
        assign = "The client: "+client+", has the book: "+book
        self.__assigned_books.append(assign)
    
    def showAssigned(self):
        print(self.__assigned_books)