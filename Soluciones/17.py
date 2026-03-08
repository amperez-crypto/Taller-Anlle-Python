import pandas as pd

datos = pd.read_csv("data/personas.csv")

def limpiar_activo(valor):
    valor = str(valor).strip().lower()
    if valor in ['true', '1', 'yes', 'si', 'sí', 'verdadero']:
        return True
    elif valor in ['false', '0', 'no', 'falso']:
        return False
    return None

datos['activo_limpio'] = datos['activo'].apply(limpiar_activo)
print(f"Activos True: {datos[datos['activo_limpio'] == True].shape[0]}")
# Respuesta esperada: 139582