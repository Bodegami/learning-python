from datetime import datetime, timedelta


yesterday = (datetime.now() - timedelta(1)).strftime('%d-%m-%Y')

print(yesterday)


listIndex = ['novo_09-05-2022', 'velho_09-05-2022', 'novo_10-05-2022', 'novo_08-05-2022']

str_match = [index for index in listIndex if index.__contains__(yesterday)]
print(str_match)
