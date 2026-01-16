# Nel ciclo for della ricorsione:

neighbors = list(self._graph[last_node])

# TRUCCO: Ordina i vicini per peso e prendi solo i primi K (es. 5)
# Questo riduce la complessità da O(N!) a O(K^Depth)
sorted_neighbors = sorted(
    neighbors,
    key=lambda x: self._graph[last_node][x]['weight'],
    reverse=True # O False se cerchi minimi
)

for neighbor in sorted_neighbors[:5]:
    # ... logica ricorsiva ...