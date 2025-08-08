class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def descricao_aluno(self):
        return f"Olá {self.nome}, você tem {self.idade} anos!"

class Aluno(Pessoa):

    @staticmethod
    def matricula():
        return "Sua matrícula: 202523021"


alunot = Aluno("Renato", 10)
print(alunot.descricao_aluno(),alunot.matricula())