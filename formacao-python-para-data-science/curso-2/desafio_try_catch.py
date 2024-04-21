funcionarios = {'José': 2000, 'Ana': 2200,'João': 2500, 'Maria': 3800}


try:
  aumento = list(map(lambda x: x * 1.1, funcionarios.values()))
except ValueError as e:
  print(type(e), f'Erro: {e}')
else:
  print(aumento)
finally:
  print("Processo concluido!")

  
try:
  aumento = list(map(lambda x: x[1] * 1.1, funcionarios.items()))
except ValueError as e:
  print(type(e), f'Erro: {e}')
else:
  print(aumento)
finally:
  print("Processo concluido!")  