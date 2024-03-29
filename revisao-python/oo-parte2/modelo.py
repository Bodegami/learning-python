
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


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)

    @property
    def listagem(self):
        return self._programas




vingadores = Filme("vingadores - guerra infinita", 2018, 160)
atlanta = Serie("atlanta", 2018, 2)
tmep = Filme("todo mundo em panico", 1999, 100)
demolidor = Serie("demolidor", 2016, 2)

vingadores.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
atlanta.dar_like()
atlanta.dar_like()

print(f'{vingadores.nome} - {vingadores.duracao}: {vingadores.likes}')
print(f'{atlanta.nome} - {atlanta.temporadas}: {atlanta.likes}')

atlanta.nome = 'atanda'
print(f'{vingadores.nome} - {vingadores.duracao}: {vingadores.likes}')
print("\n ===================================================\n")

print(str(1234123))

filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

for programa in playlist_fim_de_semana:
    print(programa)

print(f'Tamanho do playlist: {len(playlist_fim_de_semana)}')

print(f'Tá ou não tá? {demolidor in playlist_fim_de_semana}')

print(playlist_fim_de_semana[1])

print(len(playlist_fim_de_semana))
