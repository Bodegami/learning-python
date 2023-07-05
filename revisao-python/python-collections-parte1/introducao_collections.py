idade1 = 39
idade2 = 30
idade3 = 27
idade4 = 18

idades = [39, 30, 27, 18]

print(type(idades))
print(idades)

print(len(idades))

print(idades[2])

idades.append(15)

print(idades)

print(idades[4])

for idade in idades:
    print(idade)

result = [print("Idade: ", idade) for idade in idades]

idades.append(27) # Adiciona um elemento no final da lista

print(idades)

idades.remove(27) # remove o primeiro elemento que encontrar na lista

print(idades)

idades.clear() # Remove todos elementos da lista

print(idades)


