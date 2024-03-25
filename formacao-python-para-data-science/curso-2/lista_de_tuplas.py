from random import randint

def gera_codigo():
  return str(randint(0,999))


estudantes = ["João", "Maria", "José", "Cláudia", "Ana"]
print(estudantes)

codigo_estudantes = []

for i in range(len(estudantes)):
  codigo_estudantes.append((estudantes[i], estudantes[i][0] + gera_codigo()))

print(codigo_estudantes)
