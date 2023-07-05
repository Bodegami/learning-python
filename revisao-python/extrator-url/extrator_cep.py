
import re # Regular Expression -- Regex

endereco = "Rua da Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

# 5 digitos + hífen (opcional) + digitos

padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")
busca = padrao.search(endereco) # Retorna um Match ou None caso não encontre

if busca:
    cep = busca.group() # Retorna a String que foi encontrado no padrao
    print(busca.start()) # Retorna a posição (index) inicial da String
    print(busca.end()) # Retorna a posição (index) final da String
    print(cep)
