import pandas as pd
import sqlite3

conn = sqlite3.connect("data/personas_limpias.db")
datos = pd.read_sql("SELECT * FROM personas", conn)
conn.close()

ingenieros = datos[datos['profesion'] == 'INGENIERO']
ciudad = ingenieros['ciudad'].value_counts().idxmax()
total = ingenieros['ciudad'].value_counts().max()
print(f"Ciudad con más ingenieros: {ciudad} con {total}")
# Respuesta esperada: POPAYAN con 618