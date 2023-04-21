import time
#pip install memory_profiler
from memory_profiler import memory_usage

class Node:
    def __init__(self,data):
        self.data =data
        self.next= None
        self.prev=None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail  = None
        self.lenght = 0

    def print_list(self):
        if self.head is None:
            print("Lista vacía")
        else:
            current =self.head
            array_with_values= list()
            while current is not None:
                array_with_values.append(current.data)
                current=current.next
            return array_with_values

    def add_node_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            current=self.head
            #Recorremos la lista hasta el final
            while current.next is not None:
                #de esta forma visito el siguiente nodo
                current=current.next
            #Generamos los dos enlaces del nuevo nodo
            current.next=new_node
            new_node.prev=current
        self.lenght+=1

    def add_node_at_start(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
        self.lenght +=1

    def add_node_in_position(self,position,data):
        print('Cantidad de nodos',self.lenght)
        if position < 1 or position > self.lenght+1:
            raise IndexError("Posicion fuera de rango")
        new_node =Node(data)
        if position==1:
            self.add_node_at_start(data)
        elif position == self.lenght+1:
            self.add_node_at_end(data)
        else:
            current_node=self.head
            for i in range(1,position -1):
                current_node=current_node.next
            new_node.next=current_node.next
            new_node.prev=current_node
            #.prev del nodo mirando hacia atras
            current_node.next.prev=new_node
            current_node.next=new_node
            self.lenght +=1

    def remove_node_at_start(self):
        if self.head is None:
            return
        else:
            self.head=self.head.next
            if self.head is not None:
                self.head.prev=None
        self.lenght -=1
    
    def remove_node_at_end(self):
        if self.head is None:
            return
        elif self.head.next is None:
            self.head=None
        else:
            current = self.head
            while current.next is not None:
                current=current.next
            current.prev.next =None
        self.lenght -=1

    def remove_node_by_position(self, position):
        if position < 1 or position > self.lenght+1:
            raise IndexError("Posicion fuera de rango")
        current_node= self.head
        if position == 1:
            self.remove_node_at_start()
        elif position == self.lenght :
            self.remove_node_at_end()
        else:
            for i in range(1, position):
                current_node= current_node.next
            current_node.prev.next = current_node.next
            current_node.next.prev= current_node.prev
            self.lenght -=1
    
    def remove_node_by_value(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.remove_node_at_start()
        current= self.head
        while current is not None:
            if current.data == data:
                if current.next is not None:
                    current.next.prev= current.prev
                current.prev.next= current.next
                return
            current= current.next
            self.lenght -=1

    def get_node_at_index(self, position):
        if self.head is None:
            return None
        current= self.head
        i=1
        while current is not None and i < position:
            current = current.next
            i+= 1
        return current.data

    def update_node_at_index(self, position, data):
        if self.head is None:
            return None
        current= self.head
        i=1
        while current is not None and i < position:
            current = current.next
            i+= 1
        if current is not None:
            current.data= data

    def update_node_by_value(self, old_data, new_data):
        if self.head is None:
            return
        current = self.head
        while current is not None:
            if current.data == old_data:
                current.data= new_data
                return print(current.data)
            current= current.next

    def reverse(self):
        temp= None
        current= self.head
        #Swap next and prev for all nodes of dll
        while current is not None:
            temp= current.prev
            current.prev= current.next
            current.next= temp
            current= current.prev
        #Check if head needs to be changed
        if temp is not None:
            self.head= temp.prev

    def sort_asc(self):
        if self.head is None:
            return
        current= self.head
        while current.next is not None:
            next_node = current.next
            while next_node is not None:
                if current.data > next_node.data:
                    current.data, next_node.data = next_node.data, current.data
                next_node = next_node.next
            current=current.next

    def has_duplicates(self):
        if self.head is None:
            return print("No duplicates")
        current= self.head
        values= set()
        while current is not None:
            if current.data in values:
                return print(f"Find duplicates")
            values.add(current.data)
            current= current.next
        return print("No duplicates")

    def has_duplicates_with_information(self):
        if self.head is None:
            return
        current= self.head 
        #Creamos un diccionario
        # listas|set()|diccionario{}
        values={}
        found_duplicates = False
        while current is not None:
            if current.data in values:
                values[current.data].append(current)
                found_duplicates = True
            else:
                values[current.data]=[current]
            current = current.next
        if found_duplicates:
            message = "The duplicates values are :\n"
            for value,nodes in values.items():
                if len (nodes) > 1:
                    message+=(f"{value}: {len(nodes)} veces \n")
            print(message)
            return True
        else:
            return False

    def calculate_complexity(self, func):
        # Ejecutar la función una vez para que se compile
        func(0)

        # Calcular tiempo de ejecución
        start_time = time.time()
        func(0)
        end_time = time.time()
        exec_time = end_time - start_time

        # Calcular uso de memoria
        mem_usage = max(memory_usage((func, (0,)), interval=0.1))

        # Imprimir resultados
        print(f"Función {func.name}:")
        print(f"Tiempo de ejecución: {exec_time:.6f} segundos")
        print(f"Uso máximo de memoria: {mem_usage:.6f} MB")
        print("------------------------------------")