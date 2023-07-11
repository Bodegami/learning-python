import requests

from acesso_cep import BuscaEndereco


r = requests.get("https://viacep.com.br/ws/01001000/json/")

print(r.text)

cep = "01001000"

objeto_cep = BuscaEndereco(cep)
viacep_response = objeto_cep.acessa_viacep()
print(viacep_response)


#print(type(viacep_response.text))
#print(type(viacep_response.json()))

#print(viacep_response.text)
#print(viacep_response.json())

#print(viacep_response.json()['bairro'])

bairro, estado, cidade = objeto_cep.acessa_viacep()
print(f'Bairro: {bairro}, Cidade: {cidade}, Estado: {estado}')
