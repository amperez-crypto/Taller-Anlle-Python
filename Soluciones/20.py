import pandas as pd

datos = pd.read_csv("data/personas.csv")

datos['fecha_nacimiento'] = pd.to_datetime(datos['fecha_nacimiento'], errors='coerce')

condicion = (datos['fecha_nacimiento'].dt.year >= 1990) & (datos['fecha_nacimiento'].dt.year <= 2000)
print(f"Nacidos entre 1990 y 2000: {condicion.sum()}")
# Respuesta esperada: 37518