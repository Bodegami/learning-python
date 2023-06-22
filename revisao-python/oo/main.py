
from teste import cria_conta, deposita, saca, extrato
from conta import Conta

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
conta = Conta(321, "Bode", 200.0, 2000.0)
print(conta)



if __name__ == '__main__':
    pass