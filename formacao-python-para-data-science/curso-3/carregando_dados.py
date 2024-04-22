import numpy as np

# start, stop, increment
colunas = np.arange(1,88,1)

# carrega arquivo csv, com delimitador e definicao de colunas 
tabela_arquivo = np.loadtxt('./numpy-dados/apples_ts.csv', delimiter=',', usecols=colunas)
print(tabela_arquivo[0])

url = 'https://raw.githubusercontent.com/alura-cursos/numpy/dados/apples_ts.csv'

# carrega atabela de uma url, com delimitador e definicao de colunas 
tabela_url = np.loadtxt(url, delimiter=',', usecols=colunas)
print(tabela_url[0] == tabela_arquivo[0])

