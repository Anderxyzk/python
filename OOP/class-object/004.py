#CLASSE
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        print("Saldo:", self.saldo)

    #METODOS
    def deposito(self, deposito):
        self.saldo += deposito
        print("Deposito: ", deposito)

    def saque(self, sacar):
        self.saldo -= sacar
        print("Sacou: ", sacar)

    def saldofinal(self):
        print("Saldo atual: ", self.saldo)


#Criar instancia
op1 = ContaBancaria("Anderson", 0)

#CHAMAR
op1.deposito(100)
op1.saque(20)
op1.saldofinal()

