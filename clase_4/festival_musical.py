# camelcase: letraMayusculaConCadaPalabra

import datetime
from types import DynamicClassAttribute

class FestivalMusical:
    def __init__(self, nombre, pais, estilo_musical): ## función para inicializar la clase, self para que existen otros objetos y variables en otras clases
        self.nombre = nombre
        self.pais = pais
        self.estilo_musical = estilo_musical
    def festival_metodo(self): # el método se va autollamar, si no tenemos self nos dirá que nos sobra un argumento
        print("El mejor festival es")

    @classmethod
    def valor_ticket(cls, valor): # cls es la clase, en lugar de self toma a su propia clase como primer elemento
        cls.valor_ticket = valor

    @staticmethod
    def dia_evento(dia):
        if dia.weekday() == 5 or dia.weekday() == 6:
            return print("Es un fin de semana")
        return print("Es un día laborable")

## se crea el objeto o la instancia
festival1 = FestivalMusical("Festivalll", "España", "folk")
valor = FestivalMusical.valor_ticket(100) # se crea el valor del ticket

dia1 = datetime.date(2021, 11, 30)

# se accede al objeto
print(festival1.nombre) # Festivalll
print(festival1.pais)

# se accede al método
festival1.festival_metodo()
# se accede a los atributos del objeto
print(festival1.nombre)
# se accede al valor del ticket
print("El precio de la entrada es", festival1.valor_ticket)
# Qué día es hoy
FestivalMusical.dia_evento(dia1)