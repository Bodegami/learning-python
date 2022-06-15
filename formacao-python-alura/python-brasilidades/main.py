import re
from documento import Documento, DocCnpj, DocCpf
from validate_docbr import CPF, CNPJ

print("=================|| Construcao da classe Cpf ||=====================")
# cpf = Cpf("11111111112")
# print(cpf)

# cpf = "15616987913"
# objeto_cpf = Cpf(cpf)
#
# print(objeto_cpf)

print("=================|| Construcao da classe Cnpj ||=====================")

# exemplo_cnpj = "35379838000112"
# exemplo_cpf = "32007832062"
# # cnpj = CNPJ()
# # print(cnpj.validate(exemplo_cnpj))
# tipo_documento = "cnpj"
# documento = CpfCnpj(exemplo_cnpj, tipo_documento)
# print(documento)
#
# tipo_documento = "cpf"
# documento = CpfCnpj(exemplo_cpf,tipo_documento)
# print(documento)


print("=================|| Refatorando a classe ||=====================")

exemplo_cpf = "32007832062"
documento = Documento.cria_documento(exemplo_cpf)
print(documento)

exemplo_cnpj = "35379838000112"
documento = Documento.cria_documento(exemplo_cnpj)
print(documento)

print("=================|| Sobre REGEX ||=====================")

'''

Para construirmos este padrão, o primeiro passo é conhecer os caracteres especiais da linguagem e saber qual é 
a biblioteca responsável por isso. Encontraremos as expressões regulares dentro do texto por meio de métodos 
específicos da linguagem também.

Os colchetes [] são caracteres especiais que definem um range ou um grupo de caracteres, 
como [0-9], [a-z] ou [abc] por exemplo;

Já o * pega uma ou mais ocorrências do padrão definido anteriormente;

As chaves {} nos permitem definir uma quantidade específica de vezes que queremos que o padrão se repita 
ou um intervalo de possibilidades, como [abc]{5} por exemplo;

O \w pode ser qualquer número de zero a nove ou letra de "A" a "Z";

A barra | representa uma coisa ou outra como em @|$ por exemplo;

Os parênteses () capturam um grupo, e veremos sua importância mais adiante.

'''

padrao = "[0-9][a-z][0-9]"
texto = "123 1a2 1cc aa1"

# O metodo search espera o padrao em regex e o texto onde ele deve buscar o padrao.
# Ele retorna:
# span(inicio, fim) = posicao inicial e final onde se encontra o padrao
# match('???') = padrao encontrado dentro do texto
resposta = re.search(padrao, texto)
print(resposta)

# Retorna apenas o padrao encontrado dentro do texto
print(resposta.group())

padrao = "[0-9][a-z]{2}[0-9]"
texto = "123 1ac2 1cc aa1"

resposta = re.search(padrao, texto)
print(resposta)

# Criando um regex para email
padrao = "\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"
texto = "aaabbbcccc bodegami666@gmail.com.br humm"

resposta = re.search(padrao, texto)
print(resposta.group())
