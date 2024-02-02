from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_pizza = Restaurante('japa Express', 'Japonesa')
restaurante_mexicano = Restaurante('Mexican food', 'Mexicana')
restaurante_mexicano.alternar_estado()

#print(dir(restaurantes))
#print(vars(restaurante_praca))
#print(vars(restaurante_pizza))


def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()