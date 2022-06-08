# Evitaremos usar array puro. Se precisamos de trabalho numérico, é costume usar o numpy

import array as arr

import numpy as np

'''''
Sobre os tipos suportados, olhe na documentacao: 
https://docs.python.org/3/library/array.html

'''''

# Exemplo de array nativo do Python
array_nativo = arr.array('d', [1, 3.5])
print(array_nativo)

# Numpy é a lib mais comum utilizada para array. Ao contario do array nativo, a numpy é
# muito mais performatica para arrays de numeros inteiros ou para calculos complexos

numeros = np.array([1, 3.5])
print(numeros)

# Exemplo de alguns metodos unicos da numpy
print(numeros + 3)