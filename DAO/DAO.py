# Nel DAO
def get_all_nodes(self):
    cnx = DBConnect.get_connection()
    cursor = cnx.cursor(dictionary=True)
    query = """SELECT * FROM table_nodes WHERE ...""" # Es. Anno > 2010
    cursor.execute(query)
    result = []
    for row in cursor:
        result.append(Node(**row)) # Assumi di avere una dataclass
    cursor.close()
    cnx.close()
    return result

# Pattern "Self-Join" per gli Archi (Il più comune: iTunes, Artsmia, Genes)
# Trova coppie che condividono qualcosa in una tabella "ponte"
def get_all_edges(self, id_map):
    cnx = DBConnect.get_connection()
    cursor = cnx.cursor(dictionary=True)
    query = """
    SELECT t1.ItemId AS id1, t2.ItemId AS id2, count(*) as peso
    FROM bridging_table t1, bridging_table t2
    WHERE t1.ContainerId = t2.ContainerId -- Stessa playlist/mostra
    AND t1.ItemId < t2.ItemId -- Evita duplicati e auto-anelli
    GROUP BY t1.ItemId, t2.ItemId
    """
    cursor.execute(query)
    edges = []
    for row in cursor:
        # Grazie alla id_map recuperiamo gli oggetti velocemente
        if row['id1'] in id_map and row['id2'] in id_map:
            edges.append((id_map[row['id1']], id_map[row['id2']], row['peso']))
    cursor.close()
    cnx.close()
    return edges