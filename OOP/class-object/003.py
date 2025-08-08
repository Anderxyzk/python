#CLASSE
class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    #METODO 1
    def calcarea(self):
        return self.largura * self.altura
    #METODO 2
    def calcperimetro(self):
        return 2 * (self.largura + self.altura)

#CRIAR A INSTANCIA
area = Retangulo(5, 3)
perimetro = Retangulo(8, 5)

#CHAMA O METODO
print(area.calcarea())
print(perimetro.calcperimetro())
