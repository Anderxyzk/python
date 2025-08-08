class Relogio:
    def __init__(self, hora, minuto, segundo):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo

    def horario(self):
        print(f"Agora são {self.hora}:{self.minuto}:{self.segundo}")

h = Relogio(12, 10, 55)
h.horario()