import re

# Criando um padrão para email

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


print ("\n======================================================\n")

padrao_molde = "(xx)aaaa-wwww"

padrao = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
texto = "eu gosto do numero 2124551234 e gosto também do 11987651222"
resposta = re.findall(pattern=padrao, string=texto)

print(resposta)

padrao = "([0-9]{2,3})?([0-9]{2})?([0-9]{4,5})([0-9]{4})"
texto = "eu gosto do numero 552124551234 e gosto também do 5511987651222"
resposta = re.findall(padrao, texto)

print(resposta[1][1])

texto = "eu gosto do numero 0552124551234"
resposta = re.search(padrao, texto)
print(resposta.group(2))

print(type(resposta.group(1)))
print(resposta.group())