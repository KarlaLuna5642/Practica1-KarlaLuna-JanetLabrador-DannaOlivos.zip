import queue

grafica = {
  'A' : ['B','C', 'D', 'E'],
  'B' : ['A', 'C', 'G'],
  'C' : ['A', 'B', 'D'],
  'D' : ['H', 'E', 'A', 'C'],
  'E' : ['A', 'D', 'F'],
  'F' : ['G', 'E', 'H', 'I'],
  'G' : ['F', 'B'],
  'H' : ['F', 'D'],
  'I' : ['F']
}
cola = queue.Queue()

# BFS algorithm
def bfs(grafica, nodo_inicio):
    if nodo_inicio not in grafica:
        print("Nodo de inicio no existe en el grafo")
        return

    visitados = set()
    orden = []
    padre = {nodo_inicio: None}
    distancia = {nodo_inicio: 0}

    cola.put(nodo_inicio)
    visitados.add(nodo_inicio)

    while not cola.empty():
        v = cola.get()
        orden.append(v)

        for w in grafica.get(v, []):
            if w not in visitados:
                visitados.add(w)
                padre[w] = v
                distancia[w] = distancia[v] + 1
                cola.put(w)

    print("Recorrido BFS desde", nodo_inicio, ":", orden)
    print("Padres:", padre)
    print("Distancias:", distancia)

# Llamamos a la funcion bfs
bfs(grafica, 'A')
