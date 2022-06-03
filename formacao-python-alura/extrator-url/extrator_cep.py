endereco = "Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

import re # Regular Expression -- RegEx

# cep tem 5 digitos + hífen(opcional) + 3 digitos

# Padrao em regex para o cep
# o ? indica que o parametro é opcional
# padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")

# sobre quantificadores - utilizamos {} e passamos o valor de quantas vezes os elementos de [] podem se repetir
# padrao = re.compile("[0123456789]{5}[-]?[0123456789]{3}")

# podemos simplificar ainda mais indicando que os algarismos são de 0 a 9 usando um hifen
# padrao = re.compile("[0-9]{5}[-]?[0-9]{3}")

# no lugar do ? podemos abrir chaves e dizer o minimo e maximo de vezes que aquele elemento pode aparecer,
# dessa forma definimos um limite
padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")

busca = padrao.search(endereco) # Retorna Match caso encontrado ou None caso não encontrado
if busca:
    cep = busca.group() # retorna a String encontrada no padrão informado
    print(cep)
else:
    print("Cep não encontrado!!")
