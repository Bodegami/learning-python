
lista = ['Fabricio Daniel',9.5,9.0,8.0,True]
print(type(lista))
print(lista)

print(lista[0])

print(lista[-1])

for elemento in lista:
  print(elemento)


print(len(lista))

print(lista[1:4])

print(lista[:3])

print(lista[3:])

print(lista[:])

media = round(sum(lista[1:4]) / 3, ndigits=1)
lista.append(media)
print(lista)

notas = [10.0, 8.0, 9.0]

lista.extend(notas)
print(lista)

lista.append(notas)
print(lista)

lista.remove(notas)
print(lista)

raca_caes = ['Labrador Retriever',
             'Bulldog Francês',
             'Pastor Alemão',
             'Poodle']

print(raca_caes)

raca_caes.insert(1, 'Golden Retriever')
print(raca_caes)

print(raca_caes.pop(1))

print(raca_caes.index('Pastor Alemão'))

raca_caes.sort()
print(raca_caes)

