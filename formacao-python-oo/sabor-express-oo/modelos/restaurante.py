
class Restaurante:
    # Self é a referencia da instancia atual que esta sendo invocada
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

    # metodo __str__ retorna a representação textual do objeto
    def __str__(self):
        return f'Nome: {self.nome} | Categoria: {self.categoria} | Ativo: {self.ativo}'    


restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

restaurantes = [restaurante_praca, restaurante_pizza]

#print(dir(restaurantes))
#print(vars(restaurante_praca))
#print(vars(restaurante_pizza))

print(restaurante_praca)
print(restaurante_pizza)