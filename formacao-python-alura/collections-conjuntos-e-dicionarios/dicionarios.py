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


print("\n=================|| Retorna error ao tentar acessar uma chave que nao esta no dicionario||==================\n")

try:
    print(dicionario_string["Guilherme"])
except KeyError as ke:
    print(f'Error: Key ({ke}) not found..')


# Já ao tentar acessar uma chave que nao existe, mas utilizando o metodo get(), retorna None
print(dicionario_string.get("Guilherme"))

# Podemos ainda escolher um tipo de retorno (int, float, string, bool) caso nao encontre a chave
print(dicionario_string.get("Guilherme", "Not found..."))
