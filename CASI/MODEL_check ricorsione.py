#utile per controllare che il nodo selezionato non sia isolato e si possa calcolare un cammino

def pre_check_recursion(self, start_node):
    if not self._graph.has_node(start_node):
        return "Nodo non presente"

    # Verifica se il nodo è isolato
    degree = self._graph.degree(start_node)
    if degree == 0:
        return "Attenzione: Il nodo selezionato non ha connessioni."

    # Verifica la dimensione della componente connessa
    conn_comp = nx.node_connected_component(self._graph, start_node)
    if len(conn_comp) < 2:
        return "Componente troppo piccola per calcolare un cammino."

    return "OK"