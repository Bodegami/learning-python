print("****************************************")
print("  Bem vindo ao jogo de Adivinhação!!")
print("****************************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while (rodada <= total_de_tentativas):
    print("Tentativa", rodada, "de", total_de_tentativas)
    chute_str = input("Digite o seu numero: ")
    print("Você digitou: ", chute_str)
    chute_int = int(chute_str)

    acertou = chute_int == numero_secreto
    maior   = chute_int > numero_secreto
    menor   = chute_int < numero_secreto

    if (acertou):
        print("Você acertou!!")
    else:
        if (maior):
            print("Você errou! O seu chute foi maior do que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor do que o número secreto.")

    rodada = rodada + 1






