#utile per calcolare peso alla fine del percorso se ci sono formule o condizioni strane

def calcola_score_complesso(self, path):
    score = 0
    # Somma pesi archi
    for i in range(len(path) - 1):
        score += self._graph[path[i]][path[i + 1]]['weight']

    # Penalità strana del prof
    delta_t = (path[-1].date - path[0].date).days
    return score - delta_t