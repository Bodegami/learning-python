# Lista tradicional
usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

print("\n=======================|| Metodo built-in copy() do list() ||=======================\n")


# o metodo built-in copy() faz uma copia raza, ou seja, se a nossa lista fosse composta por objetos
# como ContaCorrente e etc. Ele devolveria uma copia da referência do objeto e não uma copia do proprio objeto.
assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)

print(assistiram)
print(len(assistiram))


print("\n=======================|| Sobre o tipo conjunto ou set() ||=======================\n")

# O conjunto ou set(), tem como caracteristica nao aceitar a repeticao de valores.
# Ele também não possui um indice e não é ordenado
assistiram_set = set(assistiram)
print(assistiram_set)


print("\n=======================|| Passando uma lista ou iteravel no construtor de set() ||=======================\n")

set_com_lista = set([1, 2, 3, 1])
print(set_com_lista)

numeros = [15, 23, 45, 56, 89, 47, 23, 45] # Criando um lista simples de inteiros
numeros_ordenados = list(enumerate(numeros)) # Criando uma lista de tuplas onde a chave é o indice
print(numeros_ordenados)

conjunto_ordenado = set(numeros_ordenados) # Criando um set com uma lista de tuplas
print(conjunto_ordenado)

# Note que a lista de numeros repete o valor 23 no indice 1 e 6, porém quando geramos um set com a lista de numeros,
# mesmo assim ele criou duas tuplas com os valores: (1, 23) e (6, 23).
# O set() so aceitou a repetira por que a chave da tupla (key) é diferente entre as duas.
# Caso a inteção fosse mudar esse comportamentos, seria necessario criar uma classe que herda de set()
# e sobrescrever o metodo de comparacao, atribuindo a nossa logica


print("\n=======================|| Instanciando um set() direto com os valores ||=======================\n")

set_sem_lista = {1, 2, 3, 1}
print(set_sem_lista)

print(type({1, 2}))


print("\n=======================|| Retorna error caso tente acessar um indice de um set()||=======================\n")

# O conjunto nao tem indice, nao sendo possivel pegar um elemento pelo indice
conjunto = {4, 89, 16, 29, 0}
try:
    print(conjunto[1])
except TypeError as te:
    print(f'Error: {te}')


print("\n=======================|| Iterando sobre um set() ||=======================\n")

usuarios = {15, 23, 45, 56, 89, 47, 23, 45}
print(usuarios)
for usuario in usuarios:
    print(usuario)


print("\n=======================|| Unindo dois conjuntos ||=======================\n")


usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}

# O set(0 não possui um metodo built-in como o extend(0 da lista,
# porem podemos utilizar o operador de ou (|) para atribuir duas listas há um set()
usuarios_nos_dois_cursos = set(usuarios_data_science | usuarios_machine_learning)
print(usuarios_nos_dois_cursos)


print("\n======================|| Unindo dois conjuntos pegandos apenas os valores em comum ||======================\n")


usuarios_dos_dois_cursos = set(usuarios_data_science & usuarios_machine_learning)
print(usuarios_dos_dois_cursos)


print("\n======================|| Pegando os valores de um set e subtraindo por outro set() ||======================\n")


usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}
print(f'Usuarios do curso de data science: {usuarios_data_science}')
print(f'Usuarios do curso de machine learning: {usuarios_machine_learning}')
usuarios_que_n_fizeram_machine_learn = usuarios_data_science - usuarios_machine_learning
print(f'Usuarios que nao fizeram machine learning: {usuarios_que_n_fizeram_machine_learn}')

print(15 in usuarios_que_n_fizeram_machine_learn)


print("\n===============|| Pegando o usuario que fez um dos cursos, mas ñ os dois / (ou exclusivo) ||===============\n")

somente_usuarios_que_fizeram_um_dos_cursos = usuarios_data_science ^ usuarios_machine_learning
print(somente_usuarios_que_fizeram_um_dos_cursos)


print("\n===============|| Mudando conjuntos em tempo real ||===============\n")

# Os conjuntos são mutaveis assim como as listas
usuarios = {1, 5, 76, 34, 52, 13, 17}
print(usuarios)
print(len(usuarios))

usuarios.add(765)
print(usuarios)
print(len(usuarios))

usuarios.remove(5)
print(usuarios)
print(len(usuarios))


print("\n===============|| Criando um conjunto imutavel (frozenset()) ||===============\n")

frozen_usuarios = frozenset(usuarios)
print(frozen_usuarios)
print(len(frozen_usuarios))

# O frozenset() nao aceita operacoes para adicionar/ remover elementos
try:
    frozen_usuarios.add(859)
except AttributeError as ae:
    print(f'Error: {ae}')


print("\n===============|| Criando um conjunto de strings ||===============\n")

meu_texto = 'Bem vindo meu nome é Renato eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro'

conjunto_string = set(meu_texto.split())
print(conjunto_string)


print("\n===============|| Sobre o metodo intersection() ||===============\n")

usuarios = {1, 5, 76, 34, 52, 13, 17}
frozen_usuarios = frozenset(usuarios)
print(frozen_usuarios)
print(len(frozen_usuarios))

usuarios_genericos = {1, 32, 52, 47}

# Retorna os elementos em comun nos dois conjuntos
usuarios_em_comum = frozen_usuarios.intersection(usuarios_genericos)
print(usuarios_em_comum)


print("\n===============|| Sobre o metodo difference() ||===============\n")

usuarios = {1, 5, 76, 34, 52, 13, 17}
frozen_usuarios = frozenset(usuarios)
print(frozen_usuarios)
print(len(frozen_usuarios))

usuarios_genericos = {1, 32, 52, 47}

# Retorna os elementos distintos do set frozen_usuarios comparado a outros
usuarios_distintos_deste_set = frozen_usuarios.difference(usuarios_genericos)
print(usuarios_distintos_deste_set)


print("\n===============|| Sobre o metodo union() ||===============\n")

usuarios = {1, 5, 76, 34, 52, 13, 17}
frozen_usuarios = frozenset(usuarios)
print(frozen_usuarios)
print(len(frozen_usuarios))

usuarios_genericos = {1, 32, 52, 47}

# Cria um novo frozenset() com os usuarios dos dois conjuntos
usuarios_dos_dois_conjuntos = frozen_usuarios.union(usuarios_genericos)
print(usuarios_dos_dois_conjuntos)
