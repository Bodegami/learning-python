from codigo.bytebank import Funcionario


class TestClass:
    # GIVEN - WHEN - THEN

    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        entrada = '13/03/2000'  # Given-Contexto
        esperado = 22

        functionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = functionario_teste.idade()  # When-Ação

        assert resultado == esperado  # Then-Desfecho
