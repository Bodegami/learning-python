
class Conta:

    # __init__ é a funcao construtor.
    # self é a referencia que sabe encontrar o objeto que esta sendo construido em memoria
    # atraves do self, definimos os atributos da classe.
    # a sintaxe __numero, __saldo e etc, representa o mesmo que o private da linguagem Java

    def __init__(self, numero=123, titular="Renato", saldo=55.0, limite=1000.0):
        print("\nconstruindo objeto.. {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor
