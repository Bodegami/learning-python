from collections import defaultdict

print("\n===========|| Contando o numero de repeticoes de cada palavra em um texto ||===========\n")

meu_texto = 'Bem vindo meu nome é Renato eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro'
meu_texto = meu_texto.lower()

print(meu_texto)

aparicoes = {}

for palavra in meu_texto.split():
    ate_agora = aparicoes.get(palavra, 0)
    aparicoes[palavra] = ate_agora + 1

print(aparicoes)

print("\n=========|| Contando o numero de repeticoes de cada palavra em um texto usando o defaultdict()||=========\n")

meu_texto = 'Bem vindo meu nome é Renato eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro'
meu_texto = meu_texto.lower()

print(meu_texto)

# O defaultdict() espera uma funcao como argumento que será usada toda vez
# que ele nao encontrar um elemento no dicionario, aqui no caso passamos a funcao int que
# também pode ser entendida como int()
dicionario = defaultdict(int)

for palavra in meu_texto.split():
    ate_agora = dicionario[palavra]
    dicionario[palavra] = ate_agora + 1

# Com essa implementacao, quando o dicionario nao encontra o elemento,
# ele chama a funcao int() que por padrao retorna 0
print(dicionario)
print(f'Contem a palavra \'Guilherme\'?: {dicionario["Guilherme"]}')

# Agora adicionamos a chave 'Guilherme' com o valor '15'
dicionario["Guilherme"] = 15

print(f'Contem a palavra \'Guilherme\'?: {dicionario["Guilherme"]}')

print("\n=========|| Melhorando a implementacao acima ||=========\n")

meu_texto = 'Bem vindo meu nome é Renato eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro'
meu_texto = meu_texto.lower()

dicionario = defaultdict(int)

for palavra in meu_texto.split():
    dicionario[palavra] += 1

print(dicionario)

print("\n=========|| Usando o Counter() ||=========\n")

from collections import Counter

meu_texto = 'Bem vindo meu nome é Renato eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro'
meu_texto = meu_texto.lower()

dicionario = Counter()
for palavra in meu_texto.split():
    dicionario[palavra] += 1

print(dicionario)

print("\n=========|| Usando o Counter() recebendo um iteravel||=========\n")

meu_texto = 'Bem vindo meu nome é Renato eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro'
meu_texto = meu_texto.lower()

# Note que podemos passar uma lista no construtor e a resposta sera o counter dos elementos da lista
dicionario = Counter(meu_texto.split())
print(dicionario)

print("\n=========|| Exemplo de uso  ||=========\n")


# Note que nessa abordagem, se ele nao encontra o elemento no dicionario ele já chama a classe
# e o seu construtor e instancia um objeto no dicionario
class Conta:
    def __init__(self):
        print("Criando uma conta")


contas = defaultdict(Conta)
contas[15]
contas[17]
print(contas)
