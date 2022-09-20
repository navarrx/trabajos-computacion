class Book:
    def __init__(self,title,author,price):
        self.__title = title
        self.__author = author
        self.__price = price
        self.__book_list = []
        
    def set_title(self,title):
        self.__title = title
        
    def set_author(self,author):
        self.__author = author
        
    def set_price(self,price):
        self.__price = price   

    def checker(self):
        print(self.__book_list)
        
    def view(self):
        print("Name: ",self.__title,"\nAuthor: ",self.__author,"\nPrice: ",self.__price)
