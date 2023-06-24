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

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    def transfere(self, valor, destino):
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
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}