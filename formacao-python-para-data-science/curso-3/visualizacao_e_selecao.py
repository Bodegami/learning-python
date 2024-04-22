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

plt.plot(datas, precos[:,0])


Moscow = precos[:,0]
Kaliningrad = precos[:,1]
Petersburg = precos[:,2]
Krasnodar = precos[:,3]
Ekaterinburg = precos[:,4]