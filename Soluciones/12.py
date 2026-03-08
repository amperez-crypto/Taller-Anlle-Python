import pandas as pd

# Leer CSV original SIN limpiar
datos = pd.read_csv("data/personas.csv")

# Contar emails con espacios antes o después
condicion = datos['email'] != datos['email'].str.strip()
print(f"Emails con espacios: {condicion.sum()}")