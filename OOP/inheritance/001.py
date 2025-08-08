class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        return "O animal faz um som"


class Cachorro(Animal):
    def falar(self):
        return "Au au!"

dog = Cachorro("Rex")

print(f"{dog.nome} diz: {dog.falar()}")
