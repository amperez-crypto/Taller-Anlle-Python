import pandas as pd
import sqlite3

conn = sqlite3.connect("data/personas_limpias.db")
datos = pd.read_sql("SELECT * FROM personas", conn)
conn.close()

condicion = (datos['nombre'] == 'Ana') & (datos['profesion'] == 'MEDICO')
print(f"Ana y Medico: {datos[condicion].shape[0]}")
# Respuesta esperada: 170