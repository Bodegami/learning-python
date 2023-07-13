from codigo.bytebank import Funcionario

lucas = Funcionario(nome='Lucas Carvalho', data_nascimento='13/03/2000', salario=1000)

print(lucas.idade())

def teste_idade():
    funcionario_teste = Funcionario('Teste', '13/03/2000', 1111)

    print(f'Teste = {funcionario_teste.idade()}')

teste_idade()
