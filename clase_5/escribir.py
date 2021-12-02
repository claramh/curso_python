import io


entrada = "En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivia un"
entrada2 = " añadir"

#with open("quijote_ext01.txt", "x") as file: # con x si el archivo existe lo sobrescribe, si existe
                                    # crea un archivo con el nombre que decidamos
    #file.write(entrada)

#with open("quijote_ext01.txt", "a") as file: # a para agregar texto
#    file.write(entrada2)

with open("quijote_ext01.txt", "r") as file: # leer de un caracter a un caracter determinados
    file.seek(12)
    contenido = file.read(42)
    print(contenido)