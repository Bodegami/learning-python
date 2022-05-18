

class Conta:

    ## __init__ == construtor
    ## self == this
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de R$ {} do titular {}.".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    ## Uma classe deve ser coesa, ela deve seguir o principio de responsabilidade unica,
    ## logo, o metodo abaixo nao deveria fazer parte desta classe, pois o cliente pode ser inadimplente,
    ## mas a classe nao.
    ##def en_inadimplente(self, cliente):

