import pandas as pd
import re

datos = pd.read_csv("data/personas.csv")

condicion = ~datos['fecha_nacimiento'].astype(str).str.match(r'^\d{4}-\d{2}-\d{2}$')
print(f"Fechas con formato diferente: {condicion.sum()}")
# Respuesta esperada: 89823