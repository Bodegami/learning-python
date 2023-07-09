from Cpf import Cpf
from validate_docbr import CPF

cpf = str(15616957801)

# novo_cpf = Cpf(cpf)
# print(novo_cpf)

validador = CPF()
print(validador.validate(cpf))


