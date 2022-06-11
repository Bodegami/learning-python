print("\n=================|| Quebrando uma string e adicionando a um conjunto ||===================\n")

meu_texto = 'Bem vindo meu nome é Renato eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro'

conjunto_string = set(meu_texto.split())
print(conjunto_string)


print("\n=================|| Criando um dicionario ||===================\n")

dicionario_string = {
    "Renato" : 1,
    "cachorro" : 2,
    "gosto" : 2
}
print(dicionario_string)


print("\n=================|| Criando um dicionario pelo construtor dict()||===================\n")

dict_construtor = dict(Renato = 2, cachorro = 2, gosto = 2, eu = 1, meu = 3)
print(dict_construtor)


print("=================|| Acessando um elemento do dicionario pela chave (key) ||===================")

print(dicionario_string["cachorro"])
print(dicionario_string.get("Renato"))


print("\n================|| Retorna error ao tentar acessar uma chave que nao esta no dicionario ||=================\n")

try:
    print(dicionario_string["Guilherme"])
except KeyError as ke:
    print(f'Error: Key ({ke}) not found..')


# Já ao tentar acessar uma chave que nao existe, mas utilizando o metodo get(), retorna None
print(dicionario_string.get("Guilherme"))

# Podemos ainda escolher um tipo de retorno (int, float, string, bool) caso nao encontre a chave
print(dicionario_string.get("Guilherme", "Not found..."))


print("\n================|| Adicionando um elemento ao dicionario ||==================\n")

print(dicionario_string)

dicionario_string["Carlos"] = 1
print(dicionario_string)


print("\n================|| Substituindo o valor de um elemento no dicionario ||==================\n")

print(dicionario_string)

# Note que o dicionario tem o mesmo comportamento do set() de não permitir a repeticao de chaves no conjunto
dicionario_string["Carlos"] = 3
print(dicionario_string)


print("\n================|| Removendo um elemento do dicionario ||==================\n")

print(dicionario_string)

del dicionario_string["Carlos"]

print(dicionario_string)


print("\n================|| Validando se um elemento esta dentro do dicionario ||==================\n")

print(dicionario_string)

valida = "cachorro" in dicionario_string
print(f'A palavra cachorro está no dicionario: {valida}')


print("\n================|| Iterando sobre um dicionario atraves da chave||==================\n")

print(dicionario_string)

# Podemos explicitar atraves .keys() ou nao, o resultado sera o mesmo
# for key in dicionario_string:
for key in dicionario_string.keys():
    print(key)


print("\n================|| Iterando sobre um dicionario atraves dos valores ||==================\n")

print(dicionario_string)

for value in dicionario_string.values():
    print(value)


print("\n================|| Iterando sobre um dicionario e imprimindo a chave e o valor||==================\n")

print(dicionario_string)

for elemento in dicionario_string:
    print(f'Key: {elemento} - Value: {dicionario_string[elemento]}')


print("\n===========|| Iterando sobre um dicionario e imprimindo a chave e o valor atraves do items() ||===========\n")

print(dicionario_string)

for elemento in dicionario_string.items():
    print(elemento)


print("\n===========|| Iterando sobre um dicionario e desempacotando ||===========\n")

print(dicionario_string)

# Note que só é possivel realizar o desempacotamento pq estamos iterando sobre o dicionario com o metodo items(),
# que devolve uma lista de tuplas
for key, value in dicionario_string.items():
    print(f'{key} = {value}')


print("\n===========|| Utilizando o list comprehensions nos dicionarios ||===========\n")

lista_transformada = ["palavra {}".format(chave) for chave in dicionario_string.keys()]
print(type(lista_transformada))
print(lista_transformada)

