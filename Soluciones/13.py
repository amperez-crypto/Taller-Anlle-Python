import pandas as pd
import re

datos = pd.read_csv("data/personas.csv")

condicion = datos['salario'].astype(str).apply(lambda x: bool(re.search(r'[^0-9.]', x)))
print(f"Salarios con caracteres no numéricos: {condicion.sum()}")