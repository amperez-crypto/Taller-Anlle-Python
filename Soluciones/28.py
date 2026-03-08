import pandas as pd
import re

datos = pd.read_csv("data/personas.csv")

# Limpiar profesion
datos['profesion'] = (
    datos['profesion']
    .astype(str)
    .str.strip()
    .str.replace("á","a").str.replace("é","e")
    .str.replace("í","i").str.replace("ó","o").str.replace("ú","u")
    .str.upper()
    .str.replace(r'[^A-Z ]', '', regex=True)
    .str.strip()
)

mapeo_profesiones = {
    'CONTDOR': 'CONTADOR', 'ELCTRICIST': 'ELECTRICISTA',
    'PRIODIST': 'PERIODISTA', 'ECONOMIST': 'ECONOMISTA',
    'PROGRMDOR': 'PROGRAMADOR', 'PLOMRO': 'PLOMERO',
    'ENFRMRO': 'ENFERMERO', 'INGNIRO': 'INGENIERO',
    'TRDUCTOR': 'TRADUCTOR', 'DISNDOR': 'DISENADOR',
    'VTRINRIO': 'VETERINARIO', 'MDICO': 'MEDICO',
    'ABOGDO': 'ABOGADO', 'ADMINISTRDOR': 'ADMINISTRADOR',
    'ARQUITCTO': 'ARQUITECTO', 'CRPINTRO': 'CARPINTERO',
    'PROFSOR': 'PROFESOR', 'MCNICO': 'MECANICO', 'CHF': 'CHEF'
}
datos['profesion'] = datos['profesion'].replace(mapeo_profesiones)

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

resultado = datos.groupby('profesion')['salario_limpio'].mean()
profesion = resultado.idxmax()
promedio = round(resultado.max(), 2)
print(f"Profesión con salario promedio más alto: {profesion} con {promedio}")
# Respuesta esperada: ADMINISTRADOR con 8071640.0