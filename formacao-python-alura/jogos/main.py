# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


print("Bem vindo no jogo de Adivinhação")

jogo = "Adivinhação"

print("Do que é esse jogo?", jogo)
print("Bem", "vindo", "no", "jogo", "de", jogo, sep="-")

print("Tentativa {1} de {1}".format(3,10))
print("R$ {:f}".format(1.59))
print("R$ {:.2f}".format(1.59))
print("R$ {:.2f}".format(1234.5))
print("R$ {:7.2f}".format(1234.5))
print("R$ {:7.2f}".format(4.5))
print("R$ {:07.2f}".format(4.5))
print("R$ {:07d}".format(46))
print("Data {:02d}/{:02d}".format(9,11))


## List == estruturas de dados mutaveis
inteiros = [1,2,4,6,7]
print(inteiros)

inteiros.append(9)
print(inteiros)

inteiros.pop()
print(inteiros)

print(inteiros.__getitem__(2))

print(inteiros[2])

print(inteiros.__contains__(3))


## Tuple == estruturas de dados imutaveis

palavras = ("banana", "maca", "uva")
print(palavras)

print(palavras.__getitem__(2))

print(palavras.__contains__("maca"))

map1 = ("Nico", 39)
map2 = ("Flavio", 37)

listMap = [map1, map2]
print("List map:", listMap)

tupleMap = tuple(listMap)
print("Tuple map:", tupleMap)

outraLista = list(tupleMap)
print("Tupla convertida em lista:", outraLista)


## Set == estrutura de dados não ordenada e que não aceita elementos duplicados

colecao = {11122233344, 22233344455, 33344455566}
print(colecao)

colecao.add(55562562525)
print(colecao)

colecao.add(55562562525)
print(colecao)








