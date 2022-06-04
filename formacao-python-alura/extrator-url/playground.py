from datetime import date, timedelta
import random

lista =[]
data_hoje = date.today()

count = random.randrange(1,31)

data_mes_atras = (data_hoje - timedelta(31)).strftime('%Y-%m-%d')
print(data_mes_atras)

for data in range(1,31):
    aleatorio = random.randrange(1, 31)
    data_mes_atras = (data_hoje - timedelta(aleatorio)).strftime('%Y-%m-%d')
    string_data = f"pedidos_de_{data_mes_atras}"
    print(string_data)
    lista.append(string_data)


data_limite = '2022-05-22'

for data in lista:
    data_result = data.find('05-22')
    if data == data_limite:
        print("achou")


## O metodo dir retorna todos os metodos do objeto passado como argumento
print(dir(str))


