from cpf_cnpj import CpfCnpj, Documento

cpf = str(83977647040)
# novo_cpf = CpfCnpj(cpf, "cpf")
# print(novo_cpf)

cnpj = str(55874162000140)
# novo_cnpj = CpfCnpj(cnpj, "cnpj")
# print(novo_cnpj)

documento = Documento.cria_documento(cnpj)
print(documento)

documento = Documento.cria_documento(cpf)
print(documento)




