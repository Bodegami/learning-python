import os


def exibir_nome_do_programa():
    print("""

█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
""")

def exibir_opcoes():
   print('1. Cadastrar restaurante')
   print('2. Listar restaurante')
   print('3. Ativar restaurante')
   print('4. Sair\n')

def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção: '))
    # O Retorno da funcao input() sempre é do tipo str
    #opcao_escolhida = int(opcao_escolhida)

    print(f'Você escolheu a opção: {opcao_escolhida}')

#    if opcao_escolhida == 1:
#       print('Cadastrar restaurante')
#    elif opcao_escolhida == 2:
#       print('Listar restaurante')
#    elif opcao_escolhida == 3:
#       print('Ativar restaurante')
#    else:
#       finalizar_app() 

    match opcao_escolhida:
        case 1:
             print('Cadastrar restaurante')
        case 2:
             print('Listar restaurante')
        case 3:
             print('Ativar restaurante')                          
        case 4:
             finalizar_app()
        case _:
             print('Opção inválida!')             


def finalizar_app():
    os.system('cls')
    print('Finalizando o app!\n')   

    
def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
        

if __name__ == '__main__':
    main()