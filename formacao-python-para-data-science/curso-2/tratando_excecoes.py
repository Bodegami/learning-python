
#try:
#    notas = {'João': [8.0, 9.0, 10.0], 'Maria': [9.0, 7.0, 6.0], 'José': [3.4, 7.0, 8.0],'Cláudia': [5.5, 6.6, 8.0], 'Ana': [6.0, 10.0, 9.5], 'Joaquim': [5.5, 7.5, 9.0], 'Júlia': [6.0, 8.0, 7.0], 'Pedro': [3.0, 4.0, 6.0]}
#    nome = input("Digite o nome do(a) estudante: ")
#    resultado = notas[nome]
#    print(resultado)
#except KeyError as ke:
#    print(type(ke), f'Erro: Estudante {ke} não matriculado(a) na turma!')


#try:
#    notas = {'João': [8.0, 9.0, 10.0], 'Maria': [9.0, 7.0, 6.0], 'José': [3.4, 7.0, 8.0],'Cláudia': [5.5, 6.6, 8.0], 'Ana': [6.0, 10.0, 9.5], 'Joaquim': [5.5, 7.5, 9.0], 'Júlia': [6.0, 8.0, 7.0], 'Pedro': [3.0, 4.0, 6.0]}
#    nome = input("Digite o nome do(a) estudante: ")
#    resultado = notas[nome]
#except KeyError as ke:
#    print(type(ke), f'Erro: Estudante {ke} não matriculado(a) na turma!')
#else:    # O fluxo do else é executado caso execute com sucesso o bloco do try
#    print(resultado)


try:
    notas = {'João': [8.0, 9.0, 10.0], 'Maria': [9.0, 7.0, 6.0], 'José': [3.4, 7.0, 8.0],'Cláudia': [5.5, 6.6, 8.0], 'Ana': [6.0, 10.0, 9.5], 'Joaquim': [5.5, 7.5, 9.0], 'Júlia': [6.0, 8.0, 7.0], 'Pedro': [3.0, 4.0, 6.0]}
    nome = input("Digite o nome do(a) estudante: ")
    resultado = notas[nome]
except KeyError as ke:
    print(type(ke), f'Erro: Estudante {ke} não matriculado(a) na turma!')
else:    # O fluxo do else é executado caso execute com sucesso o bloco do try
    print(resultado) 
finally: # o finally é um bloco que é executado tanto no caso de sucesso do try quanto de erro do except
    print("A consulta foi encerrada!")       