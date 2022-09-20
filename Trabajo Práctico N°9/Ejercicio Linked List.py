#Listas Enlazadas: en vez de tener un grupo continuo de espacios de memoria para asignar, funciona con un grupo de nodos y estos van a tener dos componentes
#Conjunto de nodos
#Un nodo tiene 2 atributos

class Nodo:
    def __init__(self,data = None, next = None):
        self.data =  data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beggining(self,data):
        node = Nodo(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("La lista esta vacía")

        iterator = self.head
        str_list = ""

        while iterator:
            str_list += str(iterator.data) + "-->"
            iterator = iterator.next
        print(str_list)

    def size(self):
        if self.head is None:
            print("La lista esta vacía")

        counter = 0
        iterator = self.head

        while iterator:
            counter = counter + 1
            iterator = iterator.next
            #iterator.next guarda el nodo
        return counter

    def insert_at(self, index, data):
        print(index,data)
        if index < 0 or index > self.size():
            #si usamos self.size lo llamamos como método y con self.size() lo llamamos como atributo
            raise Exception("Ingresaste un indice válido")

        if index == 0:
            self.insert_at_beggining(data)
            return

        counter = 0
        iterator = self.head

        while iterator:
            if counter == index - 1:
                node = Nodo(data, iterator.next)
                iterator.next = node
                break
        counter += 1
        iterator = iterator.next

    def insert_at_end(self,data):
        index = self.size()
        counter = 0
        iterator = self.head
        while iterator:
            if counter == index - 1:
                node = Nodo(data, iterator.next)
                iterator.next = node
                break
            counter = counter + 1
            iterator = iterator.next

ll = LinkedList()
ll.insert_at_beggining(23)
ll.insert_at_beggining(12)
ll.insert_at_beggining(56)
ll.insert_at(1, 8888)
ll.insert_at(1, 9998)
ll.print()
ll.insert_at_end(98)
ll.print()
