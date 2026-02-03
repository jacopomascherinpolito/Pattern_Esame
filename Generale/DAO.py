class DAO:

    # METODO 1: Scaricare i Nodi
    # Scarica TUTTE le entità che faranno parte del grafo.
    # Spesso filtrati per un input utente (es. Anno, Categoria).
    @staticmethod
    def get_all_nodes(filtro_utente):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)  # Dictionary=True per leggere row['colonna']

        # Query generica: Prendi ID e info utili
        query = """SELECT id, nome, valore_extra
                   FROM tabella_entita
                   WHERE categoria = %s"""

        cursor.execute(query, (filtro_utente,))

        result = []
        for row in cursor:
            # Creiamo l'oggetto (Bean)
            # È meglio aver definito una classe Entita in model/entita.py
            obj = Entita(row['id'], row['nome'], row['valore_extra'])
            result.append(obj)

        cursor.close()
        conn.close()
        return result

    # METODO 2: Scaricare gli Archi (O i dati per costruirli)
    # Questo serve se la relazione è scritta nel DB (es. tabella 'connessioni').
    # Se il grafo è "Completo" o "Geometrico", questo metodo potrebbe non servire.
    @staticmethod
    def get_all_edges(filtro_utente):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        # Pattern "Self-Join" generico
        # Trova coppie (id1, id2) che soddisfano una condizione
        # SUM(valore) serve se il peso è un'aggregazione
        query = """
                SELECT t1.id as id1, t2.id as id2, SUM(t1.val) as peso
                FROM tabella t1, \
                     tabella t2
                WHERE t1.gruppo = t2.gruppo -- Condizione di collegamento
                  AND t1.id < t2.id         -- Evita duplicati (Grafo Non Orientato)
                GROUP BY t1.id, t2.id \
                """
        cursor.execute(query)
        result = []
        for row in cursor:
            # Restituisco tuple semplici (id_partenza, id_arrivo, peso)
            result.append((row['id1'], row['id2'], row['peso']))

        cursor.close()
        conn.close()
        return result