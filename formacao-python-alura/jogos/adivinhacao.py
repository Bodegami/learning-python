print("****************************************")
print("  Bem vindo ao jogo de Adivinhação!!")
print("****************************************")

numero_secreto = 42 ## Variaveis tem o tipo dinamico (ele atribiu através da inferência)
chute_str = input("Digite o seu numero: ") ## A variavel do input recebe o valor digitado

tipo = type(chute_str) ## No python 3 o input devolve um tipo string
print("o tipo do input é:", tipo)

chute_int = int(chute_str)  ## Podemos fazer o parse através do metodo int()

# Poderiamos fazer assim também: chute = int(input("Digite o seu numero: "))

print("Você digitou: ", chute_str)

## Na linguagem python, para indicar que é um bloco de execucao usamos os :
## Além disso, uma caracteristica importante da linguagem é a endentação, que espera 4 espaços
if (numero_secreto == chute_int):
    print("Você acertou!!")
else:
    print("Você errou!")








