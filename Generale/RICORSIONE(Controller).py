def handle_calcola_percorso(self, e):
    # 1. Lettura Input (es. Nodo partenza e Target)
    nodo_id = self._view.dd_nodo.value
    if nodo_id is None:
        self._view.create_alert("Seleziona un nodo di partenza!")
        return

    target = self._view.txt_target.value  # (Se c'è un input numerico)

    # 2. Feedback "Sto lavorando"
    self._view.txt_result.controls.clear()
    self._view.txt_result.controls.append(ft.Text("Calcolo in corso..."))
    self._view.update_page()  # Aggiorno subito la grafica!

    # 3. Chiamata Ricorsiva
    # Nota: Potrebbe metterci un po'
    path, score = self._model.find_best_path(nodo_id, target)

    # 4. Visualizzazione Risultati
    self._view.txt_result.controls.clear()

    if not path:
        self._view.txt_result.controls.append(ft.Text("Nessun percorso trovato."))
    else:
        self._view.txt_result.controls.append(ft.Text(f"Percorso Ottimo Trovato!"))
        self._view.txt_result.controls.append(ft.Text(f"Score: {score}"))
        self._view.txt_result.controls.append(ft.Text(f"Lunghezza: {len(path)}"))

        # Stampa elenco nodi
        for p in path:
            self._view.txt_result.controls.append(ft.Text(f"-> {p}"))

    self._view.update_page()