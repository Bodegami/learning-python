
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


conta1 = ContaSalario(37)
conta2 = ContaSalario(37)
print(conta1, conta2)

print(conta1 == conta2)


class ContaMultiploSalario(ContaSalario):
    pass