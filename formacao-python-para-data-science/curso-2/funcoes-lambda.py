
# Comparando uma função de qualitativo no formato de função para função anônima 
nota = float(input("Digite a nota do(a) estudante: "))

def qualitativo(x):
    return x + 0.5
    
print(f"Usando uma funcao customizada: {qualitativo(nota)}")

qualitativo_2 = lambda x: x + 0.5

print(f"Usando uma funcao lambda: {qualitativo_2(nota)}")


# Recebendo as notas e calculando a média ponderável
N1 = float(input("Digite a 1ª nota do(a) estudante: "))
N2 = float(input("Digite a 2ª nota do(a) estudante: "))
N3 = float(input("Digite a 3ª nota do(a) estudante: "))

media_ponderada = lambda x, y, z: (x * 3 + y * 2 + z * 5) / 10
media_estudante = media_ponderada(N1, N2, N3)

print(media_estudante)
print(f'O(a) estudante atingiu uma média de {media_estudante}.')


# Notas do(a) estudante
notas = [6.0, 7.0, 9.0, 5.5, 8.0]
print(notas)
qualitativo = 0.5
print(qualitativo)

# notas_atualizadas = lambda x: x + qualitativo
notas_atualizadas = map(lambda x: x + qualitativo, notas)
notas_atualizadas = list(notas_atualizadas)

print(notas_atualizadas)
