from datetime import datetime

# Nel costruttore del tuo oggetto
def __init__(self, ... date_str ...):
    # Se arriva come stringa, convertila subito!
    if isinstance(date_str, str):
        # Attenzione al formato! YYYY-MM-DD HH:MM:SS è standard
        self.datetime = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    else:
        self.datetime = date_str # È già un oggetto datetime

# Per le stringhe: Strip()
self.city = city_name.strip().upper() # Rimuove spazi extra e uniforma