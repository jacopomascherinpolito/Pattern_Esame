def handle_analizza(self, e):
    # 1. Feedback immediato
    self._view.btn_analizza.disabled = True
    self._view.txt_result.value = "Elaborazione in corso..."
    self._view.update_page()  # FONDAMENTALE: Forza l'aggiornamento grafico

    # 2. Lavoro pesante
    try:
        self._controller.crea_grafo(...)
        self._view.txt_result.value = "Grafo creato!"
    except Exception as ex:
        self._view.txt_result.value = f"Errore: {ex}"

    # 3. Riabilita tutto
    self._view.btn_analizza.disabled = False
    self._view.update_page()