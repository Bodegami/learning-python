import os

restaurantes = ['Pizza', 'Sushi']

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

def opcao_invalida():
    print('Opção Inválida!')
    input('Digite um tecla para voltar ao menu principal')
    main()

def cadastrar_novo_restaurante():
    os.system('cls')
    print('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)   
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    input('Digite um tecla para voltar ao menu principal')
    main()

def listar_restaurantes():
    os.system('cls')
    print('Listando os restaurantes:\n')
    
    for restaurante in restaurantes:
        print(f'.{restaurante}')            

    input('\nDigite um tecla para voltar ao menu principal')
    main()
        

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # O Retorno da funcao input() sempre é do tipo str
        #opcao_escolhida = int(opcao_escolhida)

        print(f'Você escolheu a opção: {opcao_escolhida}')
        #    print(1 < opcao_escolhida <= 3) -> opcao escolhida 2

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
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                print('Ativar restaurante')                          
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()                 


def finalizar_app():
    os.system('cls')
    print('Finalizando o app!\n')   

    
def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
        

if __name__ == '__main__':
    main()