import pandas as pd
import sqlite3

conn = sqlite3.connect("data/personas_limpias.db")
datos = pd.read_sql("SELECT * FROM personas", conn)
conn.close()

datos['fecha_nacimiento'] = pd.to_datetime(datos['fecha_nacimiento'], errors='coerce')

condicion = (
    (datos['ciudad'] == 'BARRANQUILLA') & 
    (datos['activo_limpio'] == 1) & 
    (datos['fecha_nacimiento'].dt.year > 1980)
)
print(f"Barranquilla, activos, nacidos después de 1980: {datos[condicion].shape[0]}")
# Respuesta esperada: 2082