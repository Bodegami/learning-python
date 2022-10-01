from codigo.bytebank import Funcionario

#lucas = Funcionario('Lucas Carvalho', '13/03/2000', 1000)

#print(lucas.idade())


def teste_idade():
    functionario_teste = Funcionario('Teste', '13/03/2000', 1111)
    print(f'Teste = {functionario_teste.idade()}')

teste_idade()