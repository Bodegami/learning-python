
# url = "http://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
url = "https://bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real"
print(url)
url = "     1   a    "

# Sanitização da URL
url = url.replace(" ", "")
# Podemos usar o url.strip´() para remover espacos em brancos e caracteres especiais

# Validação da URL
if url == "":
    raise ValueError("A URL está vazia!")

# Separa a base e os parametros
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

# Busca o valor de um parametro
parametro_busca = 'quantidade'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]

print(valor)




