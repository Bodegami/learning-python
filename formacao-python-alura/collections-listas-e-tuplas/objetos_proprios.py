class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return f'[>>Codigo {self.codigo} - Saldo {self.saldo}<<]'


conta_do_gui = ContaCorrente(15)
print(conta_do_gui)

conta_do_gui.deposita(500)
print(conta_do_gui)

conta_da_dani = ContaCorrente(47685)
conta_da_dani.deposita(1000)
print(conta_da_dani)

contas = [conta_do_gui, conta_da_dani]
print(contas)

for conta in contas:
    print(conta)

contas.append(conta_do_gui)
print(contas[0])

conta_do_gui.deposita(100)

# É importante notar que quando criamos uma lista com conta_do_gui e conta_da_dani,
# estamos passando a referência daquele objeto e não criando um novo na lista.
# Tome cuidado ao trabalhar com objetos com mais de uma referência, como no caso de
# contas_do_gui e contas[0]. Caso ocorra alguma alteração em uma das referências,
# isso impactara no resultado esperado em todas as referências daquele objeto.

print("Contas do gui primeira e segunda referência!!!")
print(conta_do_gui)
print(contas[0])

print("Contas do gui alterando apenas a segunda referência!!!")
contas[0].deposita(200)
print(conta_do_gui)
print(contas[0])

print("END!")

print("==================Tuplas====================")


# A tupla é imutavel


def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)


contas = [conta_do_gui, conta_da_dani]
print(contas[0], contas[1])
deposita_para_todas(contas)
print(contas[0], contas[1])

contas.insert(0, 76)
print(contas[0], contas[1], contas[2])

try:
    deposita_para_todas(contas)
    print(contas[0], contas[1], contas[2])
except AttributeError as ae:
    print("Error:", ae)

# tupla - ela pode ter um numero indefinido de valores e variados tipos
guilherme = ('Guilherme', 37, 1981)
daniela = ('Daniela', 31, 1987)

# Ela nao tem o .append()
try:
    guilherme.append(6754)
except AttributeError as ae:
    print("Error:", ae)

# Representando a classe ContaCorrente como uma tupla
conta_do_gui = (15, 1000)
# conta_do_gui.deposita() ## variação OO

print(conta_do_gui[1])
try:
    conta_do_gui[1] += 100
    print(conta_do_gui[1])
except TypeError as te:
    print("Error:", te)


def deposita(conta):  # variação "funcional" (separando o comportamento dos dados)
    novo_saldo = conta[1] + 100
    codigo = conta[0]
    return (codigo, novo_saldo)


conta_do_gui_atualizada = deposita(conta_do_gui)

print(conta_do_gui)
print(conta_do_gui_atualizada)
