class SingleLinkedList:

    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def show_list(self):
        # 1. Declarar una array vacío que contendraá los valores de los nodos de SLL
        array_with_nodes_value = list()
        current_node = self.head 
        # Mientras el nodo actual que estoy visitando sea diferente de None
        while(current_node != None):
            # Añado al final de la lista el valor extraido del nodo
            array_with_nodes_value.append(current_node.value)
            # Visito el próximo nodo antes de salir del while
            current_node = current_node.next
        # Imprimimos la lista
        print(array_with_nodes_value)
    
    def create_node_sll_ends(self, value):
        # Creamos una variable que va a tener la estructura de un nodo
        new_node = self.Node(value)
        # Validar si la SLL tiene nodos o no
        if self.head == None:
            # Al nuevo nodo se convierte en la cabeza y cola de la lista
            self.head = new_node
            self.tail = new_node
        else:
            # Si ingresa en esta condición, es porque ya existe al menos un nodo
            # 1. Debemos relacionar al nuevo nodo con la cola de la lista
            # 2. Convertir al nuevo nodo en la cola de la lista
            self.tail.next = new_node
            self.tail = new_node
        # Incrementamos en 1 el tamaño de la lista
        self.length +=1
    
    def create_node_sll_unshift(self, value):
        new_node = self.Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            print(self.head.value)
        else:
            new_node.next = self.head
            self.head = new_node
        # Incrementamos en 1 el tamaño de la lista
        self.length +=1

    def delete_node_sll_pop(self):
        if self.length == 0:
            print('>> Lista vacía no hay nodos por eliminar <<')
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            current_node = self.head
            new_tail = current_node
            while current_node.next != None:
                new_tail = current_node
                current_node = current_node.next
            print(f'Valor del nodo a eliminar es: {self.tail.value}')
            self.tail = new_tail
            self.tail.next = None
            self.length -= 1

    '''Eliminar nodo al inicio de la lista'''
    def shift_node_sll(self):
        if self.length == 0:
            print('>> Lista vacía no hay nodos por eliminar <<')
        elif self.length == 1:

            self.head = None
            self.tail = None
            self.length -= 1
        else:
            remove_node = self.head
            print(f'Valor del nodo a eliminar es: {remove_node.value}')
            self.head = remove_node.next
            self.length -=1


    def get_node(self, index):
        if index < 1 or index > self.length:
            return None
        elif index == 1:
            return self.head
        elif index == self.length:
            return self.tail
        else:
            current_node = self.head
            node_counter = 1
            while(index != node_counter):
                current_node = current_node.next
                node_counter += 1
            return current_node

    def get_node_value(self, index):
        if index < 1 or index > self.length:
            return 'No se encontro'
        elif index == 1:
            return self.head.value
        elif index == self.length:
            return self.tail.value
        else:
            current_node = self.head
            node_counter = 1
            #Validar que el nodo a consultar sea el mismo del contador
            while(index != node_counter):
                current_node = current_node.next
                node_counter += 1
            return current_node.value

    def update_node_value(self, index, new_value):
        search_node = self.get_node(index)
        if search_node != None:
            print(f'Actualizando el valor del nodo ...\n           >> {search_node.value} << a\n           >>{new_value}<<')
            search_node.value = new_value
        else:
            print("     >> No se encontro el nodo <<") 

    def remove_node(self, index):
        if index == 1:
            self.shift_node_sll()
        elif index == self.length:
            self.delete_node_sll_pop()
        else:
            remove_node_sll = self.get_node(index)
            if remove_node_sll!= None:
                previous_node = self.get_node(index - 1)
                print(self.get_node(index).value)
                previous_node.next = remove_node_sll.next
                remove_node_sll.next = None
            else:
                print('     >> No se encontro el nodo <<')

    def get_list_length(self):
        array_with_nodes_value = list()
        current_node = self.head 
        while(current_node != None):
            array_with_nodes_value.append(current_node.value)
            current_node = current_node.next
        print(f"Tamaño: {len(array_with_nodes_value)}") 

    def get_index_of_value(self, value):
        if self.length == 0:
            print("Lista vacía")
        elif self.length == 1:
            print("1")
        else:
            current_node = self.head.next
            node_counter = 2
            while(value != current_node.value):
                current_node = current_node.next
                node_counter += 1
            print(node_counter)

    def reverse_sll(self):
        previous_node = None
        current_node = self.head
        next= None
        while (current_node != None):
            next = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next
        self.head= previous_node
        return self.head

    def delete_all_items(self):
        current_node= self.head
        while(current_node != None):
            self.head.next=None
            self.head = None
            current_node= current_node.next

    def sort_elements_sll(self):
        array_with_nodes_value = list()
        sort_list= list()
        current_node = self.head 
        while(current_node != None):
            array_with_nodes_value.append(current_node.value)
            current_node = current_node.next
        sort_list= array_with_nodes_value
        sort_list.sort()
        print(sort_list)

    def create_node_sll_at_determinate_position(self, value, index):
        new_node = self.Node(value)
        if not self.head :
            self.head = new_node
            return
        elif index == 1:
            new_node.next= self.head
            self.head= new_node
            return
        current_node = self.head
        previous_node = None
        node_counter = 1
        while(current_node and node_counter!= index):
            previous_node= current_node
            current_node= current_node.next
            node_counter +=1
        if node_counter == index:
            previous_node.next= new_node
            new_node.next= current_node
        else:
            previous_node.next= new_node
        self.length +=1

    def is_empty(self):
        if self.head == None:
            print("Lista vacía")
        else:
            print("La lista contiene elementos")