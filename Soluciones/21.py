import pandas as pd

datos = pd.read_csv("data/personas.csv")

datos['fecha_nacimiento'] = pd.to_datetime(datos['fecha_nacimiento'], errors='coerce')

condicion = datos['fecha_nacimiento'].dt.year < 1960
print(f"Nacidos antes de 1960: {condicion.sum()}")
# Respuesta esperada: 46713