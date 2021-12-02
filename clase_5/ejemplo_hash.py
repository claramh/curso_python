import hashlib

nombre = "quijote-ext01.txt"

nombre_codificado = nombre.encode()

nombre_hash = hashlib.sha512(nombre_codificado)

print("Objeto:", nombre_hash)
print("Hexadecimal:", nombre_hash.hexdigest()) # esta firma cambiará si el fichero quijote... ha sido modificado