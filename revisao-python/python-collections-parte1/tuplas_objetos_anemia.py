
class ContaCorrente:

    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return f"[>>codigo {self.codigo} Saldo {self.saldo}<<]"


conta_gui = ContaCorrente(15)
conta_gui.deposita(500)
conta_dani = ContaCorrente(47685)
conta_dani.deposita(1000)


def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)


contas = [conta_gui, conta_dani]
[print(conta) for conta in contas]
deposita_para_todas(contas)
[print(conta) for conta in contas]


contas.insert(0, 76)
print(contas)

# deposita_para_todas(contas) -> lista são mutaveis, por isso ela aceitou um int, mas quebrou na logica do deposita()

# TUPLAS
# Tuplas são imutaveis

guilherme = ('Guilherme', 37, 1981)
daniela = ('Daniela', 31, 1987)

# guilherme[0] += 'Novo' -> Quebra pois a tupla é imutavel
print(guilherme)
