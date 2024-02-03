import requests

cep = input('Digite o cep: ')

url = f'https://viacep.com.br/ws/{cep}/json/'

response = requests.get(url)

if response.status_code == 200:
    print(response.json())
else:
    print(f'O status de erro foi {response.status_code}')