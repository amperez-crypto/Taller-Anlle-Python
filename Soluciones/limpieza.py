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

# ===========