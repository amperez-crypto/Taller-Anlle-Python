import sqlite3
import pandas as pd

conn = sqlite3.connect("data/personas_limpias.db")
datos = pd.read_sql("SELECT * FROM personas", conn)
conn.close()

apellido_frecuente = datos['apellido'].value_counts().idxmax()
cantidad = datos['apellido'].value_counts().max()
print(f"Apellido más frecuente: {apellido_frecuente} con {cantidad} veces")
# Respuesta esperada: Rivera 7490