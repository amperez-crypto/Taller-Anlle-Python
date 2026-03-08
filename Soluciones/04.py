import sqlite3
import pandas as pd

conn = sqlite3.connect("data/personas_limpias.db")
datos = pd.read_sql("SELECT * FROM personas", conn)
conn.close()

nombre_frecuente = datos['nombre'].value_counts().idxmax()
cantidad = datos['nombre'].value_counts().max()
print(f"Nombre más frecuente: {nombre_frecuente} con {cantidad} veces")
# Respuesta esperada: Gonzalo 4221