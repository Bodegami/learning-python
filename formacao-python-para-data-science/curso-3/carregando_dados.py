import numpy as np

# start, stop, increment
colunas = np.arange(1,88,1)

# carrega arquivo csv, com delimitador e definicao de colunas 
dado_arquivo = np.loadtxt('./numpy-dados/apples_ts.csv', delimiter=',', usecols=colunas)
print(dado_arquivo[0])

url = 'https://raw.githubusercontent.com/alura-cursos/numpy/dados/apples_ts.csv'

# carrega atabela de uma url, com delimitador e definicao de colunas 
dado_url = np.loadtxt(url, delimiter=',', usecols=colunas)
print(dado_url[0] == dado_arquivo[0])

dado = dado_url

# ndim retorna o numero de dimensoes, aqui no caso 2 (linhas e colunas)
print(dado.ndim)

# size retorna o numero de elementos do dado
print(dado.size)

# shape retorna o numero de elementos por dimensoes, aqui no caso 2 (linhas e colunas)
print(dado.shape)

# T (transposicao da matematica) faz a conversão de linha para colunas e vice-versa
print(dado.T)

dado_transposto = dado.T