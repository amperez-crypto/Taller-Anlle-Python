#Cargar datos
import pandas as pd

RUTA_ARCHIVO="data/personas,csv"

datos = pd.read_csv('data/personas.csv')

def decifrar_palabra(palabra_cifrada):
    import codecs
    nueva_palabra = codecs.encode(palabra_cifrada,"rot13")
    return nueva_palabra

datos["nombre"] = datos ["nombre_cifrado"].apply(decifrar_palabra)
condicion = datos["nombre"] =="Juan"
print("Juan aparece:",datos[condicion].shape[0])
