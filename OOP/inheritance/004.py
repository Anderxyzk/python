class Funcionario:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def descricao(self):
        return f"Olá {self.nome}! Você tem {self.idade} anos."

class Gerente(Funcionario):

    def departamento(self):
       return f"Seu departamento é: Gerente"

funcionarios = Gerente("Anderson", 20)

print(funcionarios.descricao(),funcionarios.departamento())
