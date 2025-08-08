class Person:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"{self.nome}\n{self.idade}"

p1 = Person("John", 36)
print(p1)