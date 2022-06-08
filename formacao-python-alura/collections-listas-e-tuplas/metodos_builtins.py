idades = [15, 87, 32, 65, 56, 32, 49, 37]

# Imprimindo o valor e a posicao de cada elemento da lista
print("=========================|| Imprimindo o indice e o valor com o range ||==============================")
print(range(len(idades)))

# range(start, stop)
for i in range(0, len(idades)):
    print(i, idades[i])

print("========================|| Sobre a caracteristica Lazy do range() e o enumerate() ||===========================")
# É importante ressaltar que o range e o enumerate só geram a lista quando são chamados...
# enquanto nao sao chamados, eles ficam apenas em estado "ready"
print(type(range(len(idades)))) # lasy
print(enumerate(idades)) # lasy

print("=========================|| Forçando a impressão com o construtor de list() ||==============================")
print(list(range(len(idades)))) # forcei a geracao dos valores atraves do construtor de List() que aceita um interavel
print(list(enumerate(idades))) # forcei a geracao dos valores atraves do construtor de List() que aceita um interavel

idades_enumeradas = list(enumerate(idades))
print(f"Idades enumeradas: {idades_enumeradas}")

print("=========================|| Uso recomendado do enumerate() ||==============================")
# Utilizando a caracterictica lazy do enumerate - recomendado para listas com grande volume, pois dessa forma
# o enumerate só vai gerando o valor conforme o necessario.
for valor in enumerate(idades):
    print(valor)

# Aproveitando a caracteristica da tupla - dessa forma desempacotamos a tupla e recuperamos o indice e o valor
print("=========================|| Desempacotando a tupla ||==============================")
for indice, valor in enumerate(idades): # unpacking da nossa tupla
    print(indice, "x", valor)

print("=======================|| Desempacotando a tupla e imprimindo um atributo do objeto ||=========================")
usuarios = [("Guilherme", 37, 1981),
            ("Daniela", 31, 1987),
            ("Paulo", 39, 1979)]

print(f"Lista de tuplas de usuarios: {usuarios}")

for nome, idade, nascimento in usuarios: # já desempacontando
    print(f'Idade do primeiro usuario: {idade}')


for nome, _, _ in usuarios: # já desempacontando, ignorando os outros atributos do objeto
    print(f'Nome do primeiro usuario: {nome}')


print("=======================|| Retorna error caso omitimos um dos atributos no unpacking ||=========================")
# Quando utilizamos a estrategia de desempacotar durante o for, temos que listar ou ignorar todos os atributos,
# mas podemos omitir como no exemplo abaixo, senão retorna um ValueError
try:
    for nome, _ in usuarios: # já desempacontando, ignorando os outros atributos do objeto
        print(f'Nome do primeiro usuario: {nome}')
except ValueError as ve:
    print(f'Error: {ve}')


