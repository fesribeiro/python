class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo um objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    
    def extrato(self):
        print("Seu saldo é de {} no nome do titular {}".format(self.__saldo, self.__titular))

    def saca(self, valor):
        self.__saldo -= valor

    def depositar(self, valor):
        self.__saldo += valor

    def transfere(self, valor, origem, destino):
        origem.saca(valor)
        destino.depositar(valor)


