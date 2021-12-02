# llama al módulo de la carpeta paquetes

from paquete import modulo1, modulo2

llamar_modulo = modulo1.Clase1("Clase1") # creamos así una instancia/objeto
print(llamar_modulo) # me da la dirección del objeto
print(modulo1.Clase1.mostrar) # me da la dirección de la clase
print(llamar_modulo.mostrar())

llamar_modulo2 = modulo2.Clase2("Clase2") # creamos así una instancia/objeto
print(llamar_modulo2) # me da la dirección del objeto
print(modulo2.Clase2.mostrar) # me da la dirección de la clase
print(llamar_modulo2.mostrar())