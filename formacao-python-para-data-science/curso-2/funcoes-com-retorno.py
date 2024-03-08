
notas = [6.0, 7.0, 9.0, 5.0]
print(notas)

def boletim(lista: list):
    media = round(sum(lista) / len(lista), ndigits=2)
    #return "Aprovado(a)" if media >= 6 else "Reprovado(a)"

    if media >= 6:
        situacao = "Aprovado(a)"
    else:
        situacao = "Reprovado(a)"

    return (media, situacao)    

print(boletim(notas))

nota_media, situacao = boletim(notas)

print(f'O(a) estudante atingiu uma média de {nota_media} e foi {situacao}.')