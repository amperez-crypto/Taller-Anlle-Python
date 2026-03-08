import pandas as pd
import sqlite3

conn = sqlite3.connect("data/personas_limpias.db")
datos = pd.read_sql("SELECT * FROM personas", conn)
conn.close()

condicion = (datos['nombre'] == 'Jose') & (datos['apellido'] == 'Garcia')
print(f"Jose Garcia: {datos[condicion].shape[0]}")
# Respuesta esperada: 96