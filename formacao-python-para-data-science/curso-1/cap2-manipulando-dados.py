
# Nomes que não podemos definir para variáveis:
#
# Nomes que começam com números. Exemplos: 10_notas, 2_nomes_casa.
#
# Palavras separadas por espaço. Exemplos: Nome escola, notas estudantes.
#
# Nomes de funções do Python. Exemplos: print, type.

idade = 5
print(idade)

idade = 10
print(idade)

idade = 15
print(idade)

nome = "Gabriel"
print(nome)

# Tipos de variaveis

print(type(idade))
print(type(nome))

f = 9.8
b = True
print(type(f))
print(type(b))

nome_aluno = 'Fabricio Daniel'
idade_aluno = 15
media_aluno = 8.45
situacao_aprovado = True
print(nome_aluno, idade_aluno, media_aluno, situacao_aprovado)

# variaveis numericas

q_seguranca = 5
s_seguranca = 3000

q_docente = 16
s_docente = 6000

q_diretoria = 1
s_diretoria = 12500

total_empregados = q_seguranca + q_docente + q_diretoria
print(total_empregados)

diferenca_salario = s_diretoria - s_seguranca
print(diferenca_salario)

media = ((q_seguranca * s_seguranca) + (q_docente * s_docente) + (q_diretoria * s_diretoria)) / (total_empregados)
print(media)
print(media.__round__(2))

# variaveis do tipo string

s1 = 'Alura'
s2 = "Alura"
s3 = f"Alura"

print(s1, s2, s3)

texto_correto = "GEOVANA ALESSANDRA DIAS SANTOS"
texto = '          Geovana Alessandra dias Sanyos'
print(f'Texto correto: {texto_correto}')
print(f'Texto sem tratamento: {texto}')

texto_corrigido = texto.strip().replace("y", "t").upper()
print(f'Texto tratado: {texto_corrigido}')

print(chr(64))

# coletando dados

nome = input('Escreva o seu nome: ')
print(nome)

ano_entrada = input("Escreva o ano de ingresso do(a) estudante")
print(type(ano_entrada))

ano_entrada = int(input("Escreva o ano de ingresso do(a) estudante"))
print(type(ano_entrada))


