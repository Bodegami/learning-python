from operator import attrgetter

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


idades = [15, 87, 32, 65, 56, 32, 49, 37]

print(15 < 32)

nomes = ['Guilherme', 'Daniela', 'Paulo']
print(nomes)
nomes = ['guilherme', 'Daniela', 'Paulo']
print(nomes)

conta_gui = ContaSalario(17)
conta_gui.deposita(500)

conta_dani = ContaSalario(3)
conta_dani.deposita(1000)

conta_paulo = ContaSalario(13)
conta_paulo.deposita(510)

contas = [conta_gui, conta_dani, conta_paulo]

for conta in contas:
    print(conta)

# objetos de Classes proprias, não podem ser ordenadas por padrao.
#print(sorted(conta))


# criamos uma função para que seja possivel a ordenacao de objetos proprios com o sorted. Mas é uma má pratica acessar
# um atributo protegido como o metodo abaixo.
def extrai_saldo(conta):
    return conta._saldo


# Mas podemos ordenar passando uma KEY que será usado cpara comparacao e por fim gerar a ordenacao
for conta in sorted(contas, key=extrai_saldo):
    print(f'ExtraiSaldo(): {conta}')

# Ordenando objetos proprios com o attrgetter. Ainda assim não é das melhores praticas

for conta in sorted(contas, key=attrgetter('_saldo')):
    print(f'AttrGetter: {conta}')


