# Ejemplo iterar sobre items

frutas = ["banana", "manzana", "pera", "naranja"]
for f in frutas:
    print(f, "es una fruta y tiene", len(f), "letras")
print("")

# Ejemplo iterar sobre frecuencia de números
x = input("Dame un número: ")
x = int(x) # hay que convertir el string en integer
y = input("Dame otro: ")
y = int(y)
for i in range (x,y):
    print(i)

print("Ahora te imprimo del 0 al 9:")
for i in range(10):
    print(i)
