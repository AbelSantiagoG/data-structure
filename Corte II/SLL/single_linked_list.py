class SingleLinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    #Por fuera de la clase nodo
    def __init__(self):
        self.head = None
        self.tail = None
        self.length= 0
    
    def show_list(self):
        # 1. Declarar un array(Lista) vacío que contendrá los valores de los nodos
        array_with_nodes_value = list()
        current_node = self.head
        # Mientras el nodo actual que estoy visitando sea diferente de None
        while(current_node != None):
            #Añado al final de la lista el valor extraido 
            array_with_nodes_value.append(current_node.value)
            #Incrementamos en 1 el valor del nodo visitado
            #current_node +=1 NO SIRVE PARA PASAR AL SIGUIENTE NODO DE UNA SLL 
            #Pasamos del nodo actual al siguiente nodo mediante el puntero
            current_node= current_node.next
        #Imprimimos los valores de la lista
        print(array_with_nodes_value)
    
    def create_node_sll_ends (self, value):
        #Creamos una variable que va a tener la estrucutura de un nodo
        new_node = self.Node(value)
        # Validar si la SLL tiene nodos o no

        if self.head == None:
            # El nuevo nodo se convierte en la cabeza y la cola de la lista
            self.head = new_node
            self.tail = new_node
        else:
            # Si ingresa en esta condición, es porque ya existe al menos un nodo
            # 1. Debemos relacionar al nuevo nodo con la cola de la lista
            # 2. Convertir al nuevo nodo en la cola de la lista
            self.tail.next = new_node
            self.tail = new_node
        #Incrementamos en 1 el tamaño de la lista
        self.length +=1

    def create_node_sll_unshift (self, value):
        new_node = self.Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            # 1. Debemos relacionar al nuevo nodo con la cabeza de la lista
            # 2. Convertir al nuevo nodo en la cabeza de la lista
            new_node.next = self.head
            self.head = new_node
        self.length +=1
    
    def delete_node_sll_pop (self):
        # 1. validar si la lista está vacía
        # 2. Validar si la lista tiene un único nodo
        # 3. Si tiene más de un nodo eliminar el nodo que es la cola de la lista
        # 4. Asignar al nodo anterior como la nueva cola de la lista
        if self.length == 0:
            print(">> Lista vacía, no hay nodos por eliminar <<")
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            current_node = self.head
            # 2. Validar mediante el enlace del nodo actual
            new_tail= current_node
            while current_node.next != None:
                # 3. Convertimos en la cola de la lista el nodo que actualmente visitamos en la iteración
                new_tail = current_node
                # 4. Pasamos al siguiente nodo antes de salir del while
                current_node = current_node.next
            # 5. Actualizamos la cola de la lista
            self.tail = new_tail
            self.tail.next= None
            # 6. Restamos 1 en el tamaño de la lista
            self.length -= 1
    
    def shift_node_sll(self):
        if self.length == 0:
            print(">> Lista vacía, no hay nodos por eliminar <<")
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            #Actualizamos el nombre de la cabeza con la variable auxiliar
            remove_node = self.head
            # Actualizamod la cabeza de la lista
            self.head= remove_node.next
            #Eliminamos el enlace de remove_node con la lista
            self.length-=1

    def get_node(self, index):
        if index < 1 or index> self.length:
            return None
        elif index == 1:
            return self.head
        elif index == self.head:
            return self.tail
        else:
            current_node = self.head
            node_counter = 1
            while(index != node_counter):
                current_node = current_node.next
                node_counter +=1
            return current_node

    def get_node_value(self, index):
        if index < 1 or index> self.length:
            print("No se encontró")
        elif index == 1:
            print(self.head.value)
        elif index == self.head:
            print(self.tail.value)
        else:
            current_node = self.head
            node_counter = 1
            while(index != node_counter):
                current_node = current_node.next
                node_counter +=1
            print(current_node.value)
    
    def update_node_value(self, index, new_value):
        search_node = self.get_node(index)
        if search_node != None:
            #Encontró el nodo y se puede actualizar
            print(f'Actualizando el valor del nodo ...\n        >>{search_node.value}<< por {new_value}')
            search_node.value= new_value
        else:
            #Si no se encuentra el nodo pos nada
            print("     >>No se encontró el nodo<<")
    
    def remove_node(self, index):
        if index == 1:
            self.shift_node_sll()
        elif index == self.length:
            self.delete_node_sll_pop()
        else:
            remove_node_sll = self.get_node(index)
            if(remove_node_sll != None):
                previous_node = self.get_node(index-1)
                previous_node.next = remove_node_sll.next
                remove_node_sll.next = None
            else:
                print("     >>No se encontró el nodo<<")