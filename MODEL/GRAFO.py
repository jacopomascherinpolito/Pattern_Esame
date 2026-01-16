def build_graph(self):
    self._graph.clear()
    # 1. Nodi
    self._nodes = self._dao.get_all_nodes()
    self._graph.add_nodes_from(self._nodes)

    # 2. Id Map (Fondamentale per le performance)
    self._id_map = {n.id: n for n in self._nodes}

    # 3. Archi
    edges = self._dao.get_all_edges(self._id_map)
    for u, v, w in edges:
        self._graph.add_edge(u, v, weight=w)

    # Extra: Se serve Componente Connessa (iTunes, Artsmia)
    # connected_components = list(nx.connected_components(self._graph))