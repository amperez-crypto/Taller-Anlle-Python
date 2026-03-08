import pandas as pd
import codecs
import re

# =============================================
# CARGAR DATOS
# =============================================
datos = pd.read_csv("data/personas.csv")

# =============================================
# COLUMNA: nombre_cifrado → nombre
# =============================================
datos['nombre_cifrado_limpio'] = (
    datos['nombre_cifrado']
    .astype(str)
    .str.strip()
    .str.replace(r'[^a-zA-Z]', '', regex=True)
)
datos['nombre'] = datos['nombre_cifrado_limpio'].apply(
    lambda x: codecs.decode(x, 'rot_13')
)

# =============================================
# COLUMNA: apellido_cifrado → apellido
# =============================================
datos['apellido_cifrado_limpio'] = (
    datos['apellido_cifrado']
    .astype(str)
    .str.strip()
    .str.replace(r'[^a-zA-Z]', '', regex=True)
)
datos['apellido'] = datos['apellido_cifrado_limpio'].apply(
    lambda x: codecs.decode(x, 'rot_13')
)
def limpiar_salario(valor):
    valor = str(valor).strip()
    # Si tiene coma, es separador decimal tipo europeo: 14024383,00
    if ',' in valor:
        valor = valor.replace(',', '.')  # convertir a punto decimal
    # Quitar todo lo que no sea número o punto
    valor = re.sub(r'[^0-9.]', '', valor)
    try:
        resultado = float(valor)
        if resultado < 1000:
            return None
        return resultado
    except:
        return None
    
def limpiar_salario(valor):
    valor = str(valor).strip()
    # Reemplazar letras que parecen números
    valor = valor.replace('l', '1').replace('L', '1')
    valor = valor.replace('O', '0').replace('o', '0')
    # Quitar "aprox."
    valor = valor.replace('aprox.', '')
    # Reemplazar coma decimal
    valor = valor.replace(',', '.')
    # Quitar todo lo que no sea número o punto
    valor = re.sub(r'[^0-9.]', '', valor)
    try:
        resultado = float(valor)
        if resultado < 1000:
            return None
        return resultado
    except:
        return None

# ===========