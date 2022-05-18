# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from teste import cria_conta, deposita, saca, extrato

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


from conta import Conta

## exemplo de dicionario
teste = {"numero": 123, "titular": "Nico", "saldo": 55.0, "limite": 1000.0}

conta1 = cria_conta(123, "Nico", 55.0, 1000.0)
print(conta1)

saca(conta1, 20.0)
print(conta1)

deposita(conta1, 15.0)
extrato(conta1)

#print(Conta())
conta2 = Conta(123, "Marco", 55.5, 1000.0)
print(conta2)

conta2.extrato()

conta2.deposita(100)
conta2.extrato()

conta2.saca(50)
conta2.extrato()

conta3 = Conta(123,"Pedro", 78.9, 1000.0)
conta3.extrato()
print(type(conta3))

## O None no Python é o equivalente ao Null em Java
conta3 = None
print(type(conta3))

conta4 = Conta(123,"Pedro", 78.9, 1000.0)