lista_completa = [[('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')],
                  [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]],
                  [9.0, 7.3, 5.8, 6.7, 8.5],
                  ['Aprovado', 'Aprovado', 'Reprovado', 'Aprovado', 'Aprovado']]

colunas = ["Notas", "Média Final", "Situação"]

cadastro = {colunas[i]: lista_completa[i + 1] for i in range(len(colunas))}
print(cadastro)

cadastro["Estudante"] = [lista_completa[0][i][0] for i in range(len(lista_completa[0]))]
print(f"Cadastro {cadastro}")

resultado = [f'Estudante: {cadastro["Estudante"][i]} | Média Final: {cadastro["Média Final"][i]} | Estudante: {cadastro["Situação"][i]}' for i in range(len(cadastro["Estudante"]))]

[print(item + "\n") for item in resultado]

"""
    Desafio:

    Recebemos uma demanda da instituição de ensino do nosso projeto que nos repassou uma lista de 20 estudantes e 
    suas respectivas médias finais. Aqui, nós precisamos selecionar estudantes que tenham média final maior ou igual a 9.0. 
    Esses(as) estudantes serão premiados(as) com uma bolsa de estudos para o próximo ano letivo.

    Para filtrar os dados, temos que gerar um dicionário cujas chaves são os nomes e os valores são as médias dos(as) estudantes selecionados(as). 
    Estes são os dados recebidos:

"""

nomes_estudantes = [ "Enrico Monteiro", "Luna Pereira", "Anthony Silveira", "Letícia Fernandes", 
                    "João Vitor Nascimento", "Maysa Caldeira", "Diana Carvalho", "Mariane da Rosa",
                    "Camila Fernandes", "Levi Alves", "Nicolas da Rocha", "Amanda Novaes", 
                    "Laís Moraes", "Letícia Oliveira", "Lucca Novaes", "Lara Cunha", 
                    "Beatriz Martins", "João Vitor Azevedo", "Stephany Rosa", "Gustavo Henrique Lima" ]

medias_estudantes = [5.4, 4.1, 9.1, 5.3, 6.9, 3.1, 10.0, 5.0, 8.2, 5.5,
                    8.1, 7.4, 5.0, 3.7, 8.1, 6.2, 6.1, 5.6, 6.7, 8.2]

resultado_de_todos_alunos = {nomes_estudantes[i]: medias_estudantes[i] for i in range(len(nomes_estudantes))}
print(resultado_de_todos_alunos)

resultado_dos_aprovados= {nomes_estudantes[i]: medias_estudantes[i] for i in range(len(nomes_estudantes)) if medias_estudantes[i] >= 9.0}
print(f"Aprovados para bolsa de estudos: {resultado_dos_aprovados}")

bolsistas = {nome: media for nome, media in zip(nomes_estudantes, medias_estudantes) if media >= 9.0}
print(bolsistas)