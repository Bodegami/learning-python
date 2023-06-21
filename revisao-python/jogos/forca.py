import random


def jogar():

    imprime_msg_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    print("Fim do jogo!")


def imprime_msg_abertura():
    print("*********************************")
    print("***Bem vindo no jogo de Forca!***")
    print("*********************************")


# Podemos definir um parametro opcional, para isso indicamos o nome do parametro 'nome_arquivo' e em seguida
# atribuimos um valor padrão (="palavras.txt") que será usado caso o parametro não seja informado na chamada do metodo
# Note que da forma que implementamos, tanto o nome_arquivo e o primeira_linha_valida são parametros opcionais,
# que podem ser enviados juntos, somente um ou nenhum.
# Além disso, aqui usamos outro recuso que se chama parametros nomeados, que seja enviado os parametros na chamda
# do metodo em qualquer ordem.
def carrega_palavra_secreta(nome_arquivo="palavras.txt", primeira_linha_valida=1):
    arquivo = open(nome_arquivo, "r")
    lista_palavras = []

    for linha in arquivo:
        linha = linha.strip().upper()
        lista_palavras.append(linha)

    arquivo.close()

    numero = random.randrange(primeira_linha_valida, len(lista_palavras))
    palavra_secreta = lista_palavras[numero]
    return palavra_secreta


def inicializa_letras_acertadas(palavra: str):
    # List Comprehensions
    # Para cada letra da palavra, gera uma sequencia de '_'
    letras_acertadas = ["_" for letra in palavra]
    return letras_acertadas


def pede_chute():
    chute = input("Qual a letra?")
    chute = chute.strip().upper()
    return chute


def marca_chute_correto(chute: str, letras_acertadas: list[str], palavra_secreta: str):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if (__name__ == "__main__"):
    jogar()