
from teste import cria_conta, deposita, saca, extrato
from conta import Conta
from cliente import Cliente

print("*************PARADIGMA PROCEDURAL*****************\n")
conta = cria_conta(123, "Renato", 55.0, 1000.0)
print(conta)
print(conta["saldo"])

deposita(conta, 15.0)
extrato(conta)

saca(conta, 20.0)
extrato(conta)

# Como no paradigma procedural nao obriga um contrato, é fácil inserir um código como o abaixo

# conta2 = cria_conta(321, 200.0)
# deposita(conta2, 200.0)
# extrato(conta2)

# conta3 = cria_conta(titular="Nico", limite=1000.0)
# deposita(conta3, 100.0)


print("\n*************PARADIGMA ORIENTADO A OBJETO*****************\n")

# guarda a referencia do objeto em memoria
# construindo objeto com valores default
conta = Conta()
print(conta)

# passando os valores no construtor
conta2 = Conta(321, "Bode", 200.0, 2000.0)
print(conta)


print("\n*************ACESSANDO ATRIBUTOS*****************\n")

# print(conta.titular)
# print(conta.limite)
# print(conta.saldo)
# print(conta.numero)


print("\n*************ACESSANDO METODOS DA CLASSE*****************\n")

conta.extrato()
conta2.extrato()

conta.deposita(15.0)
conta.extrato()

conta2.deposita(10.0)
conta2.extrato()

conta.saca(15.0)
conta.extrato()

conta2.saca(10.0)
conta2.extrato()


print("\n*************ENCAPSULANDO ATRIBUTOS*****************\n")

# Quebra o código, pois fizemos o encapsulamento dos atributos
# print(conta.titular)
# print(conta.limite)
# print(conta.saldo)
# print(conta.numero)

# Permite o acesso direto ao atributo, porem a sintaxe "_Conta__saldo" é um aviso do python que essa forma
# de acesso é considera uma má prática.
print(conta._Conta__saldo)


print("\n*************ENCAPSULANDO METODOS*****************\n")


conta.extrato()
conta2.extrato()

# conta.transfere(-10.0, conta2)
conta.transfere(10.0, conta2)

conta.extrato()
conta2.extrato()


print("\n*************GETTERS AND SETTERS*****************\n")

print(conta.get_saldo())
print(conta2.limite)
print(conta2.get_titular())

conta2.limite = 10000.0

print(conta2.limite)


print("\n*************OUTRA SOLUCAO PARA GETTERS E SETTERS*****************\n")

cliente = Cliente("marco")

print(cliente.nome)

cliente.nome = "paulo"

print(cliente.nome)


print("\n*************METODOS PRIVADOS*****************\n")

conta.extrato()
conta.saca(1200.0)

conta.extrato()
conta.saca(100.0)
conta.extrato()


print("\n*************METODOS DE CLASSE/METODOS ESTATICOS*****************\n")
# Metodos estaticos podem ser chamados pela classe 'Conta' ou pelo objeto 'conta'

print(conta.codigo_banco())
print(Conta.codigo_banco())

print(conta.codigos_bancos())
print(Conta.codigos_bancos())


print("\n*************FIM!*****************\n")


if __name__ == '__main__':
    pass