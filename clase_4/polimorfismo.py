# ejemplo_coche

class Coche:
    def __init__(self, marca, modelo, tipo):
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo
        self.capacidad_gasolina = 15
        self.nivel_gasolina = 0

    def gasolina_completo(self):
        self.nivel_gasolina = self.capacidad_gasolina
        print("El depósito de gasolina está lleno")

    def conducir(self):
        print(f"El {self.modelo} está siendo conducido")

class CocheElectrico(Coche): ##una clase que se refiere a otra
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo, tipo) # este super está retomando la def init de arriba
        self.tamano_bateria = 100
        self.cambio_nivel = 0
    def cargar(self):
        self.nivel_carga = 100
        print("El coche está cargado")
    def gasolina_completo(self):
        print("El coche no tiene depósito de gasolina porque es eléctrico")

# ya creamos las instancias
objeto_coche = Coche('SEAT', "Ateca", "1.0")

print(objeto_coche.marca)
objeto_coche.gasolina_completo()
objeto_coche.conducir()

coche_electrico = CocheElectrico("Tesla", "Modelo3", "Berlina")

print(coche_electrico.modelo)
coche_electrico.cargar()

print(CocheElectrico.__mro__) ## (<class '__main__.CocheElectrico'>, <class '__main__.Coche'>, <class 'object'>) ---> la clase CocheElectrico viene de la clase Coche, que viene de la metaclase de python objeto, ya predeterminada y que engloba todos los objetos