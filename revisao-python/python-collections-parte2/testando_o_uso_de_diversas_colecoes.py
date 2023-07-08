from collections import Counter

texto1 = """
Ao contrário da crença popular, o Lorem Ipsum não é simplesmente texto aleatório. Tem raízes numa peça de literatura clássica em Latim, de 45 AC, tornando-o com mais de 2000 anos. Richard McClintock, um professor de Latim no Colégio Hampden-Sydney, na Virgínia, procurou uma das palavras em Latim mais obscuras (consectetur) numa passagem Lorem Ipsum, e atravessando as cidades do mundo na literatura clássica, descobriu a sua origem. Lorem Ipsum vem das secções 1.10.32 e 1.10.33 do "de Finibus Bonorum et Malorum" (Os Extremos do Bem e do Mal), por Cícero, escrito a 45AC. Este livro é um tratado na teoria da ética, muito popular durante a Renascença. A primeira linha de Lorem Ipsum, "Lorem ipsum dolor sit amet..." aparece de uma linha na secção 1.10.32.

O pedaço mais habitual do Lorem Ipsum usado desde os anos 1500 é reproduzido abaixo para os interessados. As secções 1.10.32 e 1.10.33 do "de Finibus Bonorum et Malorum" do Cícero também estão reproduzidos na sua forma original, acompanhados pela sua tradução em Inglês, versões da tradução de 1914 por H. Rackham.
"""

texto2 = """
Existem muitas variações das passagens do Lorem Ipsum disponíveis, mas a maior parte sofreu alterações de alguma forma, pela injecção de humor, ou de palavras aleatórias que nem sequer parecem suficientemente credíveis. Se vai usar uma passagem do Lorem Ipsum, deve ter a certeza que não contém nada de embaraçoso escondido no meio do texto. Todos os geradores de Lorem Ipsum na Internet acabam por repetir porções de texto pré-definido, como necessário, fazendo com que este seja o primeiro verdadeiro gerador na Internet. Usa um dicionário de 200 palavras em Latim, combinado com uma dúzia de modelos de frases, para gerar Lorem Ipsum que pareçam razoáveis. Desta forma, o Lorem Ipsum gerado é sempre livre de repetição, ou de injecção humorística, etc.
"""

# Passando uma String que é iteravel no construtor do Counter, ele nos retorna o dicionario com a quantidade de repeticoes de cada caractere
aparicoes = Counter(texto1)
print(aparicoes)

# Podemos fazer a soma do total de caracteres chamando o metodo sum()
total_de_caracteres = sum(aparicoes.values())
print(total_de_caracteres)

# Podemos inclusive calcular a porcentagem de aparicoes de uma letra, divindo a frequencia pelo total de caracteres
for letra, frequencia in aparicoes.items():
    tupla = (letra, (frequencia / total_de_caracteres) * 100)
    print(tupla)

proporcoes = [(letra, (frequencia / total_de_caracteres) * 100) for letra in aparicoes.items()]

# Com o Counter, podemos chamar o metodo most_common() passando como parametro o numero de elementos que deve ser retornado
# e contador vai retornar um dicionario ordenado pelo valor
proporcoes = Counter(dict(proporcoes))
print(proporcoes.most_common(10))


def analisa_frquecia_de_letras(texto: str):
    aparicoes = Counter(texto.lower())
    total_de_caracteres = sum(aparicoes.values())
    proporcoes = [(letra, (frequencia / total_de_caracteres)) for letra, frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))
    mais_comuns = proporcoes.most_common(10)
    for caractere, proporcao in mais_comuns:
        print("{} => {:.2f}%".format(caractere, proporcao * 100))


print("======================================")

print(analisa_frquecia_de_letras(texto1))

print(analisa_frquecia_de_letras(texto2))

# Curiosamente, a frequencia de aparicoes de um caractere independente do texto, é muita parecida com qualquer outro
# texto da mesma lingua. Por exemplo, em portugues a frequencia de aparicoes de espaços em branco e vogais são bem
# proximas de um texto para outro.
