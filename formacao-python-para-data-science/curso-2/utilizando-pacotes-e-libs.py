import matplotlib.pyplot as plt
from random import choice
from random import randrange, sample

estudantes = ["João", "Maria", "José"]
notas = [8.5, 9, 6.5]

# Imprime um grafico
# plt.bar(x=estudantes, height=notas)

estudantes_2 = ["João", "Maria", "José", "Ana"]
print(estudantes_2)

help(choice)

estudante = choice(estudantes_2)
print(estudante)

# ************************************

lista = []

for i in range(0, 20):
  lista.append(randrange(100))

sample(lista, 5)

# ************************************

import math 

n = int(input("Digite um número positivo para calcular sua raiz quadrada:"))
print(f"\nA raiz quadrada de {n} é igual a {math.sqrt(n)}")

# ************************************

from math import * 

n = int(input("Digite um número positivo para calcular sua raiz quadrada:"))
print(f"\nA raiz quadrada de {n} é igual a {sqrt(n)}")


