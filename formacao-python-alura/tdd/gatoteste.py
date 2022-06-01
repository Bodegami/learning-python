import unittest
from gato import Gato


class GatoTeste(unittest.TestCase):

    def teste_comer_fruta(self):
        comida_racao = 'racao'
        expected_fruta = 'gostosoo..'

        self.assertEqual(
            Gato.comer(True, comida_racao), expected_fruta)

    def teste_comer_algo_que_nao_seja_fruta(self):
        comida_fruta = 'fruta'
        expected_fruta = 'eckkaaaa..'

        self.assertEqual(
            Gato.comer(True, comida_fruta), expected_fruta)

    def teste_escolhe_uma_atividade_aleatoaria(self):
        gato = Gato('felix')
        expected_response = 'saiu pulando..'

        self.assertEqual(
            Gato.aleatorio(gato), expected_response)
        self.assertTrue(Gato.aleatorio(gato), expected_response)
