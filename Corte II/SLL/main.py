from single_linked_list import SingleLinkedList

inst_single_linked_list= SingleLinkedList()

#Añadir nodo
inst_single_linked_list.create_node_sll_ends("Batman")
inst_single_linked_list.create_node_sll_ends("Robin")
inst_single_linked_list.create_node_sll_ends("Wolverine")
inst_single_linked_list.create_node_sll_unshift("Hulk")
inst_single_linked_list.create_node_sll_ends("Gatúbela")
inst_single_linked_list.create_node_sll_ends("Deadpool")
inst_single_linked_list.show_list()

#Eliminar nodo
print("     >>Eliminar último nodo<<")
inst_single_linked_list.delete_node_sll_pop()
inst_single_linked_list.show_list()
print("     >>Eliminar primer nodo<<")
inst_single_linked_list.shift_node_sll()
inst_single_linked_list.show_list()

print("-----------------------------------------------")
print("\n   >>Consultar valor del nodo")
inst_single_linked_list.get_node_value(1)
inst_single_linked_list.get_node_value(2)

print("-----------------------------------------------")
print("\n   >>Actualizar valor del nodo<<")
inst_single_linked_list.update_node_value(1, "Linterna verde")
inst_single_linked_list.show_list()

print("-----------------------------------------------")
print("\n   >>Eliminar nodo específico<<")
inst_single_linked_list.remove_node(2)
inst_single_linked_list.show_list()