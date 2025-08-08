import math
class Forma:
    def area(self):
        pass

class Retangulo(Forma):

    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

class Circulo(Forma):

    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return math.pi * self.raio**2


retangulo_area = Retangulo(6, 2)
circulo_area = Circulo(6)

print(f"{retangulo_area.area()}, {circulo_area.area():.1f}")


