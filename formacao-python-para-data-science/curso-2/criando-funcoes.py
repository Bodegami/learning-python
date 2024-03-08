
def media():
    calculo = (10 + 9 + 8) / 3
    print(calculo)

media()

def media_1(nota_1, nota_2, nota_3):
    calculo = (nota_1 + nota_2 + nota_3) / 3
    print(calculo)

# parametros do lado esquerdo e argumentos do lado direito
media_1(nota_1= 3, nota_2= 6, nota_3= 9)

notas = [8.5, 9.0, 6.0, 10.0]
def media_2(lista: list):
    calculo = round(sum(lista) / len(lista), ndigits=1)
    print(calculo)

resultado = media_2(notas)

print(resultado)



