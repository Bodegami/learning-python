from abc import ABCMeta, abstractmethod

# Utilizamos o metaclass=ABCMETA para definir a classe como uma classe abstrata

class Conta(metaclass=ABCMeta):
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return f'[>>Codigo {self._codigo} - Saldo {self._saldo}<<]'

# Utilizamos o @abstractmethod para indicar que é um metodo abstrato e que as classes filhas devem implementa-lo
    @abstractmethod
    def passa_o_mes(self):
        pass


class ContaCorrente(Conta):

    def passa_o_mes(self):
        self._saldo -= 2


class ContaPoupanca(Conta):

    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3


class ContaInvestimento(Conta):
    # TODO - implementar o metodo abstrato da classe mae
    pass


conta16 = ContaCorrente(16)
conta16.deposita(1000)
# conta16.passa_o_mes()
print(conta16)

conta17 = ContaPoupanca(17)
conta17.deposita(1000)
# conta17.passa_o_mes()
print(conta17)


contas = [conta16, conta17]
for conta in contas:
    conta.passa_o_mes() # duck typing
    print(conta)


conta764 = ContaInvestimento(764)