from collections import defaultdict, Counter

meu_texto = "Bem vindo meu no é XPTO eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachos"
meu_texto = meu_texto.lower()

aparicoes = defaultdict(int)
for palavra in meu_texto.split():
    aparicoes[palavra] += 1

[print(palavra) for palavra in aparicoes.items()]


class Conta:
    def __init__(self):
        print("Imprimindo uma conta")


contas = defaultdict(Conta)

# Caso não encontre o elemento, retorna o valor padrao que instaciar uma conta
contas[15]

contas[17]

contas[15]

print(len(contas))

# O Counter() pode receber um iteravel como parametro e ele automaticamente vai contar cada repeticao dos elementos
aparicoes = Counter(meu_texto.split())
[print(palavra) for palavra in aparicoes.items()]