from Listas import LinkedList

l = LinkedList()
print(f"¿L esta vacia?: { l.is_empety() }")
l.append(10)
l.append(5)
l.append(6)
l.append(20)
l.append(2)
print(f"¿L esta vacia?: { l.is_empety() }")
l.transversal()
l.remove(6)
l.transversal()
l.remove(10)
l.transversal()
l.preppend(80)
l.transversal()
x = l.tail()
print(x.data)
