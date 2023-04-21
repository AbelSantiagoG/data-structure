from double_linked_list import DoubleLinkedList

inst_dll =DoubleLinkedList()

inst_dll.add_node_at_end(12)
inst_dll.add_node_at_end(4)
inst_dll.add_node_at_start(-7)
inst_dll.add_node_at_end(135)
inst_dll.add_node_at_end(34)
inst_dll.add_node_at_start(-2)


inst_dll.print_list()

inst_dll.add_node_in_position(6,30)

inst_dll.print_list()

inst_dll.remove_node_at_start()
inst_dll.remove_node_at_end()

inst_dll.print_list()

'''print("Eliminar el segundo nodo")
inst_dll.remove_node_by_position(2)
inst_dll.print_list()

print("Eliminar el tercer nodo")
inst_dll.remove_node_by_position(3)
inst_dll.print_list()

print("Eliminar el primer nodo")
inst_dll.remove_node_by_position(1)
inst_dll.print_list()

print("Eliminar el último nodo")
inst_dll.remove_node_by_position(2)
inst_dll.print_list()

print("Eliminar el último nodo")
inst_dll.remove_node_by_position(1)
inst_dll.print_list()'''

inst_dll.remove_node_by_value(90)
inst_dll.print_list()

print(inst_dll.get_node_at_index(2))

inst_dll.update_node_at_index(3, 214)
inst_dll.print_list()

inst_dll.update_node_by_value(12, 0)

inst_dll.reverse()
inst_dll.print_list()

inst_dll.sort_asc()
print(inst_dll.print_list())

inst_dll.add_node_at_start(4)
inst_dll.add_node_at_start(4)
inst_dll.print_list()

inst_dll.has_duplicates()

inst_dll.has_duplicates_with_information()