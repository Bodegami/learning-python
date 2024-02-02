from modelos.cardapio.item_cardapio import Item_cardapio

class Bebida(Item_cardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self._tamanho = tamanho

    def __str__(self) -> str:
        return self._nome   