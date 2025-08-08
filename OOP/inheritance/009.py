class Animal:

    def __init__(self, nome):
        self.nome = nome


    def nome_do_animal(self):
        print(f"O nome desse animal é {self.nome}")

    def falar(self):
        print(f"Ele faz um som!")


class Gato(Animal):

    def falar(self):
        print(f"Miau!")

class Passaro(Animal):

    def falar(self):
        print(f"Piu piu!")




gato = Gato("Calabreso")
passaro = Passaro("La ele")

passaro.nome_do_animal()
passaro.falar()
gato.nome_do_animal()
gato.falar()
