class Veiculo:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def estilo(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"

class Carro(Veiculo):

    def portas(self):
        return "4 portas."


carro = Carro("Ford", "Fiesta")
print(f"{carro.estilo()}\n{carro.portas()}")