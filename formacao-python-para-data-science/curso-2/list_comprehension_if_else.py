nomes = [('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')]
notas = [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]]
medias = [9.0, 7.3, 5.8, 6.7, 8.5]

situacao = ["Aprovado(a)" if media >= 6  else "Reprovado(a)" for media in medias]
print(situacao)

cadastro = [x for x in [nomes, notas, medias, situacao]]
print(cadastro)

lista_completa = [nomes, notas, medias, situacao]
print(lista_completa)