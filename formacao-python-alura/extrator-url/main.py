from extrator_url import ExtratorURL

## url = 'https://bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real'
# url = 'https://bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar'
url = "    a      "
print(url)

# Sanitização da URL
# replace() = o primeiro paramento é o que queremos remover e o segundo é o que queremos adicionar no lugar
# url = url.replace(" ", "")

# strip() = remove todos os espaços em brancos no inicio e no fim da string, remove caracteres especiais e etc
# url = url.strip()

# lstrip() = remove todos os espaços em branco a esquerda
#url = url.lstrip()

# rstrip() = remove todos os espaços em branco a direita
#url = url.rstrip()


url = url.strip()

# Validação da URL
if url == "":
    raise ValueError("A URL está vazia")

## O fatiamento tem uma propriedade interessante que é omitir o parametro
## quando usado no inicio, ele pega o ponto inicial da string
## quando usado no final, ele pega do ponto inicial até o final da variavel url

# Separa a base e os parâmetros
# Primeira solução estática
indice_interrogacao = url.find('?')
url_base = url[0:indice_interrogacao]
print(url_base)
url_parametros = url[indice_interrogacao + 1:]
print(url_parametros)

print("====================||Separa a base e os parâmetros||======================")

'''''
 Buscando os valores de moedaOrigem no path

    Primeiro eu crio uma variavel que recebe o nome do meu parametro como valor,
    Depois eu busca a posicao no meu parametro na url
    Depois eu pego o tamanho (size) do valor da minha variavel parametro_busca
    Depois crio uma variavel indice_valor que vai somar a posicao do meu parametro, 
    o tamanho da variavel busca e + 1 que representa o caractere '=' na minha url
    Crio uma variavel valor que vai pega o restante da variavel url a partir da minha
    variavel indice_valor 

'''''

parametro_busca = 'moedaOrigem'
indice_parametro = url.find(parametro_busca)
tamanho_parametro = len(parametro_busca)
indice_valor = indice_parametro + tamanho_parametro + 1
valor = url[indice_valor:]
print(valor)

print("====================||Busca o valor de um parâmetro||======================")
# Busca o valor de um parâmetro

# Adaptando a lógica para pegar o valor de qualquer parametro

parametro_busca = 'quantidade'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]
print(valor)

print("====================||Sobre o tipo especial NONE||======================")

print(type(None))
extrator = ExtratorURL("")
