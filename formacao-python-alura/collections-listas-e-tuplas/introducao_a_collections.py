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

idades = [39, 30, 27, 18]
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

# verifica se um elemento esta na lista e retorna um booleano
idades = [39, 30, 27, 18, 15]
print(15 in idades)

# insere os elementos de uma lista em outra lista
lista = [38, 46, 17]
print(lista)
idades.extend(lista)
print(idades)

# imprimir todos os elementos da lista somando 1 em cada em elemento

# FORMA COMUM

# idades_no_ano_que_vem = []
# for idade in idades:
#     idades_no_ano_que_vem.append(idade + 1)
# print(idades_no_ano_que_vem)

# FORMA PYTHONIC - LIST COMPREHENSION
idades_no_ano_que_vem = [(idade + 1) for idade in idades]
print(idades_no_ano_que_vem)

# criar uma nova lista a partir de uma lista populada aplicando filtro
lista_filtrada = [(idade) for idade in idades if idade > 21]
print(lista_filtrada)

# melhorando a legibilidade - LIST COMPREHENSION
# cenario
lista_pouco_legivel = [idade + 1 for idade in idades if idade > 21]


def proximo_ano(idade):
    return idade + 1


def valida_idade(idade, limite):
    return idade > limite


lista_legivel = [proximo_ano(idade) for idade in idades if valida_idade(idade, 21)]
print(lista_legivel)

# Exemplos de problemas por conta da mutabilidade da lista
# Quando passamos um objeto mutavel como parametro de algum metodo, ocorre o risco desse objeto ser alterado,
#  o que poderia ocasionar um erro. Por isso parte da comunidade defende o usa objetos imutaveis
idades = [16, 21, 29, 56, 43]


def faz_processamento_de_visualizacao(lista):
    print(len(lista))
    lista.append(13)


faz_processamento_de_visualizacao(idades)
print(idades)


# Outro problema é quando definimos um valor padrao
# Quando definimos um valor padrao, esse valor sera cacheado em algum lugar e depedendo da manipulacao
# que ocorrer no metodo, o retorno pode nao ser o esperado
# Veja no exemplo a abaixo que a lista vazia definida como padrao vai sendo incrementada  cada vez que ela é chamada

def faz_processamento_de_visualizacao2(lista=[]):
    print(len(lista))
    lista.append(13)


faz_processamento_de_visualizacao2()
faz_processamento_de_visualizacao2()
faz_processamento_de_visualizacao2()


# Para corrigir o problema do metodo acima, o ideal é indicar que o valor de referencia é None
# e depois fazemos um validacao dentro do metodo para o caso de receber None, instanciar uma nova lista
# Dessa forma contarmos o problema de imutabilidade

def faz_processamento_de_visualizacao3(lista=None):
    if lista is None:
        lista = list()
    print(len(lista))
    lista.append(13)


faz_processamento_de_visualizacao3()
faz_processamento_de_visualizacao3()
faz_processamento_de_visualizacao3()
