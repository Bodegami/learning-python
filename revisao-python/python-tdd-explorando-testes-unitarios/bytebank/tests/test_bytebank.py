from codigo.bytebank import Funcionario

class TestClass:

    # Para o pytest reconhece esse metodo como um test, é preciso que a assinatura comece com test_
    def test_quando_idade_recebe_13_03_2000_deve_retornar_23(self):

        entrada = '13/03/2000' # given (contexto)
        esperado = 23
        funcionario_teste = Funcionario(nome='Teste', data_nascimento=entrada, salario=1111)

        resultado = funcionario_teste.idade() # when (ação)

        assert resultado == esperado # then (desfecho)
