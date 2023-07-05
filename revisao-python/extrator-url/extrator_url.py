import re


class ExtratorURL:
    def __init__(self, url: str):
        self.url = self.__sanitiza_url(url)
        self.__valida_url()

    def __len__(self):
        return len(self.url)

    def __str__(self) -> str:
        return self.url + "\nParâmetros: " + self.get_url_parametros() + "\nURL Base: " + self.get_url_base()

    def __eq__(self, other):
        return self.url == other.url

    def __sanitiza_url(self, url: str):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    # if not self.url ou if self.url == "" , internamente chamam o bool para executar essa comparacao
    def __valida_url(self):
        if not self.url:  # if not self.url ou if self.url == ""
            raise ValueError("A URL está vazia!")

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)

        if not match:
            raise ValueError("A URL não é válida!")

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor


url = "https://bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real"
extrator_url = ExtratorURL(url)
print("O tamanho da URL: ", len(extrator_url)) # implementando o metodo __len__()

valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(valor_quantidade)

print("Quais os metodos/atributos da classe: ", dir(extrator_url))
print("Quantos métodos/atributos tem a classe: ", len(dir(extrator_url)))

print(extrator_url) # Implementando o metodo __str__()

extrator_url2 = ExtratorURL(url)
print(extrator_url == extrator_url2) # Implementando o metodo __eq__()

print(id(extrator_url)) # O metodo id() retorna o numero que representa o endereco de memoria do objeto
print(id(extrator_url) == id(extrator_url2))
