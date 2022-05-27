## SOBRE CLASSES ABSTRATAS

from abc import ABC # abstract base classes

from collections.abc import MutableSequence
# from numbers import Complex
#
# class Numero(Complex):
#     def __getitem__(self, item):
#         super().__getitem__()
#
# filmes = Numero()
#


# from collections.abc import Sized
#
# class MinhaListagem(Sized):
#     def __init__(self, descricao):
#         self.descricao = descricao
#
#     def __str__(self):
#         return self.descricao
#
# lista = MinhaListagem()
# print(lista)


from abc import ABCMeta, abstractmethod
class Programa(metaclass = ABCMeta):
    @abstractmethod
    def __str__(self):
        pass