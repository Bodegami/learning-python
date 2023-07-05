
idades = [39, 30, 27, 18]

if 15 in idades:
    print(15)

idades.insert(0, 20)

print(idades)

idades.append([27, 19])

print(idades)

for elemento in idades:
    print(f'Recebi o elemento: {elemento}')

idades = [39, 30, 27, 18]
print(idades)

idades.extend([15, 19])
print(idades)

for idade in idades:
    print(idade + 1)

idades_no_ano_que_vem = []
for idade in idades:
    idades_no_ano_que_vem.append(idade + 1)

print(idades_no_ano_que_vem)

# list Comprehension

idades_no_ano_que_vem2 = [(idade + 1) for idade in idades]
print(idades_no_ano_que_vem2)

lista_filtrada = [(idade) for idade in idades if idade > 21]
print(lista_filtrada)

