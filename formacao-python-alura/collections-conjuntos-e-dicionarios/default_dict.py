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