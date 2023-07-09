from validate_docbr import CPF, CNPJ


class CpfCnpj:

    def __init__(self, documento, tipo_documento):
        self.tipo_documento = tipo_documento
        documento = str(documento)
        if self.tipo_documento == "cpf":
            if self.cpf_eh_valido(documento):
                self.documento = documento
            else:
                raise ValueError("CPF inválido!")
        elif self.tipo_documento == "cnpj":
            if self.cnpj_eh_valido(documento):
                self.documento = documento
            else:
                raise ValueError("CNPJ inválido!")
        else:
            raise ValueError("Documento inválido!")

    def __str__(self):
        if self.tipo_documento == "cpf":
            return self.format_cpf()
        elif self.tipo_documento == "cnpj":
            return self.format_cnpj()

    def cpf_eh_valido(self, documento):
        if len(documento) == 11:
            validador = CPF()
            return validador.validate(documento)
        else:
            raise ValueError("Quantidade de digitos inválida!!")

    def cnpj_eh_valido(self, documento):
        if len(documento) == 14:
            validador = CNPJ()
            return validador.validate(documento)
        else:
            raise ValueError("Quantidade de digitos inválida!!")

    def format_cpf(self):
        mascara = CPF()
        return mascara.mask(self.documento)

    def format_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.documento)



