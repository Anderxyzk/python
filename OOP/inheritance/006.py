class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def descricao(self):
        print(f"Olá! {self.nome}, você tem {self.idade}\n")

class Professor(Pessoa):

    def disciplina(self):
        print("Disciplina: Banco de Dados")


materia = Professor("Renato", 32)
print(materia.descricao(), materia.disciplina())