import pandas as pd
import sqlite3

conn = sqlite3.connect("data/personas_limpias.db")
datos = pd.read_sql("SELECT * FROM personas", conn)
conn.close()

condicion = (datos['profesion'] == 'ABOGADO') & (datos['salario_limpio'] > 10000000)
print(f"Abogados con salario > 10,000,000: {datos[condicion].shape[0]}")
# Respuesta esperada: 4269