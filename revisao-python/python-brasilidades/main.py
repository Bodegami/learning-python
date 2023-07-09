from cpf_cnpj import CpfCnpj

cpf = str(83977647040)
novo_cpf = CpfCnpj(cpf, "cpf")
print(novo_cpf)

cnpj = str(55874162000140)
novo_cnpj = CpfCnpj(cnpj, "cnpj")
print(novo_cnpj)




