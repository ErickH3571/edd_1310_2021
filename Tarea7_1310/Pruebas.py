from Listas import DoubleLinkedList

l = DoubleLinkedList()
print(f"¿L esta vacia?: { l.is_empety() }")
l.append(10)
l.append(5)
l.append(6)
l.append(20)
l.append(6)
l.append(2)
print(f"¿L esta vacia?: { l.is_empety() }")
l.transversal()
l.reverse_transversal()
print(f"Numero de elementos {l.get_Size()}")
l.find_from_head(20)
l.find_from_tail(6)
l.remove_from_head(5)
l.remove_from_tail(2)
l.transversal()
l.reverse_transversal()
