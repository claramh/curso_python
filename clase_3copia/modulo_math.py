# para importar todos los métodos del módulo
import math

raiz_cuadrada = math.sqrt(10)
logaritmo_base10 = 20 * math.log10(2)

print(raiz_cuadrada)
print(logaritmo_base10)

# para importar la parte que nos interesa del módulo, no todos los métodos
from math import sqrt, log10

raiz_cuadrada = sqrt(10)
logaritmo_base10 = 20 * log10(2)

print(raiz_cuadrada)
print(logaritmo_base10)