from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    # Self é a referencia da instancia atual que esta sendo invocada
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    # metodo __str__ retorna a representação textual do objeto
    def __str__(self):
        return f'Nome: {self._nome} | Categoria: {self._categoria} | Ativo: {self._ativo}'  

    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Nome do restaurante".ljust(24)} | {"Categoria".ljust(25)} | {"Avaliacao".ljust(25)} | {"Status"}')
        [print(f'{restaurante._nome.ljust(25)}| {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}') for restaurante in cls.restaurantes]

    @property
    def ativo(self):
        return '☒' if self._ativo else '☐'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)  

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return "-"
        
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)

        return media   