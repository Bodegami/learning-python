aparicoes = {
    "Guilherme": 1,
    "cachorro": 2,
    "nome": 2,
    "vindo": 1
}
print(aparicoes)

print(type(aparicoes))

print(aparicoes["Guilherme"])

print(aparicoes["cachorro"])

# Lança KeyError quando não encontra a chave. Podemos contar esse comportamento utilizando o metodo get()
# print(aparicoes["xpto"])

print(aparicoes.get("Guilherme"))
print(aparicoes.get("cachorro"))
print(aparicoes.get("xpto"))

# Alem disso, podemos definir como segundo parametro o valor padrao de retorno caso não encontre a chave
print(aparicoes.get("xpto", "Chave não encontrada"))

# podemos usar o dict() para instanciar um dicionario. Note que a semantica muda um pouco
aparicoes = dict(Guilherme=2, cachorro=1)
print(aparicoes)
print(type(aparicoes))
