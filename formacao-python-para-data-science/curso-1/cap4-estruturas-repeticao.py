
# nota_1 = float(input('Digite a 1° nota: '))
# nota_2 = float(input('Digite a 2° nota: '))
# nota_3 = float(input('Digite a 3° nota: '))
#
# print(f'Média: {(nota_1+nota_2+nota_3)/3}')
#
# nota_1 = float(input('Digite a 1° nota: '))
# nota_2 = float(input('Digite a 2° nota: '))
#
# print(f'Média: {(nota_1+nota_2)/2}')
#
# nota_1 = float(input('Digite a 1° nota: '))
# nota_2 = float(input('Digite a 2° nota: '))
#
# print(f'Média: {(nota_1+nota_2)/2}')

# LAÇO WHILE

# contador = 1
# while contador <= 10:
#   print(contador)
#   contador += 1
#
#
# contador = 1
# while contador <= 3:
#   nota_1 = float(input('Digite a 1° nota: '))
#   nota_2 = float(input('Digite a 2° nota: '))
#
#   print(f'Média: {(nota_1+nota_2)/2}')
#   contador += 1

# LAÇO FOR

for contador in range(1,11):
  print(contador)

for contador in range(1,4):
  nota_1 = float(input('Digite a 1° nota: '))
  nota_2 = float(input('Digite a 2° nota: '))

  print(f'Média: {(nota_1+nota_2)/2}')

print("Exemplo de 'for' com 'continue'")
for i in range(1,6):
    if i == 4:
        continue
    print(i)

print("Exemplo de 'for' com 'break'")
for i in range(1,6):
    if i == 4:
        break
    print(i)
