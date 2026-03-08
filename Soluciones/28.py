import pandas as pd
import sqlite3

conn = sqlite3.connect("data/personas_limpias.db")
datos = pd.read_sql("SELECT * FROM personas", conn)
conn.close()

resultado = datos.groupby('profesion')['salario_limpio'].mean()
profesion = resultado.idxmax()
promedio = round(resultado.max(), 2)
print(f"Profesión con salario promedio más alto: {profesion} con {promedio}")