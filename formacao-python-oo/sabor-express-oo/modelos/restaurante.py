
class Restaurante:
    restaurantes = []

    # Self é a referencia da instancia atual que esta sendo invocada
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    # metodo __str__ retorna a representação textual do objeto
    def __str__(self):
        return f'Nome: {self.nome} | Categoria: {self.categoria} | Ativo: {self.ativo}'  

    def listar_restaurantes():
        [print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}') for restaurante in Restaurante.restaurantes]


restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

Restaurante.listar_restaurantes()

#print(dir(restaurantes))
#print(vars(restaurante_praca))
#print(vars(restaurante_pizza))
