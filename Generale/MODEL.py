import networkx as nx


class Model:
    def __init__(self):
        # Scegliere qui: Graph (Non Orientato) o DiGraph (Orientato)
        self._graph = nx.Graph()

        # Cache dei dati per non richiamare il DB inutilmente
        self._nodes = []

        # LA MAPPA FONDAMENTALE (ID -> Oggetto)
        # Ci serve per tradurre velocemente gli ID che arrivano dal DAO o dalla GUI
        self._id_map = {}

    def build_graph(self, filtro_utente):
        # 1. Pulizia: Fondamentale se l'utente clicca il bottone due volte
        self._graph.clear()

        # 2. Recupero Nodi dal DAO
        self._nodes = DAO.get_all_nodes(filtro_utente)

        # 3. Riempio la Mappa (TRUCCO SALVAVITA)
        # Associa l'ID univoco all'oggetto intero.
        # Ci permette di trovare un oggetto in O(1) invece che cercarlo nella lista
        self._id_map = {node.id: node for node in self._nodes}

        # 4. Aggiungo i nodi al grafo
        # NetworkX accetta la lista di oggetti direttamente
        self._graph.add_nodes_from(self._nodes)

        # 5. Costruzione Archi
        # CASO A: Archi dal DB (es. tabella connessioni)
        raw_edges = DAO.get_all_edges(filtro_utente)
        for u_id, v_id, peso in raw_edges:
            # Controllo che i nodi esistano (potrebbero essere stati filtrati via)
            if u_id in self._id_map and v_id in self._id_map:
                # Recupero gli oggetti veri dalla mappa
                nodo_u = self._id_map[u_id]
                nodo_v = self._id_map[v_id]

                # Aggiungo l'arco con il peso
                self._graph.add_edge(nodo_u, nodo_v, weight=peso)

        # OPPURE

        # CASO B: Archi calcolati in Python (es. Grafo Completo o Geometrico)
        # for i in range(len(self._nodes)):
        #    for j in range(i+1, len(self._nodes)):
        #        distanza = calcola_distanza(self._nodes[i], self._nodes[j])
        #        if distanza < soglia:
        #             self._graph.add_edge(self._nodes[i], self._nodes[j], weight=distanza)

        # 6. Debug / Info
        return f"Grafo creato: {len(self._graph.nodes)} nodi, {len(self._graph.edges)} archi"

    # Metodo utile per il Controller dopo
    def get_graph_details(self):
        return len(self._graph.nodes), len(self._graph.edges)