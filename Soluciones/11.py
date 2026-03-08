import sqlite3
import pandas as pd

conn = sqlite3.connect("data/personas_limpias.db")
datos = pd.read_sql("SELECT * FROM personas", conn)
conn.close()

total = datos['profesion'].nunique()
print(f"Profesiones únicas: {total}")
# Respuesta esperada: 44