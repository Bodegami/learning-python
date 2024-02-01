import os

restaurantes = [{'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False},
                {'nome': 'Pizza', 'categoria': 'Pizza', 'ativo': True},
                {'nome': 'Cantina', 'categoria': 'Italiana', 'ativo': False}]

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
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_do_restaurante = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')

    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria_do_restaurante, 'ativo': False}

    restaurantes.append(dados_do_restaurante)   
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes:')
    for restaurante in restaurantes:
        print(f'- {restaurante["nome"]} | {restaurante["categoria"]} | {restaurante["ativo"]}')            
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('Alternando o estado do restaurante:')   

    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)

    if not restaurante_encontrado:
        print(f'O restaurante {nome_restaurante} não foi encontrado!')        


    voltar_ao_menu_principal()

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
                alternar_estado_restaurante()                        
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()                 

def finalizar_app():
    exibir_subtitulo('Finalizando o app!') 

def voltar_ao_menu_principal():
    input('Digite um tecla para voltar ao menu principal ')
    main()

def exibir_subtitulo(texto: str):
    os.system('cls')
    print(f'{texto}\n')        

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
        

if __name__ == '__main__':
    main()