from operator import attrgetter
from functools import total_ordering


# Implementamos os metodos __eq__() e __lt__() que são requisitos basicos do decorator total_ordering.
# O total_ordering utiliza as duas implementações citadas acima para nos dar outros implementações como
#  __lt__(), __le__(), __gt__(), or __ge__().
@total_ordering
class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return f"[>>codigo {self._codigo} Saldo {self._saldo}<<]"

    def __eq__(self, other):
        # poderiamos usar o isIstance() para verificar se é um tipo filho de ContaSalario
        if type(other) != ContaSalario:
            return False

        return self._codigo == other._codigo and self._saldo == other._saldo

    def __lt__(self, other):
        if self._saldo != other._saldo:
            return self._saldo < other._saldo
        return self._codigo < other._codigo




conta_gui = ContaSalario(1700)
conta_gui.deposita(500)

conta_dani = ContaSalario(3)
conta_dani.deposita(1000)

conta_paulo = ContaSalario(133)
conta_paulo.deposita(500)

contas = [conta_gui, conta_dani, conta_paulo]

# primeiro ordena pelo saldo, depois pelo codigo. O attrGetter permite um ou mais atributos para melhorar a ordenacao
for conta in sorted(contas):
    print(conta)


print(conta_gui < conta_dani)

# só é possivel fazer essa comparação graças ao decorator total_ordering
print(conta_paulo <= conta_gui)






