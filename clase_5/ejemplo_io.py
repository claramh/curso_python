import io

#fichero = open("quijote.txt", "r") # "r" de read

#for linea in fichero:
#    print(linea)
#fichero.close

## leer los primeros 500 caracteres

with open("quijote.txt", "r") as file:
    contenido = file.read(500)
    print("Primeros 500 caracteres")
    print(contenido)

with open("quijote.txt", "r") as file:
    contenido = file.readline()
    print("")
    print("Primera línea")
    print(contenido)

with open("quijote.txt", "r") as file:
    contenido = file.readlines(2000)
    print("")
    print("Primeras líneas")
    print(contenido)
    for c in contenido:
        print(c.strip()) # ni idea de para qué
