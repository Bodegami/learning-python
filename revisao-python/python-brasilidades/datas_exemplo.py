from datetime import datetime, timedelta, timezone

"""
    %A retorna os dias da semana por extenso, como Sunday;

    %d exibe os dias do mês com números de 01 a 31;
    
    %m retorna meses em números de 01 a 12;
    
    %y mostra o ano com apenas dois dígitos;
    
    %Y apresenta o ano em formato de quatro números;
    
    %H retorna o horário no formato decimal, como 00, 001 e etc;
    
    %M exibe os minutos de forma decimal;
    
    %S apresenta os segundos em decimal.
"""


print(datetime.now())
print(datetime.today())

hoje = datetime.today()
hoje_formatado = hoje.strftime("%d/%m/%Y %H:%M")

print(hoje)
print(hoje_formatado)

amanha = datetime.today() + timedelta(days=1, hours=20)
print(amanha - hoje)