class BinaryTree:
    #El constructor del árbol necesita el valor del nodo e identificar hacia que lado está
    #sub-árbol
    def __init__(self, value):
        self.value= value
        self.left_node= None
        self.right_node= None
    
    #Insertar nodo en el arbol
    def insert(self, root, node):
        #Si no existe raíz en el árbol
        if root is None:
            root= node
        else:
            #Si el valor del nodo es menor que la raiz
            if root.value > node.value:
                #Si no existe nodo izquierdo
                if root.left_node is None:
                    root.left_node= node
                else:
                    #Si existe el nodo izquierdo, se inserta el nodo en el subárbol izquierdo
                    self.insert(root.left_node, node)
            else:
                #Si no existe nodo derecho
                if root.right_node is None:
                    root.right_node= node
                else:
                    #20, 21
                    #Si existe nodo derecho, se inserta el nodo en el subárbol derecho
                    self.insert(root.right_node, node)
        
    def print_tree(self, root):
        #Valor menor | raiz | valor mayor
        #16 | 20 | 21
        if root is not None:
            self.print_tree(root.left_node)
            print(root.value)
            self.print_tree(root.right_node)

        '''if self.left_node:
            self.left_node.print_tree()
        print(self.value)
        if self.right_node:
            self.right_node.print_tree()'''
    

