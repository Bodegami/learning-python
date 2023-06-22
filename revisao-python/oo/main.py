
from teste import cria_conta, deposita, saca, extrato

conta = cria_conta(123, "Renato", 55.0, 1000.0)
print(conta)
print(conta["saldo"])

deposita(conta, 15.0)
extrato(conta)

saca(conta, 20.0)
extrato(conta)


conta2 = cria_conta(321, 200.0)
deposita(conta2, 200.0)
extrato(conta2)


conta3 = cria_conta(titular="Nico", limite=1000.0)
deposita(conta3, 100.0)


if __name__ == '__main__':
    print()

