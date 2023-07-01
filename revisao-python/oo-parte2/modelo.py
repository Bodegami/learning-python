
# __likes == modificador de acesso private
# _likes == modificador de acesso protected
# likes = modificador de acesso public
# super().__init__(nome, ano) === chama o construtor da classe mae

# Exemplo de if ternario utilizando o hasattr (funciona como o contains do Java, passando o objeto e atributo):
# detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas

class Programa:
    def __init__(self, nome: str, ano: int):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f'Nome: {self._nome} - Ano: {self.ano} - {self._likes} likes'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __self__(self):
        return f'Nome: {self._nome} - Ano: {self.ano} - Duração: {self.duracao} min - {self._likes} likes'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self._nome} - Ano: {self.ano} - Temporadas: {self.temporadas} temporadas - {self._likes} likes'


vingadores = Filme("vingadores - guerra infinita", 2018, 160)
vingadores.dar_like()
print(f'{vingadores.nome} - {vingadores.duracao}: {vingadores.likes}')

atlanta = Serie("atlanta", 2018, 2)
atlanta.dar_like()
atlanta.dar_like()
print(f'{atlanta.nome} - {atlanta.temporadas}: {atlanta.likes}')

atlanta.nome = 'atanda'
print(f'{vingadores.nome} - {vingadores.duracao}: {vingadores.likes}')
print("\n ===================================================\n")

filmes_e_series = [vingadores, atlanta]

for programa in filmes_e_series:
    print(programa)

print(str(1234123))
