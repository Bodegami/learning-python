import numpy as np

colunas = np.arange(start=1,stop=6,step=1)
url = 'https://raw.githubusercontent.com/allanspadini/numpy/dados/citrus.csv'

dado = np.loadtxt(url, delimiter=',', usecols=colunas, skiprows=1)
print(dado)
print(dado.size)
print(dado.shape)