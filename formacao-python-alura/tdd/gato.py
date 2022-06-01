import random

class Gato:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def comer(self, comida):
        miado = ''
        if comida == 'racao':
            miado = 'gostosoo..'
        else:
            miado = 'eckkaaaa..'
        return miado

    def pular(self):
        return 'saiu pulando..'

    def correr(self):
        return 'saiu correndo..'

    def brincar(self):
        return 'saiu brincando..'

    def dormir(self):
        return 'saiu para dormir..'

    def aleatorio(self):
        atividades = [self.pular(), self.correr(), self.brincar(), self.dormir()]
        alt = random.randrange(0,1)
        return atividades[alt]


