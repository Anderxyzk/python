class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome}\nR${self.preco}"

product = Produto("Amaciante", 15)
print(product)
