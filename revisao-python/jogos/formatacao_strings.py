print("Tentativa {} de {}.".format(1, 3))

#Podemos inverter a ordem apenas nomeando qual parametro devera preencher o colchetes
print("Tentativa {1} de {0}.".format(1, 3))

#Podemos formatar o tipo float e indicar quantas casas decimais queremos imprimir
print("R$ {:07.2f}".format(1.59))

#O primeiro valor indica quanta casas deve ter o float e caso o valor não tenha, ele vai preencher com 0
#O segundo valor após o "ponto", é quantidade de casas queremos imprimir após a vírgula
print("R$ {:07.2f}".format(1234.59))

#A formatação também funciona para tipos Int()
print("R$ {:07d}".format(4))

#Aqui ele vai compor o valor com 0 na frente casa só tenha uma casa decimal
print("Data: {:02d}/{:02d}".format(1, 4))
print("Data: {:02d}/{:02d}".format(19, 11))