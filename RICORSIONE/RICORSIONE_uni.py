def cerca_cammino_ottimo(self, start_node):
    self._best_path = []
    self._best_score = 0

    # Inizia ricorsione
    parziale = [start_node]
    self._ricorsione(parziale)
    return self._best_path, self._best_score


def _ricorsione(self, parziale):
    # 1. Calcola score attuale
    current_score = self.get_score(parziale)

    # 2. Aggiorna Best (se migliore)
    if current_score > self._best_score:
        self._best_score = current_score
        self._best_path = list(parziale)  # COPIA LA LISTA!

    # 3. Ottimizzazione (PRUNING) - Se il grafo è denso, questo ti salva dal TIMEOUT
    last_node = parziale[-1]
    neighbors = list(self._graph.neighbors(last_node))

    # Ordina: es. prova prima gli archi più pesanti
    neighbors.sort(key=lambda x: self._graph[last_node][x]['weight'], reverse=True)

    # Prendi solo i primi K (es. 5) se l'esame permette approssimazioni o se va lento
    # for neighbor in neighbors[:5]:
    for neighbor in neighbors:

        # 4. Vincoli (Loop, Peso, etc)
        if neighbor not in parziale:  # Evita cicli
            # Esempio vincolo: arco deve avere peso crescente
            # if self._graph[last_node][neighbor]['weight'] > last_weight:

            parziale.append(neighbor)
            self._ricorsione(parziale)
            parziale.pop()  # Backtracking