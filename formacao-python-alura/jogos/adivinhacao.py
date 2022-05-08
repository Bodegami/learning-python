import random

print("****************************************")
print("  Bem vindo ao jogo de Adivinhação!!")
print("****************************************")

numero_secreto = random.randrange(1,101)
total_de_tentativas = 0

print("Qual o nível de dificuldade?")
print("(1) Fácil (2) médio (3) difícil")

nivel = int(input("Define um nível: "))

if nivel == 1:
    total_de_tentativas = 20
elif nivel == 2:
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou: ", chute_str)
    chute_int = int(chute_str)

    if chute_int < 1 or chute_int > 100:
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = chute_int == numero_secreto
    maior   = chute_int > numero_secreto
    menor   = chute_int < numero_secreto

    if (acertou):
        print("Você acertou!!")
        break
    else:
        if (maior):
            print("Você errou! O seu chute foi maior do que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor do que o número secreto.")
print("Fim do jogo!")
print("O número secreto é", numero_secreto)





