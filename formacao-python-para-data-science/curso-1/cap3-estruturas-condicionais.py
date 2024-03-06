

if 2 < 7:
    print('condição verdadeira')


lista = dict({"Renato": 2, "Caio": 1, "Paulo": 3})

if "Renato" in lista:
    print(lista["Renato"])


media = float(input('Digite a média:  '))

if media >= 6.0:
  print('Aprovado(a)')
elif 6.0 > media >= 4.0:
  print('Recuperação')
else:
  print('Reprovado(a)')

t1 = t2 = True
f1 = f2 = False

# OPERADOR AND

if t1 and t2:
  print('expressão verdadeira')
else:
  print('expressão falsa')

if t1 and f2:
  print('expressão verdadeira')
else:
  print('expressão falsa')


# OPERADOR OR

if f1 or f2:
  print('expressão verdadeira')
else:
  print('expressão falsa')


if t1 or f2:
  print('expressão verdadeira')
else:
  print('expressão falsa')


# OPERADOR NOT

if not t1:
  print('expressão verdadeira')
else:
  print('expressão falsa')


if not t1:
  print('expressão verdadeira')
else:
  print('expressão falsa')


if not f1:
  print('expressão verdadeira')
else:
  print('expressão falsa')


# OPERADOR IN

lista = 'José da Silva, Maria Oliveira, Pedro Martins, Ana Souza, Carlos Rodrigues, Juliana Santos, Bruno Gomes, Beatriz Costa, Felipe Almeida, Mariana Fernandes, João Pinto, Luísa Nascimento, Gabriel Souza, Manuela Santos, Thiago Oliveira, Sofia Ferreira, Rafael Albuquerque, Isabella Gomes, Bruno Costa, Maria Martins, Rafaela Souza, Matheus Fernandes, Luísa Almeida, Beatriz Pinto, Mariana Rodrigues, Gabriel Nascimento, João Ferreira, Maria Albuquerque, Felipe Oliveira'

nome_1 = 'Mariana Rodrigues'
nome_2 = 'Marcelo Nogueira'

if nome_1 in lista:
  print(f'{nome_1} está na lista')
else:
  print(f'{nome_1} não está na lista')

if nome_2 in lista:
  print(f'{nome_2} está na lista')
else:
  print(f'{nome_2} não está na lista')


