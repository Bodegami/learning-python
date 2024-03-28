notas = [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]]


def media(lista: list=[0]) -> float:
  ''' Função para calcular a média de notas passadas por uma lista

  lista: list, default [0]
    Lista com as notas para calcular a média
  return = calculo: float
    Média calculada
  '''
  
  calculo = sum(lista) / len(lista)

  return calculo

medias = [round(media(nota), 1) for nota in notas]

print(medias)

nomes = [('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')]
medias = [9.0, 7.3, 5.8, 6.7, 8.5]

nomes = [nome[0] for nome in nomes]
print(nomes)

# O zip recebe duas listas como argumentos e retorna um zip de tuplas
estudantes = list(zip(nomes, medias))
print(estudantes)

candidatos = [estudante[0] for estudante in estudantes if estudante[1] >= 8]
print(candidatos)
