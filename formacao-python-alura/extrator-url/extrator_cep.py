endereco = "Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

import re # Regular Expression -- RegEx

# cep tem 5 digitos + hífen(opcional) + 3 digitos

# Padrao em regex para o cep
# o ? indica que o parametro é opcional
padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")
busca = padrao.search(endereco) # Retorna Match caso encontrado ou None caso não encontrado
if busca:
    cep = busca.group() # retorna a String encontrada no padrão informado
    print(cep)
else:
    print("Cep não encontrado!!")
