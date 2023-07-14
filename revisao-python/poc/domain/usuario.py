

class Usuario:
    def __init__(self, nome, idade, documento, endereco):
        self._nome = nome
        self._idade = idade
        self._documento = documento
        self._endereco = endereco

    def __eq__(self, other):
        return self._documento == other._documento

    def __str__(self):
        return f'[Nome: {self._nome} | Idade: {self._idade} | Documento: {self._documento} | Endereco: {self._endereco}]'

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

    @property
    def documento(self):
        return self._documento

    @property
    def endereco(self):
        return self._endereco

