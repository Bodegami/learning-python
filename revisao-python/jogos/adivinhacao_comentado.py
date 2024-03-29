import random


def jogar():
    print("*********************************")
    print("Bem vindo no jogo de Adivinhação!")
    print("*********************************")

    #No exemplo abaixo geramos um numero aleatorio arredondado, mas com riso desse número ser 0
    # numero_random = random.random() * 100
    # numero_secreto = round(numero_random)

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil | (2) Médio | (3) Difícil")
    nivel = int(input("Define o nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5


    #O range é exclusivo, ou seja, ele nao itera sobre o ultimo elemento (3), por isso adicionamos + 1
    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        #O input alem de imprimir a frase, também recebe a entrada sempre como String
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")

            # Calcula o valor absoluto entre o numero secreto menos o chute
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos

    print("Fim do jogo!")

#Com o if abaixo permitimos que, essa classe possa ser importada em outra e executada atraves da função jogar()
#ou executar essa classe direto no terminal apenas chamando ela pelo nome
if (__name__ == "__main__"):
    jogar()