# !/usr/bin/python3
# hola.py
# Imprime un nombre

nombre = "Clara"
print("Hola", nombre)

# abrir consola python y py_compile.compile("hola.py") para compilar y hacer una ejecución más rápida
# pyinstaller <archivo> para convertir el py en un exe

lista = [1, 2.5, 'DevCode', [5,6] ,4]
print(lista[0]) # 1
tupla = ("Python", True, "Zope", 5) ## igual que la lista, pero inmutable
print(tupla[1]) # True
diccionario = {'nombre' : 'Carlos', 'edad' : 22, 'cursos': ['Python','Django','JavaScript']}
print(diccionario['nombre']) # Carlos
print(diccionario['cursos'][2]) # JavaScript

## iterar en una lista
coordenadas_madrid = [9870.97, 65268479]
for coordenada in coordenadas_madrid:
    print(f"Coordenada:", coordenada)
coord1 = coordenadas_madrid[0]
coord2 = coordenadas_madrid[1]
print("Coordenada 1:", coord1)
print("Coordenada 2:", coord2)

## para iterar sobre un diccionario de frutas
frutas = {"manzana":"roja", "caqui":"naranja", "pera":"verde"}
llave = frutas.keys()
print(llave)
valor = frutas.values()
print(valor)
diccionario_frutas = frutas.items()
print(diccionario_frutas)
for llave, valor in diccionario_frutas:
    print (llave,"--->",valor)