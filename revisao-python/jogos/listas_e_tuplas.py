#No python, lista e Strings tem um comum o fato de serem uma sequencia
#String sendo uma sequencia de caracteres e lista uma sequencia de valores

lista = [2, 5, 2, 8, 5]
palavra = "banana"

print(len(lista))
print(len(palavra))

print(lista[2])
print(palavra[2])

serie = range(0, 10, 2) #range(apartir de, ate tal, pulando)
print(serie[4])

#Listas são estruturas de dados mutaveis
dias = ["S", "T", "Q", "Q", "S", "S", "D"]
print("Formato: {} - Values: {}".format(type(dias), dias))

#Tuplas é uma estrutura de dados imutaveis
dias = ("S", "T", "Q", "Q", "S", "S", "D")
print("Formato: {} - Values: {}".format(type(dias), dias))

p1 = (3, 5)
p2 = (4, 6)
p3 = (5, 7)
line = [p1, p2, p3]
print(line)

p1 = ("Nico", 39)
p2 = ("Flavio", 37)
instrutores = [p1, p2]
print(instrutores)
print("Buscando a idade da primeira tupla dentro da lista: {}".format(instrutores[0][1]))


palavras = []
palavras.append("banana")
palavras.append("abacaxi")
nova = tuple(palavras)
print(nova)

outra = list(nova)
print(outra)