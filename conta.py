


class Conta:


    def __init__(self, numero, titular, saldo, limite):
        print("Construindo um objeto...{}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite



conta = Conta(123, "Felipe", 55.0, 1000.0)
conta2 = Conta(123, "Victor", 55.0, 1000.0)