# Enlista todos los ficheros de un dirctorio.
# Después del archivo en la línea de comandos hay que poner 
# el argumento del directorio que queremos que liste

import argparse
import os
import sys


mi_parser = argparse.ArgumentParser(prog="ejemplo_argparse.py", 
                                    description="Listado del contenido del directorio",
                                    epilog="Muchas gracias")

mi_parser.add_argument("Path",
                        metavar="Ruta",
                        type=str,
                        help="La ruta al directorio")

args = mi_parser.parse_args()
dir_ruta = args.Path

if not os.path.isdir(dir_ruta):
    print("Este directorio no existe")
    sys.exit()

print("\n".join(os.listdir(dir_ruta)))