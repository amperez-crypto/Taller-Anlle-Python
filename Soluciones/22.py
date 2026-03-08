import pandas as pd

datos = pd.read_csv("data/personas.csv")

datos['fecha_nacimiento'] = pd.to_datetime(datos['fecha_nacimiento'], errors='coerce')

fecha_actual = pd.Timestamp('2026-02-26')
condicion = (fecha_actual - datos['fecha_nacimiento']).dt.days / 365.25 > 50
print(f"Personas con más de 50 años: {condicion.sum()}")
# Respuesta esperada: 101536