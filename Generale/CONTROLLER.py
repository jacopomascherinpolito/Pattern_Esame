def handle_crea_grafo(self, e):
    # 1. Lettura Input
    # Leggo cosa ha scelto l'utente nella tendina o casella di testo
    valore = self._view.dd_filtro.value

    # 2. Controllo Difensivo (Validazione Input)
    # Mai fidarsi dell'utente. Se non ha scelto nulla, fermati.
    if valore is None:
        self._view.create_alert("Attenzione: Seleziona un valore!")
        return

    # 3. Blocco UI (Feedback utente)
    # Se il grafo è grosso, l'app si congela. Diciamo all'utente di aspettare.
    self._view.txt_result.controls.clear()
    self._view.txt_result.controls.append(ft.Text("Creazione grafo in corso..."))
    self._view.update_page()

    # 4. Chiamata al Model (Lavoro sporco)
    # Nota: Potrebbe restituire una stringa o nulla, dipende come l'hai fatto.
    try:
        msg = self._model.build_graph(valore)

        # 5. Output Successo
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Successo!"))
        self._view.txt_result.controls.append(ft.Text(msg))

        # 6. (Opzionale) Abilitare tasti successivi
        # Spesso i tasti per il Punto 2 sono disabilitati finché non crei il grafo
        self._view.btn_calcola_percorso.disabled = False

    except Exception as e:
        # Gestione Errori (es. Database scollegato)
        self._view.txt_result.controls.append(ft.Text(f"Errore: {e}"))

    # 7. Aggiornamento finale pagina
    self._view.update_page()