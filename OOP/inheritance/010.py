class Forma:

    def __init__(self, lado):
        self.lado = lado

class Quadrado(Forma):

    def area(self):
        print(self.lado * self.lado)


calcular = Quadrado(4)
calcular.area()