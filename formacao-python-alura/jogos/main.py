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

texto = "Vai cavalo!"
listaDinamica = [letra.upper() for letra in texto]
print(listaDinamica)

inteiros = [5,7,2,4,9]
quadrados = [num*num for num in inteiros]
print(quadrados)

# for numero in inteiros:
#     if numero % 2 == 0:
#         pares.append(numero)

inteiros = [1,3,4,5,7,8,9]
pares = [numero for numero in inteiros if numero % 2 == 0] ## Massa d+ / codigo comentado em uma linha
print(pares)


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


## Leitura e escritura de arquivos

## O Python já nos entrega uma funcao built-in chamada "open()" para I/O
## No primeiro parametro indicamos o nome e a extensao do arquivo,
## No segundo parametro indicamos qual operacao queremos fazer. ex:
## "a" -> append (incrementar um arquivo já existente)
## "r" -> readOnly (apenas leitura)
## "w" -> write (escrita) obs: caso o arquivo já exista, ele vai apagar e criar um novo somente com as novas informacoes
## podemos passar um terceiro parametro que representa o enconding do nosso arquivo

arquivo = open("palavras.txt", "w", encoding='UTF-8')
print(arquivo)
print(type(arquivo))

arquivo.write("banana\n")
arquivo.write("melancia\n")
arquivo.close()

arquivo = open("palavras.txt", "a", encoding='UTF-8')
arquivo.write("morango\n")
arquivo.write("maça\n")
arquivo.close()

arquivo = open("palavras.txt", "r", encoding='UTF-8')
print(arquivo.read())
print(arquivo.read()) ## O metodo read só o arquivo uma vez, para ler novamente é necessario abrir o arquivo de novo
arquivo.close()

arquivo = open("palavras.txt", "r", encoding='UTF-8')
for linha in arquivo:
    print(linha)
arquivo.close()

arquivo = open("palavras.txt", "r", encoding='UTF-8')
linha = arquivo.readline()
print(linha)
print(linha.strip())
arquivo.close()

arquivo = open("palavras.txt", "r", encoding='UTF-8')
linha = arquivo.readline(4)
print(linha)
print(linha.strip())
arquivo.close()




