
idades = [15, 87, 32, 65, 56, 32, 49, 37]

for i in range(len(idades)):
    print((i, idades[i]))

enumerate(idades) # lazy, ou seja, ele se prepara para gerar a estrutura, mas só vai gerar quando for chamado

list(range(len(idades))) # forcei a geração dos valores com o construtor do list() que espera um iteravel

list(enumerate(idades)) # assim como o list() acima, forcei a geração, porem o enumerate retorna uma lista de tuplas

for valor in enumerate(idades):
    print(valor)

for indice, idade in enumerate(idades):
    print(indice, "x", idade)


usuarios = [
    ('Guilherme', 37, 1981),
    ('Daniela', 31, 1987),
    ('Paulo', 39, 1979)
]

# imprimindo tupla por tupla
for usuario in usuarios:
    print(usuario)

# desempacotando a tupla e imprimindo apenas o nome
for nome, idade, nascimento in usuarios:
    print(nome)

# desempacotando a tupla e imprimindo o nome e ignorando os outros elementos
for nome, _, _ in usuarios:
    print(nome)