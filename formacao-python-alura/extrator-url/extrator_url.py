import re


class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia!")

        padrao_url = re.compile("(http(s)?://)?(www.)?(bytebank.com)(.br)?(/cambio)")
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError("A URL não é valida!!!")

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[0:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    # Note que é possivel chamar um metodo da classe e depois fazer o fatiamento da String
    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + "\n" + "Parâmetros: " + self.get_url_parametros() + "\n" + "URL Base: " + self.get_url_base()

    def __eq__(self, other):
        return self.url == other.url


url = 'https://bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real'
extrator_url = ExtratorURL(url)
extrator_url2 = ExtratorURL(url)
print("O tamanho da URL: ", len(extrator_url))
print(extrator_url)

valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(valor_quantidade)

print(extrator_url == extrator_url2) # extrator_url.__eq__(extrator_url2)

# implementacao padrao do __eq__() utiliza o id()
print(id(extrator_url))
print(id(extrator_url2))
print(extrator_url is extrator_url2)

print("=====================|| Igualdade e Identidade||=========================")
# A metodo de comparacao utilizando o id() por de baixo dos panos, funciona muito bem p/ strings
# mas para objetos já não funciona como esperado, pq dentro da linguagem Python, dois objetos
# podem ser iguais, mas não idênticos

string_teste = "Banana"
string_teste2 = "Banana"
print(id(string_teste))
print(id(string_teste2))

print(string_teste is string_teste2)

print("=====================||Desafio conversor dolar||=========================")

VALOR_DOLAR = 5.50  # 1 dólar = 5.50 reais
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
quantidade = extrator_url.get_valor_parametro("quantidade")

if moeda_origem == "real" and moeda_destino == "dolar":
    valor_conversao = int(quantidade) / VALOR_DOLAR
    print("O valor de R$" + quantidade + " reais é igual a $" + str(valor_conversao) + " dólares.")
elif moeda_origem == "dolar" and moeda_destino == "real":
    valor_conversao = int(quantidade) * VALOR_DOLAR
    print("O valor de $" + quantidade + " dólares é igual a R$" + str(valor_conversao) + " reais.")
else:
    print(f"Câmbio de {moeda_origem} para {moeda_destino} não está disponível.")

