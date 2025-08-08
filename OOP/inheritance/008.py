class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario


    def descricao(self):
        print(f"Olá! {self.nome}\nSeu salário atual: R${self.salario:.2f}")


class Vendedor(Funcionario):

    def comissao(self):
        print(f"Você ganhará 2% de comissão por venda: R${self.salario * 0.02}")




desc_fun = Vendedor("Renato", 2300)
desc_fun.descricao()
desc_fun.comissao()