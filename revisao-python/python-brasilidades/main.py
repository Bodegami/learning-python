from cpf_cnpj import CpfCnpj, Documento
from telefones_br import TelefonesBr
from datas_br import DatasBr
from acesso_cep import BuscaEndereco

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

telefone = TelefonesBr("5511987654321")
print(telefone)

cadastro = DatasBr()
print(cadastro)
print(cadastro.mes_cadastro())
print(cadastro.dia_cadastro())
print(cadastro.tempo_cadastro())

cep = 25870146
objeto_cep = BuscaEndereco(cep)
print(objeto_cep)





