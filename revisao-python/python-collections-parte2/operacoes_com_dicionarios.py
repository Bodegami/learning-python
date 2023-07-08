
aparicoes = {
    "Guilherme": 1,
    "cachorro": 2,
    "nome": 2,
    "vindo": 1
}

# Adiciona um elemento com a chave Carlos e valor 1
aparicoes["Carlos"] = 1

print(aparicoes)

# altera o valor de um elemento a partir da chave. Note que isso nos indica que os dicionarios são mutaveis
aparicoes["Carlos"] = 2

print(aparicoes)

# remove um elemento a partir da chave
del aparicoes["Carlos"]

print(aparicoes)

# verifica se existe um elemento com o mesmo nome no dicionario
isPresent = "cachorro" in aparicoes

print(isPresent)

# podemos iterar sobre o dicionario
for elemento in aparicoes:
    print(elemento)

# iterando sobre as chaves
for elemento in aparicoes.keys():
    print(elemento)

# iterando sobre os valores
for elemento in aparicoes.values():
    print(elemento)

# iterando sobre a chave e o valor
for elemento in aparicoes.items():
    print(elemento)

# utilizando o .items, é possivel descompactar cada linha do dicionario e quebrar em chave e valor
for key, value in aparicoes.items():
    print(f'Key: {key} | Value: {value}')

# Podemos utilizar o list comprehension com dicionarios
lista_customizada = ["palavra {}".format(chave) for chave in aparicoes.keys()]
print(lista_customizada)