import sqlite3
import pandas as pd

conn = sqlite3.connect("data/personas_limpias.db")
datos = pd.read_sql("SELECT * FROM personas", conn)
conn.close()

condicion = datos['nombre'] == 'Juan'
print(f"Juan aparece: {datos[condicion].shape[0]}")
# Respuesta esperada: 3986
