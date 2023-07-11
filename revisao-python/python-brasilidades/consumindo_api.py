import requests

from acesso_cep import BuscaEndereco


r = requests.get("https://viacep.com.br/ws/01001000/json/")

print(r.text)

cep = "01001000"

objeto_cep = BuscaEndereco(cep)
print(objeto_cep.acessa_viacep().text)