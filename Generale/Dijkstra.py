#Dato un nodo di partenza scelto dall'utente e uno di arrivo, trovare il percorso a costo minimo

#MODEL

def get_cammino_minimo(self, id_partenza, id_arrivo):
    # 1. Recupero gli oggetti dalla mappa (sempre!)
    source = self._id_map[id_partenza]
    target = self._id_map[id_arrivo]

    # 2. Controllo se sono collegati (opzionale, nx lancia eccezione se no)
    if not nx.has_path(self._graph, source, target):
        return None, 0

    # 3. Calcolo il percorso (Lista di nodi)
    path = nx.shortest_path(self._graph, source, target, weight='weight')

    # 4. Calcolo il costo (Numero)
    # Nota: potrei sommare i pesi del path manualmente, ma nx ha la funzione apposta
    costo = nx.shortest_path_length(self._graph, source, target, weight='weight')

    return path, costo

#CONTROLLER

    def handle_shortest_path(self, e):
        destinazione = self._view.dd_destinazione.value  # Ipotizziamo ci sia
        partenza = self._view.dd_squadra.value

        if not destinazione or not partenza:
            return

        try:
            path, costo = self._model.get_cammino_minimo(partenza, destinazione)

            if path is None:
                self._view.create_alert("I due nodi non sono collegati!")
            else:
                self._view.txt_result.controls.append(ft.Text(f"Costo minimo: {costo}"))
                for p in path:
                    self._view.txt_result.controls.append(ft.Text(f"-> {p.name}"))
                self._view.update_page()

        except Exception as e:
            self._view.create_alert("Errore nel calcolo del percorso.")