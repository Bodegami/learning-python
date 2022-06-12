from cpf_cnpj import CpfCnpj
from validate_docbr import CPF, CNPJ

print("=================|| Construcao da classe Cpf ||=====================")
# cpf = Cpf("11111111112")
# print(cpf)

# cpf = "15616987913"
# objeto_cpf = Cpf(cpf)
#
# print(objeto_cpf)

print("=================|| Construcao da classe Cnpj ||=====================")

exemplo_cnpj = "35379838000112"
# cnpj = CNPJ()
# print(cnpj.validate(exemplo_cnpj))
tipo_documento = "cnpj"
documento = CpfCnpj(exemplo_cnpj, tipo_documento)
