# fnmatch: coincidencia de nombres de archivos por patrón
# también me da error de módulop

import fnmatch
import os

patron = "clase_5/*"
print("Patrón: ", patron)

ficheros = os.listdir("./") # llamamos al sistema operativo para obtener una lista de directorios

for nombre in ficheros:
    print("Nombre: %-25s %s" % (nombre, fnmatch.fnmatch(nombre, patron)))