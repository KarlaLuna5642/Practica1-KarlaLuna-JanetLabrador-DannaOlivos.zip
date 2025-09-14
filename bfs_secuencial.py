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
    """
    Implementa el algoritmo BFS para recorrer un grafo conexo o un árbol.
    
    Parameters:
    grafica (dict): Grafo representado como diccionario de listas de adyacencia.
    nodo_inicio (str): Nodo desde donde comienza el recorrido BFS.
    
    Returns:
    tupla : (orden, padre, distancia) 
    """
    if nodo_inicio not in grafica:
        print("Nodo de '{nodo_inicio}' no existe en el grafo")
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
    return orden, padre, distancia

def crear_grafo():
    """
    Crea un grafo a partir de la entrada del usuario.
    
    Returns:
    dict: Grafo representado como diccionario de listas de adyacencia
    """
    grafica = {}
    print("=== CREA TU GRÁFICA ===")
    print("Ingrese las conexiones de cada nodo (ejemplo: A = B C D), donde A es el nodo a quien estamos asignando B C D como adyacencias")
    print("Escriba 'fin' cuando termine de ingresar todos los nodos")
    print("-" * 30)
    
    while True:
        entrada = input("Ingrese nodo y sus vecinos (ej: A = B C D): ").strip()
        
        if entrada.lower() == 'fin':
            break
            
        if not entrada:
            continue
            
        partes = entrada.split()
        nodo = partes[0]
        vecinos = partes[2:]
        grafica[nodo] = vecinos
        
        for vecino in vecinos:
            if vecino not in grafica:
                grafica[vecino] = [nodo]
            elif nodo not in grafica[vecino]:
                grafica[vecino].append(nodo)
    
    return grafica

def resultados(orden, padre, distancia, nodo_inicio):
    """
    Muestra los resultados del recorrido BFS.
    
    Parameters:
    orden (list): Orden de visita de los nodos
    padre (dict): Diccionario de padres
    distancia (dict): Diccionario de distancias
    nodo_inicio (str): Nodo inicial del recorrido
    """
    print(f"\n=== RESULTADOS BFS DESDE '{nodo_inicio}' ===")
    print(f"Recorrido completo: {' -> '.join(orden)}")
    
    print("\nDetalles por nodo:")
    print("-" * 30)
    print(f"{'Nodo':<5} {'Padre':<5} {'Distancia':<10}")
    print("-" * 30)
    
    for nodo in orden:
        pad = padre[nodo] if padre[nodo] is not None else "None"
        dist = distancia[nodo]
        print(f"{nodo:<5} {pad:<5} {dist:<10}")


def mostrar_grafo(grafica):
    """
    Muestra el grafo de forma ordenada.
    
    Parameters:
    grafica (dict): Grafo a mostrar
    """
    print("\n=== GRAFO INGRESADO ===")
    for nodo, vecinos in sorted(grafica.items()):
        print(f"{nodo}: {', '.join(sorted(vecinos))}")

def main():

    print("=== ALGORITMO BFS ===")
    grafica = crear_grafo()
    
    if not grafica:
        print("No se ingresó ningún grafo. Saliendo...")
        return
    
    mostrar_grafo(grafica)
    print(f"\nNodos disponibles: {', '.join(sorted(grafica.keys()))}")
    
    while True:
        nodo_inicio = input("\nIngrese el nodo de inicio para BFS: ").strip()
        
        if nodo_inicio in grafica:
            break
        else:
            print(f"Error: El nodo '{nodo_inicio}' no existe en el grafo")
            print(f"Nodos válidos: {', '.join(sorted(grafica.keys()))}")

    resultado = bfs(grafica, nodo_inicio)
    
    if resultado:
        orden, padre, distancia = resultado
        resultados(orden, padre, distancia, nodo_inicio)

main()
