import os

print("""

█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
        """)

print('1. Cadastrar restaurante')
print('2. Listar restaurante')
print('3. Ativar restaurante')
print('4. Sair\n')

opcao_escolhida = int(input('Escolha uma opção: '))
# O Retorno da funcao input() sempre é do tipo str
#opcao_escolhida = int(opcao_escolhida)

print(f'Você escolheu a opção: {opcao_escolhida}')

def finalizar_app():
    os.system('cls')
    print('Finalizando o app!\n')



if opcao_escolhida == 1:
    print('Cadastrar restaurante')
elif opcao_escolhida == 2:
    print('Listar restaurante')
elif opcao_escolhida == 3:
    print('Ativar restaurante')
else:
    finalizar_app()           