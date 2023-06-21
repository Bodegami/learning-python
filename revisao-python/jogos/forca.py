import random


def jogar():

    imprime_msg_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual a letra?")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Você ganhou!!")
    else:
        print("Você perdeu!!")

    print("Fim do jogo!")


def imprime_msg_abertura():
    print("*********************************")
    print("***Bem vindo no jogo de Forca!***")
    print("*********************************")


def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    lista_palavras = []

    for linha in arquivo:
        linha = linha.strip().upper()
        lista_palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(lista_palavras))
    palavra_secreta = lista_palavras[numero]
    return palavra_secreta


def inicializa_letras_acertadas(palavra: str):
    # List Comprehensions
    # Para cada letra da palavra, gera uma sequencia de '_'
    letras_acertadas = ["_" for letra in palavra]
    return letras_acertadas

if (__name__ == "__main__"):
    jogar()