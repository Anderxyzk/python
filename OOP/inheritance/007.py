class Conta:

    def __init__(self, dono, saldo):
        self.dono = dono
        self.saldo = saldo


    def descricao(self):
        print(f"Olá! {self.dono}\nSaldo: R${self.saldo:.2f}\n")


class ContaPoupanca(Conta):

    def rendimento(self):
        print(f"Você tem uma conta poupança! O rendimendo é -> R${self.saldo * 0.05}")


bank_acc = ContaPoupanca("Anderson", 2520)

bank_acc.descricao()
bank_acc.rendimento()
