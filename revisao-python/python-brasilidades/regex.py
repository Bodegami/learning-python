import re

padrao = "[0-9][a-z][0-9]"
texto = "123 1a2 1cc aa1"

# retorna a o elemento encontrado e a posicao na string
resposta = re.search(pattern=padrao, string=texto)
print(resposta)

print(resposta.group())


padrao = "\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"
texto = "aaannnccc  renato@gmail.com.br hahahaee kiussssssa"

resposta = re.search(pattern=padrao, string=texto)
print(resposta)
print(resposta.group())