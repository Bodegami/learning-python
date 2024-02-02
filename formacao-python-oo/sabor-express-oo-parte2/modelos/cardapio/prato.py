from modelos.cardapio.item_cardapio import Item_cardapio

class Prato(Item_cardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self._descricao = descricao

    def __str__(self) -> str:
        return self._nome       