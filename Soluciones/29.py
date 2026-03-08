import pandas as pd

datos = pd.read_csv("data/personas.csv")

datos['email'] = datos['email'].astype(str).str.strip()
condicion = datos['email'].str.endswith('@gmail.com')
print(f"Emails con gmail.com: {condicion.sum()}")
# Respuesta esperada: 49273