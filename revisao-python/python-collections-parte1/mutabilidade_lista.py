# Problemas com a mutabilidade da lista

# def faz_processamento_de_visualizacao(lista = []):
#     print(len(lista))
#     print(lista)
#     lista.append(13)
#
#
# idades = [16, 21, 29, 56, 43]
# faz_processamento_de_visualizacao()
# faz_processamento_de_visualizacao()
# faz_processamento_de_visualizacao()
# faz_processamento_de_visualizacao()



def faz_processamento_de_visualizacao(lista=None):
    if lista == None:
        lista = list()
    print(len(lista))
    print(lista)
    lista.append(13)


idades = [16, 21, 29, 56, 43]
faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()

print(idades)


print(idades)
