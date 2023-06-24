import conta


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

    def __valida_valor(self, valor):
        return valor > 0

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def transfere(self, valor, destino):
        if (not self.__valida_valor(valor)):
            raise ArithmeticError("Insira um valor válido!")

        self.saca(valor)
        destino.deposita(valor)

    # getter com implementacao tipo Java
    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    # getter com implementacao python
    @property
    def limite(self):
        return self.__limite

    # setter com implementacao python
    @limite.setter
    def limite(self, limite):
        if (not self.__valida_valor(limite)):
            raise ArithmeticError("Insira um valor válido!")

        self.__limite = limite