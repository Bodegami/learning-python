from validate_docbr import CPF, CNPJ


# Aqui fazemos uso design pattern Factory. Criamos a classe documento que é um factory responsavel
# por validar o numero de caracteres do documentos e chamar a classe correta criando uma instancia da mesma

class Documento:

    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de digitos incorreta!!")


class DocCpf:

    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            ValueError("CPF inválido!!")

    def __str__(self):
        return self.format()

    def valida(self, documento: str):
        validador = CPF()
        return validador.validate(documento)

    def format(self):
        mascara = CPF()
        return mascara.mask(self.cpf)


class DocCnpj:

    def __init__(self, documento: str):
        if self.valida(documento):
            self.cnpj = documento
        else:
            ValueError("CNPJ inválido!!")

    def __str__(self):
        return self.format()

    def valida(self, documento):
        validador = CNPJ()
        return validador.validate(documento)

    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

