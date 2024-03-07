

peso = float(input("Digite o peso, em quilogramas: "))
altura = float(input("Digite a altura, em metros: "))

imc = round(peso / pow(altura, 2), 2)

print(f"O IMC da pessoa é: {imc}")