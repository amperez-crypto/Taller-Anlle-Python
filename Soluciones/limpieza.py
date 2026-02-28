import pandas as pd

datos= pd.read_csv("data/personas.csv")

#cambiar letras con tilde por letras sin tilde
datos["ciudad"] = datos["ciudad"].str.replace("á","a")
datos["ciudad"] = datos["ciudad"].str.replace("é","e")
datos["ciudad"] = datos["ciudad"].str.replace("í","i")
datos["ciudad"] = datos["ciudad"].str.replace("ó","o")
datos["ciudad"] = datos["ciudad"].str.replace("ú","u")

#cambiar letras mayusculas por minusculas
datos["ciudad"] = datos["ciudad"].str.upper()
#cuentame cuantas ciudades contienen caracteres especiales
    
#quitar espacios al inicio y al final de la ciudad
datos["ciudad"] = datos["ciudad"].str.strip()   

#quitar caracteres especiales de la ciudad
datos["ciudad"] = datos["ciudad"].str.replace("[^A-Z ]","")     

#quitar carater "@"
datos["ciudad"] = datos["ciudad"].str.replace("@","")
# quitar caracteres especiales de la ciudad   

#identifica los caracteres especiales en la ciudad e imprimelos agrupados y cuentalos 
caracteres_especiales = datos["ciudad"].str.extractall("([^A-Z ])")[0].value_counts()
print("Caracteres especiales en la ciudad:",caracteres_especiales)  

#quitar carater especial "*,!,%,#,_,3"
datos["ciudad"] = datos["ciudad"].str.replace("*","")
#datos["ciudad"] = datos["ciudad"].str.replace("!")
#datos["ciudad"] = datos["ciudad"].str.replace("%")
#datos["ciudad"] = datos["ciudad"].str.replace("#")
#datos["ciudad"] = datos["ciudad"].str.replace("_")
#datos["ciudad"] = datos["ciudad"].str.replace("3")

#agrupar por ciudad y cuenta cuantas ciudades hay de cada tipo
ciudades_agrupadas = datos["ciudad"].value_counts()
print("Ciudades agrupadas:",ciudades_agrupadas)

condicion = datos["ciudad"].str.contains("[^A-Z ]")
print("Ciudades con caracteres especiales:",datos[condicion].shape[0])  

print(datos.head)  