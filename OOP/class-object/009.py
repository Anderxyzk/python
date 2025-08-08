class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        print(f"Olá {self.nome}! seu salário atual é: R${self.salario:.2f}")

    def aumento(self):
        new = self.salario * 0.10
        return new + self.salario

funcionario = Funcionario("Renato", 1200)
print(f"Seu novo salário -> R$ {funcionario.aumento()}")