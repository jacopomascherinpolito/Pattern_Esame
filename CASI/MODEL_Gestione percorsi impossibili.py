#utile per grafi con isole

import networkx as nx

try:
    path = nx.shortest_path(self._graph, source, target, weight='weight')
    return path
except nx.NetworkXNoPath:
    return [] # O None, gestiscilo poi nella GUI dicendo "Nessun percorso trovato"
except nx.NodeNotFound:
    return None # Uno dei nodi non è nel grafo