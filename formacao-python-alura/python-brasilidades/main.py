from documento import Documento, DocCnpj, DocCpf
from validate_docbr import CPF, CNPJ

print("=================|| Construcao da classe Cpf ||=====================")
# cpf = Cpf("11111111112")
# print(cpf)

# cpf = "15616987913"
# objeto_cpf = Cpf(cpf)
#
# print(objeto_cpf)

print("=================|| Construcao da classe Cnpj ||=====================")

# exemplo_cnpj = "35379838000112"
# exemplo_cpf = "32007832062"
# # cnpj = CNPJ()
# # print(cnpj.validate(exemplo_cnpj))
# tipo_documento = "cnpj"
# documento = CpfCnpj(exemplo_cnpj, tipo_documento)
# print(documento)
#
# tipo_documento = "cpf"
# documento = CpfCnpj(exemplo_cpf,tipo_documento)
# print(documento)


print("=================|| Refatorando a classe ||=====================")

exemplo_cpf = "32007832062"
documento = Documento.cria_documento(exemplo_cpf)
print(documento)

exemplo_cnpj = "35379838000112"
documento = Documento.cria_documento(exemplo_cnpj)
print(documento)
