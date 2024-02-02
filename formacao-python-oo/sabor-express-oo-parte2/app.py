from modelos.restaurante import Restaurante
from modelos.restaurante import Avaliacao

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_pizza = Restaurante('japa Express', 'Japonesa')
restaurante_mexicano = Restaurante('Mexican food', 'Mexicana')
restaurante_mexicano.alternar_estado()

restaurante_praca.receber_avaliacao('Renato', 10)
restaurante_praca.receber_avaliacao('Lais', 8)
restaurante_praca.receber_avaliacao('Emy', 2)

print(restaurante_praca.media_avaliacoes)

#print(dir(restaurantes))
#print(vars(restaurante_praca))
#print(vars(restaurante_pizza))


def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()