import sqlite3
import pandas as pd

conn = sqlite3.connect("data/personas_limpias.db")
datos = pd.read_sql("SELECT * FROM personas", conn)
conn.close()

condicion = datos['ciudad'] == 'BOGOTA'
print(f"Bogota: {datos[condicion].shape[0]}")
# Respuesta esperada: 14739