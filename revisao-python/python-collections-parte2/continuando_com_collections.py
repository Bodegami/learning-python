
usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

print(usuarios_data_science)
print(usuarios_machine_learning)

# faz uma copia da lista e depois adicionamos os elementos da outra lista, porem gera duplicidade
assistiram = usuarios_data_science.copy() # copia raza
assistiram.extend(usuarios_machine_learning)
print(assistiram)

# set() é conjunto que não permite a repetição de elementos
print(set(assistiram))

print({1, 2, 3, 1})

# forma classica set([])
print(type(set([1, 2, 3, 1])))
# forma literal set({})
print(type({1, 2, 3, 1}))

for numero in set(assistiram):
    print(numero)


usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}

# O set(0 não possui extend, mas existe a abordagem abaixo que funciona de forma similar
assistiram = usuarios_data_science | usuarios_machine_learning
print(assistiram)

# A operacao abaixo retorna apenas os elementos existentes nos dois conjuntos
assistiram = usuarios_data_science & usuarios_machine_learning
print(assistiram)

# A operacao abaixo retorna apenas os elementos que estao no primeiro set e nao estão no segundo
assistiram = usuarios_data_science - usuarios_machine_learning
print(assistiram)


print(15 in usuarios_data_science | usuarios_machine_learning)


# A operacao abaixo é o OU Exclusivo (retorna os usuarios que não fizeram machine_learning e os usuarios que não fizaram
# data_science
assistiram = usuarios_data_science ^ usuarios_machine_learning
print(assistiram)

