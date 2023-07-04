
# url = "http://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
url = "https://bytebank.com/cambio?moedaOrigem=real"

print(url)

indice_interrogacao = url.find('?')
# Omitindo o primeito elemento, o python entende que deve pegar do inicio da String
url_base = url[:indice_interrogacao]
print(url_base)

# Omitindo o segundo elemento, o python entende que deve pegar os elementos ate o final da String
url_parametros = url[indice_interrogacao+1:]
print(url_parametros)