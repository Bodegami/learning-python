import array as arr
import numpy as np # lib comum para calculos matematicos


array = arr.array('d', [1, 3.5])

print(array)

# Evitamos usar array puro. Se precisamos de trabalho númerico, é costume usar o numpy

numeros = np.array([1., 3.5])
print(numeros)


print(numeros.sum())




