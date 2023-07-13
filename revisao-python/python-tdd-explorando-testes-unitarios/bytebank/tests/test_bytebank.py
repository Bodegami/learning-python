import pytest

from codigo.bytebank import Funcionario

class TestClass:

    # Para o pytest reconhece esse metodo como um test, é preciso que a assinatura comece com test_
    def test_quando_idade_recebe_13_03_2000_deve_retornar_23(self):

        entrada = '13/03/2000' # given (contexto)
        esperado = 23
        funcionario_teste = Funcionario(nome='Teste', data_nascimento=entrada, salario=1111)

        resultado = funcionario_teste.idade() # when (ação)

        assert resultado == esperado # then (desfecho)

    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):

        entrada = ' Lucas Carvalho '
        esperado = 'Carvalho'
        funcionario_teste = Funcionario(nome=entrada, data_nascimento='13/03/2000', salario=1111)

        resultado = funcionario_teste.sobrenome()

        assert resultado == esperado

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):

        entrada_salario = 100000 # given
        entrada_nome = 'Paulo Bragança'
        esperado = 90000
        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)

        funcionario_teste.decrescimo_salario() # when
        resultado = funcionario_teste.salario

        assert resultado == esperado # then

    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):

        entrada_salario = 1000 # given
        esperado = 100
        funcionario_teste = Funcionario('teste', '11/11/2000', entrada_salario)

        resultado = funcionario_teste.calcular_bonus() # when

        assert resultado == esperado # then

    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_Exception(self):
        with pytest.raises(Exception):
            entrada_salario = 1000000  # given

            funcionario_teste = Funcionario('teste', '11/11/2000', entrada_salario)
            resultado = funcionario_teste.calcular_bonus()  # when

            assert resultado # then


