url = 'https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real'
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

parametro_busca = 'moedaOrigem'
indice_parametro = url.find(parametro_busca)
tamanho_parametro = len(parametro_busca)
indice_valor = indice_parametro + tamanho_parametro + 1
valor = url[indice_valor:]
print(valor)

'''''
 Buscando os valores no path
 
    Primeiro eu crio uma variavel que recebe o nome do meu parametro como valor,
    Depois eu busca a posicao no meu parametro na url
    Depois eu pego o tamanho (size) do valor da minha variavel parametro_busca
    Depois crio uma variavel indice_valor que vai somar a posicao do meu parametro, 
    o tamanho da variavel busca e + 1 que representa o caractere '=' na minha url
    Crio uma variavel valor que vai pega o restante da variavel url a partir da minha
    variavel indice_valor 
    
'''''

