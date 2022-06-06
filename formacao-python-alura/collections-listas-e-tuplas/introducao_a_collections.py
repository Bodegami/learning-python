idade1 = 39
idade2 = 30
idade3 = 27
idade4 = 18

print(idade1)
print(idade2)
print(idade3)
print(idade4)

## sobre uma lista com diversos valores do mesmo tipo
# Lista é uma sequência de acesso aleatorio (acessamos pela posicao)

idades =[39, 30, 27, 18]
print(type(idades))

# verificando o tamanho de uma lista
print(len(idades))

# acessando um elemento da lista pela posicao
print(idades[2])

# imprimindo os elementos da lista
print(idades)

# adiciona um elemento no final da lista
idades.append(15)
print(idades)

# retorna error caso tente acessar um elemento fora do range da lista
try:
    print(idades[6])
except IndexError as e:
    print("Error:", e)

# aplicando o for numa lista
for idade in idades:
    print(idade)

# removendo um elemento da lista
idades.remove(30)
print(idades)

# retorna error ao tentar remover um elemento que nao esta na lista
try:
    idades.remove(30)
except ValueError as ve:
    print("Error:", ve)

## em caso de duplicidade, remove o primeiro elemento que aparecer
idades.append(27)
print(idades)
idades.remove(27)
print(idades)

# adiciona um elemento na lista na posicão informada (primeiro params index, segundo value)
idades.insert(0, 42)
print(idades)

# remove todos os elementos da lista
idades.clear()
print(idades)