
class Restaurante:
    restaurantes = []

    # Self é a referencia da instancia atual que esta sendo invocada
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    # metodo __str__ retorna a representação textual do objeto
    def __str__(self):
        return f'Nome: {self._nome} | Categoria: {self._categoria} | Ativo: {self._ativo}'  

    def listar_restaurantes():
        print(f'{"Nome do restaurante".ljust(24)} | {"Categoria".ljust(25)} | {"Status"}')
        [print(f'{restaurante._nome.ljust(25)}| {restaurante._categoria.ljust(25)} | {restaurante._ativo}') for restaurante in Restaurante.restaurantes]

    @property
    def ativo(self):
           return '☒' if self._ativo else '☐'


restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_pizza = Restaurante('pizza Express', 'Italiana')

restaurante_pizza.nome = 'Pizza 21'

Restaurante.listar_restaurantes()

#print(dir(restaurantes))
#print(vars(restaurante_praca))
#print(vars(restaurante_pizza))
