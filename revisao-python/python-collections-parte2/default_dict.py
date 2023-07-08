from collections import defaultdict

meu_texto = "Bem vindo meu no é XPTO eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachos"
meu_texto = meu_texto.lower()

# Podemos utilizar o defaultDict para trabalhar com valores padrao. No caso o defaultdict espera uma fabrica de padrao
# e com isso podemos passar o 'int' para indicar que o valor padrao caso ele não encontre o elemento é 0.
aparicoes = defaultdict(int)

for palavra in meu_texto.split():
    ate_agora = aparicoes.get(palavra, 0)
    aparicoes[palavra] = ate_agora + 1

[print(palavra) for palavra in aparicoes.items()]

