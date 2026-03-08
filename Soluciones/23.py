import pandas as pd
import sqlite3

conn = sqlite3.connect("data/personas_limpias.db")
datos = pd.read_sql("SELECT * FROM personas", conn)
conn.close()

condicion = (datos['nombre'] == 'Carlos') & (datos['ciudad'] == 'CALI')
print(f"Carlos en Cali: {datos[condicion].shape[0]}")
# Respuesta esperada: 186