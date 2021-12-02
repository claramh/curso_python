import sys


print("Nombre del script:", (sys.argv[0]))
print("Argumentos del script:", (sys.argv[1:])) ## al ejecutar en terminarl, se hace python <nombre_script> arg1 arg2...
print("Cantidad de argumentos:", len(sys.argv), "argumentos")
print("Lista de argumentos:", str(sys.argv))