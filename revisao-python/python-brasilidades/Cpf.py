class Cpf:

    def __init__(self, documento):
        documento = str(documento)
        if self.cpf_eh_valido(documento):
            self.documento = documento
        else:
            raise ValueError("CPF inválido!")

    def __str__(self):
        return self.format_cpf()

    def cpf_eh_valido(self, documento):
        if len(documento) == 11:
            return True
        else:
            return False

    def format_cpf(self):
        fatia_um = self.documento[:3]
        fatia_dois = self.documento[3:6]
        fatia_tres = self.documento[6:9]
        fatia_quatro = self.documento[9:11]
        return f'{fatia_um}.{fatia_dois}.{fatia_tres}-{fatia_quatro}'



