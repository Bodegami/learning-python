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



conta = cria_conta(123, "Nico", 55.0, 1000.0)
print(conta)

saca(conta, 20.0)
print(conta)

deposita(conta, 15.0)
extrato(conta)