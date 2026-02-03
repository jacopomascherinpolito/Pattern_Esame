# METODO PUBBLICO: Inizializza e lancia la ricorsione
def find_best_path(self, nodo_partenza, soglia_o_target):
    # 1. Pulizia variabili della soluzione migliore
    self._best_path = []
    self._best_score = 0

    # 2. Inizializzo il percorso parziale con il nodo di partenza
    parziale = [nodo_partenza]

    # 3. Lancio la funzione ricorsiva
    self._ricorsione(parziale, soglia_o_target)

    # 4. Ritorno il risultato
    return self._best_path, self._best_score


# METODO PRIVATO: Il motore ricorsivo
def _ricorsione(self, parziale, target):
    # A. CALCOLO SCORE ATTUALE
    # Calcolo quanto "vale" il cammino che sto esplorando ora
    current_score = self.get_score(parziale)  # (Metodo da scrivere a parte)

    # B. CONTROLLO SE È IL MIGLIORE (Max)
    # Se il cammino è valido e ha un punteggio più alto del record precedente...
    if current_score > self._best_score:
        self._best_score = current_score
        self._best_path = list(parziale)  # <--- FONDAMENTALE: Copia la lista, non il riferimento!

    # C. CONDIZIONE DI TERMINAZIONE (Opzionale ma utile)
    # Es. Se ho superato una lunghezza massima, mi fermo.
    # if len(parziale) > 10: return

    # D. TROVO I CANDIDATI SUCCESSIVI
    last_node = parziale[-1]

    # Recupero i vicini dal grafo
    vicini = list(self._graph.neighbors(last_node))

    # D1. Ordinamento (Euristica/Pruning)
    # Spesso richiesto: "prova prima i vicini con peso più alto"
    # Questo aiuta a trovare una soluzione buona subito.
    # vicini.sort(key=lambda x: self._graph[last_node][x]['weight'], reverse=True)

    # D2. Pruning (Taglio)
    # Se il grafo è denso, ciclo solo sui primi K vicini (es. [:5])

    for v in vicini:

        # E. VINCOLI E FILTRI
        # Qui si gioca l'esame. Devo evitare cicli e rispettare le regole.

        # Regola 1: Non ripassare dallo stesso nodo (Cammino semplice)
        if v not in parziale:
            # Regola 2: Eventuali vincoli specifici (es. Peso arco > X, Data crescente...)
            # peso_arco = self._graph[last_node][v]['weight']
            # if peso_arco > target:

            # F. BACKTRACKING (Il cuore della ricorsione)
            parziale.append(v)  # 1. Aggiungo
            self._ricorsione(parziale, target)  # 2. Scendo
            parziale.pop()  # 3. Tolgo (per provare altre strade)


# Helper per calcolare il punteggio
def get_score(self, path):
    score = 0
    if len(path) < 2: return 0
    for i in range(len(path) - 1):
        u, v = path[i], path[i + 1]
        score += self._graph[u][v]['weight']
    return score