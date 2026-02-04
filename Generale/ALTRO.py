#GESTIONE DATE

from datetime import datetime

# 1. PARSING: Da Stringa a Oggetto
str_data = "2023-10-15 14:30:00"
# %Y=Anno(4), %m=Mese, %d=Giorno, %H=Ore(24), %M=Minuti, %S=Secondi
obj_data = datetime.strptime(str_data, "%Y-%m-%d %H:%M:%S")

# 2. DIFFERENZA (Timedelta)
data_inizio = datetime(2023, 10, 15, 14, 0, 0)
data_fine = datetime(2023, 10, 15, 16, 30, 0)

durata = data_fine - data_inizio  # Restituisce un oggetto timedelta

# Ottenere i valori numerici
minuti_totali = duration.total_seconds() / 60  # 150.0 minuti
giorni = duration.days


#GEOGRAFIA

# Devi aver installato: pip install geopy
from geopy.distance import geodesic

# Coordinate: (Latitudine, Longitudine)
coord_A = (45.0703, 7.6869) # Torino
coord_B = (41.9028, 12.4964) # Roma

# Calcolo distanza in Chilometri
distanza_km = geodesic(coord_A, coord_B).km
distanza_miles = geodesic(coord_A, coord_B).miles


#COMPONENTE CONNESSA

# Restituisce una lista di insiemi di nodi
connesse = list(nx.connected_components(self._graph))

num_componenti = len(connesse)

# Trovare la componente più grande (quella con più nodi)
largest_cc = max(connesse, key=len)

# Creare un sottografo con solo quei nodi (utile per il punto 2)
subgraph = self._graph.subgraph(largest_cc).copy()


#CAMMINO MINIMO

# Restituisce la lista dei nodi [A, C, D, B]
path = nx.shortest_path(self._graph, source=nodo_A, target=nodo_B, weight='weight')

# Restituisce solo il costo numerico
costo = nx.shortest_path_length(self._graph, source=nodo_A, target=nodo_B, weight='weight')


