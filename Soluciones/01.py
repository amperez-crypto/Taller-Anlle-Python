import sqlite3
import pandas as pd
import re

# Leer desde la base de datos ya limpia
conn = sqlite3.connect("data/personas_limpias.db")
datos = pd.read_sql("SELECT * FROM personas", conn)
conn.close()

# Identificar ids con caracteres no numéricos
condicion = datos['id'].astype(str).apply(lambda x: bool(re.search(r'\D', x)))

cantidad = datos[condicion].shape[0]
print(f"IDs con caracteres no numéricos: {cantidad}")
# Respuesta esperada: 83648