
def media(lista: list=[0]) -> float:
    ''' 
        Função para calcular a média de notas passadas por uma lista

        lista: list, default[0]
        Lista com as notas para calcular a média
        return calculo: float
        Média calculada
    '''

    calculo = sum(lista) / len(lista)

    if len(lista) > 4:
        raise ValueError("A lista não pode possuir mais de 4 notas.")
        
    return calculo

print("\nTestando Try-Catch lançando o TypeError: ")

notas = [5.9, 6.7, 8.2, 5.1, "7"]
try:
    resultado = media(notas)
except TypeError as te: # o TypeError é lançado antes do ValueError, pq o erro ocorre quando a função tenta executar o calculo
    print("Não foi possível calcular a média do(a) estudante. Só são aceitos valores númericos!")    
except ValueError as ve:
    print(ve)
else:
    print(resultado)    
finally:
    print("A consulta foi encerrada!")


print("\nTestando Try-Catch lançando o ValueError: ")

notas = [5.9, 6.7, 8.2, 5.1, 7]
try:
    resultado = media(notas)
except TypeError as te: # o TypeError é lançado antes do ValueError, pq o erro ocorre quando a função tenta executar o calculo
    print("Não foi possível calcular a média do(a) estudante. Só são aceitos valores númericos!")    
except ValueError as ve:
    print(ve)
else:
    print(resultado)    
finally:
    print("A consulta foi encerrada!")    
