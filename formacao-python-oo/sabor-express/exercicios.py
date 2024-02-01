import os

"""
Exercicios Capitulo 3

1 - Crie uma lista para cada informação a seguir:
Lista de números de 1 a 10;
Lista com quatro nomes;
Lista com o ano que você nasceu e o ano atual.

2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

"""

os.system('cls')

# 1 
print('\nDesafio 1\n')
lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_de_nomes = ['Renato', 'Paulo', 'Erika', 'Gustavo']
lista_de_anos = [1986, 2024]

#2
print('\nDesafio 2\n')
lista_de_nomes = ['Renato', 'Paulo', 'Erika', 'Gustavo']
[print(nome) for nome in lista_de_nomes]

#3
print('\nDesafio 3\n')
numero_total = 0
for numero in range(1, 11, 2): # O terceiro elemento do range garante que só seram considerados numeros impares
    numero_total += numero

print(numero_total)    
       
#4
print('\nDesafio 4\n')
[print(numero) for numero in sorted(lista_de_numeros, reverse=True)]

#5
print('\nDesafio 5\n')
numero_da_tabuada = int(input('Digite um numero: '))
if numero_da_tabuada:
    [print(f'{numero_da_tabuada} x {numero} = {numero_da_tabuada * numero}') for numero in range(1,11)]

#6
print('\nDesafio 6\n')   
lista_aleatoria = [None, 1, 2, 3, 4, "5", 6, 7, 8, 9, 10, None]
numero_final = 0
for numero in lista_aleatoria:
    try:
        numero_final += numero
    except:    
        pass
print(numero_final)

#7
print('\nDesafio 7\n')   
lista_random = [None, 1, 2, 3, 4, "5", 6, 7, 8, 9, 10, None]
numero_final = 0
numeros_validos = 0
numeros_invalidos = 0
for numero in lista_random:
    try:
        numero_final += numero
        numeros_validos += 1
    except:
        numeros_invalidos += 1    
        pass
print(f'Numero final: {numero_final}')    
print(f'Numeros validos: {numeros_validos}')    
print(f'Numeros invalidos: {numeros_invalidos}') 
print(f'A Média dos numeros é {round(numero_final / numeros_validos, 2)}')

