class Conta:
    def __init__(self, titular, saldo, dinheiro):
        self.titular = titular
        self.saldo = saldo
        self.dinheiro = dinheiro

    def operacao(self):
        print(f"1. Depositar\n2. Saque\n3. Saldo")
        n = int(input("Escolha qual operação bancária você quer realizar: "))
        if n == 1:
            self.depositar()
        elif n == 2:
            self.sacar()
        elif n == 3:
            self.mostrar_saldo()

    def depositar(self):
        valor = int(input("Digite o valor do deposito: "))
        self.saldo += valor
        self.dinheiro -= valor
        if self.dinheiro >= valor:
            print(f"{valor}R$ foram depositados na conta de {self.titular}")
        else:
            print(f"O Deposito não foi realizado com sucesso por dinheiro insuficiente")

    def sacar(self):
        valor = int(input("Digite o valor do sacado: "))
        self.dinheiro += valor
        if self.saldo >= valor:
            print(f"{valor}R$ foi sacado com sucesso.")
            self.saldo -= valor
        else:
            print("O saque não foi realizado com sucesso.")

    def mostrar_saldo(self):
        print(f"Saldo Atual: {self.saldo}R$\nDinheiro em espécie: {self.dinheiro} ")





thiago = Conta("Thiago", 1500, 100)
thiago.operacao()