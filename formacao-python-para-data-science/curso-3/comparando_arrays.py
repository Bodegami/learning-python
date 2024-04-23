import numpy as np
import matplotlib.pyplot as plt

colunas = np.arange(1,88,1)

dado = np.loadtxt('./numpy-dados/apples_ts.csv', delimiter=',', usecols=colunas)

dado_transposto = dado.T
print(dado_transposto)

# [:] pega todas as linhas 
# [:,0] pega os elementos de todas as linhas da coluna 0
datas = dado_transposto[:,0]
print(datas)

# [:,0] pega os elementos de todas as linhas da coluna 1 até o 5
precos = dado_transposto[:,1:6]
print(precos)

datas = np.arange(1,88,1)

Moscow = precos[:,0]
Kaliningrad = precos[:,1]
Petersburg = precos[:,2]
Krasnodar = precos[:,3]
Ekaterinburg = precos[:,4]

print(Moscow.shape)

# fatiando os preços de Moscow por ano
Moscow_ano1 = Moscow[0:12] 
Moscow_ano2 = Moscow[12:24]
Moscow_ano3 = Moscow[24:36]
Moscow_ano4 = Moscow[36:48]

# criando um grafico com os 4 anos e adicionando uma legenda
plt.plot(np.arange(1, 13, 1), Moscow_ano1)
plt.plot(np.arange(1, 13, 1), Moscow_ano2)
plt.plot(np.arange(1, 13, 1), Moscow_ano3)
plt.plot(np.arange(1, 13, 1), Moscow_ano4)
plt.legend(['ano1', 'ano2', 'ano3', 'ano4'])

# comparando se um array é igual ao outro
print(np.array_equal(Moscow_ano3, Moscow_ano4))

# allclose recebe 2 arrays e um float que é a margem de variação para comparação dos arrays
print(np.allclose(Moscow_ano3, Moscow_ano4, 1.0))