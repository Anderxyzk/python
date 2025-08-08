class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def carro(self):
        print(f"Especificações do carro:\nMarca:{self.marca}\nModelo:{self.modelo}\nAno:{self.ano}")

car = Carro("Honda", "Civic", "2016")
car.carro()