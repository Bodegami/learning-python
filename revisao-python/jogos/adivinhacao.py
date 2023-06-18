print("*********************************")
print("Bem vindo no jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

#O input alem de imprimir a frase, também recebe a entrada
#O porem ele sempre recebe a entrada como String
chute_str = input("Digite o seu numero: ")

print("Você digitou ", chute_str)

chute = int(chute_str)

if(numero_secreto == chute):
    print("Você acertou!")
else:
    print("Você errou!")

print("Fim do jogo!")