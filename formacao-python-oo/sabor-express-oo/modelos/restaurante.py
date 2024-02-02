
class Restaurante:
    restaurantes = []

    # Self é a referencia da instancia atual que esta sendo invocada
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self._ativo = False
        Restaurante.restaurantes.append(self)

    # metodo __str__ retorna a representação textual do objeto
    def __str__(self):
        return f'Nome: {self.nome} | Categoria: {self.categoria} | Ativo: {self.ativo}'  

    def listar_restaurantes():
        print(f'{"Nome do restaurante".ljust(24)} | {"Categoria".ljust(25)} | {"Status"}')
        [print(f'{restaurante.nome.ljust(25)}| {restaurante.categoria.ljust(25)} | {restaurante.ativo}') for restaurante in Restaurante.restaurantes]

    @property
    def ativo(self):
           return '☒' if self._ativo else '☐'


restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

Restaurante.listar_restaurantes()

#print(dir(restaurantes))
#print(vars(restaurante_praca))
#print(vars(restaurante_pizza))
