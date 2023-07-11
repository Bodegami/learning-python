from datetime import datetime


class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.format_data()

    def mes_cadastro(self):
        meses_do_ano = ["janeiro", "fevereiro", "março",
                        "abril", "maio", "junho", "julho",
                        "agosto", "setembro", "outubro",
                        "novembro", "dezembro"]
        mes_cadastro = self.momento_cadastro.month - 1
        return meses_do_ano[mes_cadastro]

    def dia_cadastro(self):
        dias_da_semana = ["segunda", "terça", "quarta",
                          "quinta", "sexta", "sabado",
                          "domingo"]
        dia_cadastro = self.momento_cadastro.weekday()
        print(dia_cadastro)
        return dias_da_semana[dia_cadastro]

    def format_data(self):
        return self.momento_cadastro.strftime("%d/%m/%Y %H:%M")