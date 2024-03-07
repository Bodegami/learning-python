
#Notas do(a) estudante
notas = {'19 Trimestre': 8.5, '2° Trimestre': 9.5, '3º trimestre': 7}
print(notas)

soma = 0

for nota in notas.values():
    soma += nota

print(soma)

somatorio = sum(notas.values())
print(somatorio)

qtd_notas = len(notas)
print(qtd_notas)

media = somatorio / qtd_notas
print(media)

media = round(media, ndigits=1)
print(media)

# help(round)
