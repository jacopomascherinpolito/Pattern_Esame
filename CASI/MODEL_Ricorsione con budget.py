def get_cammino_budget(self, start_node, budget_max):
    self._best_path = []
    self._best_len = 0
    # Passo il budget rimanente alla ricorsione
    self._ricorsione_budget([start_node], budget_max)


def _ricorsione_budget(self, parziale, budget_residuo):
    # Aggiorno il best se il cammino è più lungo
    if len(parziale) > self._best_len:
        self._best_len = len(parziale)
        self._best_path = list(parziale)

    last = parziale[-1]

    for neighbor in self._graph[last]:
        costo_arco = self._graph[last][neighbor]['weight']

        # --- IL BLOCCO DIFENSIVO ---
        # Posso permettermelo?
        if neighbor not in parziale and budget_residuo >= costo_arco:
            parziale.append(neighbor)
            # Riduco il budget per il prossimo livello
            self._ricorsione_budget(parziale, budget_residuo - costo_arco)
            parziale.pop()