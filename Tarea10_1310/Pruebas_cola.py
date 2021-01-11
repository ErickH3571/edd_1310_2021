from Colas import Queue,BoundedPriorityQueue

maestres = {"Prioridad":4, "Descripcion":"maestre", "Personas":["Pedro G","Doroti H"]}
niños = {"Prioridad":2, "Descripcion":"niños", "Personas":["Hector H","Elmo H"]}
mecanicos = {"Prioridad":4, "Descripcion":"mecanicos", "Personas":["Fernanda F","Maria Z"]}
mujeres = {"Prioridad":3, "Descripcion":"mujeres", "Personas":["Lu P","Sarah S"]}
ancianos = {"Prioridad":2, "Descripcion":"ancianos", "Personas":["Goku S","Vegetta F"]}
niñas = {"Prioridad":1, "Descripcion":"niñas", "Personas":["Milk B","Videl A"]}
hombre = {"Prioridad":3, "Descripcion":"hombre", "Personas":["Gohan S","Trunks B"]}
vigia = {"Prioridad":4, "Descripcion":"vigia", "Personas":["John C","Jaime M"]}
capitan = {"Prioridad":5, "Descripcion":"capitan", "Personas":["Bulma B","Kami S"]}
timonel = {"Prioridad":4, "Descripcion":"timonel", "Personas":["Panfila P","Cassandra E"]}

cpa = BoundedPriorityQueue(7)
cpa.enqueue(maestres['Prioridad'], maestres)
cpa.enqueue(niños['Prioridad'], niños)
cpa.enqueue(mecanicos['Prioridad'], mecanicos)
cpa.enqueue(mujeres['Prioridad'], mujeres)
cpa.enqueue(ancianos['Prioridad'], ancianos)
cpa.enqueue(niñas['Prioridad'], niñas)
cpa.enqueue(hombre['Prioridad'], hombre)
cpa.enqueue(vigia['Prioridad'], vigia)
cpa.enqueue(capitan['Prioridad'], capitan)
cpa.enqueue(timonel['Prioridad'], timonel)

while not cpa.is_empty():
    cpa.to_string()
    sig = cpa.dequeue()
    print(f"Los que evacuaran el barco ahora seran los {sig}")
cpa.to_string()
print("Ya no queda nadie por evacuar")
