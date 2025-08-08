class Triangulo:
    def __init__(self, l1, l2, l3):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3

    def verify(self):
        if self.l1 + self.l2 > self.l3 and self.l1 + self.l3 > self.l2 and self.l2 + self.l3 > self.l1:
            print("Triângulo válido!")
        else:
            print("Triângulo inválido!")

verificar = Triangulo(2, 2, 5)
verificar.verify()