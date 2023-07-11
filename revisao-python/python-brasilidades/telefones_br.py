import re


class TelefonesBr:
    def __init__(self, telefone):
        if self.valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError("Numero incorreto!")

    def __str__(self):
        return self.numero

    def valida_telefone(self, telefone):
        padrao = "[0-9]{2,3}[0-9]{2}[0-9]{4,5}[0-9]{4}"
        resposta = re.findall(pattern=padrao, string=telefone)
        if resposta:
            return True
        else:
            return False