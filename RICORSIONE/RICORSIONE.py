def get_best_path(self, start_node, max_edges=None):
    self._best_path = []
    self._best_score = 0

    parziale = [start_node]
    self._ricorsione(parziale)
    return self._best_path, self._best_score


def _ricorsione(self, parziale):
    # 1. Controllo se è una soluzione migliore (Max peso o Max lunghezza)
    current_score = self.calcola_peso(parziale)  # O len(parziale)
    if current_score > self._best_score:
        self._best_score = current_score
        self._best_path = list(parziale)

    # 2. Condizione di terminazione (opzionale, es. max 5 archi)
    # if len(parziale) > max_edges: return

    # 3. Trova candidati
    last_node = parziale[-1]
    # Ottimizzazione BASEBALL (Pruning): Prendi solo i vicini "migliori" se richiesto
    neighbors = sorted(self._graph[last_node],
                       key=lambda x: self._graph[last_node][x]['weight'],
                       reverse=True)

    for neighbor in neighbors:
        edge_weight = self._graph[last_node][neighbor]['weight']

        # 4. Vincoli (Es. Peso decrescente, nodo non visitato)
        if neighbor not in parziale:
            # if edge_weight < last_weight: (Esempio vincolo decrescente)

            parziale.append(neighbor)
            self._ricorsione(parziale)
            parziale.pop()  # Backtracking