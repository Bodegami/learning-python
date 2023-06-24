
class Conta:

    # __init__ é o construtor
    # self é a referencia que sabe encontrar o objeto que esta sendo construido em memoria
    # atraves do self, definimos os atributos da classe
    def __init__(self, numero=123, titular="Renato", saldo=55.0, limite=1000.0):
        print("\nconstruindo objeto.. {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.saldo, self.titular))

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor
