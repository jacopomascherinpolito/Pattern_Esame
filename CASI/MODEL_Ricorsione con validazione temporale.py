from datetime import datetime


# Assumi che ogni nodo (oggetto) abbia un attributo .date (datetime)
def _ricorsione_temporale(self, parziale):
    last_node = parziale[-1]

    # Prendo i vicini ordinati (magari per data o peso)
    neighbors = self._graph[last_node]

    for neighbor in neighbors:
        if neighbor not in parziale:
            # --- IL BLOCCO DIFENSIVO ---
            date_curr = self._nodes_map[last_node].datetime
            date_next = self._nodes_map[neighbor].datetime

            # Calcolo delta giorni
            delta = (date_next - date_curr).days

            # Vincolo: Deve essere futuro, ma entro 3 giorni
            if 0 < delta <= 3:
                parziale.append(neighbor)
                self._ricorsione_temporale(parziale)
                parziale.pop()