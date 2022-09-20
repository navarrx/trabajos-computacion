class Client:
    def __init__(self,name,age,address):
        self.__client_list = []
        self.__name = name
        self.__age = age
        self.__address = address
    def set_name(self,name):
        self.__name = name
    def set_age(self,age):
        self.__age = age
    def set_address(self,address):
        self.__address = address
    def add_client_list(self,name,age,address):
        add = "Name: "+name+", Age: "+age+", Address: "+address
        self.__client_list.append(add)
        print(self.__client_list)
        
    def view(self):
        print("Name: ",self.__name,"\nAge: ",self.__age,"\nAddress: ",self.__address)