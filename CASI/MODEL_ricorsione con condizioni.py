#utile per calcoli che implicano condizioni "successive"

def _ricorsione(self, parziale, ultimo_tipo_visto):
    # ... condizioni di terminazione ...

    last_node = parziale[-1]

    for neighbor in self._graph[last_node]:
        if neighbor not in parziale:
            # RECUPERO IL TIPO DEL VICINO (es. dal grafo o dizionario nodi)
            tipo_vicino = self._nodes_map[neighbor].tipo

            # IL VINCOLO
            if tipo_vicino == ultimo_tipo_visto:
                continue  # Salta questo vicino, violerebbe la regola

            # Se passa, vai avanti aggiornando lo stato
            parziale.append(neighbor)
            self._ricorsione(parziale, tipo_vicino)  # Passo il nuovo tipo
            parziale.pop()