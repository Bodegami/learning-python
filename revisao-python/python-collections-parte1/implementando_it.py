
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
        return self._saldo < other._saldo


conta_gui = ContaSalario(17)
conta_gui.deposita(500)

conta_dani = ContaSalario(3)
conta_dani.deposita(1000)

conta_paulo = ContaSalario(13)
conta_paulo.deposita(510)

contas = [conta_gui, conta_dani, conta_paulo]

print(conta_gui < conta_dani)

for conta in sorted(contas, reverse=True):
    print(conta)

    


