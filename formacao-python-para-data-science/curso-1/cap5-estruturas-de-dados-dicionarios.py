
dicionario = {'chave_1':1,
              'chave_2':2}
print(dicionario)

cadastro = {'matricula': 2000168933,
            'dia_cadastro': 25,
            'mes_cadastro': 10,
            'turma': '2E'}
print(cadastro)

print(cadastro['matricula'])
print(cadastro['turma'])

cadastro['turma'] = '2G'
print(cadastro)

cadastro['modalidade'] = 'EAD'
print(cadastro)

print(cadastro.pop('turma'))

print(cadastro)

print(cadastro.items())

print(cadastro.keys())

print(cadastro.values())

for chaves in cadastro.keys():
  print(cadastro[chaves])

for valores in cadastro.values():
  print(valores)

for chaves, valores in cadastro.items():
  print(chaves, valores)

print("\n***********************************\n")

loja = {'nomes': ['televisão', 'celular', 'notebook', 'geladeira', 'fogão'],
        'precos': [2000, 1500, 3500, 4000, 1500]}

for chave, elementos in loja.items():
  print(f'Chave: {chave}\nElementos:')
  for dado in elementos:
    print(dado)
