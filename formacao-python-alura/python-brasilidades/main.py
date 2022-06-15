from acesso_cep import BuscaEndereco
from datetime import datetime, timedelta
from datasBr import DatasBr
import re
from telefonesBr import TelefonesBr
from documento import Documento, DocCnpj, DocCpf
from validate_docbr import CPF, CNPJ

print("=================|| Construcao da classe Cpf ||=====================")
# cpf = Cpf("11111111112")
# print(cpf)
#
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

# Criando um padrao para telefone

padrao_molde = "(xx)aaaa-wwww"
padrao = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
texto = "Eu gosto do numero 2126451234 e gosto também do 2136431234"

# O metodo findall retorna uma lista com todos os padrões encontrados dentro do texto
resposta = re.findall(padrao, texto)
print(resposta)
print(re.search(padrao, texto).group())


print("=================|| Testando a classe TelefonesBr ||=====================")

telefone = "551126481234"

telefone_class = TelefonesBr(telefone)


print("=================|| Definindo a mascara ||=====================")

padrao = "([0-9]{2,3})([0-9]{2})([0-9]{4,5})([0-9]{4})"
telefone = "551126481234"
resposta = re.findall(padrao, telefone)
print(resposta)

# Utilizando o agrupamento no regex '()', podemos pegar apenas um grupo no metodo group() passando a posicao dele
print(re.search(padrao, telefone).group(2))


# Utilizando o depois do agrupamento '?' indicamos que ele é opcional
padrao = "([0-9]{2,3})?([0-9]{2})?([0-9]{4,5})([0-9]{4})"
telefone = "1126481234"
print(re.search(padrao, telefone).group())

telefone = "26481234"
print(re.search(padrao, telefone).group())


print("=================|| Testando a mascara da classe TelefonesBr ||=====================")

telefone = "551126481234"
telefone_objeto = TelefonesBr(telefone)
print(telefone_objeto)


print("=================|| Sobre a lib datetime ||=====================")

# retorna a data e hora atual
print(datetime.today())

# imprimindo a data e hora a partir da nossa classe
cadastro = DatasBr()
print(cadastro.momento_cadastro)

# utilizando o metodo 'month' do datetime na nossa classe
print(cadastro.mes_cadastro())

# utilizando o metodo 'weekday' do datetime na nossa classe
print(cadastro.dia_semana())


print("=================|| Formatando o padrao de datas ||=====================")

# Sem formatacao
hoje = datetime.today()

# Aplicando uma formatacao usando o metodo 'strftime'
hoje_formatado = hoje.strftime("%d/%m/%Y %H:%M")

print(hoje)
print(hoje_formatado)

# O tipo do objeto datetime
print(type(hoje))

# Aqui é importante falar que quando chamamos o metodo 'strftime', ele retona uma string ao inves de um objeto datetime
print(type(hoje_formatado))

# Testando a formatacao da data na nossa classe DatasBr
hoje_classe_datasBr = DatasBr()
print(hoje_classe_datasBr)


print("=================|| Sobre o import timedelta da lib datetime ||=====================")

hoje = datetime.today()

# aqui utilizamos ele para acrescentar um dia a data de hoje
amanha = datetime.today() + timedelta(days=1)

# o timedelta suporta operacoes aritmeticas como soma, subtracao, multiplicacao e etc.
print(amanha - hoje)


print("=================|| Testando o metodo tempo_cadastro de nossa classe DatasBr ||=====================")

hoje = DatasBr()
print(hoje.tempo_cadastro())


print("=================|| Criando a classe BuscaEndereco ||=====================")

# Testando o metodo 'cep_e_valido' de nossa classe BuscaEndereco com um cep invalido
# Ao passar um cep invalido, deve retornar o error: Cep Invalido
cep = 2587014
try:
    objeto_cep = BuscaEndereco(cep)
except ValueError as ve:
    print(f'Error: {ve}')

# Testando o metodo 'cep_e_valido' de nossa classe BuscaEndereco com um cep valido
cep = 25870146
objeto_cep = BuscaEndereco(cep)

# Testando os metodos 'format_cep' e '__str__' da nossa classe BuscaEndereco
print(objeto_cep)
