# glob: expansión del patrón de nombres de ruta de estilo unix, encuentra todos los nombres de ruta que coincidan con ese patrón
# ERROR CON EL MÓDULO GLOB

import glob

carpeta = glob("../clase_4/*")

for fichero in carpeta: # todos los ficheros de clase_4
    print(fichero)