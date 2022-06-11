from collections import Counter

texto1 = """
Java é uma das tecnologias de back-end mais poderosas, que tem a segunda classificação, de acordo com o Índice TIOBE 2021. James Gosling desenvolveu essa tecnologia de programação originalmente em 1991, mas foi publicada em 1995 pela Sun Microsystems.
Os desenvolvedores preferem fazer aplicativos da web adaptáveis e ricos em recursos com Java há anos. No entanto, você pode usar o Java para dispositivos móveis, graves e desenvolvimento de software de microcontrolador também.
Simples e altamente escalonável: Java EE é altamente escalável porque permite várias instâncias para solicitações de servidor. A disponibilidade instantânea de componentes Java e tecnologia de sintaxe inequívoca também torna simples para os desenvolvedores usar essa linguagem de back-end.
Multi-Threading: Java permite tratar todas as solicitações em threads independentes devido a um servidor web multi-threaded. Com esse recurso de multithreading, o Java funciona muito bem para aplicativos com uso intensivo de CPU.
Bibliotecas de código aberto: uma variedade de bibliotecas de código aberto, como análise JSON, mensagens, PDF, teste de unidade e bibliotecas do Excel disponíveis para Java. Os desenvolvedores Java podem usar esses recursos para agilizar suas tarefas do lado do servidor.
Segurança: Java oferece recursos incríveis para superar os riscos de segurança. Da mesma forma, as Java Virtual Machines examinam os bytecodes java para detectar e reduzir o risco de vírus. Da mesma forma, o modelo de segurança do Java e o teste de códigos reutilizáveis ajudam os desenvolvedores a evitar ameaças à segurança.
"""

texto2 = """
O conceito de Arquitetura Hexagonal foi proposto por Alistair Cockburn, em meados dos anos 90, em um artigo postado na primeira wiki que foi desenvolvida, chamada WikiWikiWeb (cujos artigos tratavam principalmente de temas relacionados com Engenharia de Software).
Os objetivos de uma Arquitetura Hexagonal são parecidos com os de uma Arquitetura Limpa, tal como descrevemos em um outro artigo. Mas, para reforçar, a ideia é construir sistemas que favorecem reusabilidade de código, alta coesão, baixo acoplamento, independência de tecnologia e que são mais fáceis de serem testados.
Uma Arquitetura Hexagonal divide as classes de um sistema em dois grupos principais:
Classes de domínio, isto é, diretamente relacionadas com o negócio do sistema.
Classes relacionadas com infraestrutura, tecnologias e responsáveis pela integração com sistemas externos (tais como bancos de dados).
Além disso, em uma Arquitetura Hexagonal, classes de domínio não devem depender de classes relacionadas com infraestrutura, tecnologias ou sistemas externos. A vantagem dessa divisão é desacoplar esses dois tipos de classes.
Assim, as classes de domínio não conhecem as tecnologias – bancos de dados, interfaces com usuário e quaisquer outras bibliotecas – usadas pelo sistema. Consequentemente, mudanças de tecnologia podem ser feitas sem impactar as classes de domínio. Talvez ainda mais importante, as classes de domínio podem ser compartilhadas por mais de uma tecnologia. Por exemplo, um sistema pode ter diversas interfaces (Web, mobile, etc).
Em uma arquitetura hexagonal, a comunicação entre as classes dos dois grupos é mediada por adaptadores, isto é, por classes que implementam o padrão de projeto de mesmo nome que estudamos no Capítulo 6. Iremos explicar melhor o papel dos adaptadores logo a seguir.
Visualmente, a arquitetura é representada por meio de dois hexágonos concêntricos (veja figura). No hexágono interno, ficam as classes do domínio (ou classes de negócio, se você preferir). No hexágono externo, ficam os adaptadores. Por fim, as classes de interface com o usuário, classes de tecnologia ou de sistemas externos ficam fora desses dois hexágonos.
"""

texto1_minusculo = texto1.lower()
print("Texto minusculo: \n", texto1_minusculo)

texto1_separado = texto1_minusculo.split()
print("\nTexto transformado em lista de palavras:\n", texto1_separado)

aparicoes = Counter(texto1_minusculo)
print("\nNumero de aparicoes de cada letra do texto:\n", aparicoes)

total_de_caracteres = sum(aparicoes.values())
print(f'\nTotal de caracteres: {total_de_caracteres}\n')

print(f'\nPercentil de aparicoes de cada letra:\n')
for letra, frequencia in aparicoes.items():
    tupla = (letra, (frequencia / total_de_caracteres) * 100)
    print(tupla)


proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
proporcoes = Counter(dict(proporcoes))
print(proporcoes)

print('\nImprimindo as 10 letras mais comuns do texto1:\n', proporcoes.most_common(10))

# Com base nas experimentacoes acima ja podemos criar a nossa funcao

print("\nCriando a nossa funcao de analisa de frequencia de letras de um texto:\n")
print("\nAnalisando o texto 1 em % de aparicoes\n")


def analisa_frequencia_de_letras(texto):
    aparicoes_texto = Counter(texto.lower())
    total_de_caracteres_texto = sum(aparicoes_texto.values())

    proporcoes_texto = [(letra, frequencia / total_de_caracteres_texto) for letra, frequencia in aparicoes_texto.items()]
    proporcoes_texto = Counter(dict(proporcoes_texto))
    mais_comuns = proporcoes_texto.most_common(10)
    for caracter, proporcao in mais_comuns:
        print(f'{caracter} => {round(proporcao * 100, 2)}%')


analisa_frequencia_de_letras(texto1)

print("\nAnalisando o texto 2 em % de aparicoes\n")
analisa_frequencia_de_letras(texto2)
