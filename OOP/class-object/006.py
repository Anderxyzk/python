class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def calcularmedia(self):
        media = (self.nota1 + self.nota2) / 2
        print("Média: ", media)
        return media

nota = Aluno("Anderson", 5, 6)

nota.calcularmedia()
