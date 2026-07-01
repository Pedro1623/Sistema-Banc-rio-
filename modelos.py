class Conta_Bancária:
    def __init__(self, titular, numero_conta, idade, endereco, telefone, email, saldo_inicial=0.0):
        self.titular = titular
        self.numero_conta = numero_conta
        self.idade = idade
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.saldo = saldo_inicial
        self.historico = []
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor

            print(f"O seu deposito de {valor:.2f} reais foi concluído com sucesso \n")
            print(f"Saldo Atual: {self.saldo:.2f}")

            self.historico.append(f"Depósito: R${valor:.2f}")

        else:
            print(f"Não foi possível realizar est deposito")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Não é possível realizar o saque")

        elif valor <= 0:
            print("Por favor, digite um valor positivo")
            
        else:
            self.saldo -= valor
            print(f"Saque de {valor:.2f} reais realizado com sucesso")

            self.historico.append(f"Saque: R${valor:.2f}")

    def extrato(self):
        if not self.historico:
            print("Nenhuma movimentação realizada ainda.")
        else:
            for item in self.historico:
                print(item)

        print(f"Saldo Atual: R${self.saldo:.2f}")