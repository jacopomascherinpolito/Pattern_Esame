def _ricorsione_tappa(self, parziale, ha_visitato_tappa):
    # Condizione di fine: sono arrivato a destinazione E ho visitato la tappa
    if parziale[-1] == TARGET and ha_visitato_tappa:
        # Salva soluzione...
        return

    last = parziale[-1]
    for v in self._graph[last]:
        if v not in parziale:
            # Aggiorno lo stato del flag
            nuovo_stato_tappa = ha_visitato_tappa or (v.id == NODO_TAPPA)

            parziale.append(v)
            self._ricorsione_tappa(parziale, nuovo_stato_tappa)
            parziale.pop()