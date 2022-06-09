from operator import attrgetter
from functools import total_ordering


class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __lt__(self, other):
        return self._saldo < other._saldo

    def __str__(self):
        return f"[>>Codigo {self._codigo} - Saldo {self._saldo}<<]"

    def __eq__(self, other):
        if type(other) != ContaSalario:
            return False

        return self._codigo == other._codigo and self._saldo == other._saldo


print("\n==============|| Ordenacao natural de nossas classes ||===============\n")

conta_do_guilherme = ContaSalario(1700)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(500)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(500)

print("\n==============|| Definindo um segundo parametro de desempate ||===============\n")

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]

# Repare que dentro do attrgetter podemos passar um segundo parametro que será usado
# como um segundo comparador para casos de empate do primeiro comparador
for conta in sorted(contas, key=attrgetter('_saldo', '_codigo')):
    print(conta)


print("\n==============|| Definindo um segundo parametro de desempate - Orientado a Objetos ||===============\n")


class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __lt__(self, other):
        if self._saldo != other._saldo:
            return self._saldo < other._saldo

        return self._codigo < other._codigo

    def __str__(self):
        return f"[>>Codigo {self._codigo} - Saldo {self._saldo}<<]"

    def __eq__(self, other):
        if type(other) != ContaSalario:
            return False

        return self._codigo == other._codigo and self._saldo == other._saldo


print("\n==============|| Comparando os valores - Orientado a Objetos ||===============\n")

conta_do_guilherme = ContaSalario(1700)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(500)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(500)

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]

for conta in sorted(contas):
    print(conta)


print("\n==============|| Retorna error caso tente comparar usando <= ou >= ||===============\n")

try:
    print(conta_do_guilherme <= conta_da_daniela)
except TypeError as te:
    print(f'Error: {te}')


print("\n==============|| Implementando o comparador ||===============\n")

# Para corrigir o problema dos operadores de comparacao, podemos implementar um a um
# (lt, le, gt, ge, eq e etc) na classe principal
# Outra abordagem é usar o 'total_ordering' da lib 'functools'. O total_ordering
# precisa apenas que na classe principal tenha a implemtancao para o metodo __lt__() e o __eq__().
# Além disso, anotamos a classe com o decorator @total_ordering.
# Dessa forma nossa classe está pronta para todos os tipos de comparação


@total_ordering
class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __lt__(self, other):
        if self._saldo != other._saldo:
            return self._saldo < other._saldo

        return self._codigo < other._codigo

    def __str__(self):
        return f"[>>Codigo {self._codigo} - Saldo {self._saldo}<<]"

    def __eq__(self, other):
        if type(other) != ContaSalario:
            return False

        return self._codigo == other._codigo and self._saldo == other._saldo


conta_do_guilherme = ContaSalario(1700)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(500)

conta_do_paulo = ContaSalario(1700)
conta_do_paulo.deposita(500)

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]
print("conta_do_guilherme <= conta_da_daniela :", conta_do_guilherme <= conta_da_daniela)
print("conta_do_guilherme == conta_do_paulo :", conta_do_guilherme == conta_do_paulo)
print("conta_do_paulo >= conta_do_guilherme :", conta_do_paulo > conta_do_guilherme)