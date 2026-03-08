import pandas as pd
import re

datos = pd.read_csv("data/personas.csv")

def limpiar_salario(valor):
    valor = str(valor).strip()
    valor = valor.replace('l', '1').replace('L', '1')
    valor = valor.replace('O', '0').replace('o', '0')
    valor = valor.replace('aprox.', '')
    valor = valor.replace(',', '.')
    valor = re.sub(r'[^0-9.]', '', valor)
    try:
        resultado = float(valor)
        if resultado < 1000:
            return None
        return resultado
    except:
        return None

datos['salario_limpio'] = datos['salario'].apply(limpiar_salario)
print(f"Salario promedio: {round(datos['salario_limpio'].mean(), 2)}")
# Respuesta esperada: 8007002.59