# Crear un programa que le pregunte al usuario su nombre y edad y le muestre el año en que cumplirá los 100 años

print("¿Cómo te llamas?")
nombre = input("")
print("¿Cuántos años tienes?")
edad = input("")
edad = int(edad)
cien_anyos = (2021 - edad) + 100
print("")
print(f"{nombre}, en {cien_anyos} tendrás 100 años")