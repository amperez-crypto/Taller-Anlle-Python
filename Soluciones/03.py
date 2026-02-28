#Cargar datos
import pandas as pd
import codecs

datos = pd.read_csv('data/personas.csv')
#----------------------------------------
#--------Fin cargar datos----------------

texto_original = "Juan"

#Cifrar ROT13
texto_cifrado = codecs.encode(texto_original,'rot_13')
print(f"Cifrado_ {texto_cifrado}")

# MARIA = ZNEVN

condicion = datos['nombre_cifrado'] == 'Whna'

datos_nuevos =datos[condicion]

print(datos_nuevos)