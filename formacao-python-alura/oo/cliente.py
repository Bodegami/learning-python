class Cliente:

    def __init__(self, nome):
        self.__nome = nome


    # def get_nome(self):
    #     return self.nome.title()

    ## O title() transforma a primeira letra da string em maiscula
    @property
    def nome(self):
        print("Chamando @property nome()")
        return self.__nome.title()

    @nome.setter
    def nome(self, novo_nome):
        print("Chamando setter nome()")
        self.__nome = novo_nome