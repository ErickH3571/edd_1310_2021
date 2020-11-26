from Pilas import Stack

pila = Stack()
pila.push('a')
pila.push('x')
pila.to_String()
pila.push('b')
pila.push('y')
pila.to_String()
var = pila.pop()
pila.to_String()
print(f"var = {var}")
