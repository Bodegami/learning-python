import requests


class BuscaEndereco:
    def __init__(self, cep):
        cep = str(cep)
        if self.cep_eh_valido(cep):
            self.cep = cep
        else:
            raise ValueError("Cep inválido!")

    def __str__(self):
        return self.format_cep()

    def cep_eh_valido(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def acessa_viacep(self):
        url = "https://viacep.com.br/ws/{}/json".format(self.cep)
        r = requests.get(url)
        dados = r.json()
        return (
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        )

    def format_cep(self):
        return f'{self.cep[:5]}-{self.cep[5:]}'

