url = 'https://bytebank.com/cambio?moedaOrigem=real'
print(url)

## O fatiamento tem uma propriedade interessante que é omitir o parametro
## quando usado no inicio, ele pega o ponto inicial da string
## quando usado no final, ele pega do ponto inicial até o final da variavel url

# O metodo find busca um elemento dentro da string
indice_interrogacao = url.find('?')


url_base = url[0:indice_interrogacao]
print(url_base)

url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

print(url)

