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

