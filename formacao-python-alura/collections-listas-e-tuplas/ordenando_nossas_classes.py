from operator import attrgetter


class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return f"[>>Codigo {self._codigo} - Saldo {self._saldo}<<]"

    def __eq__(self, other):
        if type(other) != ContaSalario:
            return False

        return self._codigo == other._codigo and self._saldo == other._saldo


print("\n======================|| Ordem natural ||=======================\n")

nomes = ['Guilherme', 'Daniela', 'Paulo']
print(sorted(nomes))

print("\n===============|| Tentando ordenar objetos de nossas classes usando a ordenacao natural ||=================\n")

conta_do_guilherme = ContaSalario(17)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(1000)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(510)

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]
for conta in contas:
    print(conta)

# Retorna erro caso tente ordenar objetos de nossas classes, pois o python tenta usar a ordenacao natural (> ou <)
try:
    print(sorted(contas))
except TypeError as te:
    print(f"Error: {te}")

print("\n===============|| Ordenando nossos objetos usando um atributo como key ||=================\n")


def extrai_saldo(conta):
    return conta._saldo


# O sorted pode receber como um segundo argumento uma funcao que retorna o valor que vamos utilizar para comparar,
# aqui no caso criamos uma funcao extrai_saldo que retorna o saldo.
# Dessa forma o sorted vai chamar essa funcao para cada conta na lista, comparar e ordenar
for conta in sorted(contas, key=extrai_saldo):
    print(conta)

print("\n===============|| Ordenando nossos objetos usando o attrgetter como key ||=================\n")


def extrai_saldo(conta):
    return conta._saldo


# O attrgetter é uma alternativa para usar como key. Dentro da key, chamamos o attrgetter e passamos
# o atributo que será usado para comparação
for conta in sorted(contas, key=attrgetter('_codigo')):
    print(conta)